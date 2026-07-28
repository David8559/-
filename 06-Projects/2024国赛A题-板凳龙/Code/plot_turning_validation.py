"""Create the problem-4 path and full-chain speed validation figure."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent
sys.path.insert(0, str(CODE_DIR / "src"))

from turning_path import (  # noqa: E402
    TURNING_RADIUS,
    build_turning_geometry,
    path_point,
)


def apply_figure_style() -> None:
    """Apply the project's compact, colorblind-safe figure style."""

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


def sampled_xy(values, geometry):
    points = [path_point(float(value), geometry) for value in values]
    return (
        np.array([point.x for point in points]),
        np.array([point.y for point in points]),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-json", type=Path, required=True)
    args = parser.parse_args()
    result = json.loads(args.result_json.read_text(encoding="utf-8"))
    geometry = build_turning_geometry()

    apply_figure_style()
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.2, 3.15),
        constrained_layout=True,
    )

    axes[0].add_patch(
        Circle(
            (0.0, 0.0),
            TURNING_RADIUS,
            facecolor="#E6F2F8",
            edgecolor="#0072B2",
            linewidth=0.9,
            linestyle="--",
            alpha=0.50,
            zorder=0,
        )
    )
    segments = (
        (
            np.linspace(-35.0, 0.0, 500),
            "#7F7F7F",
            "Inward spiral",
        ),
        (
            np.linspace(0.0, geometry.first_length, 220),
            "#D55E00",
            "First arc",
        ),
        (
            np.linspace(
                geometry.first_length,
                geometry.total_arc_length,
                180,
            ),
            "#009E73",
            "Second arc",
        ),
        (
            np.linspace(
                geometry.total_arc_length,
                geometry.total_arc_length + 35.0,
                500,
            ),
            "#7F7F7F",
            "Outward spiral",
        ),
    )
    for values, color, label in segments:
        x, y = sampled_xy(values, geometry)
        axes[0].plot(x, y, color=color, label=label, zorder=2)

    special = (
        (geometry.entry_x, geometry.entry_y, "Entry", "#D55E00"),
        (geometry.join_x, geometry.join_y, "Arc join", "#CC79A7"),
        (geometry.exit_x, geometry.exit_y, "Exit", "#009E73"),
    )
    for x, y, label, color in special:
        axes[0].scatter(
            [x],
            [y],
            color=color,
            edgecolor="black",
            linewidth=0.4,
            s=20,
            zorder=4,
        )
        axes[0].annotate(
            label,
            (x, y),
            xytext=(5, 6),
            textcoords="offset points",
            color=color,
        )

    axes[0].set_xlim(-6.2, 6.2)
    axes[0].set_ylim(-6.2, 6.2)
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].set_xlabel("$x$ (m)")
    axes[0].set_ylabel("$y$ (m)")
    axes[0].set_title("A  Tangent spiral–biarc–spiral path", loc="left")
    axes[0].legend(loc="lower right")

    speeds = np.asarray(result["speedRows"], dtype=float)
    times = np.asarray(result["times"], dtype=float)
    image = axes[1].imshow(
        speeds,
        origin="lower",
        aspect="auto",
        extent=[times[0], times[-1], 0, speeds.shape[0] - 1],
        cmap="viridis",
        interpolation="nearest",
    )
    validation = result["validation"]
    maximum_time = float(validation["maximumSpeedTimeS"])
    maximum_index = int(validation["maximumSpeedHandleIndex"])
    maximum_speed = float(validation["maximumSpeedMPerS"])
    axes[1].scatter(
        [maximum_time],
        [maximum_index],
        color="#D55E00",
        edgecolor="white",
        linewidth=0.5,
        s=25,
        zorder=5,
        label=f"Maximum: {maximum_speed:.6f} m/s",
    )
    axes[1].axvline(
        geometry.total_arc_length,
        color="white",
        linewidth=0.8,
        linestyle=":",
        alpha=0.9,
    )
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Handle index")
    axes[1].set_title("B  Speed field for all 224 handles", loc="left")
    axes[1].legend(loc="upper left")
    colorbar = fig.colorbar(image, ax=axes[1], pad=0.02)
    colorbar.set_label("Speed (m/s)")

    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / "q4_turning_path_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    print(f"first_radius={geometry.first_radius:.12f} m")
    print(f"second_radius={geometry.second_radius:.12f} m")
    print(f"turning_arc_length={geometry.total_arc_length:.12f} m")
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
