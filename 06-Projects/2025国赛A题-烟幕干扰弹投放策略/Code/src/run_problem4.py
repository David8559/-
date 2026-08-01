"""Solve Problem 4, export evidence, and draw publication figures."""

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
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    FALSE_TARGET,
    TRUE_TARGET_BOTTOM_CENTER,
    TRUE_TARGET_HEIGHT,
    cylinder_surface_points,
    missile_position,
)
from problem3_model import intervals_duration, merge_intervals, overlap_duration
from problem4_model import (
    DRONE_IDS,
    DRONE_INITIALS,
    DroneBombStrategy,
    MultiDroneStrategy,
    burst_point,
    cloud_center_for,
    coarse_target_points,
    coordinate_refine_unit_cube,
    decode_drone_block,
    differential_evolution_unit_cube,
    drop_point,
    encode_bomb_strategy,
    exact_multi_drone_intervals,
    full_cylinder_distances_for,
    individual_centerline_duration,
    individual_centerline_proximity_score,
    individual_sampled_full_duration,
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
DRONE_COLORS = (OKABE_ITO["blue"], OKABE_ITO["orange"], OKABE_ITO["green"])
DRONE_STYLES = ("-", "--", "-.")
PROXIMITY_SEEDS = {"FY1": 20250860, "FY2": 20250861, "FY3": 20250862}
DURATION_SEEDS = {"FY1": 20250870, "FY2": 20250871, "FY3": 20250872}

# High-quality deterministic seeds obtained from the staged search. They are
# included to make reruns robust to the large zero-duration plateaus.
REFERENCE_BLOCKS = {
    "FY1": np.array(
        [0.5192901279646074, 1.0, 0.011030669226260555, 1.0]
    ),
    "FY2": np.array(
        [0.25089520200533777, 1.0, 0.14341259093312747, 0.6517330043168932]
    ),
    "FY3": np.array(
        [
            0.7173580994867695,
            0.8952739336952211,
            0.3554243349130167,
            0.20271508521467377,
        ]
    ),
}


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


def optimize() -> tuple[MultiDroneStrategy, dict[str, dict[str, object]]]:
    coarse_points = coarse_target_points()
    medium_points = cylinder_surface_points(n_theta=96, n_z=11, n_r=8)
    final_bombs: list[DroneBombStrategy] = []
    evidence: dict[str, dict[str, object]] = {}

    for drone_id in DRONE_IDS:
        proximity_objective = lambda decision, drone_id=drone_id: (
            individual_centerline_proximity_score(
                decision, drone_id, step=0.10
            )
        )
        proximity_run = differential_evolution_unit_cube(
            proximity_objective,
            seed=PROXIMITY_SEEDS[drone_id],
            population_size=96,
            generations=150,
            initial_decisions=[REFERENCE_BLOCKS[drone_id]],
            dimension=4,
        )
        duration_objective = lambda decision, drone_id=drone_id: (
            individual_centerline_duration(decision, drone_id, step=0.05)
        )
        duration_run = differential_evolution_unit_cube(
            duration_objective,
            seed=DURATION_SEEDS[drone_id],
            population_size=112,
            generations=190,
            initial_decisions=[
                REFERENCE_BLOCKS[drone_id],
                *list(proximity_run.population[:24]),
            ],
            dimension=4,
        )
        candidates = [
            REFERENCE_BLOCKS[drone_id],
            *list(duration_run.population[:16]),
            *list(proximity_run.population[:8]),
        ]
        coarse_objective = lambda decision, drone_id=drone_id: (
            individual_sampled_full_duration(
                decision, drone_id, coarse_points, step=0.03
            )
        )
        ranked = sorted(
            ((coarse_objective(item), item) for item in candidates),
            key=lambda item: item[0],
            reverse=True,
        )
        refined = []
        for _, candidate in ranked[:3]:
            decision, score, history = coordinate_refine_unit_cube(
                candidate,
                coarse_objective,
                initial_steps=(0.003, 0.006, 0.002, 0.003),
                minimum_steps=(2e-5, 2e-5, 2e-5, 2e-5),
                max_rounds=70,
            )
            refined.append((score, decision, history))
        refined.sort(key=lambda item: item[0], reverse=True)

        medium_objective = lambda decision, drone_id=drone_id: (
            individual_sampled_full_duration(
                decision, drone_id, medium_points, step=0.02
            )
        )
        decision, score, medium_history = coordinate_refine_unit_cube(
            refined[0][1],
            medium_objective,
            initial_steps=(0.001, 0.002, 0.001, 0.001),
            minimum_steps=(5e-6, 5e-6, 5e-6, 5e-6),
            max_rounds=80,
        )
        final_bombs.append(decode_drone_block(decision, drone_id))
        evidence[drone_id] = {
            "proximity_run": proximity_run,
            "duration_run": duration_run,
            "coarse_refine_history": refined[0][2],
            "medium_refine_history": medium_history,
            "medium_score": score,
            "decision": decision,
        }
    return MultiDroneStrategy(tuple(final_bombs)), evidence


def bomb_path(strategy: DroneBombStrategy, times: np.ndarray) -> np.ndarray:
    tau = times - strategy.drop_time_s
    return (
        drop_point(strategy)
        + tau[:, None] * strategy.drone_velocity
        + np.column_stack(
            [np.zeros_like(tau), np.zeros_like(tau), -4.9 * tau**2]
        )
    )


def figure_spatial(strategy: MultiDroneStrategy, figure_dir: Path) -> None:
    fig = plt.figure(figsize=(7.2, 3.5), constrained_layout=True)
    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    axxy = fig.add_subplot(1, 2, 2)
    max_time = 30.0
    missile_times = np.linspace(0.0, max_time, 400)
    missile = missile_position(missile_times)

    ax3d.plot(
        missile[:, 0],
        missile[:, 1],
        missile[:, 2],
        color=OKABE_ITO["vermillion"],
        linewidth=1.7,
        label="M1",
    )
    axxy.plot(
        missile[:, 0],
        missile[:, 1],
        color=OKABE_ITO["vermillion"],
        linewidth=1.7,
        label="M1",
    )
    for bomb, color, style in zip(
        strategy.bombs, DRONE_COLORS, DRONE_STYLES
    ):
        drone_times = np.linspace(0.0, bomb.burst_time_s, 160)
        drone = bomb.initial_position + drone_times[:, None] * bomb.drone_velocity
        path_times = np.linspace(bomb.drop_time_s, bomb.burst_time_s, 60)
        path = bomb_path(bomb, path_times)
        ax3d.plot(
            drone[:, 0],
            drone[:, 1],
            drone[:, 2],
            color=color,
            linestyle=style,
            linewidth=1.5,
            label=bomb.drone_id,
        )
        ax3d.plot(
            path[:, 0],
            path[:, 1],
            path[:, 2],
            color=color,
            linestyle=":",
            linewidth=1.3,
        )
        ax3d.scatter(
            *burst_point(bomb),
            color=color,
            edgecolor="black",
            linewidth=0.4,
            s=28,
        )
        axxy.plot(
            drone[:, 0],
            drone[:, 1],
            color=color,
            linestyle=style,
            linewidth=1.5,
            label=bomb.drone_id,
        )
        axxy.scatter(
            drop_point(bomb)[0],
            drop_point(bomb)[1],
            marker="v",
            color=color,
            edgecolor="black",
            linewidth=0.4,
            s=28,
        )
        axxy.scatter(
            burst_point(bomb)[0],
            burst_point(bomb)[1],
            marker="o",
            color=color,
            edgecolor="black",
            linewidth=0.4,
            s=28,
        )

    theta = np.linspace(0.0, 2.0 * np.pi, 60)
    for z in (0.0, TRUE_TARGET_HEIGHT):
        ax3d.plot(
            7.0 * np.cos(theta),
            200.0 + 7.0 * np.sin(theta),
            np.full_like(theta, z),
            color=OKABE_ITO["black"],
            linewidth=0.8,
        )
    ax3d.scatter(
        FALSE_TARGET[0],
        FALSE_TARGET[1],
        FALSE_TARGET[2],
        marker="x",
        color=OKABE_ITO["black"],
        s=35,
    )
    ax3d.set_xlabel("x (m)")
    ax3d.set_ylabel("y (m)")
    ax3d.set_zlabel("z (m)")
    ax3d.set_title("(a) 三机协同空间轨迹")
    ax3d.view_init(elev=21, azim=-63)
    ax3d.legend(frameon=False, loc="upper left")

    axxy.set_xlabel("x (m)")
    axxy.set_ylabel("y (m)")
    axxy.set_title("(b) 水平投影及投放/起爆点")
    axxy.grid(alpha=0.18)
    axxy.legend(frameon=False, ncol=2)
    save_figure(fig, figure_dir / "problem4_fig1_multi_drone_geometry")


def figure_gantt(
    individual: list[list],
    union: list,
    figure_dir: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 3.2), constrained_layout=True)
    for row, (drone_id, intervals, color) in enumerate(
        zip(DRONE_IDS, individual, DRONE_COLORS), start=1
    ):
        spans = [(item.start, item.duration) for item in intervals]
        ax.broken_barh(spans, (row - 0.3, 0.6), facecolors=color)
        if spans:
            ax.text(
                spans[0][0] + spans[0][1] / 2.0,
                row,
                f"{spans[0][1]:.3f} s",
                ha="center",
                va="center",
                color="white",
                fontsize=8,
            )
    union_spans = [(item.start, item.duration) for item in union]
    ax.broken_barh(
        union_spans,
        (3.7, 0.65),
        facecolors=OKABE_ITO["purple"],
    )
    ax.set_yticks([1, 2, 3, 4.02], [*DRONE_IDS, "联合"])
    ax.set_ylim(0.45, 4.55)
    ax.set_xlim(0.0, 30.0)
    ax.set_xlabel("任务下达后时间 (s)")
    ax.set_title("三机各一弹的完整圆柱有效区间与联合遮蔽")
    ax.grid(axis="x", alpha=0.18)
    save_figure(fig, figure_dir / "problem4_fig2_coverage_gantt")


