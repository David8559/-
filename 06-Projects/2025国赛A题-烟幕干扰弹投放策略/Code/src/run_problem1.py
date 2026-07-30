"""Run Problem 1, export data, and create the first four paper figures."""

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
from matplotlib.patches import Circle

from problem1_model import (
    BURST_POINT,
    BURST_TIME,
    CLOUD_DESCENT_SPEED,
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    DROP_POINT,
    DROP_TIME,
    FALSE_TARGET,
    FY1_INITIAL,
    M1_INITIAL,
    TRUE_TARGET_BOTTOM_CENTER,
    TRUE_TARGET_CENTER,
    TRUE_TARGET_HEIGHT,
    TRUE_TARGET_RADIUS,
    basic_results,
    bomb_position,
    centerline_distance,
    cloud_center,
    cylinder_surface_points,
    drone_position,
    full_cylinder_distance,
    missile_arrival_time,
    missile_position,
    point_to_segment_distance,
    representative_projection,
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
    fig.savefig(output_stem.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def draw_target_cylinder_3d(ax: plt.Axes) -> None:
    theta = np.linspace(0.0, 2.0 * np.pi, 80)
    z = np.linspace(0.0, TRUE_TARGET_HEIGHT, 2)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x = TRUE_TARGET_RADIUS * np.cos(theta_grid)
    y = 200.0 + TRUE_TARGET_RADIUS * np.sin(theta_grid)
    ax.plot_surface(
        x,
        y,
        z_grid,
        color=OKABE_ITO["green"],
        alpha=0.65,
        linewidth=0,
    )


def figure_global_scene(figure_dir: Path) -> None:
    fig = plt.figure(figsize=(7.2, 4.8))
    grid = fig.add_gridspec(1, 2, width_ratios=[1.20, 1.0], wspace=0.34)
    ax = fig.add_subplot(grid[0, 0], projection="3d")

    missile_times = np.linspace(0.0, 14.0, 300)
    missile_path = missile_position(missile_times)
    drone_times = np.linspace(0.0, BURST_TIME, 160)
    drone_path = drone_position(drone_times)
    bomb_times = np.linspace(DROP_TIME, BURST_TIME, 100)
    bomb_path = bomb_position(bomb_times)
    cloud_times = np.linspace(BURST_TIME, BURST_TIME + CLOUD_LIFETIME, 100)
    cloud_path = cloud_center(cloud_times)

    ax.plot(
        missile_path[:, 0],
        missile_path[:, 1],
        missile_path[:, 2],
        color=OKABE_ITO["vermillion"],
        linewidth=1.8,
        label="M1 轨迹",
    )
    ax.plot(
        drone_path[:, 0],
        drone_path[:, 1],
        drone_path[:, 2],
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="FY1 轨迹",
    )
    ax.plot(
        bomb_path[:, 0],
        bomb_path[:, 1],
        bomb_path[:, 2],
        color=OKABE_ITO["orange"],
        linewidth=1.8,
        linestyle="--",
        label="干扰弹轨迹",
    )
    ax.plot(
        cloud_path[:, 0],
        cloud_path[:, 1],
        cloud_path[:, 2],
        color=OKABE_ITO["gray"],
        linewidth=1.5,
        linestyle=":",
        label="烟幕中心",
    )
    ax.scatter(*FALSE_TARGET, marker="x", s=45, color=OKABE_ITO["black"], label="假目标")
    draw_target_cylinder_3d(ax)
    ax.scatter(
        *TRUE_TARGET_CENTER,
        marker="s",
        s=22,
        color=OKABE_ITO["green"],
        label="真目标",
    )
    ax.scatter(*DROP_POINT, s=25, color=OKABE_ITO["purple"], label="投放点")
    ax.scatter(*BURST_POINT, s=32, color=OKABE_ITO["yellow"], edgecolor="black", label="起爆点")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("")
    ax.text2D(0.91, 0.49, "z (m)", transform=ax.transAxes, rotation=90, va="center")
    ax.set_title("(a) 问题 1 全局三维运动场景")
    ax.view_init(elev=20, azim=-68)
    ax.legend(loc="upper left", frameon=False, ncol=2)

    ax2 = fig.add_subplot(grid[0, 1])
    ax2.plot(
        missile_path[:, 0],
        missile_path[:, 2],
        color=OKABE_ITO["vermillion"],
        linewidth=1.8,
        label="M1",
    )
    ax2.plot(
        drone_path[:, 0],
        drone_path[:, 2],
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="FY1",
    )
    ax2.plot(
        bomb_path[:, 0],
        bomb_path[:, 2],
        color=OKABE_ITO["orange"],
        linestyle="--",
        linewidth=1.8,
        label="干扰弹",
    )
    ax2.plot(
        cloud_path[:, 0],
        cloud_path[:, 2],
        color=OKABE_ITO["gray"],
        linestyle=":",
        linewidth=1.5,
        label="烟幕中心",
    )
    ax2.scatter(DROP_POINT[0], DROP_POINT[2], color=OKABE_ITO["purple"], s=28)
    ax2.scatter(
        BURST_POINT[0],
        BURST_POINT[2],
        color=OKABE_ITO["yellow"],
        edgecolor="black",
        s=34,
    )
    ax2.annotate(
        "投放",
        xy=(DROP_POINT[0], DROP_POINT[2]),
        xytext=(DROP_POINT[0] - 650, DROP_POINT[2] + 45),
        arrowprops={"arrowstyle": "->", "lw": 0.8},
    )
    ax2.annotate(
        "起爆",
        xy=(BURST_POINT[0], BURST_POINT[2]),
        xytext=(BURST_POINT[0] - 650, BURST_POINT[2] - 100),
        arrowprops={"arrowstyle": "->", "lw": 0.8},
    )
    ax2.set_xlim(15500, 20200)
    ax2.set_ylim(1500, 2050)
    ax2.set_xlabel("x (m)")
    ax2.set_ylabel("z (m)")
    ax2.set_title("(b) 交会区域 x-z 投影")
    ax2.grid(alpha=0.18)
    ax2.legend(frameon=False)
    fig.suptitle("图 1  M1、FY1、干扰弹与烟幕中心的空间关系", y=0.98)
    save_figure(fig, figure_dir / "problem1_fig1_global_scene")


def figure_occlusion_geometry(figure_dir: Path, representative_time: float) -> None:
    missile = missile_position(representative_time)
    cloud = cloud_center(representative_time)

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3))
    ax = axes[0]
    ax.plot(
        [missile[0], TRUE_TARGET_CENTER[0]],
        [missile[1], TRUE_TARGET_CENTER[1]],
        color=OKABE_ITO["black"],
        linewidth=1.2,
        label="中心视线",
    )
    theta = np.linspace(0.0, 2.0 * np.pi, 1440, endpoint=False)
    bottom_rim = np.column_stack(
        [
            TRUE_TARGET_RADIUS * np.cos(theta),
            200.0 + TRUE_TARGET_RADIUS * np.sin(theta),
            np.zeros_like(theta),
        ]
    )
    rim_distances, _ = point_to_segment_distance(cloud, missile, bottom_rim)
    worst_rim = bottom_rim[int(np.argmax(rim_distances))]
    ax.plot(
        [missile[0], worst_rim[0]],
        [missile[1], worst_rim[1]],
        color=OKABE_ITO["gray"],
        linewidth=1.0,
        linestyle="--",
        label="圆柱边缘视线",
    )
    ax.scatter(missile[0], missile[1], color=OKABE_ITO["vermillion"], s=35, label="M1")
    ax.scatter(
        cloud[0],
        cloud[1],
        color=OKABE_ITO["sky"],
        edgecolor=OKABE_ITO["blue"],
        s=45,
        label="烟幕中心",
    )
    ax.add_patch(
        Circle(
            (0.0, 200.0),
            TRUE_TARGET_RADIUS,
            facecolor=OKABE_ITO["green"],
            edgecolor=OKABE_ITO["green"],
            alpha=0.65,
            label="真目标水平截面",
        )
    )
    ax.set_xlim(-500, missile[0] + 500)
    ax.set_ylim(-30, 235)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_title(f"(a) 全局 x-y 投影，t={representative_time:.2f} s")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, loc="upper right")

    ax = axes[1]
    local_x = np.linspace(cloud[0] - 80, missile[0] + 35, 200)
    for target_z, color, linestyle, label in [
        (0.0, OKABE_ITO["black"], "-", "至目标底面视线"),
        (TRUE_TARGET_HEIGHT, OKABE_ITO["gray"], "--", "至目标顶面视线"),
    ]:
        slope = (missile[2] - target_z) / (missile[0] - 0.0)
        local_z = target_z + slope * local_x
        ax.plot(
            local_x,
            local_z,
            color=color,
            linewidth=1.1,
            linestyle=linestyle,
            label=label,
        )
    ax.scatter(missile[0], missile[2], color=OKABE_ITO["vermillion"], s=35, label="M1")
    ax.add_patch(
        Circle(
            (cloud[0], cloud[2]),
            CLOUD_RADIUS,
            facecolor=OKABE_ITO["sky"],
            edgecolor=OKABE_ITO["blue"],
            alpha=0.45,
            label="烟幕有效域",
        )
    )
    ax.set_xlim(cloud[0] - 60, missile[0] + 50)
    ax.set_ylim(cloud[2] - 45, missile[2] + 45)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("z (m)")
    ax.set_title(f"(b) 烟幕附近 x-z 实尺度放大")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, loc="lower right")
    fig.suptitle("图 2  导弹视线—烟幕球—圆柱目标遮蔽几何", y=1.01)
    save_figure(fig, figure_dir / "problem1_fig2_occlusion_geometry")


