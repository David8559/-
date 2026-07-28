"""Oriented-rectangle collision geometry for the physical benches."""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot
from typing import Iterable, Sequence

from chain import HandlePoint, HandleState


HEAD_BENCH_LENGTH = 3.41
BODY_BENCH_LENGTH = 2.20
BENCH_WIDTH = 0.30


@dataclass(frozen=True)
class BenchRectangle:
    """One physical bench represented by an oriented rectangle."""

    index: int
    center_x: float
    center_y: float
    axis_x: float
    axis_y: float
    normal_x: float
    normal_y: float
    half_length: float
    half_width: float


@dataclass(frozen=True)
class CollisionClearance:
    """Minimum signed separation among checked non-adjacent benches."""

    margin: float
    first_index: int
    second_index: int

    @property
    def is_collision(self) -> bool:
        """Return True at contact or overlap."""

        return self.margin <= 0.0


def bench_rectangles(
    states: Iterable[HandlePoint | HandleState],
) -> list[BenchRectangle]:
    """Build physical bench rectangles from handle positions or states."""

    state_list = list(states)
    if len(state_list) < 2:
        raise ValueError("at least two handle states are required")

    rectangles: list[BenchRectangle] = []
    for index, (front, rear) in enumerate(
        zip(state_list, state_list[1:])
    ):
        delta_x = rear.x - front.x
        delta_y = rear.y - front.y
        handle_distance = hypot(delta_x, delta_y)
        if handle_distance <= 0.0:
            raise ValueError(f"zero handle distance at bench {index}")

        axis_x = delta_x / handle_distance
        axis_y = delta_y / handle_distance
        bench_length = (
            HEAD_BENCH_LENGTH if index == 0 else BODY_BENCH_LENGTH
        )
        expected_handle_distance = bench_length - 0.55
        if abs(handle_distance - expected_handle_distance) > 1.0e-10:
            raise ValueError(
                f"bench {index} handle distance {handle_distance:.12f} m "
                f"does not match physical length {bench_length:.2f} m"
            )

        rectangles.append(
            BenchRectangle(
                index=index,
                center_x=0.5 * (front.x + rear.x),
                center_y=0.5 * (front.y + rear.y),
                axis_x=axis_x,
                axis_y=axis_y,
                normal_x=-axis_y,
                normal_y=axis_x,
                half_length=0.5 * bench_length,
                half_width=0.5 * BENCH_WIDTH,
            )
        )

    return rectangles


def _projection_radius(
    rectangle: BenchRectangle,
    axis_x: float,
    axis_y: float,
) -> float:
    """Return the rectangle projection radius on a unit axis."""

    return (
        rectangle.half_length
        * abs(rectangle.axis_x * axis_x + rectangle.axis_y * axis_y)
        + rectangle.half_width
        * abs(rectangle.normal_x * axis_x + rectangle.normal_y * axis_y)
    )


def rectangle_separation_margin(
    first: BenchRectangle,
    second: BenchRectangle,
) -> float:
    """Return the SAT signed margin between two rectangles.

    A positive value means the rectangles are separated.  Zero means first
    contact.  A negative value means their interiors overlap.  The value is
    the largest axis gap over the four separating-axis candidates.
    """

    center_delta_x = second.center_x - first.center_x
    center_delta_y = second.center_y - first.center_y
    largest_gap = float("-inf")

    axes = (
        (first.axis_x, first.axis_y),
        (first.normal_x, first.normal_y),
        (second.axis_x, second.axis_y),
        (second.normal_x, second.normal_y),
    )
    for axis_x, axis_y in axes:
        center_projection = abs(
            center_delta_x * axis_x + center_delta_y * axis_y
        )
        gap = (
            center_projection
            - _projection_radius(first, axis_x, axis_y)
            - _projection_radius(second, axis_x, axis_y)
        )
        largest_gap = max(largest_gap, gap)

    return largest_gap


def minimum_nonadjacent_clearance(
    rectangles: Sequence[BenchRectangle],
) -> CollisionClearance:
    """Return the minimum SAT margin over all non-adjacent bench pairs."""

    if len(rectangles) < 3:
        raise ValueError("at least three benches are required")

    best_margin = float("inf")
    best_pair = (-1, -1)
    for first_index, first in enumerate(rectangles):
        # Adjacent benches share a handle and are excluded by construction.
        for second in rectangles[first_index + 2 :]:
            margin = rectangle_separation_margin(first, second)
            if margin < best_margin:
                best_margin = margin
                best_pair = (first.index, second.index)

    if best_pair == (-1, -1):
        raise RuntimeError("no non-adjacent bench pair was checked")
    return CollisionClearance(
        margin=best_margin,
        first_index=best_pair[0],
        second_index=best_pair[1],
    )


def rectangle_corners(
    rectangle: BenchRectangle,
) -> tuple[tuple[float, float], ...]:
    """Return the four corners in counter-clockwise order."""

    along_x = rectangle.half_length * rectangle.axis_x
    along_y = rectangle.half_length * rectangle.axis_y
    across_x = rectangle.half_width * rectangle.normal_x
    across_y = rectangle.half_width * rectangle.normal_y
    return (
        (
            rectangle.center_x + along_x + across_x,
            rectangle.center_y + along_y + across_y,
        ),
        (
            rectangle.center_x - along_x + across_x,
            rectangle.center_y - along_y + across_y,
        ),
        (
            rectangle.center_x - along_x - across_x,
            rectangle.center_y - along_y - across_y,
        ),
        (
            rectangle.center_x + along_x - across_x,
            rectangle.center_y + along_y - across_y,
        ),
    )


def first_nonadjacent_collision(
    rectangles: Sequence[BenchRectangle],
) -> tuple[int, int] | None:
    """Return the first colliding non-adjacent pair, using AABB pruning."""

    half_extents = [
        (
            rectangle.half_length * abs(rectangle.axis_x)
            + rectangle.half_width * abs(rectangle.normal_x),
            rectangle.half_length * abs(rectangle.axis_y)
            + rectangle.half_width * abs(rectangle.normal_y),
        )
        for rectangle in rectangles
    ]

    for first_index, first in enumerate(rectangles):
        first_half_x, first_half_y = half_extents[first_index]
        for second_index in range(first_index + 2, len(rectangles)):
            second = rectangles[second_index]
            second_half_x, second_half_y = half_extents[second_index]
            if abs(second.center_x - first.center_x) > (
                first_half_x + second_half_x
            ):
                continue
            if abs(second.center_y - first.center_y) > (
                first_half_y + second_half_y
            ):
                continue
            if rectangle_separation_margin(first, second) <= 0.0:
                return first.index, second.index
    return None
