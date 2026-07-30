"""Problem 1 baseline model for the 2025 CUMCM A problem.

The time origin is the radar detection / task assignment instant. Coordinates
and all distances use metres; time uses seconds.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np


GRAVITY = 9.8
MISSILE_SPEED = 300.0
DRONE_SPEED = 120.0
DROP_TIME = 1.5
FUSE_DELAY = 3.6
BURST_TIME = DROP_TIME + FUSE_DELAY
CLOUD_RADIUS = 10.0
CLOUD_DESCENT_SPEED = 3.0
CLOUD_LIFETIME = 20.0

FALSE_TARGET = np.array([0.0, 0.0, 0.0])
TRUE_TARGET_BOTTOM_CENTER = np.array([0.0, 200.0, 0.0])
TRUE_TARGET_CENTER = np.array([0.0, 200.0, 5.0])
TRUE_TARGET_RADIUS = 7.0
TRUE_TARGET_HEIGHT = 10.0

M1_INITIAL = np.array([20000.0, 0.0, 2000.0])
FY1_INITIAL = np.array([17800.0, 0.0, 1800.0])

MISSILE_DIRECTION = (FALSE_TARGET - M1_INITIAL) / np.linalg.norm(
    FALSE_TARGET - M1_INITIAL
)
MISSILE_VELOCITY = MISSILE_SPEED * MISSILE_DIRECTION
DRONE_VELOCITY = np.array([-DRONE_SPEED, 0.0, 0.0])


@dataclass(frozen=True)
class EffectiveInterval:
    start: float
    end: float

    @property
    def duration(self) -> float:
        return self.end - self.start


def missile_position(t: float | np.ndarray) -> np.ndarray:
    """Return M1 position at absolute time ``t``."""
    t_array = np.asarray(t, dtype=float)
    return M1_INITIAL + np.expand_dims(t_array, axis=-1) * MISSILE_VELOCITY


def drone_position(t: float | np.ndarray) -> np.ndarray:
    """Return FY1 position at absolute time ``t``."""
    t_array = np.asarray(t, dtype=float)
    return FY1_INITIAL + np.expand_dims(t_array, axis=-1) * DRONE_VELOCITY


def bomb_position(t: float | np.ndarray) -> np.ndarray:
    """Return bomb position from release until burst."""
    tau = np.asarray(t, dtype=float) - DROP_TIME
    if np.any(tau < 0):
        raise ValueError("Bomb position is defined only after release.")
    release = drone_position(DROP_TIME)
    gravity_displacement = np.stack(
        [
            np.zeros_like(tau),
            np.zeros_like(tau),
            -0.5 * GRAVITY * tau**2,
        ],
        axis=-1,
    )
    return release + np.expand_dims(tau, axis=-1) * DRONE_VELOCITY + gravity_displacement


DROP_POINT = drone_position(DROP_TIME)
BURST_POINT = bomb_position(BURST_TIME)


def cloud_center(t: float | np.ndarray) -> np.ndarray:
    """Return smoke-cloud centre from burst onward."""
    tau = np.asarray(t, dtype=float) - BURST_TIME
    if np.any(tau < 0):
        raise ValueError("Cloud centre is defined only after burst.")
    displacement = np.stack(
        [
            np.zeros_like(tau),
            np.zeros_like(tau),
            -CLOUD_DESCENT_SPEED * tau,
        ],
        axis=-1,
    )
    return BURST_POINT + displacement


def point_to_segment_distance(
    point: np.ndarray, start: np.ndarray, ends: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Distance from one point to one or many segments ``[start, ends]``.

    Returns the Euclidean distance and the unclipped projection parameter.
    ``lambda=0`` is the missile, ``lambda=1`` is the target point.
    """
    point = np.asarray(point, dtype=float)
    start = np.asarray(start, dtype=float)
    ends = np.asarray(ends, dtype=float)
    vectors = ends - start
    offset = point - start
    denominator = np.sum(vectors * vectors, axis=-1)
    projection = np.sum(vectors * offset, axis=-1) / denominator
    clipped = np.clip(projection, 0.0, 1.0)
    closest = start + np.expand_dims(clipped, axis=-1) * vectors
    distance = np.linalg.norm(point - closest, axis=-1)
    return distance, projection


def cylinder_surface_points(
    n_theta: int = 720, n_z: int = 11, n_r: int = 8
) -> np.ndarray:
    """Deterministically sample the closed surface of the true target.

    The side wall is sampled at ``n_z`` heights. Both circular caps are
    sampled at ``n_r`` radii. This discretisation is used only for the robust
    full-cylinder visibility criterion; convergence is checked separately.
    """
    if n_theta < 8 or n_z < 2 or n_r < 2:
        raise ValueError("Cylinder sampling is too coarse.")

    theta = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    points: list[np.ndarray] = []

    for z in np.linspace(0.0, TRUE_TARGET_HEIGHT, n_z):
        points.append(
            np.column_stack(
                [
                    TRUE_TARGET_RADIUS * cos_theta,
                    200.0 + TRUE_TARGET_RADIUS * sin_theta,
                    np.full_like(theta, z),
                ]
            )
        )

    for z in (0.0, TRUE_TARGET_HEIGHT):
        for radius in np.linspace(0.0, TRUE_TARGET_RADIUS, n_r):
            points.append(
                np.column_stack(
                    [
                        radius * cos_theta,
                        200.0 + radius * sin_theta,
                        np.full_like(theta, z),
                    ]
                )
            )

    return np.vstack(points)


