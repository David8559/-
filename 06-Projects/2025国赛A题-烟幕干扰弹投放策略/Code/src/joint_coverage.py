"""Joint line-of-sight coverage by multiple smoke clouds.

The essential quantifier order is

    for every target point, there exists an active cloud blocking its sight line.

This differs from first requiring one cloud to cover the complete target and
then taking the union of those single-cloud time intervals.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Protocol

import numpy as np

from problem1_model import CLOUD_LIFETIME, CLOUD_RADIUS, EffectiveInterval


class TimedCloud(Protocol):
    @property
    def burst_time_s(self) -> float: ...


def joint_sightline_margin(
    missile: np.ndarray,
    target_points: np.ndarray,
    cloud_centers: np.ndarray,
    radius: float = CLOUD_RADIUS,
) -> float:
    """Return ``max_target min_cloud distance - radius`` for one time.

    A non-positive value means every sampled target sight line intersects at
    least one active cloud.  Empty cloud sets return positive infinity.
    """

    missile = np.asarray(missile, dtype=float)
    targets = np.asarray(target_points, dtype=float)
    clouds = np.asarray(cloud_centers, dtype=float)
    if clouds.size == 0:
        return float("inf")
    clouds = np.atleast_2d(clouds)
    vectors = targets - missile
    denominator = np.sum(vectors * vectors, axis=1)
    if np.any(denominator <= 0.0):
        raise ValueError("A target point coincides with the missile position.")

    best = np.full(len(targets), np.inf)
    for cloud in clouds:
        offset = cloud - missile
        projection = np.sum(vectors * offset, axis=1) / denominator
        projection = np.clip(projection, 0.0, 1.0)
        closest = missile + projection[:, None] * vectors
        best = np.minimum(best, np.linalg.norm(cloud - closest, axis=1))
    return float(np.max(best) - radius)


def joint_sightline_margins(
    times: np.ndarray,
    target_points: np.ndarray,
    clouds: Sequence[TimedCloud],
    missile_position_fn: Callable[[np.ndarray], np.ndarray],
    cloud_center_fn: Callable[[TimedCloud, np.ndarray], np.ndarray],
    *,
    radius: float = CLOUD_RADIUS,
    lifetime: float = CLOUD_LIFETIME,
    chunk_size: int = 24,
) -> np.ndarray:
    """Vectorized joint margins on a time grid."""

    values = np.asarray(times, dtype=float)
    targets = np.asarray(target_points, dtype=float)
    result = np.full(len(values), np.inf)
    for start in range(0, len(values), chunk_size):
        stop = min(start + chunk_size, len(values))
        chunk = values[start:stop]
        missiles = np.asarray(missile_position_fn(chunk), dtype=float)
        vectors = targets[None, :, :] - missiles[:, None, :]
        denominator = np.sum(vectors * vectors, axis=2)
        best = np.full((len(chunk), len(targets)), np.inf)
        for cloud in clouds:
            active = (chunk >= cloud.burst_time_s) & (
                chunk <= cloud.burst_time_s + lifetime
            )
            if not np.any(active):
                continue
            centers = np.zeros((len(chunk), 3), dtype=float)
            centers[active] = np.asarray(
                cloud_center_fn(cloud, chunk[active]), dtype=float
            )
            offsets = centers[:, None, :] - missiles[:, None, :]
            projection = np.sum(vectors * offsets, axis=2) / denominator
            projection = np.clip(projection, 0.0, 1.0)
            closest = missiles[:, None, :] + projection[:, :, None] * vectors
            distances = np.linalg.norm(centers[:, None, :] - closest, axis=2)
            distances[~active, :] = np.inf
            best = np.minimum(best, distances)
        result[start:stop] = np.max(best, axis=1) - radius
    return result


def _bisect_transition(
    margin_fn: Callable[[float], float],
    left: float,
    right: float,
    *,
    tolerance: float = 1e-9,
    max_iterations: int = 100,
) -> float:
    """Locate a Boolean coverage transition, including cloud life events."""

    left_effective = margin_fn(left) <= 0.0
    for _ in range(max_iterations):
        midpoint = 0.5 * (left + right)
        if right - left <= tolerance:
            return midpoint
        if (margin_fn(midpoint) <= 0.0) == left_effective:
            left = midpoint
        else:
            right = midpoint
    return 0.5 * (left + right)


def exact_joint_intervals(
    clouds: Sequence[TimedCloud],
    target_points: np.ndarray,
    missile_position_scalar_fn: Callable[[float], np.ndarray],
    missile_position_vector_fn: Callable[[np.ndarray], np.ndarray],
    cloud_center_scalar_fn: Callable[[TimedCloud, float], np.ndarray],
    cloud_center_vector_fn: Callable[[TimedCloud, np.ndarray], np.ndarray],
    end_time: float,
    *,
    scan_step: float = 0.01,
    radius: float = CLOUD_RADIUS,
    lifetime: float = CLOUD_LIFETIME,
) -> list[EffectiveInterval]:
    """Find continuous-time intervals satisfying joint complete coverage."""

    if not clouds:
        return []
    start_time = min(float(cloud.burst_time_s) for cloud in clouds)
    stop_time = min(
        float(end_time),
        max(float(cloud.burst_time_s) + lifetime for cloud in clouds),
    )
    if stop_time <= start_time:
        return []
    count = max(1, int(np.ceil((stop_time - start_time) / scan_step)))
    regular = np.linspace(start_time, stop_time, count + 1)
    events = [start_time, stop_time]
    for cloud in clouds:
        events.extend(
            [
                max(start_time, float(cloud.burst_time_s)),
                min(stop_time, float(cloud.burst_time_s) + lifetime),
            ]
        )
    times = np.unique(np.concatenate([regular, np.asarray(events)]))
    margins = joint_sightline_margins(
        times,
        target_points,
        clouds,
        missile_position_vector_fn,
        cloud_center_vector_fn,
        radius=radius,
        lifetime=lifetime,
    )

    def margin_at(value: float) -> float:
        active_centers = [
            cloud_center_scalar_fn(cloud, value)
            for cloud in clouds
            if cloud.burst_time_s <= value <= cloud.burst_time_s + lifetime
        ]
        return joint_sightline_margin(
            missile_position_scalar_fn(value),
            target_points,
            np.asarray(active_centers),
            radius,
        )

    effective = margins <= 0.0
    intervals: list[EffectiveInterval] = []
    current_start: float | None = float(times[0]) if effective[0] else None
    for index in range(len(times) - 1):
        if effective[index] == effective[index + 1]:
            continue
        crossing = _bisect_transition(
            margin_at,
            float(times[index]),
            float(times[index + 1]),
        )
        if not effective[index] and effective[index + 1]:
            current_start = crossing
        elif current_start is not None:
            intervals.append(EffectiveInterval(current_start, crossing))
            current_start = None
    if current_start is not None:
        intervals.append(EffectiveInterval(current_start, float(times[-1])))
    return intervals
