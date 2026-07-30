"""Optimize Problem 2, export evidence, and generate publication figures."""

from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from problem1_model import (
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    FALSE_TARGET,
    FY1_INITIAL,
    M1_INITIAL,
    TRUE_TARGET_BOTTOM_CENTER,
    TRUE_TARGET_CENTER,
    TRUE_TARGET_HEIGHT,
    cylinder_surface_points,
    missile_position,
)
from problem2_model import (
    Strategy,
    baseline_problem1_strategy,
    burst_point,
    centerline_distances_for,
    centerline_proxy_duration,
    cloud_center_for,
    coarse_target_points,
    coordinate_refine,
    decision_from_strategy,
    differential_evolution_maximize,
    drop_point,
    exact_full_cylinder_intervals,
    full_cylinder_distances_for,
    interval_duration,
    sampled_full_cylinder_duration,
    strategy_from_decision,
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

OPTIMIZATION_SEEDS = (20250731, 20250732, 7)


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


def optimize() -> tuple[
    Strategy,
    list,
    list[float],
    dict[int, float],
]:
    baseline = decision_from_strategy(baseline_problem1_strategy())
    proxy_runs = [
        differential_evolution_maximize(
            centerline_proxy_duration,
            seed=seed,
            population_size=96,
            generations=180,
            initial_decisions=[baseline],
        )
        for seed in OPTIMIZATION_SEEDS
    ]

    candidate_decisions: list[np.ndarray] = []
    for run in proxy_runs:
        candidate_decisions.extend(run.population[:8])

    coarse_points = coarse_target_points()
    coarse_objective = lambda decision: sampled_full_cylinder_duration(
        decision, coarse_points, step=0.02
    )
    ranked = sorted(
        (
            (float(coarse_objective(candidate)), np.asarray(candidate).copy())
            for candidate in candidate_decisions
        ),
        key=lambda item: item[0],
        reverse=True,
    )

    refined: list[tuple[float, np.ndarray, list[float]]] = []
    for _, candidate in ranked[:3]:
        decision, score, history = coordinate_refine(
            candidate,
            coarse_objective,
            initial_steps=(0.02, 1.0, 0.08, 0.02),
            minimum_steps=(1e-5, 0.005, 1e-4, 1e-5),
            max_rounds=100,
        )
        refined.append((score, decision, history))
    refined.sort(key=lambda item: item[0], reverse=True)

    # The global search consistently reaches speed=140 m/s, drop time=0, and
    # fuse fraction=1. Refine only heading and burst time with a denser target.
    medium_points = cylinder_surface_points(n_theta=96, n_z=11, n_r=8)
    medium_objective = lambda decision: interval_duration(
        exact_full_cylinder_intervals(
            strategy_from_decision(decision), medium_points, scan_step=0.01
        )
    )
    best_decision, _, exact_history = coordinate_refine(
        refined[0][1],
        medium_objective,
        initial_steps=(0.001, 0.0, 0.004, 0.0),
        minimum_steps=(1e-7, 0.0, 1e-6, 0.0),
        max_rounds=50,
    )
    strategy = strategy_from_decision(best_decision)

    convergence: dict[int, float] = {}
    for n_theta in (180, 360, 720, 1440):
        points = cylinder_surface_points(n_theta=n_theta, n_z=11, n_r=8)
        intervals = exact_full_cylinder_intervals(
            strategy, points, scan_step=0.005
        )
        convergence[n_theta] = interval_duration(intervals)
    return strategy, proxy_runs, exact_history, convergence


def bomb_path(strategy: Strategy, times: np.ndarray) -> np.ndarray:
    tau = times - strategy.drop_time_s
    return (
        drop_point(strategy)
        + tau[:, None] * strategy.drone_velocity
        + np.column_stack(
            [np.zeros_like(tau), np.zeros_like(tau), -4.9 * tau**2]
        )
    )


def figure_optimal_geometry(
    strategy: Strategy,
    interval_start: float,
    interval_end: float,
    figure_dir: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), constrained_layout=True)
    ax_xy, ax_xz = axes
    end_time = interval_end + 0.5
    missile_times = np.linspace(0.0, end_time, 260)
    missiles = missile_position(missile_times)
    drone_times = np.linspace(0.0, strategy.burst_time_s, 80)
    drones = FY1_INITIAL + drone_times[:, None] * strategy.drone_velocity
    bomb_times = np.linspace(strategy.drop_time_s, strategy.burst_time_s, 80)
    bombs = bomb_path(strategy, bomb_times)
    cloud_times = np.linspace(strategy.burst_time_s, end_time, 120)
    clouds = cloud_center_for(strategy, cloud_times)

    ax_xy.plot(
        missiles[:, 0],
        missiles[:, 1],
        color=OKABE_ITO["vermillion"],
        linewidth=1.8,
        label="M1",
    )
    ax_xy.plot(
        drones[:, 0],
        drones[:, 1],
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="FY1",
    )
    ax_xy.plot(
        bombs[:, 0],
        bombs[:, 1],
        color=OKABE_ITO["orange"],
        linestyle="--",
        linewidth=1.6,
        label="干扰弹",
    )
    cloud_xy = burst_point(strategy)[:2]
    ax_xy.scatter(
        *cloud_xy,
        color=OKABE_ITO["yellow"],
        edgecolor="black",
        zorder=5,
        label="起爆/烟幕水平位置",
    )
    for time, style, label in (
        (interval_start, "-", "遮蔽开始视线"),
        (interval_end, ":", "遮蔽结束视线"),
    ):
        missile = missile_position(time)
        ax_xy.plot(
            [missile[0], TRUE_TARGET_CENTER[0]],
            [missile[1], TRUE_TARGET_CENTER[1]],
            color=OKABE_ITO["gray"],
            linestyle=style,
            linewidth=1.0,
            label=label,
        )
    ax_xy.scatter(
        *TRUE_TARGET_CENTER[:2],
        marker="s",
        color=OKABE_ITO["green"],
        label="真目标",
    )
    ax_xy.scatter(
        *FALSE_TARGET[:2],
        marker="x",
        color=OKABE_ITO["black"],
        label="假目标",
    )
    ax_xy.set_xlabel("x (m)")
    ax_xy.set_ylabel("y (m)")
    ax_xy.set_title("(a) 水平面最优几何关系")
    ax_xy.legend(frameon=False, loc="best")
    ax_xy.grid(alpha=0.18)

    ax_xz.plot(
        missiles[:, 0],
        missiles[:, 2],
        color=OKABE_ITO["vermillion"],
        linewidth=1.8,
        label="M1",
    )
    ax_xz.plot(
        drones[:, 0],
        drones[:, 2],
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="FY1",
    )
    ax_xz.plot(
        bombs[:, 0],
        bombs[:, 2],
        color=OKABE_ITO["orange"],
        linestyle="--",
        linewidth=1.6,
        label="干扰弹",
    )
    ax_xz.plot(
        clouds[:, 0],
        clouds[:, 2],
        color=OKABE_ITO["purple"],
        linestyle=":",
        linewidth=1.8,
        label="烟幕中心",
    )
    ax_xz.scatter(
        burst_point(strategy)[0],
        burst_point(strategy)[2],
        color=OKABE_ITO["yellow"],
        edgecolor="black",
        zorder=5,
    )
    for time, style in ((interval_start, "-"), (interval_end, ":")):
        missile = missile_position(time)
        ax_xz.plot(
            [missile[0], TRUE_TARGET_CENTER[0]],
            [missile[2], TRUE_TARGET_CENTER[2]],
            color=OKABE_ITO["gray"],
            linestyle=style,
            linewidth=1.0,
        )
    ax_xz.fill_between(
        [-7.0, 7.0],
        [0.0, 0.0],
        [TRUE_TARGET_HEIGHT, TRUE_TARGET_HEIGHT],
        color=OKABE_ITO["green"],
        alpha=0.55,
        label="真目标圆柱",
    )
    ax_xz.set_xlabel("x (m)")
    ax_xz.set_ylabel("z (m)")
    ax_xz.set_title("(b) 竖直剖面的抛体与烟幕轨迹")
    ax_xz.legend(frameon=False, loc="best")
    ax_xz.grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem2_fig1_optimal_geometry")


