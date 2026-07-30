"""Solve Problem 3, export reproducible evidence, and draw paper figures."""

from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from pathlib import Path
from types import SimpleNamespace

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from problem1_model import (
    CLOUD_RADIUS,
    FY1_INITIAL,
    cylinder_surface_points,
    missile_position,
)
from problem2_model import (
    Strategy,
    burst_point,
    cloud_center_for,
    drop_point,
    full_cylinder_distances_for,
)
from problem3_model import (
    MultiBombStrategy,
    centerline_union_duration,
    coarse_target_points,
    coordinate_refine_unit_cube,
    decode_decision,
    differential_evolution_unit_cube,
    exact_multi_bomb_intervals,
    intervals_duration,
    overlap_duration,
    sampled_full_union_duration,
    seed_strategies,
)


OKABE_ITO = {
    "orange": "#E69F00",
    "sky": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
    "gray": "#6B7280",
}
BOMB_COLORS = (OKABE_ITO["blue"], OKABE_ITO["orange"], OKABE_ITO["green"])
PROXY_SEEDS = (20250802, 20250803, 19)
FULL_SEED = 20250804


def configure_style() -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": [
                "Microsoft YaHei",
                "SimHei",
                "Noto Sans CJK SC",
                "DejaVu Sans",
            ],
            "axes.unicode_minus": False,
            "font.size": 9,
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def save_figure(fig: plt.Figure, output_stem: Path) -> None:
    fig.savefig(output_stem.with_suffix(".png"), bbox_inches="tight", dpi=300)
    svg_path = output_stem.with_suffix(".svg")
    fig.savefig(svg_path, bbox_inches="tight")
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n",
        encoding="utf-8",
    )
    plt.close(fig)


def optimize() -> tuple[MultiBombStrategy, list, object, list[float]]:
    proxy_objective = lambda decision: centerline_union_duration(
        decision, step=0.06
    )
    proxy_runs = [
        differential_evolution_unit_cube(
            proxy_objective,
            seed=seed,
            population_size=128,
            generations=200,
            initial_decisions=seed_strategies(),
        )
        for seed in PROXY_SEEDS
    ]
    proxy_candidates = [
        candidate
        for run in proxy_runs
        for candidate in run.population[:8]
    ]

    coarse_points = coarse_target_points()
    coarse_objective = lambda decision: sampled_full_union_duration(
        decision, coarse_points, step=0.06
    )
    ranked = sorted(
        proxy_candidates,
        key=coarse_objective,
        reverse=True,
    )
    full_run = differential_evolution_unit_cube(
        coarse_objective,
        seed=FULL_SEED,
        population_size=72,
        generations=90,
        initial_decisions=seed_strategies() + ranked[:4],
    )

    medium_points = cylinder_surface_points(n_theta=96, n_z=7, n_r=6)
    medium_objective = lambda decision: sampled_full_union_duration(
        decision, medium_points, step=0.025
    )
    refined_decision, _, refine_history = coordinate_refine_unit_cube(
        full_run.decision,
        medium_objective,
        initial_steps=(0.004, 0.006, 0.002, 0.002, 0.002, 0.001, 0.001, 0.001),
        minimum_steps=(
            1e-5,
            1e-5,
            1e-5,
            1e-5,
            1e-5,
            5e-6,
            5e-6,
            5e-6,
        ),
        max_rounds=100,
    )
    strategy = decode_decision(refined_decision)

    # Under the strict complete-cylinder criterion, bomb 3 has zero marginal
    # contribution in the optimum. Resolve the neutral family by choosing its
    # earliest feasible release and detonation.
    strategy = MultiBombStrategy(
        heading_rad=strategy.heading_rad,
        speed_mps=strategy.speed_mps,
        drop_times_s=(
            strategy.drop_times_s[0],
            strategy.drop_times_s[1],
            strategy.drop_times_s[1] + 1.0,
        ),
        fuse_delays_s=(
            strategy.fuse_delays_s[0],
            strategy.fuse_delays_s[1],
            0.0,
        ),
    )
    return strategy, proxy_runs, full_run, refine_history


def bomb_path(strategy: Strategy, times: np.ndarray) -> np.ndarray:
    tau = times - strategy.drop_time_s
    return (
        drop_point(strategy)
        + tau[:, None] * strategy.drone_velocity
        + np.column_stack(
            [np.zeros_like(tau), np.zeros_like(tau), -4.9 * tau**2]
        )
    )


