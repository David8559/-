"""Pitch-feasibility model for problem 3.

The head travels inward from the point on the 16th turn to the circular
turning-space boundary.  For each pitch, feasibility is the minimum signed
SAT separation over that entire path, not merely at the boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt
from typing import Callable

from chain import problem1_handle_distances, solve_handle_positions
from collision import (
    CollisionClearance,
    bench_rectangles,
    minimum_nonadjacent_clearance,
    rectangle_separation_margin,
)


TURNING_RADIUS = 4.5
INITIAL_THETA = 32.0 * pi


@dataclass(frozen=True)
class PathMinimum:
    """Minimum separation for one bench pair along an inward path."""

    pitch: float
    theta: float
    head_radius: float
    margin: float
    first_index: int
    second_index: int


def boundary_theta(pitch: float) -> float:
    """Return the spiral parameter where the head reaches radius 4.5 m."""

    if pitch <= 0.0:
        raise ValueError("pitch must be positive")
    theta = 2.0 * pi * TURNING_RADIUS / pitch
    if theta > INITIAL_THETA:
        raise ValueError(
            "the 16th-turn starting point is already inside the turning space"
        )
    return theta


def head_radius(theta: float, pitch: float) -> float:
    """Return the radial distance of a spiral point."""

    return pitch * theta / (2.0 * pi)


def rectangles_at(theta: float, pitch: float):
    """Return all physical bench rectangles at one head parameter."""

    points = solve_handle_positions(
        theta,
        problem1_handle_distances(),
        pitch,
    )
    return bench_rectangles(points)


def pair_margin(
    theta: float,
    pitch: float,
    first_index: int,
    second_index: int,
) -> float:
    """Return the signed SAT margin of one non-adjacent bench pair."""

    if second_index < first_index + 2:
        raise ValueError("bench pair must be non-adjacent")
    rectangles = rectangles_at(theta, pitch)
    if second_index >= len(rectangles):
        raise IndexError("bench index is outside the physical chain")
    return rectangle_separation_margin(
        rectangles[first_index],
        rectangles[second_index],
    )


def global_clearance(theta: float, pitch: float) -> CollisionClearance:
    """Return the minimum signed separation over all non-adjacent benches."""

    return minimum_nonadjacent_clearance(rectangles_at(theta, pitch))


def _golden_section_minimum(
    function: Callable[[float], float],
    low: float,
    high: float,
    *,
    relative_tolerance: float = 1.0e-12,
    max_iterations: int = 200,
) -> tuple[float, float]:
    """Minimize a locally unimodal scalar function on a closed bracket."""

    if not low < high:
        raise ValueError("golden-section bracket must have positive width")
    golden = (sqrt(5.0) - 1.0) / 2.0
    left = high - golden * (high - low)
    right = low + golden * (high - low)
    left_value = function(left)
    right_value = function(right)

    for _ in range(max_iterations):
        midpoint = 0.5 * (low + high)
        if high - low <= relative_tolerance * max(1.0, abs(midpoint)):
            theta = midpoint
            return theta, function(theta)
        if left_value < right_value:
            high = right
            right = left
            right_value = left_value
            left = high - golden * (high - low)
            left_value = function(left)
        else:
            low = left
            left = right
            left_value = right_value
            right = low + golden * (high - low)
            right_value = function(right)

    raise RuntimeError("golden-section minimization did not converge")


def minimum_pair_clearance_over_path(
    pitch: float,
    first_index: int,
    second_index: int,
    *,
    coarse_intervals: int = 160,
    relative_tolerance: float = 1.0e-12,
) -> PathMinimum:
    """Find one pair's minimum margin from the 16th turn to the boundary."""

    if coarse_intervals < 4:
        raise ValueError("coarse_intervals must be at least four")
    theta_boundary = boundary_theta(pitch)
    theta_values = [
        theta_boundary
        + (INITIAL_THETA - theta_boundary) * index / coarse_intervals
        for index in range(coarse_intervals + 1)
    ]
    margins = [
        pair_margin(theta, pitch, first_index, second_index)
        for theta in theta_values
    ]
    minimum_index = min(range(len(margins)), key=margins.__getitem__)

    if minimum_index == 0 or minimum_index == coarse_intervals:
        theta = theta_values[minimum_index]
        margin = margins[minimum_index]
    else:
        low = theta_values[minimum_index - 1]
        high = theta_values[minimum_index + 1]
        theta, margin = _golden_section_minimum(
            lambda value: pair_margin(
                value,
                pitch,
                first_index,
                second_index,
            ),
            low,
            high,
            relative_tolerance=relative_tolerance,
        )

    return PathMinimum(
        pitch=pitch,
        theta=theta,
        head_radius=head_radius(theta, pitch),
        margin=margin,
        first_index=first_index,
        second_index=second_index,
    )


def critical_pitch_for_pair(
    first_index: int,
    second_index: int,
    *,
    low_pitch: float,
    high_pitch: float,
    pitch_tolerance: float = 1.0e-12,
) -> tuple[float, PathMinimum, PathMinimum]:
    """Bisect the pitch whose path-minimum margin is zero for one pair."""

    low_result = minimum_pair_clearance_over_path(
        low_pitch,
        first_index,
        second_index,
    )
    high_result = minimum_pair_clearance_over_path(
        high_pitch,
        first_index,
        second_index,
    )
    if low_result.margin >= 0.0:
        raise ValueError("low_pitch must be infeasible")
    if high_result.margin <= 0.0:
        raise ValueError("high_pitch must be feasible")

    while high_pitch - low_pitch > pitch_tolerance:
        middle_pitch = 0.5 * (low_pitch + high_pitch)
        middle_result = minimum_pair_clearance_over_path(
            middle_pitch,
            first_index,
            second_index,
        )
        if middle_result.margin < 0.0:
            low_pitch = middle_pitch
            low_result = middle_result
        else:
            high_pitch = middle_pitch
            high_result = middle_result

    return 0.5 * (low_pitch + high_pitch), low_result, high_result


def sampled_global_path_minimum(
    pitch: float,
    *,
    intervals: int = 240,
) -> PathMinimum:
    """Independently scan every bench pair on a uniform path grid."""

    if intervals < 1:
        raise ValueError("intervals must be positive")
    theta_boundary = boundary_theta(pitch)
    best: PathMinimum | None = None
    for index in range(intervals + 1):
        theta = (
            theta_boundary
            + (INITIAL_THETA - theta_boundary) * index / intervals
        )
        clearance = global_clearance(theta, pitch)
        candidate = PathMinimum(
            pitch=pitch,
            theta=theta,
            head_radius=head_radius(theta, pitch),
            margin=clearance.margin,
            first_index=clearance.first_index,
            second_index=clearance.second_index,
        )
        if best is None or candidate.margin < best.margin:
            best = candidate
    if best is None:
        raise RuntimeError("global path scan produced no state")
    return best
