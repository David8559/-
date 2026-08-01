"""Solve Problem 5 with a deterministic candidate-library decomposition."""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import platform
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from problem1_model import (
    CLOUD_RADIUS,
    FALSE_TARGET,
    EffectiveInterval,
    cylinder_surface_points,
)
from problem3_model import intervals_duration, merge_intervals
from problem5_model import (
    DRONE_IDS,
    DRONE_INITIALS,
    MISSILE_ARRIVAL_TIMES,
    MISSILE_IDS,
    MISSILE_INITIALS,
    BombStrategy,
    burst_point,
    centerline_intervals_for_bomb,
    cloud_center_for,
    coarse_target_points,
    coordinate_refine_unit_cube,
    coverage_durations,
    decode_fixed_path_decision,
    decode_pair_decision,
    differential_evolution_unit_cube,
    drop_point,
    exact_full_intervals_for_bomb,
    feasible_bomb_combinations,
    full_cylinder_distances_for,
    intervals_by_missile,
    exact_joint_intervals_by_missile,
    intersect_interval_sets,
    missile_position_for,
    pair_centerline_duration,
    pair_proximity_score,
    pair_sampled_full_duration,
    sampled_full_intervals_for_bomb,
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
DRONE_COLORS = {
    "FY1": OKABE_ITO["blue"],
    "FY2": OKABE_ITO["orange"],
    "FY3": OKABE_ITO["green"],
    "FY4": OKABE_ITO["purple"],
    "FY5": OKABE_ITO["vermillion"],
}
MISSILE_COLORS = {
    "M1": OKABE_ITO["blue"],
    "M2": OKABE_ITO["orange"],
    "M3": OKABE_ITO["green"],
}
MISSILE_STYLES = {"M1": "-", "M2": "--", "M3": "-."}


@dataclass(frozen=True)
class AtomicCandidate:
    bomb: BombStrategy
    intervals: tuple
    duration: float
    path_source: str


@dataclass(frozen=True)
class PlanCandidate:
    drone_id: str
    path_source: str
    atoms: tuple[AtomicCandidate, ...]
    coverage: tuple[float, float, float]
    score: float


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


def directed_seed(drone_id: str, missile_id: str) -> np.ndarray:
    initial = DRONE_INITIALS[drone_id]
    heading = np.arctan2(-initial[1], -initial[0])
    speed_fraction = (120.0 - 70.0) / 70.0
    return np.array(
        [
            (heading + np.pi) / (2.0 * np.pi),
            speed_fraction,
            0.15,
            0.65,
        ]
    )


REFERENCE_M1 = {
    "FY1": np.array([0.5192940342146074, 1.0, 0.011030669226260555, 1.0]),
    "FY2": np.array([0.2783108925052482, 0.7106643260737071, 0.17137224268222898, 0.5111631708328349]),
    "FY3": np.array([0.7173580994867697, 0.8952739336952212, 0.3554243349130167, 0.20271508521467374]),
}


def optimize_pair_paths(
    *,
    quick: bool,
) -> tuple[dict[tuple[str, str], BombStrategy], list[dict[str, object]]]:
    coarse_points = coarse_target_points()
    paths: dict[tuple[str, str], BombStrategy] = {}
    history_rows: list[dict[str, object]] = []
    prox_population = 32 if quick else 48
    prox_generations = 35 if quick else 65
    duration_population = 40 if quick else 64
    duration_generations = 45 if quick else 90

    for drone_index, drone_id in enumerate(DRONE_IDS):
        for missile_index, missile_id in enumerate(MISSILE_IDS):
            seed = 20250900 + 20 * drone_index + missile_index
            initials = [directed_seed(drone_id, missile_id)]
            if missile_id == "M1" and drone_id in REFERENCE_M1:
                initials.insert(0, REFERENCE_M1[drone_id])

            proximity_run = differential_evolution_unit_cube(
                lambda decision, drone_id=drone_id, missile_id=missile_id: (
                    pair_proximity_score(
                        decision, drone_id, missile_id, step=0.16 if quick else 0.12
                    )
                ),
                seed=seed,
                population_size=prox_population,
                generations=prox_generations,
                initial_decisions=initials,
                dimension=4,
            )
            duration_run = differential_evolution_unit_cube(
                lambda decision, drone_id=drone_id, missile_id=missile_id: (
                    pair_centerline_duration(
                        decision, drone_id, missile_id, step=0.10 if quick else 0.07
                    )
                ),
                seed=seed + 500,
                population_size=duration_population,
                generations=duration_generations,
                initial_decisions=[
                    *initials,
                    *list(proximity_run.population[:12]),
                ],
                dimension=4,
            )
            candidates = [
                *initials,
                *list(duration_run.population[:12]),
                *list(proximity_run.population[:6]),
            ]
            objective = (
                lambda decision, drone_id=drone_id, missile_id=missile_id: (
                    pair_sampled_full_duration(
                        decision,
                        drone_id,
                        missile_id,
                        coarse_points,
                        step=0.08 if quick else 0.05,
                    )
                )
            )
            ranked = sorted(
                ((objective(candidate), candidate) for candidate in candidates),
                key=lambda item: item[0],
                reverse=True,
            )
            refined: list[tuple[float, np.ndarray]] = []
            for _, candidate in ranked[: (1 if quick else 2)]:
                decision, score, _ = coordinate_refine_unit_cube(
                    candidate,
                    objective,
                    initial_steps=(0.005, 0.008, 0.004, 0.006),
                    minimum_steps=(8e-5, 8e-5, 8e-5, 8e-5),
                    max_rounds=25 if quick else 50,
                )
                refined.append((score, decision))
            refined.extend(ranked[:3])
            refined.sort(key=lambda item: item[0], reverse=True)
            best_score, best_decision = refined[0]
            paths[(drone_id, missile_id)] = decode_pair_decision(
                best_decision, drone_id, missile_id
            )
            maximum_generation = max(
                len(proximity_run.history_best), len(duration_run.history_best)
            )
            for generation in range(maximum_generation):
                history_rows.append(
                    {
                        "drone_id": drone_id,
                        "missile_id": missile_id,
                        "generation": generation,
                        "proximity_best": (
                            float(proximity_run.history_best[generation])
                            if generation < len(proximity_run.history_best)
                            else ""
                        ),
                        "duration_best_s": (
                            float(duration_run.history_best[generation])
                            if generation < len(duration_run.history_best)
                            else ""
                        ),
                        "final_coarse_full_s": (
                            float(best_score) if generation == maximum_generation - 1 else ""
                        ),
                    }
                )
            print(
                f"pair {drone_id}-{missile_id}: "
                f"{best_score:.6f} s, heading={paths[(drone_id, missile_id)].heading_deg:.3f}°"
            )
    return paths, history_rows


def fixed_path_decision_from_bomb(bomb: BombStrategy) -> np.ndarray:
    fuse_limit = min(bomb.burst_time_s, bomb.max_fuse_delay_s)
    return np.array(
        [
            bomb.burst_time_s / MISSILE_ARRIVAL_TIMES[bomb.missile_id],
            bomb.fuse_delay_s / fuse_limit if fuse_limit > 0.0 else 0.0,
        ]
    )


def generate_atomic_candidates(
    drone_id: str,
    path_source: str,
    heading_rad: float,
    speed_mps: float,
    missile_id: str,
    pair_paths: dict[tuple[str, str], BombStrategy],
    target_points: np.ndarray,
    *,
    quick: bool,
) -> list[AtomicCandidate]:
    rng = np.random.default_rng(
        20251000
        + 100 * DRONE_IDS.index(drone_id)
        + 10 * (sum(ord(character) for character in path_source) % 17)
        + MISSILE_IDS.index(missile_id)
    )
    burst_grid = np.linspace(0.0, 1.0, 23 if quick else 35)
    fuse_grid = np.linspace(0.0, 1.0, 9 if quick else 13)
    decisions = [
        np.array([burst, fuse])
        for burst in burst_grid
        for fuse in fuse_grid
    ]
    decisions.extend(rng.random((80 if quick else 180, 2)))
    if path_source == missile_id:
        decisions.insert(
            0,
            fixed_path_decision_from_bomb(pair_paths[(drone_id, missile_id)]),
        )
    if (
        drone_id == "FY1"
        and path_source == "M1-three-bomb"
        and missile_id == "M1"
    ):
        arrival = MISSILE_ARRIVAL_TIMES["M1"]
        decisions.insert(0, np.array([1.0 / arrival, 0.0]))
        decisions.insert(0, np.array([0.005102 / arrival, 1.0]))

    scored: list[tuple[float, np.ndarray, BombStrategy]] = []
    for decision in decisions:
        bomb = decode_fixed_path_decision(
            decision,
            drone_id,
            missile_id,
            heading_rad,
            speed_mps,
        )
        score = intervals_duration(
            centerline_intervals_for_bomb(
                bomb, step=0.13 if quick else 0.09
            )
        )
        scored.append((score, np.asarray(decision), bomb))
    scored.sort(key=lambda item: item[0], reverse=True)

    seed_candidates: list[np.ndarray] = []
    used_bins: set[int] = set()
    for score, decision, bomb in scored:
        if score <= 0.0 and len(seed_candidates) >= 6:
            break
        bin_id = int(np.floor(bomb.drop_time_s / (0.8 if quick else 0.55)))
        if bin_id in used_bins:
            continue
        used_bins.add(bin_id)
        seed_candidates.append(decision)
        if len(seed_candidates) >= (10 if quick else 18):
            break

    center_objective = (
        lambda decision: intervals_duration(
            centerline_intervals_for_bomb(
                decode_fixed_path_decision(
                    decision,
                    drone_id,
                    missile_id,
                    heading_rad,
                    speed_mps,
                ),
                step=0.10 if quick else 0.06,
            )
        )
    )
    refined_center: list[np.ndarray] = []
    for decision in seed_candidates[: (6 if quick else 10)]:
        refined, _, _ = coordinate_refine_unit_cube(
            decision,
            center_objective,
            initial_steps=(0.01, 0.02),
            minimum_steps=(2e-4, 2e-4),
            max_rounds=18 if quick else 32,
        )
        refined_center.append(refined)
    ranked_full: list[tuple[float, np.ndarray, tuple]] = []
    for decision in [*seed_candidates, *refined_center]:
        bomb = decode_fixed_path_decision(
            decision,
            drone_id,
            missile_id,
            heading_rad,
            speed_mps,
        )
        intervals = tuple(
            sampled_full_intervals_for_bomb(
                bomb, target_points, step=0.10 if quick else 0.06
            )
        )
        ranked_full.append((intervals_duration(intervals), decision, intervals))
    ranked_full.sort(key=lambda item: item[0], reverse=True)

    full_objective = (
        lambda decision: intervals_duration(
            sampled_full_intervals_for_bomb(
                decode_fixed_path_decision(
                    decision,
                    drone_id,
                    missile_id,
                    heading_rad,
                    speed_mps,
                ),
                target_points,
                step=0.08 if quick else 0.045,
            )
        )
    )
    final_pool: list[tuple[float, np.ndarray, tuple]] = list(ranked_full)
    for _, decision, _ in ranked_full[: (1 if quick else 3)]:
        refined, _, _ = coordinate_refine_unit_cube(
            decision,
            full_objective,
            initial_steps=(0.006, 0.012),
            minimum_steps=(8e-5, 8e-5),
            max_rounds=20 if quick else 38,
        )
        bomb = decode_fixed_path_decision(
            refined,
            drone_id,
            missile_id,
            heading_rad,
            speed_mps,
        )
        intervals = tuple(
            sampled_full_intervals_for_bomb(
                bomb, target_points, step=0.06 if quick else 0.035
            )
        )
        final_pool.append((intervals_duration(intervals), refined, intervals))
    final_pool.sort(key=lambda item: item[0], reverse=True)

    selected: list[AtomicCandidate] = []
    for duration, decision, intervals in final_pool:
        if duration <= 0.0:
            continue
        bomb = decode_fixed_path_decision(
            decision,
            drone_id,
            missile_id,
            heading_rad,
            speed_mps,
        )
        start = intervals[0].start if intervals else -1.0
        if any(
            abs(bomb.drop_time_s - item.bomb.drop_time_s) < 0.45
            and abs(start - item.intervals[0].start) < 0.45
            for item in selected
        ):
            continue
        selected.append(
            AtomicCandidate(
                bomb=bomb,
                intervals=tuple(intervals),
                duration=float(duration),
                path_source=path_source,
            )
        )
        if len(selected) >= (4 if quick else 7):
            break
    if (
        drone_id == "FY1"
        and path_source == "M1-three-bomb"
        and missile_id == "M1"
    ):
        arrival = MISSILE_ARRIVAL_TIMES["M1"]
        for forced_decision in (
            np.array([0.005102 / arrival, 1.0]),
            np.array([1.0 / arrival, 0.0]),
        ):
            bomb = decode_fixed_path_decision(
                forced_decision,
                drone_id,
                missile_id,
                heading_rad,
                speed_mps,
            )
            intervals = tuple(
                sampled_full_intervals_for_bomb(
                    bomb, target_points, step=0.035
                )
            )
            candidate = AtomicCandidate(
                bomb=bomb,
                intervals=intervals,
                duration=intervals_duration(intervals),
                path_source=path_source,
            )
            if candidate.duration > 0.0 and all(
                abs(candidate.bomb.drop_time_s - item.bomb.drop_time_s) > 1e-8
                or abs(candidate.bomb.fuse_delay_s - item.bomb.fuse_delay_s) > 1e-8
                for item in selected
            ):
                selected.append(candidate)
    return selected


def build_plan_library(
    pair_paths: dict[tuple[str, str], BombStrategy],
    *,
    quick: bool,
) -> tuple[dict[str, list[PlanCandidate]], list[dict[str, object]]]:
    points = coarse_target_points()
    libraries: dict[str, list[PlanCandidate]] = {}
    atomic_rows: list[dict[str, object]] = []

    for drone_id in DRONE_IDS:
        all_plans: list[PlanCandidate] = []
        path_variants = [
            (
                missile_id,
                pair_paths[(drone_id, missile_id)].heading_rad,
                pair_paths[(drone_id, missile_id)].speed_mps,
            )
            for missile_id in MISSILE_IDS
        ]
        if drone_id == "FY1":
            path_variants.append(
                (
                    "M1-three-bomb",
                    np.radians(9.236484),
                    103.596493,
                )
            )
        for path_source, heading_rad, speed_mps in path_variants:
            atoms: list[AtomicCandidate] = []
            for missile_id in MISSILE_IDS:
                generated = generate_atomic_candidates(
                    drone_id,
                    path_source,
                    heading_rad,
                    speed_mps,
                    missile_id,
                    pair_paths,
                    points,
                    quick=quick,
                )
                atoms.extend(generated)
                for atom in generated:
                    atomic_rows.append(
                        {
                            "drone_id": drone_id,
                            "path_source": path_source,
                            "missile_id": missile_id,
                            "heading_deg": atom.bomb.heading_deg,
                            "speed_mps": atom.bomb.speed_mps,
                            "drop_time_s": atom.bomb.drop_time_s,
                            "fuse_delay_s": atom.bomb.fuse_delay_s,
                            "coarse_duration_s": atom.duration,
                        }
                    )
            for chosen_bombs in feasible_bomb_combinations(
                [atom.bomb for atom in atoms]
            ):
                chosen_atoms = tuple(
                    next(atom for atom in atoms if atom.bomb == bomb)
                    for bomb in chosen_bombs
                )
                durations = coverage_durations(
                    (atom.bomb, atom.intervals) for atom in chosen_atoms
                )
                coverage = tuple(durations[missile_id] for missile_id in MISSILE_IDS)
                all_plans.append(
                    PlanCandidate(
                        drone_id=drone_id,
                        path_source=path_source,
                        atoms=chosen_atoms,
                        coverage=coverage,
                        score=float(sum(coverage)),
                    )
                )

        best_by_signature: dict[tuple[int, int, int], list[PlanCandidate]] = {}
        for plan in sorted(all_plans, key=lambda item: item.score, reverse=True):
            signature = tuple(
                sum(atom.bomb.missile_id == missile_id for atom in plan.atoms)
                for missile_id in MISSILE_IDS
            )
            bucket = best_by_signature.setdefault(signature, [])
            if len(bucket) < 2:
                bucket.append(plan)
        diverse = [
            plan for bucket in best_by_signature.values() for plan in bucket
        ]
        diverse.sort(
            key=lambda item: (
                item.score,
                min(value for value in item.coverage if value > 0.0)
                if any(value > 0.0 for value in item.coverage)
                else 0.0,
            ),
            reverse=True,
        )
        keep = 8 if quick else 14
        libraries[drone_id] = diverse[:keep]
        if not libraries[drone_id]:
            raise RuntimeError(f"No positive-duration plan for {drone_id}.")
        print(
            f"library {drone_id}: {len(libraries[drone_id])} plans, "
            f"best={libraries[drone_id][0].score:.6f} s"
        )
    return libraries, atomic_rows


def score_plan_tuple(
    plans: Sequence[PlanCandidate],
) -> tuple[float, float, tuple[float, float, float]]:
    durations = coverage_durations(
        (atom.bomb, atom.intervals)
        for plan in plans
        for atom in plan.atoms
    )
    vector = tuple(durations[missile_id] for missile_id in MISSILE_IDS)
    return float(sum(vector)), float(min(vector)), vector


def select_fleet(
    libraries: dict[str, list[PlanCandidate]],
) -> tuple[tuple[PlanCandidate, ...], list[dict[str, object]]]:
    best: tuple[float, float, tuple[PlanCandidate, ...], tuple[float, ...]] | None = None
    leaders: list[tuple[float, float, tuple[float, ...]]] = []
    for plans in itertools.product(*(libraries[drone_id] for drone_id in DRONE_IDS)):
        total, minimum, vector = score_plan_tuple(plans)
        if minimum <= 0.0:
            continue
        if best is None or (total, minimum) > (best[0], best[1]):
            best = (total, minimum, tuple(plans), vector)
        leaders.append((total, minimum, vector))
    if best is None:
        raise RuntimeError("Candidate libraries cannot cover all three missiles.")
    leaders.sort(key=lambda item: (item[0], item[1]), reverse=True)
    rows = [
        {
            "rank": index + 1,
            "total_duration_s": item[0],
            "minimum_missile_duration_s": item[1],
            **{
                f"{missile_id}_duration_s": item[2][missile_index]
                for missile_index, missile_id in enumerate(MISSILE_IDS)
            },
        }
        for index, item in enumerate(leaders[:200])
    ]
    return best[2], rows


def exact_recompute(
    selected_plans: Sequence[PlanCandidate],
    theta_values: Sequence[int],
) -> tuple[
    list[tuple[BombStrategy, tuple]],
    dict[str, tuple],
    dict[str, float],
    dict[int, dict[str, float]],
]:
    bombs = [atom.bomb for plan in selected_plans for atom in plan.atoms]
    convergence: dict[int, dict[str, float]] = {}
    final_pairs: list[tuple[BombStrategy, tuple]] = []
    final_grouped: dict[str, tuple] = {}
    final_durations: dict[str, float] = {}
    for theta in theta_values:
        points = cylinder_surface_points(n_theta=theta, n_z=5, n_r=4)
        pairs = [
            (
                bomb,
                tuple(exact_full_intervals_for_bomb(bomb, points, scan_step=0.012)),
            )
            for bomb in bombs
        ]
        grouped = exact_joint_intervals_by_missile(
            bombs, points, scan_step=0.012
        )
        durations = {
            missile_id: intervals_duration(grouped[missile_id])
            for missile_id in MISSILE_IDS
        }
        simultaneous = intersect_interval_sets(
            [grouped[missile_id] for missile_id in MISSILE_IDS]
        )
        convergence[int(theta)] = {
            **durations,
            "total": float(sum(durations.values())),
            "minimum": float(min(durations.values())),
            "simultaneous": intervals_duration(simultaneous),
        }
        final_pairs = pairs
        final_grouped = {
            missile_id: tuple(grouped[missile_id]) for missile_id in MISSILE_IDS
        }
        final_durations = durations
        print(
            f"theta={theta}: total={sum(durations.values()):.6f} s "
            + ", ".join(
                f"{missile_id}={durations[missile_id]:.6f}"
                for missile_id in MISSILE_IDS
            )
        )
    return final_pairs, final_grouped, final_durations, convergence


def write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def draw_geometry(
    final_pairs: Sequence[tuple[BombStrategy, tuple]],
    figure_dir: Path,
) -> None:
    fig = plt.figure(figsize=(12, 5.2), constrained_layout=True)
    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    ax2d = fig.add_subplot(1, 2, 2)
    for missile_id in MISSILE_IDS:
        times = np.linspace(0.0, MISSILE_ARRIVAL_TIMES[missile_id], 160)
        track = missile_position_for(missile_id, times)
        color = MISSILE_COLORS[missile_id]
        style = MISSILE_STYLES[missile_id]
        ax3d.plot(track[:, 0], track[:, 1], track[:, 2], style, color=color, label=missile_id)
        ax2d.plot(track[:, 0], track[:, 1], style, color=color, label=missile_id)
    for drone_id in DRONE_IDS:
        bombs = sorted(
            [bomb for bomb, _ in final_pairs if bomb.drone_id == drone_id],
            key=lambda bomb: bomb.drop_time_s,
        )
        if not bombs:
            continue
        last_time = max(bomb.burst_time_s for bomb in bombs)
        times = np.linspace(0.0, last_time, 100)
        positions = (
            DRONE_INITIALS[drone_id][None, :]
            + times[:, None] * bombs[0].drone_velocity[None, :]
        )
        color = DRONE_COLORS[drone_id]
        ax3d.plot(
            positions[:, 0],
            positions[:, 1],
            positions[:, 2],
            color=color,
            lw=1.5,
            label=f"{drone_id} 航迹",
        )
        ax2d.plot(positions[:, 0], positions[:, 1], color=color, lw=1.5)
        for bomb in bombs:
            drop = drop_point(bomb)
            burst = burst_point(bomb)
            ax3d.scatter(*drop, color=color, marker="o", s=20)
            ax3d.scatter(*burst, color=color, marker="x", s=28)
            ax2d.scatter(drop[0], drop[1], color=color, marker="o", s=20)
            ax2d.scatter(burst[0], burst[1], color=color, marker="x", s=28)
    ax3d.scatter(*FALSE_TARGET, color=OKABE_ITO["black"], marker="s", s=28, label="假目标")
    ax2d.scatter(FALSE_TARGET[0], FALSE_TARGET[1], color=OKABE_ITO["black"], marker="s", s=28)
    ax3d.set_title("(a) 五机三导弹空间策略")
    ax3d.set_xlabel("x (m)")
    ax3d.set_ylabel("y (m)")
    ax3d.set_zlabel("z (m)")
    ax3d.legend(frameon=False, ncol=3)
    ax2d.set_title("(b) 水平投影")
    ax2d.set_xlabel("x (m)")
    ax2d.set_ylabel("y (m)")
    ax2d.grid(alpha=0.2)
    ax2d.set_ylim(-3500.0, 2500.0)
    save_figure(fig, figure_dir / "problem5_fig1_fleet_geometry")


def draw_allocation(
    final_pairs: Sequence[tuple[BombStrategy, tuple]],
    durations: dict[str, float],
    figure_dir: Path,
) -> None:
    counts = np.zeros((len(DRONE_IDS), len(MISSILE_IDS)), dtype=int)
    for bomb, _ in final_pairs:
        counts[DRONE_IDS.index(bomb.drone_id), MISSILE_IDS.index(bomb.missile_id)] += 1
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3), constrained_layout=True)
    image = axes[0].imshow(counts, cmap="cividis", vmin=0, vmax=3, aspect="auto")
    axes[0].set_xticks(range(len(MISSILE_IDS)), MISSILE_IDS)
    axes[0].set_yticks(range(len(DRONE_IDS)), DRONE_IDS)
    axes[0].set_xlabel("干扰导弹")
    axes[0].set_ylabel("无人机")
    axes[0].set_title("(a) 无人机—导弹分配矩阵")
    for row in range(counts.shape[0]):
        for col in range(counts.shape[1]):
            axes[0].text(
                col,
                row,
                str(counts[row, col]),
                ha="center",
                va="center",
                color="white" if counts[row, col] >= 2 else "black",
                fontweight="bold",
            )
    colorbar = fig.colorbar(image, ax=axes[0], shrink=0.82)
    colorbar.set_label("干扰弹数量")
    values = [durations[missile_id] for missile_id in MISSILE_IDS]
    bars = axes[1].bar(
        MISSILE_IDS,
        values,
        color=[MISSILE_COLORS[item] for item in MISSILE_IDS],
    )
    axes[1].set_ylim(0.0, max(values) * 1.2)
    axes[1].set_ylabel("并集有效时长 (s)")
    axes[1].set_title("(b) 各导弹有效遮蔽")
    for bar, value in zip(bars, values):
        axes[1].text(
            bar.get_x() + bar.get_width() / 2.0,
            value,
            f"{value:.3f}",
            ha="center",
            va="bottom",
        )
    save_figure(fig, figure_dir / "problem5_fig2_allocation_matrix")