def figure_geometry(strategy: MultiBombStrategy, figure_dir: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.35), constrained_layout=True)
    ax_xy, ax_xz = axes
    times = np.linspace(0.0, 8.0, 300)
    drone = FY1_INITIAL + times[:, None] * strategy.bombs[0].drone_velocity
    missile = missile_position(times)

    for ax, dimensions in ((ax_xy, (0, 1)), (ax_xz, (0, 2))):
        ax.plot(
            missile[:, dimensions[0]],
            missile[:, dimensions[1]],
            color=OKABE_ITO["vermillion"],
            linewidth=1.8,
            label="M1",
        )
        ax.plot(
            drone[:, dimensions[0]],
            drone[:, dimensions[1]],
            color=OKABE_ITO["purple"],
            linewidth=1.5,
            label="FY1",
        )
        for index, (bomb, color) in enumerate(
            zip(strategy.bombs, BOMB_COLORS), start=1
        ):
            path_times = np.linspace(
                bomb.drop_time_s, bomb.burst_time_s, 20
            )
            path = bomb_path(bomb, path_times)
            ax.plot(
                path[:, dimensions[0]],
                path[:, dimensions[1]],
                color=color,
                linestyle="--",
                linewidth=1.3,
                label=f"干扰弹 {index}",
            )
            drop = drop_point(bomb)
            burst = burst_point(bomb)
            ax.scatter(
                drop[dimensions[0]],
                drop[dimensions[1]],
                marker="v",
                s=32,
                color=color,
                edgecolor="black",
                linewidth=0.4,
                zorder=4,
            )
            ax.scatter(
                burst[dimensions[0]],
                burst[dimensions[1]],
                marker="o",
                s=32,
                color=color,
                edgecolor="black",
                linewidth=0.4,
                zorder=4,
            )
        ax.grid(alpha=0.18)
        ax.set_xlabel("x (m)")
    ax_xy.set_ylabel("y (m)")
    ax_xz.set_ylabel("z (m)")
    ax_xy.set_xlim(17500.0, 18700.0)
    ax_xy.set_ylim(-10.0, 150.0)
    ax_xy.set_title("(a) 水平面局部投放排程")
    ax_xz.set_title("(b) 竖直剖面")
    ax_xy.legend(frameon=False, ncol=2)
    ax_xz.legend(frameon=False, ncol=2)
    save_figure(fig, figure_dir / "problem3_fig1_spatial_schedule")


def figure_intervals(
    individual: list[list],
    union: list,
    figure_dir: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 3.15), constrained_layout=True)
    for row, (intervals, color) in enumerate(
        zip(individual, BOMB_COLORS), start=1
    ):
        spans = [(item.start, item.end - item.start) for item in intervals]
        if spans:
            ax.broken_barh(spans, (row - 0.3, 0.6), facecolors=color)
        else:
            ax.text(
                2.0,
                row,
                "严格判据下无有效区间",
                color=OKABE_ITO["gray"],
                va="center",
                fontsize=8,
            )
    union_spans = [(item.start, item.end - item.start) for item in union]
    ax.broken_barh(
        union_spans,
        (3.7, 0.65),
        facecolors=OKABE_ITO["purple"],
    )
    ax.set_yticks([1, 2, 3, 4.02], ["弹 1", "弹 2", "弹 3", "并集"])
    ax.set_ylim(0.45, 4.55)
    ax.set_xlim(0.0, 8.0)
    ax.set_xlabel("任务下达后时间 (s)")
    ax.set_title("三枚干扰弹的完整圆柱有效区间与联合遮蔽")
    ax.grid(axis="x", alpha=0.18)
    save_figure(fig, figure_dir / "problem3_fig2_coverage_gantt")


