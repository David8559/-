"""Arc-length parameterization of the problem-4 turning path.

The path joins the inward Archimedean spiral to its centrally symmetric
outward spiral by two oppositely curved, externally tangent circular arcs.
The entry point is path coordinate s=0 and the head travels in increasing s.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import asinh, atan2, cos, hypot, pi, sin, sqrt

from geometry import spiral_dxy_dtheta, spiral_xy


TURNING_PITCH = 1.7
TURNING_RADIUS = 4.5
RADIUS_RATIO = 2.0


@dataclass(frozen=True)
class PathPoint:
    """Position and unit tangent at one path arc-length coordinate."""

    s: float
    x: float
    y: float
    tangent_x: float
    tangent_y: float
    segment: str


@dataclass(frozen=True)
class TurningGeometry:
    """Complete geometry of the fixed-endpoint two-arc connection."""

    pitch: float
    boundary_theta: float
    entry_x: float
    entry_y: float
    exit_x: float
    exit_y: float
    tangent_x: float
    tangent_y: float
    normal_x: float
    normal_y: float
    radius_sum: float
    first_radius: float
    second_radius: float
    first_center_x: float
    first_center_y: float
    second_center_x: float
    second_center_y: float
    join_x: float
    join_y: float
    first_start_angle: float
    first_sweep: float
    second_start_angle: float
    second_sweep: float
    first_length: float
    second_length: float
    total_arc_length: float


def _spiral_scale(pitch: float) -> float:
    if pitch <= 0.0:
        raise ValueError("pitch must be positive")
    return pitch / (2.0 * pi)


def _spiral_primitive(theta: float, pitch: float) -> float:
    """Return Archimedean-spiral arc length measured from theta=0."""

    if theta < 0.0:
        raise ValueError("theta must be non-negative")
    b = _spiral_scale(pitch)
    return 0.5 * b * (
        theta * sqrt(1.0 + theta * theta) + asinh(theta)
    )


def _positive_sweep(start: float, end: float, *, clockwise: bool) -> float:
    """Return the positive angular sweep from start to end."""

    if clockwise:
        return (start - end) % (2.0 * pi)
    return (end - start) % (2.0 * pi)


def build_turning_geometry(
    pitch: float = TURNING_PITCH,
    turning_radius: float = TURNING_RADIUS,
    radius_ratio: float = RADIUS_RATIO,
) -> TurningGeometry:
    """Construct the two tangent arcs at the turning-space boundary."""

    if turning_radius <= 0.0:
        raise ValueError("turning_radius must be positive")
    if radius_ratio <= 0.0:
        raise ValueError("radius_ratio must be positive")

    b = _spiral_scale(pitch)
    theta = turning_radius / b
    entry_x, entry_y = spiral_xy(theta, pitch)
    exit_x, exit_y = -entry_x, -entry_y
    derivative_x, derivative_y = spiral_dxy_dtheta(theta, pitch)
    derivative_norm = hypot(derivative_x, derivative_y)

    # Inward motion on the entry spiral and outward motion on the centrally
    # symmetric exit spiral have the same unit tangent at the two endpoints.
    tangent_x = -derivative_x / derivative_norm
    tangent_y = -derivative_y / derivative_norm
    normal_x = -tangent_y
    normal_y = tangent_x

    delta_x = exit_x - entry_x
    delta_y = exit_y - entry_y
    right_normal_projection = (
        delta_x * (-normal_x) + delta_y * (-normal_y)
    )
    if right_normal_projection <= 0.0:
        raise RuntimeError("turning orientation does not admit positive radii")

    # C2-C1 = (B-A) + (R1+R2)n for the chosen right-then-left S turn.
    # External tangency requires |C2-C1|=R1+R2, yielding the fixed sum.
    radius_sum = (
        delta_x * delta_x + delta_y * delta_y
    ) / (2.0 * right_normal_projection)
    second_radius = radius_sum / (radius_ratio + 1.0)
    first_radius = radius_ratio * second_radius

    first_center_x = entry_x - first_radius * normal_x
    first_center_y = entry_y - first_radius * normal_y
    second_center_x = exit_x + second_radius * normal_x
    second_center_y = exit_y + second_radius * normal_y
    center_delta_x = second_center_x - first_center_x
    center_delta_y = second_center_y - first_center_y
    center_distance = hypot(center_delta_x, center_delta_y)
    if abs(center_distance - radius_sum) > 1.0e-11:
        raise RuntimeError("constructed circles are not externally tangent")

    join_x = first_center_x + first_radius * center_delta_x / radius_sum
    join_y = first_center_y + first_radius * center_delta_y / radius_sum

    first_start_angle = atan2(
        entry_y - first_center_y,
        entry_x - first_center_x,
    )
    first_join_angle = atan2(
        join_y - first_center_y,
        join_x - first_center_x,
    )
    second_start_angle = atan2(
        join_y - second_center_y,
        join_x - second_center_x,
    )
    second_end_angle = atan2(
        exit_y - second_center_y,
        exit_x - second_center_x,
    )
    first_sweep = _positive_sweep(
        first_start_angle,
        first_join_angle,
        clockwise=True,
    )
    second_sweep = _positive_sweep(
        second_start_angle,
        second_end_angle,
        clockwise=False,
    )
    if first_sweep > pi or second_sweep > pi:
        raise RuntimeError("constructed path selected a major circular arc")

    first_length = first_radius * first_sweep
    second_length = second_radius * second_sweep
    return TurningGeometry(
        pitch=pitch,
        boundary_theta=theta,
        entry_x=entry_x,
        entry_y=entry_y,
        exit_x=exit_x,
        exit_y=exit_y,
        tangent_x=tangent_x,
        tangent_y=tangent_y,
        normal_x=normal_x,
        normal_y=normal_y,
        radius_sum=radius_sum,
        first_radius=first_radius,
        second_radius=second_radius,
        first_center_x=first_center_x,
        first_center_y=first_center_y,
        second_center_x=second_center_x,
        second_center_y=second_center_y,
        join_x=join_x,
        join_y=join_y,
        first_start_angle=first_start_angle,
        first_sweep=first_sweep,
        second_start_angle=second_start_angle,
        second_sweep=second_sweep,
        first_length=first_length,
        second_length=second_length,
        total_arc_length=first_length + second_length,
    )


def fixed_endpoint_arc_length(
    first_radius_fraction: float,
    geometry: TurningGeometry | None = None,
) -> float:
    """Return the two-arc length for any positive split of the fixed sum.

    With centrally symmetric endpoints and equal endpoint tangents, both arc
    sweeps are fixed.  Therefore redistributing the fixed radius sum cannot
    shorten the connection.
    """

    if not 0.0 < first_radius_fraction < 1.0:
        raise ValueError("first_radius_fraction must lie strictly in (0, 1)")
    geometry = geometry or build_turning_geometry()
    first_radius = first_radius_fraction * geometry.radius_sum
    second_radius = geometry.radius_sum - first_radius
    return (
        first_radius * geometry.first_sweep
        + second_radius * geometry.second_sweep
    )


def _theta_from_spiral_increment(
    arc_increment: float,
    geometry: TurningGeometry,
    *,
    relative_tolerance: float = 1.0e-15,
) -> float:
    """Invert outward spiral arc length measured from the boundary."""

    if arc_increment < 0.0:
        raise ValueError("arc_increment must be non-negative")
    theta_low = geometry.boundary_theta
    target = _spiral_primitive(theta_low, geometry.pitch) + arc_increment
    theta_high = max(theta_low + 1.0, theta_low * 1.1)
    while _spiral_primitive(theta_high, geometry.pitch) < target:
        theta_high *= 1.5

    b = _spiral_scale(geometry.pitch)
    theta = min(
        theta_high,
        max(
            theta_low,
            sqrt(
                geometry.boundary_theta**2
                + 2.0 * arc_increment / b
            ),
        ),
    )
    for _ in range(100):
        value = _spiral_primitive(theta, geometry.pitch)
        if value < target:
            theta_low = theta
        else:
            theta_high = theta
        if theta_high - theta_low <= relative_tolerance * max(1.0, theta):
            return 0.5 * (theta_low + theta_high)

        derivative = b * sqrt(1.0 + theta * theta)
        newton = theta - (value - target) / derivative
        if not theta_low < newton < theta_high:
            newton = 0.5 * (theta_low + theta_high)
        theta = newton
    raise RuntimeError("spiral arc-length inversion did not converge")


def path_point(
    s: float,
    geometry: TurningGeometry | None = None,
) -> PathPoint:
    """Return position and forward unit tangent at path coordinate s."""

    geometry = geometry or build_turning_geometry()
    if s <= 0.0:
        theta = _theta_from_spiral_increment(-s, geometry)
        x, y = spiral_xy(theta, geometry.pitch)
        derivative_x, derivative_y = spiral_dxy_dtheta(
            theta,
            geometry.pitch,
        )
        derivative_norm = hypot(derivative_x, derivative_y)
        return PathPoint(
            s=s,
            x=x,
            y=y,
            tangent_x=-derivative_x / derivative_norm,
            tangent_y=-derivative_y / derivative_norm,
            segment="inward-spiral",
        )

    if s <= geometry.first_length:
        angle = geometry.first_start_angle - s / geometry.first_radius
        return PathPoint(
            s=s,
            x=geometry.first_center_x + geometry.first_radius * cos(angle),
            y=geometry.first_center_y + geometry.first_radius * sin(angle),
            tangent_x=sin(angle),
            tangent_y=-cos(angle),
            segment="first-arc",
        )

    if s <= geometry.total_arc_length:
        local = s - geometry.first_length
        angle = (
            geometry.second_start_angle + local / geometry.second_radius
        )
        return PathPoint(
            s=s,
            x=geometry.second_center_x + geometry.second_radius * cos(angle),
            y=geometry.second_center_y + geometry.second_radius * sin(angle),
            tangent_x=-sin(angle),
            tangent_y=cos(angle),
            segment="second-arc",
        )

    theta = _theta_from_spiral_increment(
        s - geometry.total_arc_length,
        geometry,
    )
    inward_x, inward_y = spiral_xy(theta, geometry.pitch)
    derivative_x, derivative_y = spiral_dxy_dtheta(theta, geometry.pitch)
    derivative_norm = hypot(derivative_x, derivative_y)
    return PathPoint(
        s=s,
        x=-inward_x,
        y=-inward_y,
        tangent_x=-derivative_x / derivative_norm,
        tangent_y=-derivative_y / derivative_norm,
        segment="outward-spiral",
    )