def figure_metrics(
    strategy: MultiDroneStrategy,
    union: list,
    target_points: np.ndarray,
    figure_dir: Path,
) -> tuple[np.ndarray, np.ndarray]:
    times = np.linspace(0.0, 30.0, 1201)
    rows = []
    for bomb in strategy.bombs:
        row = np.full(times.shape, np.inf)
        active = (times >= bomb.burst_time_s) & (
            times <= bomb.burst_time_s + CLOUD_LIFETIME
        )
        row[active] = full_cylinder_distances_for(
            bomb, times[active], target_points
        )
        rows.append(row)
    distances = np.vstack(rows)
    count = np.sum(distances <= CLOUD_RADIUS, axis=0)

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(7.2, 4.6),
        gridspec_kw={"height_ratios": [2.2, 1.0]},
        constrained_layout=True,
    )
    for drone_id, row, color, style in zip(
        DRONE_IDS, distances, DRONE_COLORS, DRONE_STYLES
    ):
        plot_row = np.where(np.isfinite(row), row, np.nan)
        axes[0].plot(
            times,
            plot_row,
            color=color,
            linestyle=style,
            linewidth=1.45,
            label=drone_id,
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
    axes[0].set_ylim(0.0, 45.0)
    axes[0].set_title("(a) 三个烟幕球的完整圆柱判据")
    axes[0].legend(frameon=False, ncol=4)
    axes[0].grid(alpha=0.18)

    axes[1].step(
        times,
        count,
        where="mid",
        color=OKABE_ITO["purple"],
        linewidth=1.7,
    )
    axes[1].fill_between(
        times,
        count,
        step="mid",
        color=OKABE_ITO["purple"],
        alpha=0.20,
    )
    axes[1].set_xlabel("任务下达后时间 (s)")
    axes[1].set_ylabel("同时有效弹数")
    axes[1].set_yticks([0, 1, 2, 3])
    axes[1].set_ylim(-0.1, 3.2)
    axes[1].set_title("(b) 联合覆盖计数")
    axes[1].grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem4_fig3_coverage_metrics")
    return times, distances


def figure_optimization(
    evidence: dict[str, dict[str, object]],
    individual: list[list],
    figure_dir: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.1), constrained_layout=True)
    for drone_id, color, style in zip(DRONE_IDS, DRONE_COLORS, DRONE_STYLES):
        run = evidence[drone_id]["duration_run"]
        axes[0].plot(
            run.history_best,
            color=color,
            linestyle=style,
            linewidth=1.45,
            label=drone_id,
        )
    axes[0].set_xlabel("进化代数")
    axes[0].set_ylabel("中心线个体时长 (s)")
    axes[0].set_title("(a) 三个单机代理搜索")
    axes[0].legend(frameon=False)
    axes[0].grid(alpha=0.18)

    values = [intervals_duration(items) for items in individual]
    bars = axes[1].bar(
        DRONE_IDS,
        values,
        color=DRONE_COLORS,
        width=0.62,
    )
    axes[1].set_ylim(0.0, 5.0)
    axes[1].set_ylabel("完整圆柱有效时长 (s)")
    axes[1].set_title("(b) 逐机种子与联合复算")
    axes[1].bar_label(bars, fmt="%.3f", padding=3, fontsize=8)
    axes[1].grid(axis="y", alpha=0.18)
    save_figure(fig, figure_dir / "problem4_fig4_optimization")


