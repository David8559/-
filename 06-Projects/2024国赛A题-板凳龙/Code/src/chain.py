"""Rigid handle-chain geometry on the inward Archimedean spiral.

Each bench fixes the Euclidean distance (the chord) between two consecutive
handle centres.  It does not fix the spiral arc length between them.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, hypot, pi, sqrt
from typing import Iterable

from geometry import (
    DEFAULT_PITCH,
    HeadState,
    spiral_dxy_dtheta,
    spiral_scale,
    spiral_xy,
)


HEAD_HANDLE_DISTANCE = 2.86
BODY_HANDLE_DISTANCE = 1.65
PROBLEM1_BENCH_COUNT = 223
PROBLEM1_HANDLE_COUNT = PROBLEM1_BENCH_COUNT + 1


@dataclass(frozen=True)
class HandlePoint:
    """Position of one handle centre on the spiral."""

    index: int
    theta: float
    x: float
    y: float


@dataclass(frozen=True)
class HandleState:
    """Position and velocity of one handle centre on the spiral."""

    index: int
    theta: float
    theta_rate: float
    x: float
    y: float
    vx: float
    vy: float
    speed: float


def chord_distance_squared(
    theta_a: float,
    theta_b: float,
    pitch: float = DEFAULT_PITCH,
) -> float:
    """Return the squared straight-line distance between two spiral points."""

    if theta_a < 0.0 or theta_b < 0.0:
        raise ValueError("spiral parameters must be non-negative")
    b = spiral_scale(pitch)
    return b * b * (
        theta_a * theta_a
        + theta_b * theta_b
        - 2.0 * theta_a * theta_b * cos(theta_b - theta_a)
    )


def _bisect_first_chord_root(
    theta_previous: float,
    distance: float,
    pitch: float,
    *,
    theta_tolerance: float,
    max_iterations: int,
) -> float:
    """Find the nearest outward parameter satisfying the chord constraint."""

    if theta_previous < 0.0:
        raise ValueError("theta_previous must be non-negative")
    if distance <= 0.0:
        raise ValueError("distance must be positive")

    b = spiral_scale(pitch)
    target_squared = distance * distance

    def residual(theta_next: float) -> float:
        return (
            chord_distance_squared(theta_previous, theta_next, pitch)
            - target_squared
        )

    # Local arc-length approximation supplies a scale for the first bracket.
    delta_estimate = distance / (b * sqrt(1.0 + theta_previous**2))
    upper_delta = max(delta_estimate, 1.0e-8)
    upper_residual = residual(theta_previous + upper_delta)

    # The required point is the nearest root outside the previous point.
    # In the problem-1 domain it occurs well before a half turn.  The pi bound
    # guards against silently jumping to a different spiral turn.
    while upper_residual < 0.0 and upper_delta < pi:
        upper_delta *= 1.25
        upper_residual = residual(theta_previous + upper_delta)

    if upper_residual < 0.0 or upper_delta >= pi:
        raise RuntimeError(
            "failed to bracket the nearest chord root before a half turn"
        )

    low = theta_previous
    high = theta_previous + upper_delta
    for _ in range(max_iterations):
        middle = 0.5 * (low + high)
        if residual(middle) < 0.0:
            low = middle
        else:
            high = middle
        if high - low <= theta_tolerance * max(1.0, abs(middle)):
            return 0.5 * (low + high)

    raise RuntimeError("chord-root bisection did not converge")


def next_handle_theta(
    theta_previous: float,
    distance: float,
    pitch: float = DEFAULT_PITCH,
    *,
    theta_tolerance: float = 1.0e-15,
    max_iterations: int = 200,
) -> float:
    """Return the nearest outward spiral parameter at the required chord."""

    return _bisect_first_chord_root(
        theta_previous,
        distance,
        pitch,
        theta_tolerance=theta_tolerance,
        max_iterations=max_iterations,
    )


def solve_handle_positions(
    theta_head: float,
    handle_distances: Iterable[float],
    pitch: float = DEFAULT_PITCH,
) -> list[HandlePoint]:
    """Solve a finite rigid handle chain from head to tail."""

    x_head, y_head = spiral_xy(theta_head, pitch)
    points = [HandlePoint(index=0, theta=theta_head, x=x_head, y=y_head)]

    theta_previous = theta_head
    for index, distance in enumerate(handle_distances, start=1):
        theta_next = next_handle_theta(theta_previous, distance, pitch)
        x_next, y_next = spiral_xy(theta_next, pitch)
        points.append(
            HandlePoint(
                index=index,
                theta=theta_next,
                x=x_next,
                y=y_next,
            )
        )
        theta_previous = theta_next

    return points


def solve_handle_states(
    head: HeadState,
    handle_distances: Iterable[float],
    pitch: float = DEFAULT_PITCH,
) -> list[HandleState]:
    """Solve positions and analytical velocities from head to tail.

    For consecutive points q_(i-1) and q_i, differentiating the fixed-chord
    constraint gives

        (q_i - q_(i-1)) dot (v_i - v_(i-1)) = 0.

    Since v_i = q_i'(theta_i) * theta_rate_i, the equation is linear in the
    unknown theta_rate_i and can be propagated along the rigid chain.
    """

    points = solve_handle_positions(head.theta, handle_distances, pitch)
    states = [
        HandleState(
            index=0,
            theta=head.theta,
            theta_rate=head.theta_rate,
            x=head.x,
            y=head.y,
            vx=head.vx,
            vy=head.vy,
            speed=head.speed,
        )
    ]

    for point in points[1:]:
        previous = states[-1]
        delta_x = point.x - previous.x
        delta_y = point.y - previous.y
        dx_dtheta, dy_dtheta = spiral_dxy_dtheta(point.theta, pitch)

        numerator = delta_x * previous.vx + delta_y * previous.vy
        denominator = delta_x * dx_dtheta + delta_y * dy_dtheta
        scale = max(
            1.0,
            hypot(delta_x, delta_y) * hypot(dx_dtheta, dy_dtheta),
        )
        if abs(denominator) <= 1.0e-14 * scale:
            raise RuntimeError(
                f"velocity recursion is singular at handle {point.index}"
            )

        theta_rate = numerator / denominator
        vx = dx_dtheta * theta_rate
        vy = dy_dtheta * theta_rate
        states.append(
            HandleState(
                index=point.index,
                theta=point.theta,
                theta_rate=theta_rate,
                x=point.x,
                y=point.y,
                vx=vx,
                vy=vy,
                speed=hypot(vx, vy),
            )
        )

    return states


def first_bench_distances(bench_count: int) -> list[float]:
    """Return handle distances for the head and following body benches."""

    if bench_count < 1:
        raise ValueError("bench_count must be at least one")
    return [HEAD_HANDLE_DISTANCE] + [BODY_HANDLE_DISTANCE] * (bench_count - 1)


def problem1_handle_distances() -> list[float]:
    """Return all 223 fixed distances for the 224 problem-1 handles."""

    return first_bench_distances(PROBLEM1_BENCH_COUNT)