def objective_landscape(
    strategy: Strategy,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    headings = np.linspace(strategy.heading_deg - 2.0, strategy.heading_deg + 2.0, 41)
    burst_times = np.linspace(
        max(0.05, strategy.burst_time_s - 0.35),
        strategy.burst_time_s + 0.35,
        41,
    )
    points = cylinder_surface_points(n_theta=24, n_z=4, n_r=3)
    durations = np.empty((len(burst_times), len(headings)))
    for row, burst_time in enumerate(burst_times):
        for column, heading_deg in enumerate(headings):
            candidate = Strategy(
                heading_rad=np.radians(heading_deg),
                speed_mps=140.0,
                drop_time_s=0.0,
                fuse_delay_s=float(burst_time),
            )
            durations[row, column] = sampled_full_cylinder_duration(
                decision_from_strategy(candidate), points, step=0.04
            )
    return headings, burst_times, durations


def figure_landscape(
    strategy: Strategy,
    headings: np.ndarray,
    burst_times: np.ndarray,
    durations: np.ndarray,
    figure_dir: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(5.2, 3.8), constrained_layout=True)
    image = ax.imshow(
        durations,
        origin="lower",
        aspect="auto",
        extent=[headings[0], headings[-1], burst_times[0], burst_times[-1]],
        cmap="viridis",
    )
    contours = ax.contour(
        headings,
        burst_times,
        durations,
        levels=7,
        colors="white",
        linewidths=0.55,
        alpha=0.75,
    )
    ax.clabel(contours, inline=True, fontsize=7, fmt="%.2f")
    ax.scatter(
        strategy.heading_deg,
        strategy.burst_time_s,
        marker="*",
        s=90,
        color=OKABE_ITO["vermillion"],
        edgecolor="white",
        linewidth=0.7,
    )
    ax.annotate(
        f"最终解\n({strategy.heading_deg:.3f}°, {strategy.burst_time_s:.3f} s)",
        xy=(strategy.heading_deg, strategy.burst_time_s),
        xytext=(strategy.heading_deg + 0.55, strategy.burst_time_s - 0.18),
        arrowprops={"arrowstyle": "->", "color": "white", "linewidth": 0.9},
        color="white",
        fontsize=8,
        ha="left",
        va="top",
    )
    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("完整圆柱遮蔽时长 (s)")
    ax.set_xlabel("FY1 航向 (°，正 x 轴逆时针)")
    ax.set_ylabel("起爆时刻 (s)")
    ax.set_title("问题 2 局部目标函数地形（v=140 m/s，立即投放）")
    save_figure(fig, figure_dir / "problem2_fig2_objective_landscape")


def figure_convergence(
    proxy_runs: list,
    final_duration: float,
    baseline_duration: float,
    figure_dir: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), constrained_layout=True)
    for run, seed, style in zip(proxy_runs, OPTIMIZATION_SEEDS, ("-", "--", ":")):
        axes[0].plot(
            run.history_best,
            linestyle=style,
            linewidth=1.5,
            label=f"seed={seed}",
        )
    axes[0].set_xlabel("差分进化代数")
    axes[0].set_ylabel("中心视线代理时长 (s)")
    axes[0].set_title("(a) 多起点全局搜索收敛")
    axes[0].legend(frameon=False)
    axes[0].grid(alpha=0.18)

    stage_labels = ["问题 1\n固定策略", "中心视线\n代理最优", "完整圆柱\n最终复算"]
    stage_values = [
        baseline_duration,
        max(float(run.score) for run in proxy_runs),
        final_duration,
    ]
    bars = axes[1].bar(
        stage_labels,
        stage_values,
        color=[
            OKABE_ITO["gray"],
            OKABE_ITO["orange"],
            OKABE_ITO["blue"],
        ],
        width=0.62,
    )
    axes[1].set_ylabel("遮蔽时长 (s)")
    axes[1].set_title("(b) 代理筛选与主判据复算")
    axes[1].set_ylim(0.0, 5.2)
    axes[1].bar_label(bars, fmt="%.3f", padding=3, fontsize=8)
    axes[1].grid(axis="y", alpha=0.18)
    save_figure(fig, figure_dir / "problem2_fig3_convergence")