def draw_gantt(
    final_pairs: Sequence[tuple[BombStrategy, tuple]],
    grouped: dict[str, tuple],
    figure_dir: Path,
) -> None:
    ordered = sorted(
        final_pairs,
        key=lambda item: (
            DRONE_IDS.index(item[0].drone_id),
            item[0].drop_time_s,
        ),
    )
    fig, ax = plt.subplots(figsize=(12, 6.8), constrained_layout=True)
    labels = []
    drone_counts = {drone_id: 0 for drone_id in DRONE_IDS}
    for row, (bomb, intervals) in enumerate(ordered):
        drone_counts[bomb.drone_id] += 1
        labels.append(
            f"{bomb.drone_id}-{drone_counts[bomb.drone_id]}→{bomb.missile_id}"
        )
        for interval in intervals:
            ax.broken_barh(
                [(interval.start, interval.duration)],
                (row - 0.35, 0.7),
                facecolors=MISSILE_COLORS[bomb.missile_id],
                edgecolors="black",
                linewidth=0.35,
            )
    offset = len(ordered) + 0.8
    for index, missile_id in enumerate(MISSILE_IDS):
        for interval in grouped[missile_id]:
            ax.broken_barh(
                [(interval.start, interval.duration)],
                (offset + index - 0.35, 0.7),
                facecolors=MISSILE_COLORS[missile_id],
                alpha=0.55,
            )
        labels.append(f"{missile_id} 并集")
    ax.set_yticks([*range(len(ordered)), *[offset + i for i in range(3)]], labels)
    ax.set_xlabel("绝对时间 (s)")
    ax.set_title(
        f"{len(ordered)} 枚有效投放记录及三枚导弹的有效区间并集"
    )
    ax.grid(axis="x", alpha=0.2)
    save_figure(fig, figure_dir / "problem5_fig3_coverage_gantt")