def figure_timeline(figure_dir: Path, result: dict[str, object]) -> None:
    robust_start, robust_end = result["full_cylinder_intervals_s"][0]
    arrival = result["missile_arrival_time_s"]

    fig, axes = plt.subplots(2, 1, figsize=(7.2, 4.6))
    rows = {"任务/飞行": 3, "干扰弹": 2, "烟幕": 1, "有效遮蔽": 0}

    def draw_bars(ax: plt.Axes) -> None:
        ax.hlines(rows["任务/飞行"], 0, arrival, color=OKABE_ITO["blue"], linewidth=4)
        ax.hlines(
            rows["干扰弹"],
            DROP_TIME,
            BURST_TIME,
            color=OKABE_ITO["orange"],
            linewidth=6,
        )
        ax.hlines(
            rows["烟幕"],
            BURST_TIME,
            BURST_TIME + CLOUD_LIFETIME,
            color=OKABE_ITO["gray"],
            linewidth=7,
        )
        ax.hlines(
            rows["有效遮蔽"],
            robust_start,
            robust_end,
            color=OKABE_ITO["green"],
            linewidth=8,
        )
        ax.set_yticks(list(rows.values()), list(rows.keys()))
        ax.set_ylim(-0.6, 3.75)
        ax.grid(axis="x", alpha=0.15)

    ax = axes[0]
    draw_bars(ax)
    ax.axvline(BURST_TIME + CLOUD_LIFETIME, color="#9CA3AF", linewidth=0.8, linestyle="--")
    ax.axvline(arrival, color="#9CA3AF", linewidth=0.8, linestyle="--")
    ax.text(
        BURST_TIME + CLOUD_LIFETIME,
        3.35,
        f"烟幕失效 {BURST_TIME + CLOUD_LIFETIME:.2f} s",
        ha="center",
        fontsize=7,
    )
    ax.text(
        arrival,
        3.35,
        f"M1 到达假目标 {arrival:.2f} s",
        ha="center",
        fontsize=7,
    )
    ax.set_xlim(-1, arrival + 2)
    ax.set_title("(a) 全过程")

    ax = axes[1]
    draw_bars(ax)
    early_events = [
        (0.0, "受领 0.00 s", 0.05, 3.40, "left"),
        (DROP_TIME, "投放 1.50 s", 1.35, 3.10, "left"),
        (BURST_TIME, "起爆 5.10 s", 4.75, 3.40, "center"),
        (robust_start, "遮蔽开始 8.06 s", 7.65, 3.10, "center"),
        (robust_end, "遮蔽结束 9.45 s", 9.80, 3.40, "center"),
    ]
    for time, label, text_x, text_y, alignment in early_events:
        ax.axvline(time, color="#9CA3AF", linewidth=0.7, linestyle="--")
        ax.annotate(
            label,
            xy=(time, 2.95),
            xytext=(text_x, text_y),
            ha=alignment,
            va="bottom",
            fontsize=7,
            arrowprops={"arrowstyle": "-", "lw": 0.6, "color": "#6B7280"},
        )
    ax.set_xlim(-0.3, 11.0)
    ax.set_xlabel("绝对时间 t (s)")
    ax.set_title("(b) 前 11 s 放大")
    fig.suptitle("图 3  问题 1 关键事件时间轴", y=0.995)
    fig.tight_layout()
    save_figure(fig, figure_dir / "problem1_fig3_timeline")