def figure_metric_and_timeline(
    strategy: Strategy,
    interval_start: float,
    interval_end: float,
    times: np.ndarray,
    full_distances: np.ndarray,
    center_distances: np.ndarray,
    figure_dir: Path,
) -> None:
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(7.2, 4.5),
        gridspec_kw={"height_ratios": [2.2, 1.0]},
        constrained_layout=True,
    )
    ax = axes[0]
    ax.plot(
        times,
        full_distances,
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="完整圆柱最不利视线",
    )
    ax.plot(
        times,
        center_distances,
        color=OKABE_ITO["orange"],
        linestyle="--",
        linewidth=1.4,
        label="目标中心视线",
    )
    ax.axhline(
        CLOUD_RADIUS,
        color=OKABE_ITO["black"],
        linestyle=":",
        linewidth=1.1,
        label="烟幕有效半径 10 m",
    )
    ax.axvspan(
        interval_start,
        interval_end,
        color=OKABE_ITO["sky"],
        alpha=0.22,
        label="完整圆柱有效遮蔽",
    )
    ax.set_xlabel("任务下达后时间 (s)")
    ax.set_ylabel("烟幕中心至视线距离 (m)")
    ax.set_title("(a) 最优策略的遮蔽判据随时间变化")
    ax.legend(frameon=False, ncol=2)
    ax.grid(alpha=0.18)

    timeline = axes[1]
    timeline.broken_barh(
        [(strategy.burst_time_s, CLOUD_LIFETIME)],
        (2.5, 0.55),
        facecolors=OKABE_ITO["gray"],
        alpha=0.45,
        label="烟幕有效期",
    )
    timeline.broken_barh(
        [(interval_start, interval_end - interval_start)],
        (1.45, 0.55),
        facecolors=OKABE_ITO["sky"],
        label="有效遮蔽",
    )
    timeline.scatter(
        [strategy.drop_time_s, strategy.burst_time_s],
        [0.7, 0.7],
        color=[OKABE_ITO["purple"], OKABE_ITO["yellow"]],
        edgecolor="black",
        zorder=3,
    )
    timeline.text(strategy.drop_time_s, 0.35, "投放", ha="left", va="top")
    timeline.text(strategy.burst_time_s, 0.35, "起爆", ha="center", va="top")
    timeline.set_xlim(0.0, max(interval_end + 1.0, 7.0))
    timeline.set_ylim(0.0, 3.3)
    timeline.set_yticks([0.7, 1.72, 2.77], ["事件", "遮蔽", "烟幕"])
    timeline.set_xlabel("任务下达后时间 (s)")
    timeline.set_title("(b) 投放、起爆与有效遮蔽时间轴")
    timeline.legend(frameon=False, loc="upper right")
    save_figure(fig, figure_dir / "problem2_fig4_metric_timeline")


