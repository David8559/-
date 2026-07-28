"""Rigid-handle chain constrained to a general arc-length path."""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot, isfinite
from typing import Iterable

from turning_path import PathPoint, TurningGeometry, path_point


@dataclass(frozen=True)
class PathHandleState:
    """Position and velocity of one handle on the piecewise turning path."""

    index: int
    s: float
    x: float
    y: float
    vx: float
    vy: float
    speed: float
    segment: str


def previous_handle_s(
    s_front: float,
    distance: float,
    geometry: TurningGeometry,
    *,
    s_tolerance: float = 1.0e-14,
    max_scan_distance: float = 20.0,
    max_iterations: int = 200,
) -> float:
    """Return the nearest lower path coordinate at a fixed chord distance."""

    if distance <= 0.0:
        raise ValueError("distance must be positive")
    front = path_point(s_front, geometry)
    target_squared = distance * distance

    def residual(delta: float) -> float:
        rear = path_point(s_front - delta, geometry)
        delta_x = rear.x - front.x
        delta_y = rear.y - front.y
        return (
            delta_x * delta_x
            + delta_y * delta_y
            - target_squared
        )

    # A chord cannot exceed its corresponding arc length, so the first root
    # cannot occur before delta=distance.  Scan in small increments to retain
    # the nearest root even on the higher-curvature second circular arc.
    low_delta = distance
    low_value = residual(low_delta)
    if low_value > 1.0e-12:
        raise RuntimeError("arc-length lower bound was violated")
    residual_tolerance = 1.0e-14 * max(1.0, target_squared)
    if abs(low_value) <= residual_tolerance:
        return s_front - low_delta

    high_delta = low_delta
    scan_step = min(0.05, distance / 20.0)
    while high_delta - distance <= max_scan_distance:
        high_delta += scan_step
        high_value = residual(high_delta)
        if high_value >= 0.0:
            break
        low_delta = high_delta
        low_value = high_value
    else:
        raise RuntimeError("failed to bracket the nearest path-chord root")

    # Once the nearest sign-changing interval has been isolated, bisection is
    # deliberately used instead of an endpoint-seeking Newton/secant step.
    # The residual becomes extremely flat on the outer spiral, where those
    # faster steps can stagnate without shrinking the bracket.  Bisection
    # preserves the nearest-root guarantee and has a deterministic error
    # bound for every handle and every requested output time.
    for _ in range(max_iterations):
        candidate = 0.5 * (low_delta + high_delta)
        candidate_value = residual(candidate)
        if abs(candidate_value) <= residual_tolerance:
            return s_front - candidate
        if candidate_value < 0.0:
            low_delta = candidate
        else:
            high_delta = candidate
        if high_delta - low_delta <= s_tolerance * max(1.0, candidate):
            return s_front - 0.5 * (low_delta + high_delta)

    raise RuntimeError("path-chord bisection solve did not converge")


def solve_path_handle_states(
    head_s: float,
    handle_distances: Iterable[float],
    geometry: TurningGeometry,
    *,
    head_speed: float = 1.0,
) -> list[PathHandleState]:
    """Solve a rigid chain's positions and analytical velocities."""

    if not isfinite(head_s):
        raise ValueError("head_s must be finite")
    if not isfinite(head_speed) or head_speed <= 0.0:
        raise ValueError("head_speed must be finite and positive")

    head = path_point(head_s, geometry)
    states = [
        PathHandleState(
            index=0,
            s=head_s,
            x=head.x,
            y=head.y,
            vx=head_speed * head.tangent_x,
            vy=head_speed * head.tangent_y,
            speed=head_speed,
            segment=head.segment,
        )
    ]

    for index, distance in enumerate(handle_distances, start=1):
        front = states[-1]
        rear_s = previous_handle_s(front.s, distance, geometry)
        rear: PathPoint = path_point(rear_s, geometry)
        delta_x = rear.x - front.x
        delta_y = rear.y - front.y
        numerator = delta_x * front.vx + delta_y * front.vy
        denominator = (
            delta_x * rear.tangent_x + delta_y * rear.tangent_y
        )
        scale = max(1.0, hypot(delta_x, delta_y))
        if abs(denominator) <= 1.0e-13 * scale:
            raise RuntimeError(
                f"path velocity recursion is singular at handle {index}"
            )

        s_rate = numerator / denominator
        vx = rear.tangent_x * s_rate
        vy = rear.tangent_y * s_rate
        states.append(
            PathHandleState(
                index=index,
                s=rear_s,
                x=rear.x,
                y=rear.y,
                vx=vx,
                vy=vy,
                speed=hypot(vx, vy),
                segment=rear.segment,
            )
        )

    return states
