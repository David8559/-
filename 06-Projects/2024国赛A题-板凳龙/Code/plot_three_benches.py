"""Create the three-bench geometry and chord-residual validation figure."""

from __future__ import annotations

import sys
from math import hypot
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import first_bench_distances, solve_handle_positions  # noqa: E402
from geometry import head_state, spiral_xy  # noqa: E402


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


def main() -> None:
    apply_figure_style()
    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    distances = first_bench_distances(3)
    initial_head = head_state(0.0)
    initial_points = solve_handle_positions(initial_head.theta, distances)

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.0, 3.1),
        constrained_layout=True,
    )

    # Panel A: local spiral and three rigid handle-to-handle chords.
    theta_min = initial_points[0].theta - 0.25
    theta_max = initial_points[-1].theta + 0.25
    theta_curve = np.linspace(theta_min, theta_max, 800)
    spiral_points = np.array([spiral_xy(float(theta)) for theta in theta_curve])
    axes[0].plot(
        spiral_points[:, 0],
        spiral_points[:, 1],
        color="#0072B2",
        linestyle="--",
        label="Spiral path",
        zorder=1,
    )

    x_values = np.array([point.x for point in initial_points])
    y_values = np.array([point.y for point in initial_points])
    axes[0].plot(
        x_values,
        y_values,
        color="#D55E00",
        marker="o",
        markerfacecolor="white",
        markeredgecolor="black",
        label="Rigid chords",
        zorder=2,
    )
    for point in initial_points:
        axes[0].annotate(
            f"$P_{point.index}$",
            (point.x, point.y),
            xytext=(4, 4),
            textcoords="offset points",
        )
    axes[0].set_xlabel("$x$ (m)")
    axes[0].set_ylabel("$y$ (m)")
    axes[0].set_title("A  Three-bench geometry at $t=0$ s", loc="left")
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].legend(loc="best")

    # Panel B: absolute distance-constraint residuals across 0-300 s.
    times = np.arange(0.0, 301.0, 1.0)
    residuals = np.empty((len(times), len(distances)), dtype=float)
    for row, time in enumerate(times):
        points = solve_handle_positions(head_state(float(time)).theta, distances)
        for column, expected in enumerate(distances):
            actual = hypot(
                points[column + 1].x - points[column].x,
                points[column + 1].y - points[column].y,
            )
            residuals[row, column] = max(abs(actual - expected), 1.0e-16)

    line_styles = ["-", "--", ":"]
    labels = ["Head bench (2.86 m)", "Body bench 1 (1.65 m)", "Body bench 2 (1.65 m)"]
    colors = ["#0072B2", "#D55E00", "#009E73"]
    for column, (label, style, color) in enumerate(
        zip(labels, line_styles, colors)
    ):
        axes[1].plot(
            times,
            residuals[:, column],
            label=label,
            linestyle=style,
            color=color,
        )
    axes[1].set_yscale("log")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Absolute chord error (m)")
    axes[1].set_title("B  Distance-constraint residuals", loc="left")
    axes[1].legend(loc="best")

    base = output_dir / "q1_three_benches_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    maximum_error = residuals.max()
    print(f"points={len(initial_points)}")
    print(
        "theta="
        + ", ".join(f"{point.theta:.12f}" for point in initial_points)
    )
    print(f"maximum_chord_error={maximum_error:.3e} m")
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
