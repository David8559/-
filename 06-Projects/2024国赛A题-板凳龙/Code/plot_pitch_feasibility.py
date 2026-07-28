"""Create the problem-3 minimum-pitch validation figure."""

from __future__ import annotations

import argparse
import json
import sys
from math import pi
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent
sys.path.insert(0, str(CODE_DIR / "src"))

from collision import rectangle_corners  # noqa: E402
from pitch_feasibility import (  # noqa: E402
    TURNING_RADIUS,
    minimum_pair_clearance_over_path,
    rectangles_at,
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-json", type=Path, required=True)
    args = parser.parse_args()
    result = json.loads(args.result_json.read_text(encoding="utf-8"))

    pitch = float(result["criticalPitchM"])
    theta = float(result["criticalThetaRad"])
    first_index, second_index = result["criticalPair"]
    rectangles = rectangles_at(theta, pitch)

    apply_figure_style()
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.0, 3.15),
        constrained_layout=True,
    )

    angles = np.linspace(theta, theta + 8.0 * pi, 800)
    radii = pitch * angles / (2.0 * pi)
    axes[0].plot(
        radii * np.cos(angles),
        radii * np.sin(angles),
        color="#B0B0B0",
        linewidth=0.7,
        zorder=1,
    )
    axes[0].add_patch(
        Circle(
            (0.0, 0.0),
            TURNING_RADIUS,
            facecolor="#E6F2F8",
            edgecolor="#0072B2",
            linewidth=1.0,
            linestyle="--",
            alpha=0.55,
            zorder=0,
        )
    )

    for index in range(25):
        rectangle = rectangles[index]
        if index == first_index:
            facecolor, edgecolor, alpha, zorder = (
                "#D55E00",
                "#A84300",
                0.65,
                5,
            )
        elif index == second_index:
            facecolor, edgecolor, alpha, zorder = (
                "#0072B2",
                "#005080",
                0.65,
                5,
            )
        else:
            facecolor, edgecolor, alpha, zorder = (
                "#BDBDBD",
                "#666666",
                0.28,
                2,
            )
        axes[0].add_patch(
            Polygon(
                rectangle_corners(rectangle),
                closed=True,
                facecolor=facecolor,
                edgecolor=edgecolor,
                linewidth=0.65,
                alpha=alpha,
                zorder=zorder,
            )
        )

    first = rectangles[first_index]
    second = rectangles[second_index]
    axes[0].annotate(
        "Head bench",
        (first.center_x, first.center_y),
        xytext=(-36, 21),
        textcoords="offset points",
        arrowprops={"arrowstyle": "-", "color": "#A84300", "linewidth": 0.8},
        color="#A84300",
    )
    axes[0].annotate(
        "Body bench 19",
        (second.center_x, second.center_y),
        xytext=(20, -25),
        textcoords="offset points",
        arrowprops={"arrowstyle": "-", "color": "#005080", "linewidth": 0.8},
        color="#005080",
    )
    axes[0].set_xlim(-6.3, 6.3)
    axes[0].set_ylim(-6.3, 6.3)
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].set_xlabel("$x$ (m)")
    axes[0].set_ylabel("$y$ (m)")
    axes[0].set_title("A  Critical path configuration", loc="left")

    pitches = np.linspace(pitch - 0.0045, pitch + 0.0045, 37)
    margins = np.array(
        [
            minimum_pair_clearance_over_path(
                float(candidate),
                first_index,
                second_index,
                coarse_intervals=60,
            ).margin
            for candidate in pitches
        ]
    )
    axes[1].plot(
        pitches,
        1000.0 * margins,
        color="#0072B2",
        label="Head–body 19 path-minimum margin",
    )
    axes[1].axhline(0.0, color="#555555", linewidth=0.8, linestyle="--")
    axes[1].axvline(
        pitch,
        color="#D55E00",
        linewidth=1.0,
        linestyle=":",
        label=f"Critical pitch: {pitch:.6f} m",
    )
    axes[1].scatter(
        [pitch],
        [0.0],
        color="#D55E00",
        edgecolor="black",
        linewidth=0.5,
        s=25,
        zorder=5,
    )
    axes[1].set_xlabel("Spiral pitch (m)")
    axes[1].set_ylabel("Minimum separation margin (mm)")
    axes[1].set_title("B  Feasibility threshold over the full path", loc="left")
    axes[1].legend(loc="upper left")

    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / "q3_minimum_pitch_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    print(f"critical_pitch={pitch:.12f} m")
    print(
        f"contact_pair=({first_index}, {second_index}), "
        f"head_radius={result['criticalHeadRadiusM']:.12f} m"
    )
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