def figure_metrics(
    strategy: MultiBombStrategy,
    individual: list[list],
    union: list,
    target_points: np.ndarray,
    figure_dir: Path,
) -> tuple[np.ndarray, np.ndarray]:
    times = np.linspace(0.0, 8.0, 801)
    distance_rows = []
    for bomb in strategy.bombs:
        row = np.full(times.shape, np.inf, dtype=float)
        active = (times >= bomb.burst_time_s) & (
            times <= bomb.burst_time_s + 20.0
        )
        row[active] = full_cylinder_distances_for(
            bomb, times[active], target_points
        )
        distance_rows.append(row)
    distances = np.vstack(distance_rows)
    coverage_count = np.sum(distances <= CLOUD_RADIUS, axis=0)
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(7.2, 4.55),
        gridspec_kw={"height_ratios": [2.2, 1.0]},
        constrained_layout=True,
    )
    for index, (row, color) in enumerate(
        zip(distances, BOMB_COLORS), start=1
    ):
        axes[0].plot(
            times,
            row,
            color=color,
            linewidth=1.45,
            label=f"弹 {index}",
        )
    axes[0].axhline(
        CLOUD_RADIUS,
        color=OKABE_ITO["black"],
        linestyle=":",
        linewidth=1.1,
        label="10 m 阈值",
    )
    for interval in union:
        axes[0].axvspan(
            interval.start,
            interval.end,
            color=OKABE_ITO["sky"],
            alpha=0.16,
        )
    axes[0].set_ylabel("最不利目标视线距离 (m)")
    axes[0].set_title("(a) 三个烟幕球的完整圆柱判据")
    axes[0].set_ylim(0.0, min(45.0, np.nanmax(distances[:, :780]) + 2.0))
    axes[0].legend(frameon=False, ncol=4)
    axes[0].grid(alpha=0.18)

    axes[1].step(
        times,
        coverage_count,
        where="mid",
        color=OKABE_ITO["purple"],
        linewidth=1.7,
    )
    axes[1].fill_between(
        times,
        coverage_count,
        step="mid",
        color=OKABE_ITO["purple"],
        alpha=0.20,
    )
    axes[1].set_yticks([0, 1, 2, 3])
    axes[1].set_ylim(-0.1, 3.2)
    axes[1].set_xlabel("任务下达后时间 (s)")
    axes[1].set_ylabel("同时有效弹数")
    axes[1].set_title("(b) 联合覆盖计数")
    axes[1].grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem3_fig3_coverage_metrics")
    return times, distances


def figure_convergence(
    proxy_runs: list,
    full_run: object,
    final_duration: float,
    figure_dir: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.15), constrained_layout=True)
    for run, seed, style in zip(proxy_runs, PROXY_SEEDS, ("-", "--", ":")):
        axes[0].plot(
            run.history_best,
            linestyle=style,
            linewidth=1.35,
            label=f"seed={seed}",
        )
    axes[0].set_xlabel("进化代数")
    axes[0].set_ylabel("中心线代理并集 (s)")
    axes[0].set_title("(a) 多起点代理搜索")
    axes[0].legend(frameon=False)
    axes[0].grid(alpha=0.18)

    axes[1].plot(
        full_run.history_best,
        color=OKABE_ITO["blue"],
        linewidth=1.6,
        label="粗完整圆柱目标",
    )
    axes[1].axhline(
        final_duration,
        color=OKABE_ITO["vermillion"],
        linestyle="--",
        linewidth=1.2,
        label=f"精确复算 {final_duration:.4f} s",
    )
    axes[1].set_xlabel("进化代数")
    axes[1].set_ylabel("联合遮蔽时间 (s)")
    axes[1].set_title("(b) 完整圆柱直接搜索")
    axes[1].legend(frameon=False)
    axes[1].grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem3_fig4_convergence")


def sensitivity_rows(
    strategy: MultiBombStrategy,
    target_points: np.ndarray,
) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    scenarios: dict[str, list[tuple[float, MultiBombStrategy]]] = {
        "heading_offset_deg": [
            (
                offset,
                MultiBombStrategy(
                    np.radians(strategy.heading_deg + offset),
                    strategy.speed_mps,
                    strategy.drop_times_s,
                    strategy.fuse_delays_s,
                ),
            )
            for offset in np.linspace(-1.5, 1.5, 31)
        ],
        "speed_mps": [
            (
                speed,
                MultiBombStrategy(
                    strategy.heading_rad,
                    float(speed),
                    strategy.drop_times_s,
                    strategy.fuse_delays_s,
                ),
            )
            for speed in np.linspace(
                max(70.0, strategy.speed_mps - 15.0),
                min(140.0, strategy.speed_mps + 15.0),
                31,
            )
        ],
        "second_drop_s": [
            (
                drop2,
                MultiBombStrategy(
                    strategy.heading_rad,
                    strategy.speed_mps,
                    (
                        strategy.drop_times_s[0],
                        float(drop2),
                        float(drop2 + 1.0),
                    ),
                    strategy.fuse_delays_s,
                ),
            )
            for drop2 in np.linspace(1.0, 1.5, 26)
        ],
    }
    for parameter, candidates in scenarios.items():
        for value, candidate in candidates:
            decision_intervals, union = exact_multi_bomb_intervals(
                candidate, target_points, scan_step=0.025
            )
            rows.append(
                {
                    "parameter": parameter,
                    "value": float(value),
                    "duration_s": intervals_duration(union),
                }
            )
    return rows


