"""Problem 3: three-bomb scheduling for FY1 against M1."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

import numpy as np

from problem1_model import (
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    EffectiveInterval,
    cylinder_surface_points,
    missile_position,
)
from problem2_model import (
    MAX_DRONE_SPEED,
    MAX_FUSE_DELAY,
    MIN_DRONE_SPEED,
    MISSILE_ARRIVAL_TIME,
    Strategy,
    centerline_distances_for,
    cloud_center_for,
    exact_full_cylinder_intervals,
    full_cylinder_distances_for,
    sampled_effective_intervals,
)
from joint_coverage import exact_joint_intervals, joint_sightline_margins


MIN_DROP_GAP = 1.0
DROP1_MAX = 20.0
EXTRA_GAP_MAX = 12.0
DECISION_DIMENSION = 8


@dataclass(frozen=True)
class MultiBombStrategy:
    heading_rad: float
    speed_mps: float
    drop_times_s: tuple[float, float, float]
    fuse_delays_s: tuple[float, float, float]

    @property
    def heading_deg(self) -> float:
        return float(np.degrees(self.heading_rad) % 360.0)

    @property
    def bombs(self) -> tuple[Strategy, Strategy, Strategy]:
        return tuple(
            Strategy(
                heading_rad=self.heading_rad,
                speed_mps=self.speed_mps,
                drop_time_s=drop_time,
                fuse_delay_s=fuse_delay,
            )
            for drop_time, fuse_delay in zip(
                self.drop_times_s, self.fuse_delays_s
            )
        )


@dataclass(frozen=True)
class PopulationResult:
    decision: np.ndarray
    score: float
    history_best: np.ndarray
    history_mean: np.ndarray
    population: np.ndarray
    population_scores: np.ndarray


def decode_decision(decision: Sequence[float]) -> MultiBombStrategy:
    """Map an eight-dimensional unit-cube vector to a feasible schedule."""
    values = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    if values.shape != (DECISION_DIMENSION,):
        raise ValueError("Problem 3 decision must have eight elements.")

    heading = -np.pi + 2.0 * np.pi * values[0]
    speed = MIN_DRONE_SPEED + (MAX_DRONE_SPEED - MIN_DRONE_SPEED) * values[1]
    drop1 = DROP1_MAX * values[2]
    drop2 = drop1 + MIN_DROP_GAP + EXTRA_GAP_MAX * values[3]
    drop3 = drop2 + MIN_DROP_GAP + EXTRA_GAP_MAX * values[4]
    drops = (float(drop1), float(drop2), float(drop3))

    fuse_delays: list[float] = []
    for drop_time, fraction in zip(drops, values[5:]):
        fuse_limit = min(MAX_FUSE_DELAY, MISSILE_ARRIVAL_TIME - drop_time)
        fuse_delays.append(float(max(0.0, fuse_limit) * fraction))

    strategy = MultiBombStrategy(
        heading_rad=float(heading),
        speed_mps=float(speed),
        drop_times_s=drops,
        fuse_delays_s=tuple(fuse_delays),
    )
    validate_multi_strategy(strategy)
    return strategy


def encode_strategy(strategy: MultiBombStrategy) -> np.ndarray:
    validate_multi_strategy(strategy)
    drop1, drop2, drop3 = strategy.drop_times_s
    values = np.empty(DECISION_DIMENSION, dtype=float)
    values[0] = (strategy.heading_rad + np.pi) / (2.0 * np.pi)
    values[1] = (strategy.speed_mps - MIN_DRONE_SPEED) / (
        MAX_DRONE_SPEED - MIN_DRONE_SPEED
    )
    values[2] = drop1 / DROP1_MAX
    values[3] = (drop2 - drop1 - MIN_DROP_GAP) / EXTRA_GAP_MAX
    values[4] = (drop3 - drop2 - MIN_DROP_GAP) / EXTRA_GAP_MAX
    for index, (drop_time, fuse_delay) in enumerate(
        zip(strategy.drop_times_s, strategy.fuse_delays_s), start=5
    ):
        fuse_limit = min(MAX_FUSE_DELAY, MISSILE_ARRIVAL_TIME - drop_time)
        values[index] = fuse_delay / fuse_limit if fuse_limit > 0.0 else 0.0
    return np.clip(values, 0.0, 1.0)


def validate_multi_strategy(strategy: MultiBombStrategy) -> None:
    if not MIN_DRONE_SPEED <= strategy.speed_mps <= MAX_DRONE_SPEED:
        raise ValueError("Drone speed is outside [70, 140] m/s.")
    if len(strategy.drop_times_s) != 3 or len(strategy.fuse_delays_s) != 3:
        raise ValueError("Exactly three bombs are required.")
    drops = np.asarray(strategy.drop_times_s)
    fuses = np.asarray(strategy.fuse_delays_s)
    if np.any(drops < 0.0):
        raise ValueError("Drop times must be nonnegative.")
    if np.any(np.diff(drops) < MIN_DROP_GAP - 1e-12):
        raise ValueError("Consecutive drops must be at least one second apart.")
    if np.any(fuses < 0.0) or np.any(fuses > MAX_FUSE_DELAY + 1e-12):
        raise ValueError("Fuse delay violates the above-ground burst constraint.")
    if np.any(drops + fuses > MISSILE_ARRIVAL_TIME + 1e-12):
        raise ValueError("A burst occurs after M1 reaches the false target.")


def merge_intervals(
    intervals: Iterable[EffectiveInterval], tolerance: float = 1e-9
) -> list[EffectiveInterval]:
    ordered = sorted(intervals, key=lambda interval: (interval.start, interval.end))
    if not ordered:
        return []
    merged = [ordered[0]]
    for interval in ordered[1:]:
        previous = merged[-1]
        if interval.start <= previous.end + tolerance:
            merged[-1] = EffectiveInterval(
                previous.start, max(previous.end, interval.end)
            )
        else:
            merged.append(interval)
    return merged


def intervals_duration(intervals: Iterable[EffectiveInterval]) -> float:
    return float(sum(interval.end - interval.start for interval in intervals))


def overlap_duration(
    individual_intervals: Sequence[Sequence[EffectiveInterval]],
    union_intervals: Sequence[EffectiveInterval],
) -> float:
    individual_total = sum(
        intervals_duration(intervals) for intervals in individual_intervals
    )
    return float(individual_total - intervals_duration(union_intervals))


def centerline_intervals_for_bomb(
    bomb: Strategy, step: float = 0.08
) -> list[EffectiveInterval]:
    start = bomb.burst_time_s
    end = min(start + CLOUD_LIFETIME, MISSILE_ARRIVAL_TIME)
    if end <= start:
        return []
    count = max(1, int(np.ceil((end - start) / step)))
    times = np.linspace(start, end, count + 1)
    distances = centerline_distances_for(bomb, times)
    return sampled_effective_intervals(times, distances)


def centerline_union_duration(
    decision: Sequence[float], step: float = 0.08
) -> float:
    strategy = decode_decision(decision)
    intervals = [
        interval
        for bomb in strategy.bombs
        for interval in centerline_intervals_for_bomb(bomb, step)
    ]
    return intervals_duration(merge_intervals(intervals))


def sampled_full_intervals_for_bomb(
    bomb: Strategy,
    target_points: np.ndarray,
    step: float = 0.04,
) -> list[EffectiveInterval]:
    start = bomb.burst_time_s
    end = min(start + CLOUD_LIFETIME, MISSILE_ARRIVAL_TIME)
    if end <= start:
        return []
    count = max(1, int(np.ceil((end - start) / step)))
    times = np.linspace(start, end, count + 1)
    distances = full_cylinder_distances_for(bomb, times, target_points)
    return sampled_effective_intervals(times, distances)


def sampled_full_union_duration(
    decision: Sequence[float],
    target_points: np.ndarray,
    step: float = 0.04,
) -> float:
    strategy = decode_decision(decision)
    start = min(bomb.burst_time_s for bomb in strategy.bombs)
    end = min(
        max(bomb.burst_time_s + CLOUD_LIFETIME for bomb in strategy.bombs),
        MISSILE_ARRIVAL_TIME,
    )
    count = max(1, int(np.ceil((end - start) / step)))
    times = np.linspace(start, end, count + 1)
    margins = joint_sightline_margins(
        times,
        target_points,
        strategy.bombs,
        missile_position,
        cloud_center_for,
    )
    return intervals_duration(sampled_effective_intervals(times, margins + CLOUD_RADIUS))


def exact_multi_bomb_intervals(
    strategy: MultiBombStrategy,
    target_points: np.ndarray,
    scan_step: float = 0.01,
) -> tuple[list[list[EffectiveInterval]], list[EffectiveInterval]]:
    validate_multi_strategy(strategy)
    individual = [
        exact_full_cylinder_intervals(bomb, target_points, scan_step)
        for bomb in strategy.bombs
    ]
    joint = exact_joint_intervals(
        strategy.bombs,
        target_points,
        missile_position,
        missile_position,
        cloud_center_for,
        cloud_center_for,
        MISSILE_ARRIVAL_TIME,
        scan_step=scan_step,
    )
    return individual, joint


def differential_evolution_unit_cube(
    objective: Callable[[np.ndarray], float],
    *,
    seed: int,
    population_size: int = 144,
    generations: int = 220,
    mutation: float = 0.76,
    crossover: float = 0.90,
    initial_decisions: Sequence[np.ndarray] = (),
) -> PopulationResult:
    if population_size < 12:
        raise ValueError("Population size must be at least 12.")
    rng = np.random.default_rng(seed)
    population = rng.random((population_size, DECISION_DIMENSION))
    for index, decision in enumerate(initial_decisions[:population_size]):
        population[index] = np.clip(np.asarray(decision), 0.0, 1.0)
    scores = np.array([objective(candidate) for candidate in population])
    history_best = [float(np.max(scores))]
    history_mean = [float(np.mean(scores))]

    for _ in range(generations):
        for index in range(population_size):
            pool = np.delete(np.arange(population_size), index)
            a, b, c = rng.choice(pool, size=3, replace=False)
            mutant = np.clip(
                population[a] + mutation * (population[b] - population[c]),
                0.0,
                1.0,
            )
            mask = rng.random(DECISION_DIMENSION) < crossover
            mask[rng.integers(0, DECISION_DIMENSION)] = True
            trial = np.where(mask, mutant, population[index])
            score = float(objective(trial))
            if score >= scores[index]:
                population[index] = trial
                scores[index] = score
        history_best.append(float(np.max(scores)))
        history_mean.append(float(np.mean(scores)))

    order = np.argsort(scores)[::-1]
    population = population[order]
    scores = scores[order]
    return PopulationResult(
        decision=population[0].copy(),
        score=float(scores[0]),
        history_best=np.asarray(history_best),
        history_mean=np.asarray(history_mean),
        population=population,
        population_scores=scores,
    )


def coordinate_refine_unit_cube(
    decision: Sequence[float],
    objective: Callable[[np.ndarray], float],
    *,
    initial_steps: Sequence[float] = (0.01,) * DECISION_DIMENSION,
    minimum_steps: Sequence[float] = (1e-4,) * DECISION_DIMENSION,
    max_rounds: int = 80,
) -> tuple[np.ndarray, float, list[float]]:
    current = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    current_score = float(objective(current))
    steps = np.asarray(initial_steps, dtype=float)
    minimum = np.asarray(minimum_steps, dtype=float)
    history = [current_score]

    for _ in range(max_rounds):
        improved = False
        for dimension in range(DECISION_DIMENSION):
            if steps[dimension] <= 0.0:
                continue
            best_candidate = current
            best_score = current_score
            for direction in (-1.0, 1.0):
                candidate = current.copy()
                candidate[dimension] = np.clip(
                    candidate[dimension] + direction * steps[dimension],
                    0.0,
                    1.0,
                )
                score = float(objective(candidate))
                if score > best_score + 1e-10:
                    best_candidate = candidate
                    best_score = score
            if best_score > current_score + 1e-10:
                current = best_candidate
                current_score = best_score
                improved = True
        history.append(current_score)
        if not improved:
            steps *= 0.5
        if np.all(steps <= minimum):
            break
    return current, current_score, history


def coarse_target_points() -> np.ndarray:
    return cylinder_surface_points(n_theta=32, n_z=5, n_r=4)


def seed_strategies() -> list[np.ndarray]:
    candidates = [
        MultiBombStrategy(
            heading_rad=np.radians(6.95),
            speed_mps=140.0,
            drop_times_s=(0.0, 1.0, 2.0),
            fuse_delays_s=(0.74, 0.74, 0.74),
        ),
        MultiBombStrategy(
            heading_rad=np.radians(9.23648438557577),
            speed_mps=103.59649265282755,
            drop_times_s=(0.0, 1.0, 2.0),
            fuse_delays_s=(0.005101962649377057, 0.0, 0.0),
        ),
        MultiBombStrategy(
            heading_rad=np.pi,
            speed_mps=120.0,
            drop_times_s=(0.0, 3.0, 6.0),
            fuse_delays_s=(3.6, 3.6, 3.6),
        ),
        MultiBombStrategy(
            heading_rad=np.radians(165.0),
            speed_mps=140.0,
            drop_times_s=(0.0, 4.0, 8.0),
            fuse_delays_s=(2.0, 2.0, 2.0),
        ),
    ]
    return [encode_strategy(candidate) for candidate in candidates]
