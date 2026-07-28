"""Path geometry for the 2024 CUMCM problem A bench-dragon model.

This module currently implements only the front handle of the dragon head on
an inward Archimedean spiral.  Later stages will add the rigid-chain solver.

Units:
    length: metre
    time: second
    angle: radian
"""

from __future__ import annotations

from dataclasses import dataclass
from math import asinh, cos, hypot, pi, sin, sqrt


DEFAULT_PITCH = 0.55
DEFAULT_THETA_INITIAL = 32.0 * pi
DEFAULT_HEAD_SPEED = 1.0


@dataclass(frozen=True)
class HeadState:
    """Kinematic state of the dragon-head front handle."""

    time: float
    theta: float
    theta_rate: float
    x: float
    y: float
    vx: float
    vy: float
    speed: float


def spiral_scale(pitch: float) -> float:
    """Return b in the Archimedean spiral r = b * theta."""

    if pitch <= 0.0:
        raise ValueError("pitch must be positive")
    return pitch / (2.0 * pi)


def spiral_xy(theta: float, pitch: float = DEFAULT_PITCH) -> tuple[float, float]:
    """Convert a spiral parameter to Cartesian coordinates."""

    if theta < 0.0:
        raise ValueError("theta must be non-negative for the selected branch")
    b = spiral_scale(pitch)
    radius = b * theta
    return radius * cos(theta), radius * sin(theta)


def spiral_dxy_dtheta(
    theta: float,
    pitch: float = DEFAULT_PITCH,
) -> tuple[float, float]:
    """Return the derivative of spiral Cartesian coordinates by theta."""

    if theta < 0.0:
        raise ValueError("theta must be non-negative for the selected branch")
    b = spiral_scale(pitch)
    return (
        b * (cos(theta) - theta * sin(theta)),
        b * (sin(theta) + theta * cos(theta)),
    )


def spiral_arc_primitive(
    theta: float,
    pitch: float = DEFAULT_PITCH,
) -> float:
    """Return F(theta), where F'(theta) = b * sqrt(1 + theta**2).

    The travelled arc length from theta_a down to theta_b is
    F(theta_a) - F(theta_b), provided theta_a >= theta_b >= 0.
    """

    if theta < 0.0:
        raise ValueError("theta must be non-negative for the selected branch")
    b = spiral_scale(pitch)
    return 0.5 * b * (theta * sqrt(1.0 + theta * theta) + asinh(theta))


def _invert_arc_primitive(
    target: float,
    upper_theta: float,
    pitch: float,
    *,
    theta_tolerance: float = 1.0e-15,
    max_iterations: int = 200,
) -> float:
    """Invert the strictly increasing primitive by deterministic bisection."""

    if target < 0.0:
        raise ValueError("target arc primitive must be non-negative")
    upper_value = spiral_arc_primitive(upper_theta, pitch)
    if target > upper_value:
        raise ValueError("target exceeds the supplied upper bound")
    if target == 0.0:
        return 0.0
    if target == upper_value:
        return upper_theta

    low = 0.0
    high = upper_theta
    for _ in range(max_iterations):
        middle = 0.5 * (low + high)
        middle_value = spiral_arc_primitive(middle, pitch)
        if middle_value < target:
            low = middle
        else:
            high = middle
        if high - low <= theta_tolerance * max(1.0, abs(middle)):
            return 0.5 * (low + high)

    raise RuntimeError("arc-length inversion did not converge")


def head_theta(
    time: float,
    *,
    pitch: float = DEFAULT_PITCH,
    theta_initial: float = DEFAULT_THETA_INITIAL,
    head_speed: float = DEFAULT_HEAD_SPEED,
) -> float:
    """Solve the spiral parameter of the inward-moving head front handle."""

    if time < 0.0:
        raise ValueError("time must be non-negative in problem 1")
    if theta_initial <= 0.0:
        raise ValueError("theta_initial must be positive")
    if head_speed <= 0.0:
        raise ValueError("head_speed must be positive")

    initial_primitive = spiral_arc_primitive(theta_initial, pitch)
    target = initial_primitive - head_speed * time
    if target < 0.0:
        maximum_time = initial_primitive / head_speed
        raise ValueError(
            f"time exceeds the arrival time at the spiral origin "
            f"({maximum_time:.12f} s)"
        )
    return _invert_arc_primitive(target, theta_initial, pitch)


def head_state(
    time: float,
    *,
    pitch: float = DEFAULT_PITCH,
    theta_initial: float = DEFAULT_THETA_INITIAL,
    head_speed: float = DEFAULT_HEAD_SPEED,
) -> HeadState:
    """Return position and velocity of the head front handle."""

    theta = head_theta(
        time,
        pitch=pitch,
        theta_initial=theta_initial,
        head_speed=head_speed,
    )
    b = spiral_scale(pitch)
    x, y = spiral_xy(theta, pitch)

    # Inward clockwise motion uses decreasing theta.
    dtheta_dt = -head_speed / (b * sqrt(1.0 + theta * theta))
    dx_dtheta, dy_dtheta = spiral_dxy_dtheta(theta, pitch)
    vx = dx_dtheta * dtheta_dt
    vy = dy_dtheta * dtheta_dt

    return HeadState(
        time=time,
        theta=theta,
        theta_rate=dtheta_dt,
        x=x,
        y=y,
        vx=vx,
        vy=vy,
        speed=hypot(vx, vy),
    )