def sensitivity_rows(
    strategy: MultiDroneStrategy,
    target_points: np.ndarray,
) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for bomb in strategy.bombs:
        for offset in np.linspace(-2.0, 2.0, 33):
            candidate = DroneBombStrategy(
                bomb.drone_id,
                np.radians(bomb.heading_deg + offset),
                bomb.speed_mps,
                bomb.drop_time_s,
                bomb.fuse_delay_s,
            )
            rows.append(
                {
                    "drone_id": bomb.drone_id,
                    "parameter": "heading_offset_deg",
                    "value": float(offset),
                    "duration_s": individual_sampled_full_duration(
                        encode_bomb_strategy(candidate),
                        bomb.drone_id,
                        target_points,
                        step=0.03,
                    ),
                }
            )
        low = max(70.0, bomb.speed_mps - 20.0)
        high = min(140.0, bomb.speed_mps + 10.0)
        for speed in np.linspace(low, high, 31):
            candidate = DroneBombStrategy(
                bomb.drone_id,
                bomb.heading_rad,
                float(speed),
                bomb.drop_time_s,
                bomb.fuse_delay_s,
            )
            rows.append(
                {
                    "drone_id": bomb.drone_id,
                    "parameter": "speed_mps",
                    "value": float(speed),
                    "duration_s": individual_sampled_full_duration(
                        encode_bomb_strategy(candidate),
                        bomb.drone_id,
                        target_points,
                        step=0.03,
                    ),
                }
            )
    return rows