def figure_occlusion_metric(
    figure_dir: Path, result: dict[str, object], target_points: np.ndarray
) -> None:
    times = np.linspace(7.75, 9.58, 700)
    center_distance = np.array([centerline_distance(float(t)) for t in times])
    robust_distance = np.array(
        [full_cylinder_distance(float(t), target_points) for t in times]
    )
    exit_times = np.linspace(9.30, 9.58, 500)
    projection = np.array(
        [representative_projection(float(t)) for t in exit_times]
    )
    missile_cloud_distance = np.linalg.norm(
        missile_position(exit_times) - cloud_center(exit_times), axis=1
    )
    robust_start, robust_end = result["full_cylinder_intervals_s"][0]

    fig, axes = plt.subplots(2, 1, figsize=(7.2, 5.6), sharex=False)
    ax = axes[0]
    ax.plot(
        times,
        robust_distance,
        color=OKABE_ITO["blue"],
        linewidth=1.8,
        label="圆柱完全遮蔽：最不利视线距离",
    )
    ax.plot(
        times,
        center_distance,
        color=OKABE_ITO["orange"],
        linewidth=1.5,
        linestyle="--",
        label="几何中心视线距离",
    )
    ax.axhline(CLOUD_RADIUS, color=OKABE_ITO["black"], linewidth=1.0, label="有效半径 10 m")
    ax.axvspan(robust_start, robust_end, color=OKABE_ITO["green"], alpha=0.16)
    ax.axvline(robust_start, color=OKABE_ITO["green"], linewidth=0.9, linestyle=":")
    ax.axvline(robust_end, color=OKABE_ITO["green"], linewidth=0.9, linestyle=":")
    ax.set_ylabel("视线到烟幕中心距离 (m)")
    ax.set_ylim(0.0, 22.0)
    ax.set_xlim(times[0], times[-1])
    ax.set_title("(a) 两种遮蔽口径及稳健有效区间")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False)

    ax = axes[1]
    ax.plot(
        exit_times,
        missile_cloud_distance,
        color=OKABE_ITO["vermillion"],
        linewidth=1.7,
        label="M1—烟幕中心距离",
    )
    ax.axhline(CLOUD_RADIUS, color=OKABE_ITO["black"], linewidth=1.0, label="10 m")
    ax2 = ax.twinx()
    ax2.plot(
        exit_times,
        projection,
        color=OKABE_ITO["purple"],
        linewidth=1.4,
        linestyle=":",
        label="中心视线投影参数 λ",
    )
    ax2.axhline(0.0, color=OKABE_ITO["gray"], linewidth=0.8, linestyle="--")
    ax.axvspan(robust_start, robust_end, color=OKABE_ITO["green"], alpha=0.16)
    ax.axvline(robust_end, color=OKABE_ITO["green"], linewidth=0.9, linestyle=":")
    ax.set_xlabel("绝对时间 t (s)")
    ax.set_ylabel("M1—烟幕中心距离 (m)")
    ax.set_ylim(0.0, 45.0)
    ax.set_xlim(exit_times[0], exit_times[-1])
    ax2.set_ylabel("投影参数 λ")
    ax.set_title("(b) 遮蔽结束由 M1 穿过并离开烟幕控制")
    ax.grid(alpha=0.18)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, frameon=False, loc="upper left")
    fig.suptitle("图 4  问题 1 遮蔽判据随时间变化", y=0.98)
    fig.subplots_adjust(
        left=0.10, right=0.91, bottom=0.09, top=0.86, hspace=0.42
    )
    save_figure(fig, figure_dir / "problem1_fig4_occlusion_metric")