def sensitivity_rows(strategy: Strategy) -> list[dict[str, float | str]]:
    points = coarse_target_points()
    rows: list[dict[str, float | str]] = []
    scenarios = {
        "航向偏差": [
            (
                offset,
                Strategy(
                    np.radians(strategy.heading_deg + offset),
                    strategy.speed_mps,
                    strategy.drop_time_s,
                    strategy.fuse_delay_s,
                ),
            )
            for offset in np.linspace(-1.5, 1.5, 25)
        ],
        "速度": [
            (
                value,
                Strategy(
                    strategy.heading_rad,
                    float(value),
                    strategy.drop_time_s,
                    strategy.fuse_delay_s,
                ),
            )
            for value in np.linspace(100.0, 140.0, 25)
        ],
        "投放延迟": [
            (
                delay,
                Strategy(
                    strategy.heading_rad,
                    strategy.speed_mps,
                    float(delay),
                    strategy.fuse_delay_s,
                ),
            )
            for delay in np.linspace(0.0, 0.8, 25)
        ],
        "引信延迟": [
            (
                value,
                Strategy(
                    strategy.heading_rad,
                    strategy.speed_mps,
                    strategy.drop_time_s,
                    float(value),
                ),
            )
            for value in np.linspace(
                max(0.05, strategy.fuse_delay_s - 0.25),
                strategy.fuse_delay_s + 0.25,
                25,
            )
        ],
    }
    for parameter, candidates in scenarios.items():
        for value, candidate in candidates:
            duration = sampled_full_cylinder_duration(
                decision_from_strategy(candidate), points, step=0.02
            )
            rows.append(
                {
                    "parameter": parameter,
                    "value": float(value),
                    "duration_s": float(duration),
                }
            )
    return rows