def centerline_distance(t: float) -> float:
    """Cloud-to-segment distance for the target geometric centre."""
    distance, _ = point_to_segment_distance(
        cloud_center(t), missile_position(t), TRUE_TARGET_CENTER
    )
    return float(distance)


def full_cylinder_distance(t: float, target_points: np.ndarray) -> float:
    """Worst cloud-to-line-of-sight distance over the target surface.

    If this maximum is no larger than the cloud radius, every sampled target
    point is screened from M1. Therefore this is the robust, complete-screening
    criterion used for the main result.
    """
    distances, _ = point_to_segment_distance(
        cloud_center(t), missile_position(t), target_points
    )
    return float(np.max(distances))


def _bisect_root(
    function: Callable[[float], float],
    left: float,
    right: float,
    tolerance: float = 1e-10,
    max_iterations: int = 100,
) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0.0:
        raise ValueError("Root is not bracketed.")

    for _ in range(max_iterations):
        middle = 0.5 * (left + right)
        f_middle = function(middle)
        if abs(f_middle) <= tolerance or right - left <= tolerance:
            return middle
        if f_left * f_middle <= 0.0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return 0.5 * (left + right)


def find_effective_intervals(
    distance_function: Callable[[float], float],
    start: float = BURST_TIME,
    end: float = BURST_TIME + CLOUD_LIFETIME,
    scan_step: float = 0.01,
) -> list[EffectiveInterval]:
    """Locate all intervals where distance is at most the cloud radius."""
    count = int(np.ceil((end - start) / scan_step))
    times = np.linspace(start, end, count + 1)
    margins = np.array([distance_function(float(t)) - CLOUD_RADIUS for t in times])
    effective = margins <= 0.0

    intervals: list[EffectiveInterval] = []
    interval_start: float | None = start if effective[0] else None

    for index in range(len(times) - 1):
        if effective[index] == effective[index + 1]:
            continue
        root = _bisect_root(
            lambda value: distance_function(value) - CLOUD_RADIUS,
            float(times[index]),
            float(times[index + 1]),
        )
        if not effective[index] and effective[index + 1]:
            interval_start = root
        elif effective[index] and not effective[index + 1]:
            if interval_start is None:
                raise RuntimeError("Effective interval ended before it started.")
            intervals.append(EffectiveInterval(interval_start, root))
            interval_start = None

    if interval_start is not None:
        intervals.append(EffectiveInterval(interval_start, end))
    return intervals


def total_duration(intervals: Iterable[EffectiveInterval]) -> float:
    return float(sum(interval.duration for interval in intervals))


def missile_arrival_time() -> float:
    return float(np.linalg.norm(M1_INITIAL - FALSE_TARGET) / MISSILE_SPEED)


def missile_cloud_sphere_crossings() -> np.ndarray:
    """Analytic times when M1 crosses the radius-10 cloud sphere.

    The cloud exists only after ``BURST_TIME``. Solving
    ``||M(t)-C(t)||^2=CLOUD_RADIUS^2`` gives the entry and exit times and
    independently validates the numerically located screening end.
    """
    cloud_intercept = BURST_POINT + np.array(
        [0.0, 0.0, CLOUD_DESCENT_SPEED * BURST_TIME]
    )
    relative_intercept = M1_INITIAL - cloud_intercept
    relative_velocity = MISSILE_VELOCITY + np.array(
        [0.0, 0.0, CLOUD_DESCENT_SPEED]
    )
    coefficients = [
        float(np.dot(relative_velocity, relative_velocity)),
        float(2.0 * np.dot(relative_intercept, relative_velocity)),
        float(np.dot(relative_intercept, relative_intercept) - CLOUD_RADIUS**2),
    ]
    roots = np.sort(np.roots(coefficients).real)
    return roots


def representative_projection(t: float) -> float:
    """Unclipped projection parameter for the target-centre sight line."""
    _, projection = point_to_segment_distance(
        cloud_center(t), missile_position(t), TRUE_TARGET_CENTER
    )
    return float(projection)


def basic_results(n_theta: int = 1440) -> dict[str, object]:
    """Compute the two documented Problem 1 criteria."""
    target_points = cylinder_surface_points(n_theta=n_theta)
    robust_function = lambda t: full_cylinder_distance(t, target_points)
    robust_intervals = find_effective_intervals(robust_function)
    center_intervals = find_effective_intervals(centerline_distance)

    return {
        "drop_time_s": DROP_TIME,
        "burst_time_s": BURST_TIME,
        "cloud_expiry_time_s": BURST_TIME + CLOUD_LIFETIME,
        "missile_arrival_time_s": missile_arrival_time(),
        "missile_cloud_sphere_crossings_s": missile_cloud_sphere_crossings().tolist(),
        "drop_point_m": DROP_POINT.tolist(),
        "burst_point_m": BURST_POINT.tolist(),
        "full_cylinder_intervals_s": [
            [interval.start, interval.end] for interval in robust_intervals
        ],
        "full_cylinder_duration_s": total_duration(robust_intervals),
        "centerline_intervals_s": [
            [interval.start, interval.end] for interval in center_intervals
        ],
        "centerline_duration_s": total_duration(center_intervals),
        "cylinder_n_theta": n_theta,
    }