def figure_sensitivity(rows: list[dict[str, float | str]], figure_dir: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), constrained_layout=True)
    for drone_id, color, style in zip(DRONE_IDS, DRONE_COLORS, DRONE_STYLES):
        heading = [
            row
            for row in rows
            if row["drone_id"] == drone_id
            and row["parameter"] == "heading_offset_deg"
        ]
        speed = [
            row
            for row in rows
            if row["drone_id"] == drone_id and row["parameter"] == "speed_mps"
        ]
        axes[0].plot(
            [float(row["value"]) for row in heading],
            [float(row["duration_s"]) for row in heading],
            color=color,
            linestyle=style,
            linewidth=1.45,
            label=drone_id,
        )
        axes[1].plot(
            [float(row["value"]) for row in speed],
            [float(row["duration_s"]) for row in speed],
            color=color,
            linestyle=style,
            linewidth=1.45,
            label=drone_id,
        )
    axes[0].set_xlabel("航向偏差 (°)")
    axes[0].set_ylabel("个体有效时长 (s)")
    axes[0].set_title("(a) 航向扰动")
    axes[1].set_xlabel("速度 (m/s)")
    axes[1].set_ylabel("个体有效时长 (s)")
    axes[1].set_title("(b) 速度扰动")
    for ax in axes:
        ax.legend(frameon=False)
        ax.grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem4_fig5_sensitivity")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_existing(
    output_dir: Path,
) -> tuple[MultiDroneStrategy, dict[str, dict[str, object]]]:
    result = json.loads(
        (output_dir / "problem4_result.json").read_text(encoding="utf-8")
    )
    bombs = tuple(
        DroneBombStrategy(
            item["drone_id"],
            np.radians(item["heading_deg"]),
            item["speed_mps"],
            item["drop_time_s"],
            item["fuse_delay_s"],
        )
        for item in result["drones"]
    )
    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
    with (output_dir / "problem4_optimization_history.csv").open(
        newline="", encoding="utf-8-sig"
    ) as handle:
        for row in csv.DictReader(handle):
            grouped.setdefault((row["drone_id"], row["stage"]), []).append(row)
    evidence = {}
    for drone_id in DRONE_IDS:
        run_rows = grouped[(drone_id, "duration_proxy")]
        evidence[drone_id] = {
            "duration_run": SimpleNamespace(
                history_best=np.array(
                    [float(row["best_score"]) for row in run_rows]
                )
            )
        }
    return MultiDroneStrategy(bombs), evidence


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("Code/outputs"))
    parser.add_argument("--figure-dir", type=Path, default=Path("Paper/figures"))
    parser.add_argument("--reuse-result", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    configure_style()

    if args.reuse_result:
        strategy, evidence = load_existing(args.output_dir)
    else:
        strategy, evidence = optimize()

    convergence: dict[int, float] = {}
    final_individual = None
    final_union = None
    for n_theta in (180, 360, 720, 1440):
        points = cylinder_surface_points(n_theta=n_theta, n_z=11, n_r=8)
        individual, union = exact_multi_drone_intervals(
            strategy, points, scan_step=0.005
        )
        convergence[n_theta] = intervals_duration(union)
        if n_theta == 1440:
            final_individual = individual
            final_union = union
    assert final_individual is not None and final_union is not None

    drone_rows = []
    for bomb, intervals in zip(strategy.bombs, final_individual):
        drone_rows.append(
            {
                "drone_id": bomb.drone_id,
                "heading_deg": bomb.heading_deg,
                "speed_mps": bomb.speed_mps,
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
    single_cloud_union = merge_intervals(
        interval for intervals in final_individual for interval in intervals
    )
    single_cloud_union_duration = intervals_duration(single_cloud_union)
    result = {
        "criterion": (
            "for every sampled target sight line, at least one active smoke "
            "cloud intersects the finite missile-to-target segment"
        ),
        "objective": "maximize the joint three-cloud coverage duration",
        "decomposition": (
            "individual optimization supplies strong seeds; under the joint "
            "criterion it is not a general upper-bound proof.  For the reported "
            "strategy the three single-cloud intervals are disjoint and the "
            "joint recomputation adds no material spatial synergy."
        ),
        "drones": drone_rows,
        "union_intervals_s": [
            [item.start, item.end] for item in final_union
        ],
        "union_duration_s": union_duration,
        "single_cloud_union_duration_s": single_cloud_union_duration,
        "joint_synergy_duration_s": max(
            0.0, union_duration - single_cloud_union_duration
        ),
        "single_cloud_sum_minus_joint_s": overlap_duration(
            final_individual, final_union
        ),
        "theta_convergence_duration_s": {
            str(key): value for key, value in convergence.items()
        },
        "optimization": {
            "method": (
                "per-drone proximity seeding, centerline duration "
                "differential evolution, complete-cylinder ranking and "
                "coordinate refinement"
            ),
            "proximity_seeds": PROXIMITY_SEEDS,
            "duration_seeds": DURATION_SEEDS,
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
            "matplotlib": matplotlib.__version__,
        },
    }
    (args.output_dir / "problem4_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    interval_rows = []
    for drone_id, intervals in zip(DRONE_IDS, final_individual):
        for item in intervals:
            interval_rows.append(
                {
                    "series": drone_id,
                    "start_s": item.start,
                    "end_s": item.end,
                    "duration_s": item.duration,
                }
            )
    for item in final_union:
        interval_rows.append(
            {
                "series": "union",
                "start_s": item.start,
                "end_s": item.end,
                "duration_s": item.duration,
            }
        )
    write_csv(
        args.output_dir / "problem4_intervals.csv",
        ["series", "start_s", "end_s", "duration_s"],
        interval_rows,
    )

    if not args.reuse_result:
        history_rows = []
        for drone_id in DRONE_IDS:
            for stage, key in (
                ("proximity", "proximity_run"),
                ("duration_proxy", "duration_run"),
            ):
                run = evidence[drone_id][key]
                for generation, (best, mean) in enumerate(
                    zip(run.history_best, run.history_mean)
                ):
                    history_rows.append(
                        {
                            "drone_id": drone_id,
                            "stage": stage,
                            "generation": generation,
                            "best_score": best,
                            "mean_score": mean,
                        }
                    )
        write_csv(
            args.output_dir / "problem4_optimization_history.csv",
            [
                "drone_id",
                "stage",
                "generation",
                "best_score",
                "mean_score",
            ],
            history_rows,
        )

    figure_spatial(strategy, args.figure_dir)
    figure_gantt(final_individual, final_union, args.figure_dir)
    metric_points = cylinder_surface_points(n_theta=360, n_z=11, n_r=8)
    times, distances = figure_metrics(
        strategy, final_union, metric_points, args.figure_dir
    )
    time_rows = []
    for column, time in enumerate(times):
        time_rows.append(
            {
                "time_s": time,
                "FY1_worst_distance_m": (
                    distances[0, column]
                    if np.isfinite(distances[0, column])
                    else ""
                ),
                "FY2_worst_distance_m": (
                    distances[1, column]
                    if np.isfinite(distances[1, column])
                    else ""
                ),
                "FY3_worst_distance_m": (
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
        args.output_dir / "problem4_timeseries.csv",
        [
            "time_s",
            "FY1_worst_distance_m",
            "FY2_worst_distance_m",
            "FY3_worst_distance_m",
            "coverage_count",
        ],
        time_rows,
    )
    figure_optimization(evidence, final_individual, args.figure_dir)
    sensitivity_points = cylinder_surface_points(
        n_theta=96, n_z=7, n_r=6
    )
    sensitivity = sensitivity_rows(strategy, sensitivity_points)
    write_csv(
        args.output_dir / "problem4_sensitivity.csv",
        ["drone_id", "parameter", "value", "duration_s"],
        sensitivity,
    )
    figure_sensitivity(sensitivity, args.figure_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
