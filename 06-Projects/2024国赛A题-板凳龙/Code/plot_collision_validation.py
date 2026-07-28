"""Create the problem-2 first-collision validation figure."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import problem1_handle_distances, solve_handle_states  # noqa: E402
from collision import (  # noqa: E402
    bench_rectangles,
    minimum_nonadjacent_clearance,
    rectangle_corners,
)
from geometry import head_state  # noqa: E402


def apply_figure_style() -> None:
    """Apply a compact, colorblind-safe scientific figure style."""

    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Microsoft YaHei", "DejaVu Sans"],
            "font.size": 8,
            "axes.labelsize": 9,
            "axes.titlesize": 9,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.7,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "legend.frameon": False,
            "lines.linewidth": 1.5,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.05,
        }
    )


def chain_at(time: float):
    states = solve_handle_states(
        head_state(time),
        problem1_handle_distances(),
    )
    rectangles = bench_rectangles(states)
    clearance = minimum_nonadjacent_clearance(rectangles)
    return states, rectangles, clearance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-json", type=Path, required=True)
    args = parser.parse_args()

    result = json.loads(args.result_json.read_text(encoding="utf-8"))
    critical_time = float(result["criticalTime"])
    first_index, second_index = result["collisionPair"]
    _, rectangles, critical_clearance = chain_at(critical_time)

    apply_figure_style()
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.0, 3.0),
        constrained_layout=True,
    )

    selected_indices = range(0, 13)
    for index in selected_indices:
        rectangle = rectangles[index]
        if index == first_index:
            facecolor = "#D55E00"
            edgecolor = "#A84300"
            alpha = 0.55
            zorder = 4
        elif index == second_index:
            facecolor = "#0072B2"
            edgecolor = "#005080"
            alpha = 0.55
            zorder = 4
        else:
            facecolor = "#BDBDBD"
            edgecolor = "#666666"
            alpha = 0.28
            zorder = 2
        axes[0].add_patch(
            Polygon(
                rectangle_corners(rectangle),
                closed=True,
                facecolor=facecolor,
                edgecolor=edgecolor,
                linewidth=0.8,
                alpha=alpha,
                zorder=zorder,
            )
        )

    first = rectangles[first_index]
    second = rectangles[second_index]
    axes[0].annotate(
        "Head bench",
        (first.center_x, first.center_y),
        xytext=(-30, 18),
        textcoords="offset points",
        arrowprops={"arrowstyle": "-", "color": "#A84300", "linewidth": 0.8},
        color="#A84300",
    )
    axes[0].annotate(
        "Body bench 8",
        (second.center_x, second.center_y),
        xytext=(18, -25),
        textcoords="offset points",
        arrowprops={"arrowstyle": "-", "color": "#005080", "linewidth": 0.8},
        color="#005080",
    )

    all_corners = np.array(
        [
            corner
            for index in selected_indices
            for corner in rectangle_corners(rectangles[index])
        ]
    )
    center = 0.5 * (
        np.array([first.center_x, first.center_y])
        + np.array([second.center_x, second.center_y])
    )
    half_span = max(
        2.2,
        0.65
        * np.max(np.abs(all_corners - center), axis=None),
    )
    axes[0].set_xlim(center[0] - half_span, center[0] + half_span)
    axes[0].set_ylim(center[1] - half_span, center[1] + half_span)
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].set_xlabel("$x$ (m)")
    axes[0].set_ylabel("$y$ (m)")
    axes[0].set_title("A  First physical contact", loc="left")

    times = np.arange(400.0, 413.01, 0.1)
    margins = np.empty_like(times)
    for index, time in enumerate(times):
        _, _, clearance = chain_at(float(time))
        margins[index] = clearance.margin

    axes[1].plot(times, margins, color="#0072B2", label="Minimum SAT margin")
    axes[1].axhline(0.0, color="#555555", linewidth=0.8, linestyle="--")
    axes[1].axvline(
        critical_time,
        color="#D55E00",
        linewidth=1.0,
        linestyle=":",
        label=f"Contact: {critical_time:.6f} s",
    )
    axes[1].scatter(
        [critical_time],
        [0.0],
        color="#D55E00",
        edgecolor="black",
        linewidth=0.5,
        s=24,
        zorder=5,
    )
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Minimum separation margin (m)")
    axes[1].set_title("B  Collision-event localization", loc="left")
    axes[1].legend(loc="best")

    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / "q2_first_collision_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    print(f"critical_time={critical_time:.12f} s")
    print(
        f"collision_pair=({first_index}, {second_index}), "
        f"margin={critical_clearance.margin:.3e} m"
    )
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