def figure_sensitivity(
    rows: list[dict[str, float | str]], figure_dir: Path
) -> None:
    labels = {
        "航向偏差": ("航向偏差 (°)", OKABE_ITO["blue"]),
        "速度": ("飞行速度 (m/s)", OKABE_ITO["green"]),
        "投放延迟": ("投放时刻 (s)", OKABE_ITO["purple"]),
        "引信延迟": ("引信延迟 (s)", OKABE_ITO["orange"]),
    }
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.2), constrained_layout=True)
    for panel, (parameter, (xlabel, color)) in enumerate(labels.items()):
        ax = axes.flat[panel]
        selected = [row for row in rows if row["parameter"] == parameter]
        x = np.array([float(row["value"]) for row in selected])
        y = np.array([float(row["duration_s"]) for row in selected])
        ax.plot(x, y, color=color, linewidth=1.7, marker="o", markersize=2.5)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("完整圆柱遮蔽时长 (s)")
        ax.set_title(f"({chr(97 + panel)}) {parameter}单因素扰动")
        ax.grid(alpha=0.18)
    save_figure(fig, figure_dir / "problem2_fig5_sensitivity")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("Code/outputs"))
    parser.add_argument("--figure-dir", type=Path, default=Path("Paper/figures"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    configure_style()

    strategy, proxy_runs, exact_history, convergence = optimize()
    final_points = cylinder_surface_points(n_theta=1440, n_z=11, n_r=8)
    final_intervals = exact_full_cylinder_intervals(
        strategy, final_points, scan_step=0.005
    )
    final_duration = interval_duration(final_intervals)
    if len(final_intervals) != 1:
        raise RuntimeError("Expected one effective interval for the optimal strategy.")
    effective = final_intervals[0]

    times = np.linspace(
        strategy.burst_time_s,
        min(strategy.burst_time_s + CLOUD_LIFETIME, effective.end + 1.0),
        900,
    )
    full_distances = full_cylinder_distances_for(
        strategy, times, cylinder_surface_points(n_theta=360)
    )
    center_distances = centerline_distances_for(strategy, times)
    sensitivity = sensitivity_rows(strategy)
    headings, burst_times, landscape = objective_landscape(strategy)

    baseline_points = cylinder_surface_points(n_theta=720)
    baseline_duration = interval_duration(
        exact_full_cylinder_intervals(
            baseline_problem1_strategy(), baseline_points, scan_step=0.01
        )
    )
    result = {
        "criterion": "complete-cylinder all-sampled-boundary sight lines",
        "heading_deg": strategy.heading_deg,
        "speed_mps": strategy.speed_mps,
        "drop_time_s": strategy.drop_time_s,
        "fuse_delay_s": strategy.fuse_delay_s,
        "burst_time_s": strategy.burst_time_s,
        "drop_point_m": drop_point(strategy).tolist(),
        "burst_point_m": burst_point(strategy).tolist(),
        "effective_intervals_s": [
            [interval.start, interval.end] for interval in final_intervals
        ],
        "effective_duration_s": final_duration,
        "baseline_problem1_duration_s": baseline_duration,
        "improvement_s": final_duration - baseline_duration,
        "improvement_ratio": final_duration / baseline_duration,
        "theta_convergence_duration_s": {
            str(key): value for key, value in convergence.items()
        },
        "optimization": {
            "method": "multi-seed differential evolution on centerline proxy; complete-cylinder ranking and coordinate refinement",
            "seeds": list(OPTIMIZATION_SEEDS),
            "proxy_best_duration_s": [
                float(run.score) for run in proxy_runs
            ],
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
            "matplotlib": matplotlib.__version__,
        },
    }
    (args.output_dir / "problem2_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    time_rows = [
        {
            "time_s": float(time),
            "full_cylinder_distance_m": float(full_distance),
            "centerline_distance_m": float(center_distance),
            "full_cylinder_effective": int(full_distance <= CLOUD_RADIUS),
        }
        for time, full_distance, center_distance in zip(
            times, full_distances, center_distances
        )
    ]
    write_csv(
        args.output_dir / "problem2_timeseries.csv",
        [
            "time_s",
            "full_cylinder_distance_m",
            "centerline_distance_m",
            "full_cylinder_effective",
        ],
        time_rows,
    )
    history_rows = []
    for run_index, (run, seed) in enumerate(zip(proxy_runs, OPTIMIZATION_SEEDS)):
        for generation, (best, mean) in enumerate(
            zip(run.history_best, run.history_mean)
        ):
            history_rows.append(
                {
                    "run": run_index + 1,
                    "seed": seed,
                    "generation": generation,
                    "best_proxy_duration_s": float(best),
                    "mean_proxy_duration_s": float(mean),
                }
            )
    write_csv(
        args.output_dir / "problem2_optimization_history.csv",
        [
            "run",
            "seed",
            "generation",
            "best_proxy_duration_s",
            "mean_proxy_duration_s",
        ],
        history_rows,
    )
    write_csv(
        args.output_dir / "problem2_sensitivity.csv",
        ["parameter", "value", "duration_s"],
        sensitivity,
    )

    figure_optimal_geometry(strategy, effective.start, effective.end, args.figure_dir)
    figure_landscape(
        strategy, headings, burst_times, landscape, args.figure_dir
    )
    figure_convergence(
        proxy_runs,
        final_duration,
        baseline_duration,
        args.figure_dir,
    )
    figure_metric_and_timeline(
        strategy,
        effective.start,
        effective.end,
        times,
        full_distances,
        center_distances,
        args.figure_dir,
    )
    figure_sensitivity(sensitivity, args.figure_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
