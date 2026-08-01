"""Problem 4: one smoke bomb from each of FY1, FY2, and FY3."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np

from problem1_model import (
    CLOUD_DESCENT_SPEED,
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    GRAVITY,
    TRUE_TARGET_CENTER,
    EffectiveInterval,
    _bisect_root,
    cylinder_surface_points,
    missile_position,
    point_to_segment_distance,
)
from problem2_model import (
    MAX_DRONE_SPEED,
    MIN_DRONE_SPEED,
    MISSILE_ARRIVAL_TIME,
    sampled_effective_intervals,
)
from problem3_model import intervals_duration, merge_intervals, overlap_duration
from joint_coverage import exact_joint_intervals, joint_sightline_margins


DRONE_IDS = ("FY1", "FY2", "FY3")
DRONE_INITIALS = {
    "FY1": np.array([17800.0, 0.0, 1800.0]),
    "FY2": np.array([12000.0, 1400.0, 1400.0]),
    "FY3": np.array([6000.0, -3000.0, 700.0]),
}
VARIABLES_PER_DRONE = 4
DECISION_DIMENSION = len(DRONE_IDS) * VARIABLES_PER_DRONE


@dataclass(frozen=True)
class DroneBombStrategy:
    drone_id: str
    heading_rad: float
    speed_mps: float
    drop_time_s: float
    fuse_delay_s: float

    @property
    def initial_position(self) -> np.ndarray:
        return DRONE_INITIALS[self.drone_id]

    @property
    def heading_deg(self) -> float:
        return float(np.degrees(self.heading_rad) % 360.0)

    @property
    def burst_time_s(self) -> float:
        return self.drop_time_s + self.fuse_delay_s

    @property
    def max_fuse_delay_s(self) -> float:
        return float(np.sqrt(2.0 * self.initial_position[2] / GRAVITY))

    @property
    def drone_velocity(self) -> np.ndarray:
        return self.speed_mps * np.array(
            [np.cos(self.heading_rad), np.sin(self.heading_rad), 0.0]
        )


@dataclass(frozen=True)
class MultiDroneStrategy:
    bombs: tuple[DroneBombStrategy, DroneBombStrategy, DroneBombStrategy]


@dataclass(frozen=True)
class PopulationResult:
    decision: np.ndarray
    score: float
    history_best: np.ndarray
    history_mean: np.ndarray
    population: np.ndarray
    population_scores: np.ndarray


def validate_bomb_strategy(strategy: DroneBombStrategy) -> None:
    if strategy.drone_id not in DRONE_INITIALS:
        raise ValueError(f"Unknown drone id: {strategy.drone_id}")
    if not MIN_DRONE_SPEED <= strategy.speed_mps <= MAX_DRONE_SPEED:
        raise ValueError("Drone speed is outside [70, 140] m/s.")
    if strategy.drop_time_s < 0.0 or strategy.fuse_delay_s < 0.0:
        raise ValueError("Drop time and fuse delay must be nonnegative.")
    if strategy.fuse_delay_s > strategy.max_fuse_delay_s + 1e-12:
        raise ValueError("The bomb would reach the ground before bursting.")
    if strategy.burst_time_s > MISSILE_ARRIVAL_TIME + 1e-12:
        raise ValueError("Burst occurs after M1 reaches the false target.")


def validate_multi_strategy(strategy: MultiDroneStrategy) -> None:
    if tuple(bomb.drone_id for bomb in strategy.bombs) != DRONE_IDS:
        raise ValueError("Problem 4 requires one ordered bomb from FY1/FY2/FY3.")
    for bomb in strategy.bombs:
        validate_bomb_strategy(bomb)


def decode_decision(decision: Sequence[float]) -> MultiDroneStrategy:
    values = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    if values.shape != (DECISION_DIMENSION,):
        raise ValueError("Problem 4 decision must have twelve elements.")
    bombs: list[DroneBombStrategy] = []
    for index, drone_id in enumerate(DRONE_IDS):
        offset = index * VARIABLES_PER_DRONE
        heading = -np.pi + 2.0 * np.pi * values[offset]
        speed = MIN_DRONE_SPEED + (
            MAX_DRONE_SPEED - MIN_DRONE_SPEED
        ) * values[offset + 1]
        burst_time = MISSILE_ARRIVAL_TIME * values[offset + 2]
        max_fuse = float(
            np.sqrt(2.0 * DRONE_INITIALS[drone_id][2] / GRAVITY)
        )
        fuse_limit = min(burst_time, max_fuse)
        fuse_delay = fuse_limit * values[offset + 3]
        bombs.append(
            DroneBombStrategy(
                drone_id=drone_id,
                heading_rad=float(heading),
                speed_mps=float(speed),
                drop_time_s=float(burst_time - fuse_delay),
                fuse_delay_s=float(fuse_delay),
            )
        )
    result = MultiDroneStrategy(tuple(bombs))
    validate_multi_strategy(result)
    return result


def decode_drone_block(
    decision: Sequence[float], drone_id: str
) -> DroneBombStrategy:
    if drone_id not in DRONE_INITIALS:
        raise ValueError(f"Unknown drone id: {drone_id}")
    values = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    if values.shape != (VARIABLES_PER_DRONE,):
        raise ValueError("A drone decision block must have four elements.")
    heading = -np.pi + 2.0 * np.pi * values[0]
    speed = MIN_DRONE_SPEED + (MAX_DRONE_SPEED - MIN_DRONE_SPEED) * values[1]
    burst_time = MISSILE_ARRIVAL_TIME * values[2]
    max_fuse = float(np.sqrt(2.0 * DRONE_INITIALS[drone_id][2] / GRAVITY))
    fuse_limit = min(burst_time, max_fuse)
    fuse_delay = fuse_limit * values[3]
    strategy = DroneBombStrategy(
        drone_id=drone_id,
        heading_rad=float(heading),
        speed_mps=float(speed),
        drop_time_s=float(burst_time - fuse_delay),
        fuse_delay_s=float(fuse_delay),
    )
    validate_bomb_strategy(strategy)
    return strategy


def encode_bomb_strategy(strategy: DroneBombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    fuse_limit = min(strategy.burst_time_s, strategy.max_fuse_delay_s)
    return np.array(
        [
            (strategy.heading_rad + np.pi) / (2.0 * np.pi),
            (strategy.speed_mps - MIN_DRONE_SPEED)
            / (MAX_DRONE_SPEED - MIN_DRONE_SPEED),
            strategy.burst_time_s / MISSILE_ARRIVAL_TIME,
            strategy.fuse_delay_s / fuse_limit if fuse_limit > 0.0 else 0.0,
        ]
    )


def encode_strategy(strategy: MultiDroneStrategy) -> np.ndarray:
    validate_multi_strategy(strategy)
    values = np.empty(DECISION_DIMENSION, dtype=float)
    for index, bomb in enumerate(strategy.bombs):
        offset = index * VARIABLES_PER_DRONE
        values[offset] = (bomb.heading_rad + np.pi) / (2.0 * np.pi)
        values[offset + 1] = (bomb.speed_mps - MIN_DRONE_SPEED) / (
            MAX_DRONE_SPEED - MIN_DRONE_SPEED
        )
        values[offset + 2] = bomb.burst_time_s / MISSILE_ARRIVAL_TIME
        fuse_limit = min(bomb.burst_time_s, bomb.max_fuse_delay_s)
        values[offset + 3] = (
            bomb.fuse_delay_s / fuse_limit if fuse_limit > 0.0 else 0.0
        )
    return np.clip(values, 0.0, 1.0)


def drop_point(strategy: DroneBombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    return strategy.initial_position + strategy.drop_time_s * strategy.drone_velocity


def burst_point(strategy: DroneBombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    return (
        strategy.initial_position
        + strategy.burst_time_s * strategy.drone_velocity
        + np.array(
            [0.0, 0.0, -0.5 * GRAVITY * strategy.fuse_delay_s**2],
            dtype=float,
        )
    )


def cloud_center_for(
    strategy: DroneBombStrategy, time: float | np.ndarray
) -> np.ndarray:
    validate_bomb_strategy(strategy)
    values = np.asarray(time, dtype=float)
    if np.any(values < strategy.burst_time_s):
        raise ValueError("Cloud centre is defined only after burst.")
    vertical = -CLOUD_DESCENT_SPEED * (values - strategy.burst_time_s)
    displacement = np.stack(
        [np.zeros_like(values), np.zeros_like(values), vertical],
        axis=-1,
    )
    return burst_point(strategy) + displacement


def centerline_distances_for(
    strategy: DroneBombStrategy, times: np.ndarray
) -> np.ndarray:
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
    strategy: DroneBombStrategy,
    time: float,
    target_points: np.ndarray,
) -> float:
    distances, _ = point_to_segment_distance(
        cloud_center_for(strategy, time),
        missile_position(time),
        target_points,
    )
    return float(np.max(distances))


def full_cylinder_distances_for(
    strategy: DroneBombStrategy,
    times: np.ndarray,
    target_points: np.ndarray,
    chunk_size: int = 32,
) -> np.ndarray:
    times = np.asarray(times, dtype=float)
    result = np.empty(len(times), dtype=float)
    for start in range(0, len(times), chunk_size):
        stop = min(start + chunk_size, len(times))
        chunk = times[start:stop]
        missiles = missile_position(chunk)
        clouds = cloud_center_for(strategy, chunk)
        vectors = target_points[None, :, :] - missiles[:, None, :]
        offsets = clouds[:, None, :] - missiles[:, None, :]
        denominator = np.sum(vectors * vectors, axis=2)
        projection = np.sum(vectors * offsets, axis=2) / denominator
        projection = np.clip(projection, 0.0, 1.0)
        closest = missiles[:, None, :] + projection[:, :, None] * vectors
        distances = np.linalg.norm(clouds[:, None, :] - closest, axis=2)
        result[start:stop] = np.max(distances, axis=1)
    return result


def _time_grid(strategy: DroneBombStrategy, step: float) -> np.ndarray:
    start = strategy.burst_time_s
    end = min(start + CLOUD_LIFETIME, MISSILE_ARRIVAL_TIME)
    if end <= start:
        return np.array([start])
    count = max(1, int(np.ceil((end - start) / step)))
    return np.linspace(start, end, count + 1)


def centerline_intervals_for_bomb(
    strategy: DroneBombStrategy, step: float = 0.08
) -> list[EffectiveInterval]:
    times = _time_grid(strategy, step)
    distances = centerline_distances_for(strategy, times)
    return sampled_effective_intervals(times, distances)


def sampled_full_intervals_for_bomb(
    strategy: DroneBombStrategy,
    target_points: np.ndarray,
    step: float = 0.04,
) -> list[EffectiveInterval]:
    times = _time_grid(strategy, step)
    distances = full_cylinder_distances_for(strategy, times, target_points)
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


def individual_centerline_duration(
    decision: Sequence[float], drone_id: str, step: float = 0.05
) -> float:
    strategy = decode_drone_block(decision, drone_id)
    return intervals_duration(centerline_intervals_for_bomb(strategy, step))


def individual_centerline_proximity_score(
    decision: Sequence[float], drone_id: str, step: float = 0.10
) -> float:
    """Continuous seed objective: negative minimum sight-line distance."""
    strategy = decode_drone_block(decision, drone_id)
    times = _time_grid(strategy, step)
    return -float(np.min(centerline_distances_for(strategy, times)))


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


def individual_sampled_full_duration(
    decision: Sequence[float],
    drone_id: str,
    target_points: np.ndarray,
    step: float = 0.04,
) -> float:
    strategy = decode_drone_block(decision, drone_id)
    return intervals_duration(
        sampled_full_intervals_for_bomb(strategy, target_points, step)
    )


def exact_full_intervals_for_bomb(
    strategy: DroneBombStrategy,
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


def exact_multi_drone_intervals(
    strategy: MultiDroneStrategy,
    target_points: np.ndarray,
    scan_step: float = 0.01,
) -> tuple[list[list[EffectiveInterval]], list[EffectiveInterval]]:
    validate_multi_strategy(strategy)
    individual = [
        exact_full_intervals_for_bomb(bomb, target_points, scan_step)
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
    population_size: int = 160,
    generations: int = 240,
    mutation: float = 0.76,
    crossover: float = 0.90,
    initial_decisions: Sequence[np.ndarray] = (),
    dimension: int = DECISION_DIMENSION,
) -> PopulationResult:
    if population_size < 16:
        raise ValueError("Population size must be at least 16.")
    rng = np.random.default_rng(seed)
    population = rng.random((population_size, dimension))
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
            mask = rng.random(dimension) < crossover
            mask[rng.integers(0, dimension)] = True
            trial = np.where(mask, mutant, population[index])
            score = float(objective(trial))
            if score >= scores[index]:
                population[index] = trial
                scores[index] = score
        history_best.append(float(np.max(scores)))
        history_mean.append(float(np.mean(scores)))
    order = np.argsort(scores)[::-1]
    return PopulationResult(
        decision=population[order[0]].copy(),
        score=float(scores[order[0]]),
        history_best=np.asarray(history_best),
        history_mean=np.asarray(history_mean),
        population=population[order],
        population_scores=scores[order],
    )


def coordinate_refine_unit_cube(
    decision: Sequence[float],
    objective: Callable[[np.ndarray], float],
    *,
    initial_steps: Sequence[float] | None = None,
    minimum_steps: Sequence[float] | None = None,
    max_rounds: int = 100,
) -> tuple[np.ndarray, float, list[float]]:
    current = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    current_score = float(objective(current))
    dimension = len(current)
    steps = np.asarray(
        initial_steps if initial_steps is not None else (0.01,) * dimension,
        dtype=float,
    )
    minimum = np.asarray(
        minimum_steps if minimum_steps is not None else (1e-4,) * dimension,
        dtype=float,
    )
    if steps.shape != current.shape or minimum.shape != current.shape:
        raise ValueError("Coordinate step vectors must match the decision.")
    history = [current_score]
    for _ in range(max_rounds):
        improved = False
        for axis in range(dimension):
            best_candidate = current
            best_score = current_score
            for direction in (-1.0, 1.0):
                candidate = current.copy()
                candidate[axis] = np.clip(
                    candidate[axis] + direction * steps[axis],
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
    problem3_like = MultiDroneStrategy(
        (
            DroneBombStrategy("FY1", np.radians(9.24), 103.6, 0.0, 0.005),
            DroneBombStrategy("FY2", np.radians(180.0), 120.0, 1.5, 3.6),
            DroneBombStrategy("FY3", np.radians(180.0), 120.0, 3.0, 3.6),
        )
    )
    target_directed = MultiDroneStrategy(
        tuple(
            DroneBombStrategy(
                drone_id,
                np.arctan2(-initial[1], -initial[0]),
                120.0,
                1.5,
                min(3.6, float(np.sqrt(2.0 * initial[2] / GRAVITY))),
            )
            for drone_id, initial in (
                (drone_id, DRONE_INITIALS[drone_id])
                for drone_id in DRONE_IDS
            )
        )
    )
    return [encode_strategy(problem3_like), encode_strategy(target_directed)]
