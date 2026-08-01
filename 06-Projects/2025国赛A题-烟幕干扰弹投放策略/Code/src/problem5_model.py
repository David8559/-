"""Problem 5: five drones, up to three bombs each, against M1/M2/M3."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Sequence

import numpy as np

from problem1_model import (
    CLOUD_DESCENT_SPEED,
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    FALSE_TARGET,
    GRAVITY,
    MISSILE_SPEED,
    TRUE_TARGET_CENTER,
    EffectiveInterval,
    _bisect_root,
    cylinder_surface_points,
    point_to_segment_distance,
)
from problem2_model import MAX_DRONE_SPEED, MIN_DRONE_SPEED, sampled_effective_intervals
from problem3_model import intervals_duration, merge_intervals
from problem4_model import coordinate_refine_unit_cube, differential_evolution_unit_cube
from joint_coverage import exact_joint_intervals


DRONE_IDS = ("FY1", "FY2", "FY3", "FY4", "FY5")
MISSILE_IDS = ("M1", "M2", "M3")
DRONE_INITIALS = {
    "FY1": np.array([17800.0, 0.0, 1800.0]),
    "FY2": np.array([12000.0, 1400.0, 1400.0]),
    "FY3": np.array([6000.0, -3000.0, 700.0]),
    "FY4": np.array([11000.0, 2000.0, 1800.0]),
    "FY5": np.array([13000.0, -2000.0, 1300.0]),
}
MISSILE_INITIALS = {
    "M1": np.array([20000.0, 0.0, 2000.0]),
    "M2": np.array([19000.0, 600.0, 2100.0]),
    "M3": np.array([18000.0, -600.0, 1900.0]),
}
MISSILE_VELOCITIES = {
    missile_id: MISSILE_SPEED
    * (FALSE_TARGET - initial)
    / np.linalg.norm(FALSE_TARGET - initial)
    for missile_id, initial in MISSILE_INITIALS.items()
}
MISSILE_ARRIVAL_TIMES = {
    missile_id: float(np.linalg.norm(initial - FALSE_TARGET) / MISSILE_SPEED)
    for missile_id, initial in MISSILE_INITIALS.items()
}
MIN_DROP_GAP = 1.0
MAX_BOMBS_PER_DRONE = 3


@dataclass(frozen=True)
class BombStrategy:
    drone_id: str
    missile_id: str
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
    def initial_position(self) -> np.ndarray:
        return DRONE_INITIALS[self.drone_id]

    @property
    def max_fuse_delay_s(self) -> float:
        return float(np.sqrt(2.0 * self.initial_position[2] / GRAVITY))

    @property
    def drone_velocity(self) -> np.ndarray:
        return self.speed_mps * np.array(
            [np.cos(self.heading_rad), np.sin(self.heading_rad), 0.0]
        )


@dataclass(frozen=True)
class DronePlan:
    drone_id: str
    bombs: tuple[BombStrategy, ...]

    @property
    def heading_rad(self) -> float:
        return self.bombs[0].heading_rad

    @property
    def speed_mps(self) -> float:
        return self.bombs[0].speed_mps


@dataclass(frozen=True)
class FleetStrategy:
    plans: tuple[DronePlan, ...]

    @property
    def bombs(self) -> tuple[BombStrategy, ...]:
        return tuple(bomb for plan in self.plans for bomb in plan.bombs)


def missile_position_for(
    missile_id: str, time: float | np.ndarray
) -> np.ndarray:
    if missile_id not in MISSILE_INITIALS:
        raise ValueError(f"Unknown missile id: {missile_id}")
    values = np.asarray(time, dtype=float)
    return MISSILE_INITIALS[missile_id] + np.expand_dims(
        values, axis=-1
    ) * MISSILE_VELOCITIES[missile_id]


def validate_bomb_strategy(strategy: BombStrategy) -> None:
    if strategy.drone_id not in DRONE_INITIALS:
        raise ValueError(f"Unknown drone id: {strategy.drone_id}")
    if strategy.missile_id not in MISSILE_INITIALS:
        raise ValueError(f"Unknown missile id: {strategy.missile_id}")
    if not MIN_DRONE_SPEED <= strategy.speed_mps <= MAX_DRONE_SPEED:
        raise ValueError("Drone speed is outside [70, 140] m/s.")
    if strategy.drop_time_s < 0.0 or strategy.fuse_delay_s < 0.0:
        raise ValueError("Drop time and fuse delay must be nonnegative.")
    if strategy.fuse_delay_s > strategy.max_fuse_delay_s + 1e-12:
        raise ValueError("The bomb would reach the ground before bursting.")
    if (
        strategy.burst_time_s
        > MISSILE_ARRIVAL_TIMES[strategy.missile_id] + 1e-12
    ):
        raise ValueError("Burst occurs after the assigned missile arrives.")


def validate_drone_plan(plan: DronePlan) -> None:
    if plan.drone_id not in DRONE_INITIALS:
        raise ValueError(f"Unknown drone id: {plan.drone_id}")
    if not 1 <= len(plan.bombs) <= MAX_BOMBS_PER_DRONE:
        raise ValueError("A nonempty plan must contain one to three bombs.")
    if any(bomb.drone_id != plan.drone_id for bomb in plan.bombs):
        raise ValueError("Every bomb in a plan must belong to the same drone.")
    for bomb in plan.bombs:
        validate_bomb_strategy(bomb)
        if abs(bomb.heading_rad - plan.heading_rad) > 1e-10:
            raise ValueError("A drone cannot change heading between bombs.")
        if abs(bomb.speed_mps - plan.speed_mps) > 1e-10:
            raise ValueError("A drone cannot change speed between bombs.")
    drops = np.sort([bomb.drop_time_s for bomb in plan.bombs])
    if np.any(np.diff(drops) < MIN_DROP_GAP - 1e-10):
        raise ValueError("Consecutive drops must be at least one second apart.")


def validate_fleet_strategy(strategy: FleetStrategy) -> None:
    ids = tuple(plan.drone_id for plan in strategy.plans)
    if len(ids) != len(set(ids)):
        raise ValueError("A drone may appear in at most one plan.")
    if any(drone_id not in DRONE_INITIALS for drone_id in ids):
        raise ValueError("Unknown drone in fleet strategy.")
    for plan in strategy.plans:
        validate_drone_plan(plan)


def decode_pair_decision(
    decision: Sequence[float], drone_id: str, missile_id: str
) -> BombStrategy:
    values = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    if values.shape != (4,):
        raise ValueError("A pair decision must have four elements.")
    heading = -np.pi + 2.0 * np.pi * values[0]
    speed = MIN_DRONE_SPEED + (MAX_DRONE_SPEED - MIN_DRONE_SPEED) * values[1]
    burst_time = MISSILE_ARRIVAL_TIMES[missile_id] * values[2]
    max_fuse = float(np.sqrt(2.0 * DRONE_INITIALS[drone_id][2] / GRAVITY))
    fuse_limit = min(burst_time, max_fuse)
    fuse = fuse_limit * values[3]
    result = BombStrategy(
        drone_id,
        missile_id,
        float(heading),
        float(speed),
        float(burst_time - fuse),
        float(fuse),
    )
    validate_bomb_strategy(result)
    return result


def encode_pair_strategy(strategy: BombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    fuse_limit = min(
        strategy.burst_time_s,
        strategy.max_fuse_delay_s,
    )
    return np.clip(
        np.array(
            [
                (strategy.heading_rad + np.pi) / (2.0 * np.pi),
                (strategy.speed_mps - MIN_DRONE_SPEED)
                / (MAX_DRONE_SPEED - MIN_DRONE_SPEED),
                strategy.burst_time_s
                / MISSILE_ARRIVAL_TIMES[strategy.missile_id],
                strategy.fuse_delay_s / fuse_limit if fuse_limit > 0.0 else 0.0,
            ]
        ),
        0.0,
        1.0,
    )


def decode_fixed_path_decision(
    decision: Sequence[float],
    drone_id: str,
    missile_id: str,
    heading_rad: float,
    speed_mps: float,
) -> BombStrategy:
    values = np.clip(np.asarray(decision, dtype=float), 0.0, 1.0)
    if values.shape != (2,):
        raise ValueError("A fixed-path decision must have two elements.")
    burst_time = MISSILE_ARRIVAL_TIMES[missile_id] * values[0]
    max_fuse = float(np.sqrt(2.0 * DRONE_INITIALS[drone_id][2] / GRAVITY))
    fuse_limit = min(burst_time, max_fuse)
    fuse = fuse_limit * values[1]
    result = BombStrategy(
        drone_id,
        missile_id,
        float(heading_rad),
        float(speed_mps),
        float(burst_time - fuse),
        float(fuse),
    )
    validate_bomb_strategy(result)
    return result


def drop_point(strategy: BombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    return strategy.initial_position + strategy.drop_time_s * strategy.drone_velocity


def burst_point(strategy: BombStrategy) -> np.ndarray:
    validate_bomb_strategy(strategy)
    return (
        strategy.initial_position
        + strategy.burst_time_s * strategy.drone_velocity
        + np.array([0.0, 0.0, -0.5 * GRAVITY * strategy.fuse_delay_s**2])
    )


def cloud_center_for(
    strategy: BombStrategy, time: float | np.ndarray
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


def _time_grid(strategy: BombStrategy, step: float) -> np.ndarray:
    start = strategy.burst_time_s
    end = min(
        start + CLOUD_LIFETIME,
        MISSILE_ARRIVAL_TIMES[strategy.missile_id],
    )
    if end <= start:
        return np.array([start])
    count = max(1, int(np.ceil((end - start) / step)))
    return np.linspace(start, end, count + 1)


def centerline_distances_for(
    strategy: BombStrategy, times: np.ndarray
) -> np.ndarray:
    clouds = cloud_center_for(strategy, times)
    missiles = missile_position_for(strategy.missile_id, times)
    vectors = TRUE_TARGET_CENTER - missiles
    offsets = clouds - missiles
    denominator = np.sum(vectors * vectors, axis=1)
    projection = np.sum(vectors * offsets, axis=1) / denominator
    projection = np.clip(projection, 0.0, 1.0)
    closest = missiles + projection[:, None] * vectors
    return np.linalg.norm(clouds - closest, axis=1)


def full_cylinder_distance_for(
    strategy: BombStrategy,
    time: float,
    target_points: np.ndarray,
) -> float:
    distances, _ = point_to_segment_distance(
        cloud_center_for(strategy, time),
        missile_position_for(strategy.missile_id, time),
        target_points,
    )
    return float(np.max(distances))


def full_cylinder_distances_for(
    strategy: BombStrategy,
    times: np.ndarray,
    target_points: np.ndarray,
    chunk_size: int = 24,
) -> np.ndarray:
    values = np.asarray(times, dtype=float)
    result = np.empty(len(values), dtype=float)
    for start in range(0, len(values), chunk_size):
        stop = min(start + chunk_size, len(values))
        chunk = values[start:stop]
        missiles = missile_position_for(strategy.missile_id, chunk)
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


def centerline_intervals_for_bomb(
    strategy: BombStrategy, step: float = 0.08
) -> list[EffectiveInterval]:
    times = _time_grid(strategy, step)
    return sampled_effective_intervals(
        times, centerline_distances_for(strategy, times)
    )


def sampled_full_intervals_for_bomb(
    strategy: BombStrategy,
    target_points: np.ndarray,
    step: float = 0.06,
) -> list[EffectiveInterval]:
    times = _time_grid(strategy, step)
    return sampled_effective_intervals(
        times,
        full_cylinder_distances_for(strategy, times, target_points),
    )


def exact_full_intervals_for_bomb(
    strategy: BombStrategy,
    target_points: np.ndarray,
    scan_step: float = 0.01,
) -> list[EffectiveInterval]:
    times = _time_grid(strategy, scan_step)
    margins = (
        full_cylinder_distances_for(strategy, times, target_points) - CLOUD_RADIUS
    )
    effective = margins <= 0.0
    intervals: list[EffectiveInterval] = []
    current_start: float | None = (
        float(times[0]) if effective[0] else None
    )
    for index in range(len(times) - 1):
        if effective[index] == effective[index + 1]:
            continue
        crossing = _bisect_root(
            lambda value: full_cylinder_distance_for(
                strategy, value, target_points
            )
            - CLOUD_RADIUS,
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
        intervals.append(EffectiveInterval(current_start, float(times[-1])))
    return intervals


def pair_centerline_duration(
    decision: Sequence[float],
    drone_id: str,
    missile_id: str,
    step: float = 0.08,
) -> float:
    strategy = decode_pair_decision(decision, drone_id, missile_id)
    return intervals_duration(centerline_intervals_for_bomb(strategy, step))


def pair_proximity_score(
    decision: Sequence[float],
    drone_id: str,
    missile_id: str,
    step: float = 0.12,
) -> float:
    strategy = decode_pair_decision(decision, drone_id, missile_id)
    times = _time_grid(strategy, step)
    return -float(np.min(centerline_distances_for(strategy, times)))


def pair_sampled_full_duration(
    decision: Sequence[float],
    drone_id: str,
    missile_id: str,
    target_points: np.ndarray,
    step: float = 0.06,
) -> float:
    strategy = decode_pair_decision(decision, drone_id, missile_id)
    return intervals_duration(
        sampled_full_intervals_for_bomb(strategy, target_points, step)
    )


def fixed_path_centerline_duration(
    decision: Sequence[float],
    drone_id: str,
    missile_id: str,
    heading_rad: float,
    speed_mps: float,
    step: float = 0.08,
) -> float:
    strategy = decode_fixed_path_decision(
        decision, drone_id, missile_id, heading_rad, speed_mps
    )
    return intervals_duration(centerline_intervals_for_bomb(strategy, step))


def intervals_by_missile(
    bombs_with_intervals: Iterable[
        tuple[BombStrategy, Sequence[EffectiveInterval]]
    ],
) -> dict[str, list[EffectiveInterval]]:
    grouped = {missile_id: [] for missile_id in MISSILE_IDS}
    for bomb, intervals in bombs_with_intervals:
        grouped[bomb.missile_id].extend(intervals)
    return {
        missile_id: merge_intervals(intervals)
        for missile_id, intervals in grouped.items()
    }


def coverage_durations(
    bombs_with_intervals: Iterable[
        tuple[BombStrategy, Sequence[EffectiveInterval]]
    ],
) -> dict[str, float]:
    grouped = intervals_by_missile(bombs_with_intervals)
    return {
        missile_id: intervals_duration(grouped[missile_id])
        for missile_id in MISSILE_IDS
    }


def intersect_interval_sets(
    interval_sets: Sequence[Sequence[EffectiveInterval]],
) -> list[EffectiveInterval]:
    """Return the intersection of several unions of closed intervals."""

    if not interval_sets:
        return []
    current = list(interval_sets[0])
    for intervals in interval_sets[1:]:
        next_intersection: list[EffectiveInterval] = []
        left_index = 0
        right_index = 0
        left = current
        right = list(intervals)
        while left_index < len(left) and right_index < len(right):
            start = max(left[left_index].start, right[right_index].start)
            end = min(left[left_index].end, right[right_index].end)
            if end > start:
                next_intersection.append(EffectiveInterval(start, end))
            if left[left_index].end <= right[right_index].end:
                left_index += 1
            else:
                right_index += 1
        current = next_intersection
        if not current:
            break
    return current


def exact_joint_intervals_by_missile(
    bombs: Sequence[BombStrategy],
    target_points: np.ndarray,
    scan_step: float = 0.01,
) -> dict[str, list[EffectiveInterval]]:
    """Evaluate all active clouds against every incoming missile.

    A bomb's ``missile_id`` is a planning label, not a physical restriction:
    any active cloud may block a sight line from any missile.
    """

    return {
        missile_id: exact_joint_intervals(
            bombs,
            target_points,
            lambda time, mid=missile_id: missile_position_for(mid, time),
            lambda times, mid=missile_id: missile_position_for(mid, times),
            cloud_center_for,
            cloud_center_for,
            MISSILE_ARRIVAL_TIMES[missile_id],
            scan_step=scan_step,
        )
        for missile_id in MISSILE_IDS
    }


def plan_is_drop_feasible(bombs: Sequence[BombStrategy]) -> bool:
    if not bombs:
        return True
    first = bombs[0]
    if any(bomb.drone_id != first.drone_id for bomb in bombs):
        return False
    if any(abs(bomb.heading_rad - first.heading_rad) > 1e-10 for bomb in bombs):
        return False
    if any(abs(bomb.speed_mps - first.speed_mps) > 1e-10 for bomb in bombs):
        return False
    drops = np.sort([bomb.drop_time_s for bomb in bombs])
    return bool(np.all(np.diff(drops) >= MIN_DROP_GAP - 1e-10))


def feasible_bomb_combinations(
    bombs: Sequence[BombStrategy],
    max_bombs: int = MAX_BOMBS_PER_DRONE,
) -> Iterable[tuple[BombStrategy, ...]]:
    for size in range(1, min(max_bombs, len(bombs)) + 1):
        for chosen in combinations(bombs, size):
            if plan_is_drop_feasible(chosen):
                yield tuple(sorted(chosen, key=lambda bomb: bomb.drop_time_s))


def coarse_target_points() -> np.ndarray:
    return cylinder_surface_points(n_theta=36, n_z=5, n_r=4)
