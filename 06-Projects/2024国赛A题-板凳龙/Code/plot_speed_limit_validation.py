"""Create the problem-5 continuous speed-limit validation figure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent


def apply_figure_style() -> None:
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
            "lines.linewidth": 1.3,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.05,
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-json", type=Path, required=True)
    args = parser.parse_args()
    result = json.loads(args.result_json.read_text(encoding="utf-8"))

    scan_s = np.asarray(result["scan"]["headS"], dtype=float)
    scan_ratio = np.asarray(
        result["scan"]["maximumRatio"],
        dtype=float,
    )
    local_s = np.asarray(result["localScan"]["headS"], dtype=float)
    local_ratio = np.asarray(
        result["localScan"]["maximumRatio"],
        dtype=float,
    )
    refined = result["refinedMaximum"]
    peak_s = float(refined["headSAtMaximumM"])
    peak_ratio = float(refined["maximumSpeedRatio"])
    maximum_head_speed = float(refined["maximumHeadSpeedMPerS"])

    apply_figure_style()
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.2, 3.0),
        constrained_layout=True,
    )

    axes[0].plot(scan_s, scan_ratio, color="#0072B2")
    axes[0].scatter(
        [peak_s],
        [peak_ratio],
        color="#D55E00",
        edgecolor="white",
        linewidth=0.5,
        s=28,
        zorder=4,
        label=f"Global maximum {peak_ratio:.6f}",
    )
    axes[0].axhline(1.0, color="#7F7F7F", linewidth=0.8, linestyle="--")
    axes[0].set_xlabel("Head path coordinate $s_0$ (m)")
    axes[0].set_ylabel("Maximum handle/head speed ratio")
    axes[0].set_title("A  Complete turn-transition scan", loc="left")
    axes[0].legend(loc="upper right")

    axes[1].plot(
        local_s,
        local_ratio,
        color="#009E73",
        marker=".",
        markersize=2.5,
    )
    axes[1].scatter(
        [peak_s],
        [peak_ratio],
        color="#D55E00",
        edgecolor="white",
        linewidth=0.5,
        s=28,
        zorder=4,
    )
    axes[1].annotate(
        (
            f"$s_0={peak_s:.6f}$ m\n"
            f"$k_\\max={peak_ratio:.9f}$\n"
            f"$v_{{0,\\max}}={maximum_head_speed:.9f}$ m/s"
        ),
        (peak_s, peak_ratio),
        xytext=(8, -42),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "#555555"},
    )
    axes[1].set_xlabel("Head path coordinate $s_0$ (m)")
    axes[1].set_ylabel("Maximum handle/head speed ratio")
    axes[1].set_title("B  Refined continuous maximum", loc="left")

    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / "q5_speed_limit_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
