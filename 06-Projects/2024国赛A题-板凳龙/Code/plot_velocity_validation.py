"""Create the three-bench analytical-velocity validation figure."""

from __future__ import annotations

import sys
from math import hypot
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


CODE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CODE_DIR.parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    first_bench_distances,
    solve_handle_positions,
    solve_handle_states,
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
            "lines.linewidth": 1.4,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.05,
        }
    )


def main() -> None:
    apply_figure_style()
    output_dir = PROJECT_DIR / "Paper" / "Figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    distances = first_bench_distances(3)
    times = np.arange(0.0, 301.0, 1.0)
    speeds = np.empty((len(times), 4), dtype=float)
    constraint_rate_residuals = np.empty((len(times), 3), dtype=float)

    for row, time in enumerate(times):
        states = solve_handle_states(head_state(float(time)), distances)
        speeds[row] = [state.speed for state in states]
        for column, (previous, current) in enumerate(
            zip(states, states[1:])
        ):
            constraint_rate_residuals[row, column] = abs(
                (current.x - previous.x) * (current.vx - previous.vx)
                + (current.y - previous.y) * (current.vy - previous.vy)
            )

    # Central differences are evaluated away from the t=0 boundary.
    validation_times = np.arange(1.0, 300.0, 1.0)
    step = 1.0e-3
    velocity_errors = np.empty((len(validation_times), 4), dtype=float)
    for row, time in enumerate(validation_times):
        analytical = solve_handle_states(head_state(float(time)), distances)
        before = solve_handle_positions(
            head_state(float(time - step)).theta,
            distances,
        )
        after = solve_handle_positions(
            head_state(float(time + step)).theta,
            distances,
        )
        for column, (state, point_before, point_after) in enumerate(
            zip(analytical, before, after)
        ):
            numerical_vx = (point_after.x - point_before.x) / (2.0 * step)
            numerical_vy = (point_after.y - point_before.y) / (2.0 * step)
            velocity_errors[row, column] = hypot(
                state.vx - numerical_vx,
                state.vy - numerical_vy,
            )

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(7.1, 2.75),
        constrained_layout=True,
    )
    colors = ["#000000", "#0072B2", "#D55E00", "#009E73"]
    line_styles = ["-", "--", "-.", ":"]
    labels = [r"$P_0$", r"$P_1$", r"$P_2$", r"$P_3$"]

    for column, (label, color, style) in enumerate(
        zip(labels, colors, line_styles)
    ):
        axes[0].plot(
            times,
            speeds[:, column],
            label=label,
            color=color,
            linestyle=style,
        )
        axes[1].plot(
            validation_times,
            np.maximum(velocity_errors[:, column], 1.0e-16),
            label=label,
            color=color,
            linestyle=style,
        )

    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Handle speed (m/s)")
    axes[0].set_title("A  Analytical handle speeds", loc="left")
    axes[0].legend(loc="best", ncols=2)

    axes[1].set_yscale("log")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Velocity error (m/s)")
    axes[1].set_title("B  Centred-difference check", loc="left")

    maximum_rate_residual = constraint_rate_residuals.max(axis=1)
    axes[2].plot(
        times,
        np.maximum(maximum_rate_residual, 1.0e-18),
        color="#000000",
    )
    axes[2].set_yscale("log")
    axes[2].set_xlabel("Time (s)")
    axes[2].set_ylabel(r"$\max_i|\Delta q_i\cdot\Delta v_i|$ (m$^2$/s)")
    axes[2].set_title("C  Maximum constraint-rate residual", loc="left")

    base = output_dir / "q1_three_benches_velocity_validation"
    fig.savefig(base.with_suffix(".png"), dpi=600, facecolor="white")
    fig.savefig(base.with_suffix(".pdf"), facecolor="white")
    plt.close(fig)

    print(f"maximum_velocity_error={velocity_errors.max():.3e} m/s")
    print(
        "maximum_constraint_rate_residual="
        f"{constraint_rate_residuals.max():.3e} m^2/s"
    )
    print(
        "speed_range="
        f"[{speeds.min():.12f}, {speeds.max():.12f}] m/s"
    )
    print(base.with_suffix(".png"))
    print(base.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
