"""Problem 2 single-bomb optimization for the 2025 CUMCM A problem.

The time origin, coordinate system, target geometry, and complete-cylinder
screening criterion are inherited from :mod:`problem1_model`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

import numpy as np

from problem1_model import (
    CLOUD_DESCENT_SPEED,
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    FALSE_TARGET,
    FY1_INITIAL,
    GRAVITY,
    TRUE_TARGET_CENTER,
    EffectiveInterval,
    _bisect_root,
    cylinder_surface_points,
    missile_arrival_time,
    missile_position,
    point_to_segment_distance,
)


MIN_DRONE_SPEED = 70.0
MAX_DRONE_SPEED = 140.0
MAX_FUSE_DELAY = float(np.sqrt(2.0 * FY1_INITIAL[2] / GRAVITY))
MISSILE_ARRIVAL_TIME = missile_arrival_time()

# Internal optimization variables are heading, speed, burst time, and a fuse
# fraction. The fraction maps to [0, min(burst time, time-to-ground)], which
# guarantees nonnegative drop time and an above-ground burst.
DECISION_BOUNDS = np.array(
    [
        [-np.pi, np.pi],
        [MIN_DRONE_SPEED, MAX_DRONE_SPEED],
        [0.0, MISSILE_ARRIVAL_TIME],
        [0.0, 1.0],
    ],
    dtype=float,
)


@dataclass(frozen=True)
class Strategy:
    heading_rad: float
    speed_mps: float
    drop_time_s: float
    fuse_delay_s: float

    @property
    def heading_deg(self) -> float:
        return float(np.degrees(self.heading_rad) % 360.0)

    @property
    def burst_time_s(self) -> float:
        return self.drop_time_s + self.fuse_delay_s

    @property
    def drone_velocity(self) -> np.ndarray:
        return self.speed_mps * np.array(
            [np.cos(self.heading_rad), np.sin(self.heading_rad), 0.0]
        )


@dataclass(frozen=True)
class OptimizationResult:
    decision: np.ndarray
    score: float
    history_best: np.ndarray
    history_mean: np.ndarray
    population: np.ndarray
    population_scores: np.ndarray


def strategy_from_decision(decision: Sequence[float]) -> Strategy:
    heading, speed, burst_time, fuse_fraction = np.asarray(decision, dtype=float)
    fuse_limit = min(float(burst_time), MAX_FUSE_DELAY)
    fuse_delay = float(np.clip(fuse_fraction, 0.0, 1.0) * fuse_limit)
    return Strategy(
        heading_rad=float(heading),
        speed_mps=float(speed),
        drop_time_s=float(burst_time - fuse_delay),
        fuse_delay_s=fuse_delay,
    )


def decision_from_strategy(strategy: Strategy) -> np.ndarray:
    fuse_limit = min(strategy.burst_time_s, MAX_FUSE_DELAY)
    fuse_fraction = strategy.fuse_delay_s / fuse_limit if fuse_limit > 0.0 else 0.0
    return np.array(
        [
            strategy.heading_rad,
            strategy.speed_mps,
            strategy.burst_time_s,
            fuse_fraction,
        ],
        dtype=float,
    )


def validate_strategy(strategy: Strategy) -> None:
    if not MIN_DRONE_SPEED <= strategy.speed_mps <= MAX_DRONE_SPEED:
        raise ValueError("Drone speed is outside [70, 140] m/s.")
    if strategy.drop_time_s < 0.0:
        raise ValueError("Drop time must be nonnegative.")
    if strategy.fuse_delay_s < 0.0:
        raise ValueError("Fuse delay must be nonnegative.")
    if strategy.fuse_delay_s > MAX_FUSE_DELAY + 1e-12:
        raise ValueError("The bomb would reach the ground before bursting.")
    if strategy.burst_time_s > MISSILE_ARRIVAL_TIME + 1e-12:
        raise ValueError("Burst occurs after M1 reaches the false target.")


def drop_point(strategy: Strategy) -> np.ndarray:
    validate_strategy(strategy)
    return FY1_INITIAL + strategy.drop_time_s * strategy.drone_velocity


def burst_point(strategy: Strategy) -> np.ndarray:
    validate_strategy(strategy)
    return (
        FY1_INITIAL
        + strategy.burst_time_s * strategy.drone_velocity
        + np.array(
            [0.0, 0.0, -0.5 * GRAVITY * strategy.fuse_delay_s**2],
            dtype=float,
        )
    )


def cloud_center_for(strategy: Strategy, t: float | np.ndarray) -> np.ndarray:
    validate_strategy(strategy)
    time = np.asarray(t, dtype=float)
    if np.any(time < strategy.burst_time_s):
        raise ValueError("Cloud centre is defined only after burst.")
    vertical = -CLOUD_DESCENT_SPEED * (time - strategy.burst_time_s)
    displacement = np.stack(
        [np.zeros_like(time), np.zeros_like(time), vertical],
        axis=-1,
    )
    return burst_point(strategy) + displacement


def centerline_distance_for(strategy: Strategy, t: float) -> float:
    distance, _ = point_to_segment_distance(
        cloud_center_for(strategy, t),
        missile_position(t),
        TRUE_TARGET_CENTER,
    )
    return float(distance)


def centerline_distances_for(strategy: Strategy, times: np.ndarray) -> np.ndarray:
    clouds = cloud_center_for(strategy, times)
    missiles = missile_position(times)
    vectors = TRUE_TARGET_CENTER - missiles
    offsets = clouds - missiles
    denominator = np.sum(vectors * vectors, axis=1)
    projection = np.sum(vectors * offsets, axis=1) / denominator
    projection = np.clip(projection, 0.0, 1.0)
    closest = missiles + projection[:, None] * vectors
    return np.linalg.norm(clouds - closest, axis=1)


def full_cylinder_distance_for(
    strategy: Strategy, t: float, target_points: np.ndarray
) -> float:
    distances, _ = point_to_segment_distance(
        cloud_center_for(strategy, t),
        missile_position(t),
        target_points,
    )
    return float(np.max(distances))


def full_cylinder_distances_for(
    strategy: Strategy,
    times: np.ndarray,
    target_points: np.ndarray,
    chunk_size: int = 32,
) -> np.ndarray:
    """Vectorized worst sight-line distance, chunked to bound memory."""
    times = np.asarray(times, dtype=float)
    result = np.empty(len(times), dtype=float)
    for start_index in range(0, len(times), chunk_size):
        stop_index = min(start_index + chunk_size, len(times))
        chunk = times[start_index:stop_index]
        missiles = missile_position(chunk)
        clouds = cloud_center_for(strategy, chunk)
        vectors = target_points[None, :, :] - missiles[:, None, :]
        offsets = clouds[:, None, :] - missiles[:, None, :]
        denominator = np.sum(vectors * vectors, axis=2)
        projection = np.sum(vectors * offsets, axis=2) / denominator
        projection = np.clip(projection, 0.0, 1.0)
        closest = missiles[:, None, :] + projection[:, :, None] * vectors
        distances = np.linalg.norm(clouds[:, None, :] - closest, axis=2)
        result[start_index:stop_index] = np.max(distances, axis=1)
    return result


def _time_grid(strategy: Strategy, step: float) -> np.ndarray:
    end = min(strategy.burst_time_s + CLOUD_LIFETIME, MISSILE_ARRIVAL_TIME)
    if end <= strategy.burst_time_s:
        return np.array([strategy.burst_time_s], dtype=float)
    count = max(1, int(np.ceil((end - strategy.burst_time_s) / step)))
    return np.linspace(strategy.burst_time_s, end, count + 1)


def sampled_effective_intervals(
    times: np.ndarray, distances: np.ndarray, radius: float = CLOUD_RADIUS
) -> list[EffectiveInterval]:
    """Interpolate threshold crossings on a sampled distance series."""
    times = np.asarray(times, dtype=float)
    margins = np.asarray(distances, dtype=float) - radius
    if times.ndim != 1 or margins.shape != times.shape:
        raise ValueError("Times and distances must be equal-length vectors.")

    effective = margins <= 0.0
    intervals: list[EffectiveInterval] = []
    current_start: float | None = float(times[0]) if effective[0] else None
    for index in range(len(times) - 1):
        if effective[index] == effective[index + 1]:
            continue
        left_margin = margins[index]
        right_margin = margins[index + 1]
        weight = -left_margin / (right_margin - left_margin)
        crossing = float(times[index] + weight * (times[index + 1] - times[index]))
        if not effective[index] and effective[index + 1]:
            current_start = crossing
        else:
            if current_start is None:
                raise RuntimeError("Effective interval ended before it started.")
            intervals.append(EffectiveInterval(current_start, crossing))
            current_start = None
    if current_start is not None:
        intervals.append(EffectiveInterval(current_start, float(times[-1])))
    return intervals


def interval_duration(intervals: Iterable[EffectiveInterval]) -> float:
    return float(sum(interval.duration for interval in intervals))


def centerline_proxy_duration(decision: Sequence[float], step: float = 0.05) -> float:
    strategy = strategy_from_decision(decision)
    times = _time_grid(strategy, step)
    distances = centerline_distances_for(strategy, times)
    return interval_duration(sampled_effective_intervals(times, distances))


def sampled_full_cylinder_duration(
    decision: Sequence[float],
    target_points: np.ndarray,
    step: float = 0.04,
) -> float:
    strategy = strategy_from_decision(decision)
    times = _time_grid(strategy, step)
    distances = full_cylinder_distances_for(strategy, times, target_points)
    return interval_duration(sampled_effective_intervals(times, distances))


def exact_full_cylinder_intervals(
    strategy: Strategy,
    target_points: np.ndarray,
    scan_step: float = 0.01,
) -> list[EffectiveInterval]:
    start = strategy.burst_time_s
    end = min(start + CLOUD_LIFETIME, MISSILE_ARRIVAL_TIME)
    count = max(1, int(np.ceil((end - start) / scan_step)))
    times = np.linspace(start, end, count + 1)
    function = lambda value: full_cylinder_distance_for(
        strategy, value, target_points
    )
    margins = np.array([function(float(value)) - CLOUD_RADIUS for value in times])
    effective = margins <= 0.0
    intervals: list[EffectiveInterval] = []
    current_start: float | None = start if effective[0] else None

    for index in range(len(times) - 1):
        if effective[index] == effective[index + 1]:
            continue
        crossing = _bisect_root(
            lambda value: function(value) - CLOUD_RADIUS,
            float(times[index]),
            float(times[index + 1]),
        )
        if not effective[index] and effective[index + 1]:
            current_start = crossing
        else:
            if current_start is None:
                raise RuntimeError("Effective interval ended before it started.")
            intervals.append(EffectiveInterval(current_start, crossing))
            current_start = None
    if current_start is not None:
        intervals.append(EffectiveInterval(current_start, end))
    return intervals


def _repair_decision(decision: np.ndarray) -> np.ndarray:
    repaired = np.asarray(decision, dtype=float).copy()
    repaired[0] = (repaired[0] + np.pi) % (2.0 * np.pi) - np.pi
    repaired[1:] = np.clip(
        repaired[1:],
        DECISION_BOUNDS[1:, 0],
        DECISION_BOUNDS[1:, 1],
    )
    return repaired


def differential_evolution_maximize(
    objective: Callable[[np.ndarray], float],
    *,
    seed: int,
    population_size: int = 72,
    generations: int = 100,
    mutation: float = 0.78,
    crossover: float = 0.88,
    initial_decisions: Sequence[np.ndarray] = (),
) -> OptimizationResult:
    """Small dependency-free differential-evolution implementation."""
    if population_size < 8:
        raise ValueError("Population size must be at least 8.")
    rng = np.random.default_rng(seed)
    lower = DECISION_BOUNDS[:, 0]
    upper = DECISION_BOUNDS[:, 1]
    population = rng.uniform(lower, upper, size=(population_size, len(lower)))
    for index, decision in enumerate(initial_decisions[:population_size]):
        population[index] = _repair_decision(np.asarray(decision, dtype=float))
    scores = np.array([objective(candidate) for candidate in population])
    history_best = [float(np.max(scores))]
    history_mean = [float(np.mean(scores))]

    for _ in range(generations):
        for index in range(population_size):
            pool = np.delete(np.arange(population_size), index)
            a, b, c = rng.choice(pool, size=3, replace=False)
            mutant = _repair_decision(
                population[a] + mutation * (population[b] - population[c])
            )
            use_mutant = rng.random(len(lower)) < crossover
            use_mutant[rng.integers(0, len(lower))] = True
            trial = np.where(use_mutant, mutant, population[index])
            trial = _repair_decision(trial)
            trial_score = float(objective(trial))
            if trial_score >= scores[index]:
                population[index] = trial
                scores[index] = trial_score
        history_best.append(float(np.max(scores)))
        history_mean.append(float(np.mean(scores)))

    order = np.argsort(scores)[::-1]
    population = population[order]
    scores = scores[order]
    return OptimizationResult(
        decision=population[0].copy(),
        score=float(scores[0]),
        history_best=np.asarray(history_best),
        history_mean=np.asarray(history_mean),
        population=population,
        population_scores=scores,
    )


def coordinate_refine(
    decision: Sequence[float],
    objective: Callable[[np.ndarray], float],
    *,
    initial_steps: Sequence[float] = (0.035, 2.0, 0.25, 0.035),
    minimum_steps: Sequence[float] = (2e-4, 0.02, 0.002, 2e-4),
    max_rounds: int = 90,
) -> tuple[np.ndarray, float, list[float]]:
    """Deterministic coordinate pattern search around one candidate."""
    current = _repair_decision(np.asarray(decision, dtype=float))
    current_score = float(objective(current))
    steps = np.asarray(initial_steps, dtype=float)
    minimum = np.asarray(minimum_steps, dtype=float)
    history = [current_score]

    for _ in range(max_rounds):
        improved = False
        for dimension in range(len(current)):
            if steps[dimension] <= 0.0:
                continue
            best_candidate = current
            best_score = current_score
            for direction in (-1.0, 1.0):
                candidate = current.copy()
                candidate[dimension] += direction * steps[dimension]
                candidate = _repair_decision(candidate)
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


def baseline_problem1_strategy() -> Strategy:
    return Strategy(
        heading_rad=np.pi,
        speed_mps=120.0,
        drop_time_s=1.5,
        fuse_delay_s=3.6,
    )


def coarse_target_points() -> np.ndarray:
    return cylinder_surface_points(n_theta=48, n_z=5, n_r=4)