def draw_coverage_timeline(
    final_pairs: Sequence[tuple[BombStrategy, tuple]],
    grouped: dict[str, tuple],
    figure_dir: Path,
) -> list[dict[str, object]]:
    max_time = max(MISSILE_ARRIVAL_TIMES.values())
    times = np.linspace(0.0, max_time, 1601)
    rows: list[dict[str, object]] = []
    fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True, constrained_layout=True)
    for axis, missile_id in zip(axes, MISSILE_IDS):
        count = np.zeros_like(times)
        for bomb, intervals in final_pairs:
            if bomb.missile_id != missile_id:
                continue
            for interval in intervals:
                count += ((times >= interval.start) & (times <= interval.end)).astype(float)
        axis.step(times, count, where="post", color=MISSILE_COLORS[missile_id], lw=1.4)
        for interval in grouped[missile_id]:
            axis.axvspan(interval.start, interval.end, color=MISSILE_COLORS[missile_id], alpha=0.16)
        axis.set_ylabel(f"{missile_id}\n有效烟幕数")
        axis.set_ylim(-0.1, max(1.2, float(np.max(count)) + 0.4))
        axis.grid(alpha=0.2)
        for time, value in zip(times, count):
            rows.append(
                {
                    "time_s": float(time),
                    "missile_id": missile_id,
                    "effective_cloud_count": int(value),
                    "covered": int(value > 0),
                }
            )
    axes[-1].set_xlabel("绝对时间 (s)")
    axes[0].set_title("M1、M2、M3 的联合遮蔽时序")
    save_figure(fig, figure_dir / "problem5_fig4_coverage_timeline")
    return rows