def figure_sensitivity(rows: list[dict[str, float | str]], figure_dir: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.8), constrained_layout=True)
    labels = {
        "heading_offset_deg": ("航向偏差 (°)", "(a) 航向"),
        "speed_mps": ("速度 (m/s)", "(b) 速度"),
        "second_drop_s": ("第 2 枚投放时刻 (s)", "(c) 时序"),
    }
    for ax, (parameter, (xlabel, title)), color in zip(
        axes, labels.items(), BOMB_COLORS
    ):
        subset = [row for row in rows if row["parameter"] == parameter]
        ax.plot(
            [float(row["value"]) for row in subset],
            [float(row["duration_s"]) for row in subset],
            color=color,
            linewidth=1.6,
            marker="o",
            markersize=2.2,
        )
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        ax.grid(alpha=0.18)
    axes[0].set_ylabel("联合遮蔽时间 (s)")
    save_figure(fig, figure_dir / "problem3_fig5_sensitivity")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_existing_run(
    output_dir: Path,
) -> tuple[MultiBombStrategy, list, object, list[float]]:
    result = json.loads(
        (output_dir / "problem3_result.json").read_text(encoding="utf-8")
    )
    bombs = result["bombs"]
    strategy = MultiBombStrategy(
        heading_rad=np.radians(result["heading_deg"]),
        speed_mps=result["speed_mps"],
        drop_times_s=tuple(row["drop_time_s"] for row in bombs),
        fuse_delays_s=tuple(row["fuse_delay_s"] for row in bombs),
    )
    grouped: dict[tuple[str, int], list[dict[str, str]]] = {}
    with (output_dir / "problem3_optimization_history.csv").open(
        newline="", encoding="utf-8-sig"
    ) as handle:
        for row in csv.DictReader(handle):
            key = (row["stage"], int(row["seed"]))
            grouped.setdefault(key, []).append(row)

    proxy_runs = []
    for seed in PROXY_SEEDS:
        rows = grouped[("centerline_proxy", seed)]
        proxy_runs.append(
            SimpleNamespace(
                history_best=np.asarray(
                    [float(row["best_duration_s"]) for row in rows]
                ),
                history_mean=np.asarray(
                    [float(row["mean_duration_s"]) for row in rows]
                ),
                score=max(float(row["best_duration_s"]) for row in rows),
            )
        )
    full_rows = grouped[("coarse_complete_cylinder", FULL_SEED)]
    full_run = SimpleNamespace(
        history_best=np.asarray(
            [float(row["best_duration_s"]) for row in full_rows]
        ),
        history_mean=np.asarray(
            [float(row["mean_duration_s"]) for row in full_rows]
        ),
        score=max(float(row["best_duration_s"]) for row in full_rows),
    )
    refine_history = result["optimization"]["refine_history_s"]
    return strategy, proxy_runs, full_run, refine_history


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("Code/outputs"))
    parser.add_argument("--figure-dir", type=Path, default=Path("Paper/figures"))
    parser.add_argument(
        "--reuse-result",
        action="store_true",
        help="Reuse a completed JSON result and optimization-history CSV.",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    configure_style()

    if args.reuse_result:
        strategy, proxy_runs, full_run, refine_history = load_existing_run(
            args.output_dir
        )
    else:
        strategy, proxy_runs, full_run, refine_history = optimize()
    convergence: dict[int, float] = {}
    final_individual = None
    final_union = None
    for n_theta in (180, 360, 720, 1440):
        points = cylinder_surface_points(n_theta=n_theta, n_z=11, n_r=8)
        individual, union = exact_multi_bomb_intervals(
            strategy, points, scan_step=0.005
        )
        convergence[n_theta] = intervals_duration(union)
        if n_theta == 1440:
            final_individual = individual
            final_union = union
    assert final_individual is not None and final_union is not None

    bomb_rows = []
    for index, (bomb, intervals) in enumerate(
        zip(strategy.bombs, final_individual), start=1
    ):
        bomb_rows.append(
            {
                "bomb_id": index,
                "drop_time_s": bomb.drop_time_s,
                "fuse_delay_s": bomb.fuse_delay_s,
                "burst_time_s": bomb.burst_time_s,
                "drop_point_m": drop_point(bomb).tolist(),
                "burst_point_m": burst_point(bomb).tolist(),
                "effective_intervals_s": [
                    [item.start, item.end] for item in intervals
                ],
                "effective_duration_s": intervals_duration(intervals),
            }
        )

    union_duration = intervals_duration(final_union)
    result = {
        "criterion": "complete-cylinder all-sampled-boundary sight lines",
        "objective": "maximize the measure of the union of three effective intervals",
        "heading_deg": strategy.heading_deg,
        "speed_mps": strategy.speed_mps,
        "bombs": bomb_rows,
        "union_intervals_s": [
            [item.start, item.end] for item in final_union
        ],
        "union_duration_s": union_duration,
        "overlap_duration_s": overlap_duration(
            final_individual, final_union
        ),
        "third_bomb_tie_break": (
            "zero marginal contribution under the strict criterion; "
            "choose earliest feasible release and detonation"
        ),
        "theta_convergence_duration_s": {
            str(key): value for key, value in convergence.items()
        },
        "optimization": {
            "method": (
                "three-seed centerline differential evolution; "
                "direct complete-cylinder differential evolution; "
                "coordinate refinement and exact boundary recomputation"
            ),
            "proxy_seeds": list(PROXY_SEEDS),
            "full_seed": FULL_SEED,
            "proxy_best_duration_s": [run.score for run in proxy_runs],
            "coarse_full_best_duration_s": full_run.score,
            "refine_history_s": refine_history,
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
            "matplotlib": matplotlib.__version__,
        },
    }
    (args.output_dir / "problem3_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    interval_rows = []
    for bomb_id, intervals in enumerate(final_individual, start=1):
        if intervals:
            for item in intervals:
                interval_rows.append(
                    {
                        "series": f"bomb_{bomb_id}",
                        "start_s": item.start,
                        "end_s": item.end,
                        "duration_s": item.end - item.start,
                    }
                )
        else:
            interval_rows.append(
                {
                    "series": f"bomb_{bomb_id}",
                    "start_s": "",
                    "end_s": "",
                    "duration_s": 0.0,
                }
            )
    for item in final_union:
        interval_rows.append(
            {
                "series": "union",
                "start_s": item.start,
                "end_s": item.end,
                "duration_s": item.end - item.start,
            }
        )
    write_csv(
        args.output_dir / "problem3_intervals.csv",
        ["series", "start_s", "end_s", "duration_s"],
        interval_rows,
    )

    history_rows = []
    for run, seed in zip(proxy_runs, PROXY_SEEDS):
        for generation, (best, mean) in enumerate(
            zip(run.history_best, run.history_mean)
        ):
            history_rows.append(
                {
                    "stage": "centerline_proxy",
                    "seed": seed,
                    "generation": generation,
                    "best_duration_s": best,
                    "mean_duration_s": mean,
                }
            )
    for generation, (best, mean) in enumerate(
        zip(full_run.history_best, full_run.history_mean)
    ):
        history_rows.append(
            {
                "stage": "coarse_complete_cylinder",
                "seed": FULL_SEED,
                "generation": generation,
                "best_duration_s": best,
                "mean_duration_s": mean,
            }
        )
    write_csv(
        args.output_dir / "problem3_optimization_history.csv",
        [
            "stage",
            "seed",
            "generation",
            "best_duration_s",
            "mean_duration_s",
        ],
        history_rows,
    )

    figure_geometry(strategy, args.figure_dir)
    figure_intervals(final_individual, final_union, args.figure_dir)
    metric_points = cylinder_surface_points(n_theta=360, n_z=11, n_r=8)
    times, distances = figure_metrics(
        strategy,
        final_individual,
        final_union,
        metric_points,
        args.figure_dir,
    )
    metric_rows = []
    for column, time in enumerate(times):
        metric_rows.append(
            {
                "time_s": time,
                "bomb_1_worst_distance_m": (
                    distances[0, column]
                    if np.isfinite(distances[0, column])
                    else ""
                ),
                "bomb_2_worst_distance_m": (
                    distances[1, column]
                    if np.isfinite(distances[1, column])
                    else ""
                ),
                "bomb_3_worst_distance_m": (
                    distances[2, column]
                    if np.isfinite(distances[2, column])
                    else ""
                ),
                "coverage_count": int(
                    np.sum(distances[:, column] <= CLOUD_RADIUS)
                ),
            }
        )
    write_csv(
        args.output_dir / "problem3_timeseries.csv",
        [
            "time_s",
            "bomb_1_worst_distance_m",
            "bomb_2_worst_distance_m",
            "bomb_3_worst_distance_m",
            "coverage_count",
        ],
        metric_rows,
    )
    figure_convergence(proxy_runs, full_run, union_duration, args.figure_dir)
    sensitivity_points = cylinder_surface_points(
        n_theta=96, n_z=7, n_r=6
    )
    sensitivity = sensitivity_rows(strategy, sensitivity_points)
    write_csv(
        args.output_dir / "problem3_sensitivity.csv",
        ["parameter", "value", "duration_s"],
        sensitivity,
    )
    figure_sensitivity(sensitivity, args.figure_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