def convergence_results(theta_counts: list[int]) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for count in theta_counts:
        result = basic_results(n_theta=count)
        start, end = result["full_cylinder_intervals_s"][0]
        rows.append(
            {
                "n_theta": count,
                "start_s": float(start),
                "end_s": float(end),
                "duration_s": float(result["full_cylinder_duration_s"]),
            }
        )
    return rows


def write_timeseries(
    output_path: Path, target_points: np.ndarray, start: float, end: float
) -> None:
    times = np.linspace(start, end, 1501)
    with output_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(
            [
                "time_s",
                "centerline_distance_m",
                "full_cylinder_worst_distance_m",
                "centerline_projection_lambda",
                "missile_cloud_distance_m",
            ]
        )
        for time in times:
            writer.writerow(
                [
                    f"{time:.8f}",
                    f"{centerline_distance(float(time)):.8f}",
                    f"{full_cylinder_distance(float(time), target_points):.8f}",
                    f"{representative_projection(float(time)):.10f}",
                    f"{np.linalg.norm(missile_position(time)-cloud_center(time)):.8f}",
                ]
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--figure-dir", type=Path, required=True)
    parser.add_argument("--n-theta", type=int, default=1440)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    configure_style()

    result = basic_results(n_theta=args.n_theta)
    result["convergence"] = convergence_results([360, 720, 1440, 2880])
    result["environment"] = {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "matplotlib": matplotlib.__version__,
        "platform": platform.platform(),
        "command": "python Code/src/run_problem1.py --output-dir Code/outputs --figure-dir Paper/figures",
    }

    target_points = cylinder_surface_points(n_theta=args.n_theta)
    with (args.output_dir / "problem1_result.json").open(
        "w", encoding="utf-8"
    ) as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)

    write_timeseries(
        args.output_dir / "problem1_timeseries.csv",
        target_points,
        BURST_TIME,
        11.0,
    )
    figure_global_scene(args.figure_dir)
    robust_start, robust_end = result["full_cylinder_intervals_s"][0]
    figure_occlusion_geometry(
        args.figure_dir, representative_time=0.5 * (robust_start + robust_end)
    )
    figure_timeline(args.figure_dir, result)
    figure_occlusion_metric(args.figure_dir, result, target_points)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.exit(main())