def draw_optimization_and_convergence(
    atomic_rows: Sequence[dict[str, object]],
    convergence: dict[int, dict[str, float]],
    final_theta: int,
    figure_dir: Path,
) -> None:
    pair_values = np.zeros((len(DRONE_IDS), len(MISSILE_IDS)))
    for item in atomic_rows:
        row = DRONE_IDS.index(str(item["drone_id"]))
        col = MISSILE_IDS.index(str(item["missile_id"]))
        pair_values[row, col] = max(
            pair_values[row, col],
            float(item["coarse_duration_s"]),
        )
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), constrained_layout=True)
    image = axes[0].imshow(pair_values, cmap="viridis", aspect="auto")
    axes[0].set_xticks(range(len(MISSILE_IDS)), MISSILE_IDS)
    axes[0].set_yticks(range(len(DRONE_IDS)), DRONE_IDS)
    axes[0].set_title("(a) 单弹候选路径收益")
    axes[0].set_xlabel("导弹")
    axes[0].set_ylabel("无人机")
    for row in range(pair_values.shape[0]):
        for col in range(pair_values.shape[1]):
            axes[0].text(
                col,
                row,
                f"{pair_values[row, col]:.2f}",
                ha="center",
                va="center",
                color="white" if pair_values[row, col] > np.max(pair_values) * 0.55 else "black",
            )
    colorbar = fig.colorbar(image, ax=axes[0], shrink=0.84)
    colorbar.set_label("单弹完整圆柱时长 (s)")
    theta = sorted(convergence)
    for missile_id in MISSILE_IDS:
        axes[1].plot(
            theta,
            [convergence[value][missile_id] for value in theta],
            marker="o",
            color=MISSILE_COLORS[missile_id],
            linestyle=MISSILE_STYLES[missile_id],
            label=missile_id,
        )
    axes[1].plot(
        theta,
        [convergence[value]["total"] for value in theta],
        marker="s",
        color=OKABE_ITO["black"],
        lw=1.6,
        label="合计",
    )
    axes[1].axvline(final_theta, color=OKABE_ITO["gray"], ls=":", lw=1)
    axes[1].set_xlabel("圆柱周向离散点数")
    axes[1].set_ylabel("有效时长 (s)")
    axes[1].set_title("(b) 完整圆柱离散收敛")
    axes[1].legend(frameon=False)
    axes[1].grid(alpha=0.2)
    save_figure(fig, figure_dir / "problem5_fig5_optimization_convergence")


