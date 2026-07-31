"""Build the paper-expert workflow figure and a reproducible Monte Carlo stress test."""

from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from problem1_model import cylinder_surface_points
from problem2_model import (
    MAX_DRONE_SPEED,
    MAX_FUSE_DELAY,
    MIN_DRONE_SPEED,
    Strategy,
    decision_from_strategy,
    sampled_full_cylinder_duration,
)


DEFAULT_SEED = 20260731
DEFAULT_SAMPLES = 2000
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False
NOMINAL_STRATEGY = Strategy(
    heading_rad=np.radians(6.946062920904979),
    speed_mps=140.0,
    drop_time_s=0.0,
    fuse_delay_s=0.7390416849204616,
)


@dataclass(frozen=True)
class MonteCarloResult:
    heading_error_deg: np.ndarray
    speed_error_mps: np.ndarray
    release_delay_s: np.ndarray
    fuse_error_s: np.ndarray
    duration_s: np.ndarray
    nominal_duration_s: float


def run_monte_carlo(
    *,
    samples: int = DEFAULT_SAMPLES,
    seed: int = DEFAULT_SEED,
    step: float = 0.05,
    n_theta: int = 36,
) -> MonteCarloResult:
    """Stress-test the problem-2 strategy under explicitly assumed execution errors."""
    if samples < 1:
        raise ValueError("samples must be positive")
    rng = np.random.default_rng(seed)
    heading_error_deg = rng.normal(0.0, 0.5, samples)
    speed_error_mps = rng.normal(0.0, 1.5, samples)
    release_delay_s = np.abs(rng.normal(0.0, 0.08, samples))
    fuse_error_s = rng.normal(0.0, 0.05, samples)

    target_points = cylinder_surface_points(n_theta=n_theta, n_z=3, n_r=2)
    nominal_duration_s = sampled_full_cylinder_duration(
        decision_from_strategy(NOMINAL_STRATEGY),
        target_points,
        step=step,
    )
    durations = np.empty(samples, dtype=float)
    for index in range(samples):
        strategy = Strategy(
            heading_rad=NOMINAL_STRATEGY.heading_rad
            + np.radians(heading_error_deg[index]),
            speed_mps=float(
                np.clip(
                    NOMINAL_STRATEGY.speed_mps + speed_error_mps[index],
                    MIN_DRONE_SPEED,
                    MAX_DRONE_SPEED,
                )
            ),
            drop_time_s=float(release_delay_s[index]),
            fuse_delay_s=float(
                np.clip(
                    NOMINAL_STRATEGY.fuse_delay_s + fuse_error_s[index],
                    0.0,
                    MAX_FUSE_DELAY,
                )
            ),
        )
        durations[index] = sampled_full_cylinder_duration(
            decision_from_strategy(strategy),
            target_points,
            step=step,
        )
    return MonteCarloResult(
        heading_error_deg=heading_error_deg,
        speed_error_mps=speed_error_mps,
        release_delay_s=release_delay_s,
        fuse_error_s=fuse_error_s,
        duration_s=durations,
        nominal_duration_s=float(nominal_duration_s),
    )


def summarize(result: MonteCarloResult, *, seed: int) -> dict[str, object]:
    durations = result.duration_s
    sample_count = len(durations)
    standard_error = float(np.std(durations, ddof=1) / np.sqrt(sample_count))
    variables = np.column_stack(
        [
            result.heading_error_deg,
            result.speed_error_mps,
            result.release_delay_s,
            result.fuse_error_s,
        ]
    )
    correlations = np.corrcoef(variables, durations, rowvar=False)[-1, :-1]
    return {
        "purpose": "problem-2 execution-error stress test; distributions are scenario assumptions, not题面 measurements",
        "seed": seed,
        "samples": sample_count,
        "assumptions": {
            "heading_error_deg": "Normal(0, 0.5^2)",
            "speed_error_mps": "Normal(0, 1.5^2), clipped to [70, 140] m/s",
            "release_delay_s": "abs(Normal(0, 0.08^2))",
            "fuse_error_s": "Normal(0, 0.05^2), clipped to physical fuse range",
        },
        "nominal_duration_s_same_grid": result.nominal_duration_s,
        "mean_duration_s": float(np.mean(durations)),
        "standard_deviation_s": float(np.std(durations, ddof=1)),
        "mean_95_percent_ci_s": [
            float(np.mean(durations) - 1.96 * standard_error),
            float(np.mean(durations) + 1.96 * standard_error),
        ],
        "quantiles_s": {
            "p05": float(np.quantile(durations, 0.05)),
            "p25": float(np.quantile(durations, 0.25)),
            "p50": float(np.quantile(durations, 0.50)),
            "p75": float(np.quantile(durations, 0.75)),
            "p95": float(np.quantile(durations, 0.95)),
        },
        "probability_positive": float(np.mean(durations > 0.0)),
        "probability_at_least_80_percent_nominal": float(
            np.mean(durations >= 0.8 * result.nominal_duration_s)
        ),
        "correlation_with_duration": {
            "heading_error_deg": float(correlations[0]),
            "speed_error_mps": float(correlations[1]),
            "release_delay_s": float(correlations[2]),
            "fuse_error_s": float(correlations[3]),
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
            "matplotlib": plt.matplotlib.__version__,
        },
    }


def write_samples(path: Path, result: MonteCarloResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "heading_error_deg",
                "speed_error_mps",
                "release_delay_s",
                "fuse_error_s",
                "effective_duration_s",
            ]
        )
        writer.writerows(
            zip(
                result.heading_error_deg,
                result.speed_error_mps,
                result.release_delay_s,
                result.fuse_error_s,
                result.duration_s,
            )
        )