def make_result(
    final_pairs: Sequence[tuple[BombStrategy, tuple]],
    grouped: dict[str, tuple],
    durations: dict[str, float],
    convergence: dict[int, dict[str, float]],
    selected_plans: Sequence[PlanCandidate],
) -> dict[str, object]:
    records = []
    for drone_id in DRONE_IDS:
        drone_pairs = sorted(
            [pair for pair in final_pairs if pair[0].drone_id == drone_id],
            key=lambda pair: pair[0].drop_time_s,
        )
        for bomb_number, (bomb, intervals) in enumerate(drone_pairs, start=1):
            records.append(
                {
                    "drone_id": drone_id,
                    "bomb_id": bomb_number,
                    "missile_id": bomb.missile_id,
                    "heading_deg": bomb.heading_deg,
                    "speed_mps": bomb.speed_mps,
                    "drop_time_s": bomb.drop_time_s,
                    "fuse_delay_s": bomb.fuse_delay_s,
                    "burst_time_s": bomb.burst_time_s,
                    "drop_point_m": drop_point(bomb).tolist(),
                    "burst_point_m": burst_point(bomb).tolist(),
                    "effective_intervals_s": [
                        [interval.start, interval.end] for interval in intervals
                    ],
                    "effective_duration_s": intervals_duration(intervals),
                }
            )
    return {
        "criterion": (
            "for every sampled target sight line, at least one active cloud "
            "intersects the finite missile-to-target segment"
        ),
        "objective": (
            "primary: maximize the sum of per-missile joint-coverage durations; "
            "also report the minimum per-missile duration and the simultaneous "
            "three-missile safety duration"
        ),
        "method": "pair-path continuous search, fixed-path atomic candidate library, within-drone combination, exhaustive five-drone plan selection",
        "global_optimality_boundary": "feasible numerical lower bound over the generated candidate library, not an analytic global optimum",
        "bombs": records,
        "missiles": {
            missile_id: {
                "arrival_time_s": MISSILE_ARRIVAL_TIMES[missile_id],
                "union_intervals_s": [
                    [interval.start, interval.end]
                    for interval in grouped[missile_id]
                ],
                "union_duration_s": durations[missile_id],
            }
            for missile_id in MISSILE_IDS
        },
        "aggregation_metrics": {
            "sum_duration_s": float(sum(durations.values())),
            "minimum_missile_duration_s": float(min(durations.values())),
            "simultaneous_intervals_s": [
                [interval.start, interval.end]
                for interval in intersect_interval_sets(
                    [grouped[missile_id] for missile_id in MISSILE_IDS]
                )
            ],
            "simultaneous_duration_s": intervals_duration(
                intersect_interval_sets(
                    [grouped[missile_id] for missile_id in MISSILE_IDS]
                )
            ),
        },
        "total_union_duration_s": float(sum(durations.values())),
        "theta_convergence_duration_s": {
            str(theta): values for theta, values in convergence.items()
        },
        "selected_plan_sources": {
            plan.drone_id: plan.path_source for plan in selected_plans
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
            "matplotlib": matplotlib.__version__,
        },
    }


def load_pair_paths_from_atomic_csv(path: Path) -> dict[tuple[str, str], BombStrategy]:
    candidates: dict[tuple[str, str], tuple[float, dict[str, str]]] = {}
    fallbacks: dict[tuple[str, str], dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            path_source = row["path_source"]
            if path_source not in MISSILE_IDS:
                continue
            key = (row["drone_id"], path_source)
            fallbacks.setdefault(key, row)
            if row["missile_id"] != path_source:
                continue
            duration = float(row["coarse_duration_s"])
            if key not in candidates or duration > candidates[key][0]:
                candidates[key] = (duration, row)
    result: dict[tuple[str, str], BombStrategy] = {}
    for drone_id in DRONE_IDS:
        for missile_id in MISSILE_IDS:
            key = (drone_id, missile_id)
            row = candidates.get(key, (0.0, fallbacks.get(key)))[1]
            if row is None:
                fallback = directed_seed(drone_id, missile_id)
                result[key] = decode_pair_decision(
                    fallback, drone_id, missile_id
                )
                continue
            result[key] = BombStrategy(
                drone_id=drone_id,
                missile_id=missile_id,
                heading_rad=float(np.radians(float(row["heading_deg"]))),
                speed_mps=float(row["speed_mps"]),
                drop_time_s=0.0,
                fuse_delay_s=0.0,
            )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--figure-dir", type=Path, required=True)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--reuse-pairs", action="store_true")
    parser.add_argument("--reuse-result", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    configure_style()

    if args.reuse_result:
        result_path = args.output_dir / "problem5_result.json"
        atomic_path = args.output_dir / "problem5_atomic_candidates.csv"
        if not result_path.exists() or not atomic_path.exists():
            raise FileNotFoundError(
                "--reuse-result requires problem5_result.json and "
                "problem5_atomic_candidates.csv"
            )
        result = json.loads(result_path.read_text(encoding="utf-8"))
        bombs = []
        for item in result["bombs"]:
            bomb = BombStrategy(
                drone_id=item["drone_id"],
                missile_id=item["missile_id"],
                heading_rad=float(np.radians(item["heading_deg"])),
                speed_mps=float(item["speed_mps"]),
                drop_time_s=float(item["drop_time_s"]),
                fuse_delay_s=float(item["fuse_delay_s"]),
            )
            bombs.append(bomb)
        convergence = {}
        final_pairs = []
        grouped = {}
        durations = {}
        for theta in (90, 180, 360, 720):
            points = cylinder_surface_points(n_theta=theta, n_z=5, n_r=4)
            pairs = [
                (
                    bomb,
                    tuple(
                        exact_full_intervals_for_bomb(
                            bomb, points, scan_step=0.012
                        )
                    ),
                )
                for bomb in bombs
            ]
            current_grouped = exact_joint_intervals_by_missile(
                bombs, points, scan_step=0.012
            )
            current_durations = {
                missile_id: intervals_duration(current_grouped[missile_id])
                for missile_id in MISSILE_IDS
            }
            simultaneous = intersect_interval_sets(
                [current_grouped[missile_id] for missile_id in MISSILE_IDS]
            )
            convergence[theta] = {
                **current_durations,
                "total": float(sum(current_durations.values())),
                "minimum": float(min(current_durations.values())),
                "simultaneous": intervals_duration(simultaneous),
            }
            final_pairs = pairs
            grouped = {
                missile_id: tuple(current_grouped[missile_id])
                for missile_id in MISSILE_IDS
            }
            durations = current_durations
        simultaneous = intersect_interval_sets(
            [grouped[missile_id] for missile_id in MISSILE_IDS]
        )
        pair_lookup = {
            (bomb.drone_id, round(bomb.drop_time_s, 8)): intervals
            for bomb, intervals in final_pairs
        }
        for item in result["bombs"]:
            intervals = pair_lookup[(item["drone_id"], round(item["drop_time_s"], 8))]
            item["effective_intervals_s"] = [
                [interval.start, interval.end] for interval in intervals
            ]
            item["effective_duration_s"] = intervals_duration(intervals)
        result.update(
            {
                "criterion": (
                    "for every sampled target sight line, at least one active "
                    "cloud intersects the finite missile-to-target segment"
                ),
                "objective": (
                    "primary: maximize the sum of per-missile joint-coverage "
                    "durations; also report minimum and simultaneous duration"
                ),
                "missiles": {
                    missile_id: {
                        "arrival_time_s": MISSILE_ARRIVAL_TIMES[missile_id],
                        "union_intervals_s": [
                            [interval.start, interval.end]
                            for interval in grouped[missile_id]
                        ],
                        "union_duration_s": durations[missile_id],
                    }
                    for missile_id in MISSILE_IDS
                },
                "aggregation_metrics": {
                    "sum_duration_s": float(sum(durations.values())),
                    "minimum_missile_duration_s": float(min(durations.values())),
                    "simultaneous_intervals_s": [
                        [interval.start, interval.end]
                        for interval in simultaneous
                    ],
                    "simultaneous_duration_s": intervals_duration(simultaneous),
                },
                "total_union_duration_s": float(sum(durations.values())),
                "theta_convergence_duration_s": {
                    str(theta): values for theta, values in convergence.items()
                },
            }
        )
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        with atomic_path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as stream:
            atomic_rows = list(csv.DictReader(stream))
        timeseries_rows = draw_coverage_timeline(
            final_pairs, grouped, args.figure_dir
        )
        write_csv(
            args.output_dir / "problem5_timeseries.csv",
            ["time_s", "missile_id", "effective_cloud_count", "covered"],
            timeseries_rows,
        )
        draw_geometry(final_pairs, args.figure_dir)
        draw_allocation(final_pairs, durations, args.figure_dir)
        draw_gantt(final_pairs, grouped, args.figure_dir)
        draw_optimization_and_convergence(
            atomic_rows,
            convergence,
            max(convergence),
            args.figure_dir,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    atomic_path = args.output_dir / "problem5_atomic_candidates.csv"
    if args.reuse_pairs:
        if not atomic_path.exists():
            raise FileNotFoundError(
                "--reuse-pairs requires an existing problem5_atomic_candidates.csv"
            )
        pair_paths = load_pair_paths_from_atomic_csv(atomic_path)
        history_path = args.output_dir / "problem5_pair_search_history.csv"
        if history_path.exists():
            with history_path.open(
                "r", encoding="utf-8-sig", newline=""
            ) as stream:
                history_rows = list(csv.DictReader(stream))
        else:
            history_rows = []
    else:
        pair_paths, history_rows = optimize_pair_paths(quick=args.quick)
    libraries, atomic_rows = build_plan_library(pair_paths, quick=args.quick)
    selected_plans, fleet_rows = select_fleet(libraries)
    theta_values = (72, 144) if args.quick else (90, 180, 360, 720)
    final_pairs, grouped, durations, convergence = exact_recompute(
        selected_plans, theta_values
    )
    final_theta = theta_values[-1]

    result = make_result(
        final_pairs, grouped, durations, convergence, selected_plans
    )
    (args.output_dir / "problem5_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    interval_rows = []
    for bomb, intervals in final_pairs:
        for index, interval in enumerate(intervals, start=1):
            interval_rows.append(
                {
                    "kind": "bomb",
                    "drone_id": bomb.drone_id,
                    "bomb_id": next(
                        item["bomb_id"]
                        for item in result["bombs"]
                        if item["drone_id"] == bomb.drone_id
                        and abs(item["drop_time_s"] - bomb.drop_time_s) < 1e-8
                    ),
                    "missile_id": bomb.missile_id,
                    "interval_id": index,
                    "start_s": interval.start,
                    "end_s": interval.end,
                    "duration_s": interval.duration,
                }
            )
    for missile_id in MISSILE_IDS:
        for index, interval in enumerate(grouped[missile_id], start=1):
            interval_rows.append(
                {
                    "kind": "union",
                    "drone_id": "",
                    "bomb_id": "",
                    "missile_id": missile_id,
                    "interval_id": index,
                    "start_s": interval.start,
                    "end_s": interval.end,
                    "duration_s": interval.duration,
                }
            )
    write_csv(
        args.output_dir / "problem5_intervals.csv",
        [
            "kind",
            "drone_id",
            "bomb_id",
            "missile_id",
            "interval_id",
            "start_s",
            "end_s",
            "duration_s",
        ],
        interval_rows,
    )
    write_csv(
        args.output_dir / "problem5_pair_search_history.csv",
        [
            "drone_id",
            "missile_id",
            "generation",
            "proximity_best",
            "duration_best_s",
            "final_coarse_full_s",
        ],
        history_rows,
    )
    write_csv(
        args.output_dir / "problem5_atomic_candidates.csv",
        [
            "drone_id",
            "path_source",
            "missile_id",
            "heading_deg",
            "speed_mps",
            "drop_time_s",
            "fuse_delay_s",
            "coarse_duration_s",
        ],
        atomic_rows,
    )
    write_csv(
        args.output_dir / "problem5_fleet_candidates.csv",
        [
            "rank",
            "total_duration_s",
            "minimum_missile_duration_s",
            "M1_duration_s",
            "M2_duration_s",
            "M3_duration_s",
        ],
        fleet_rows,
    )
    timeseries_rows = draw_coverage_timeline(final_pairs, grouped, args.figure_dir)
    write_csv(
        args.output_dir / "problem5_timeseries.csv",
        ["time_s", "missile_id", "effective_cloud_count", "covered"],
        timeseries_rows,
    )
    draw_geometry(final_pairs, args.figure_dir)
    draw_allocation(final_pairs, durations, args.figure_dir)
    draw_gantt(final_pairs, grouped, args.figure_dir)
    draw_optimization_and_convergence(
        atomic_rows, convergence, final_theta, args.figure_dir
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