def plot_workflow(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=180)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    colors = ["#4472C4", "#5B9BD5", "#70AD47", "#ED7D31", "#A5A5A5"]
    boxes = [
        (0.5, 4.9, 2.0, 1.0, "题意与坐标系\n输入：位置、速度、规则"),
        (3.0, 4.9, 2.0, 1.0, "统一运动学\n导弹—无人机—烟幕"),
        (5.5, 4.9, 2.0, 1.0, "完整圆柱判据\n最不利视线距离"),
        (8.0, 4.9, 2.0, 1.0, "区间测度\n端点求根与并集合并"),
        (10.0, 2.7, 1.5, 1.0, "分层优化\n连续+离散"),
    ]
    for index, (x, y, width, height, label) in enumerate(boxes):
        patch = FancyBboxPatch(
            (x, y),
            width,
            height,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            linewidth=1.6,
            edgecolor=colors[index],
            facecolor=colors[index] + "18",
        )
        ax.add_patch(patch)
        ax.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=10)
    arrow_pairs = [
        ((2.5, 5.4), (3.0, 5.4)),
        ((5.0, 5.4), (5.5, 5.4)),
        ((7.5, 5.4), (8.0, 5.4)),
        ((9.0, 4.9), (10.35, 3.7)),
    ]
    for start, end in arrow_pairs:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=1.4,
                color="#4F4F4F",
            )
        )

    problem_boxes = [
        (0.7, 1.0, "问题1\n固定策略基准", "#4472C4"),
        (2.9, 1.0, "问题2\n单弹连续优化", "#5B9BD5"),
        (5.1, 1.0, "问题3\n同机多弹排程", "#70AD47"),
        (7.3, 1.0, "问题4\n多机协同", "#ED7D31"),
        (9.5, 1.0, "问题5\n多目标混合优化", "#A5A5A5"),
    ]
    for x, y, label, color in problem_boxes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                1.8,
                0.85,
                boxstyle="round,pad=0.06,rounding_size=0.06",
                linewidth=1.3,
                edgecolor=color,
                facecolor=color + "18",
            )
        )
        ax.text(x + 0.9, y + 0.425, label, ha="center", va="center", fontsize=9.5)
    for index in range(4):
        ax.add_patch(
            FancyArrowPatch(
                (problem_boxes[index][0] + 1.8, 1.425),
                (problem_boxes[index + 1][0], 1.425),
                arrowstyle="-|>",
                mutation_scale=11,
                linewidth=1.2,
                color="#666666",
            )
        )
    ax.add_patch(
        FancyArrowPatch(
            (10.75, 2.7),
            (10.4, 1.85),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color="#666666",
        )
    )
    ax.text(
        6.0,
        0.25,
        "同一机理逐级扩展：固定计算 → 连续优化 → 区间排程 → 多机协同 → 离散—连续联合分配",
        ha="center",
        va="center",
        fontsize=10,
        color="#404040",
    )
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_monte_carlo(path: Path, result: MonteCarloResult, summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), dpi=180)
    durations = result.duration_s
    axes[0].hist(durations, bins=36, color="#5B9BD5", edgecolor="white", alpha=0.92)
    axes[0].axvline(
        result.nominal_duration_s,
        color="#C00000",
        linewidth=2.0,
        label=f"nominal={result.nominal_duration_s:.3f} s",
    )
    axes[0].axvline(
        float(summary["mean_duration_s"]),
        color="#2F5597",
        linestyle="--",
        linewidth=1.8,
        label=f"mean={float(summary['mean_duration_s']):.3f} s",
    )
    axes[0].set_xlabel("Effective duration (s)")
    axes[0].set_ylabel("Frequency")
    axes[0].set_title("Monte Carlo duration distribution")
    axes[0].legend(frameon=False)
    axes[0].grid(axis="y", alpha=0.2)

    correlations = summary["correlation_with_duration"]
    labels = ["Heading", "Speed", "Release delay", "Fuse timing"]
    values = [
        correlations["heading_error_deg"],
        correlations["speed_error_mps"],
        correlations["release_delay_s"],
        correlations["fuse_error_s"],
    ]
    colors = ["#4472C4" if value >= 0 else "#ED7D31" for value in values]
    axes[1].barh(labels, values, color=colors, alpha=0.9)
    axes[1].axvline(0.0, color="#404040", linewidth=0.8)
    axes[1].set_xlim(-1.0, 1.0)
    axes[1].set_xlabel("Pearson correlation with duration")
    axes[1].set_title("Execution-error sensitivity")
    axes[1].grid(axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("Code/outputs"))
    parser.add_argument("--figure-dir", type=Path, default=Path("Paper/figures"))
    parser.add_argument("--samples", type=int, default=DEFAULT_SAMPLES)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> dict[str, object]:
    args = parse_args()
    result = run_monte_carlo(samples=args.samples, seed=args.seed)
    summary = summarize(result, seed=args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    write_samples(args.output_dir / "paper_expert_monte_carlo.csv", result)
    (args.output_dir / "paper_expert_validation.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    plot_workflow(args.figure_dir / "paper_expert_fig1_workflow.png")
    plot_monte_carlo(
        args.figure_dir / "paper_expert_fig2_monte_carlo.png",
        result,
        summary,
    )
    return summary


if __name__ == "__main__":
    main()
