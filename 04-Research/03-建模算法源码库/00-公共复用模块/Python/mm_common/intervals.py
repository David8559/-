"""Closed-interval operations for schedules, coverage, and event windows."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from math import isfinite

Interval = tuple[float, float]


def _checked_interval(interval: Sequence[float]) -> Interval:
    if len(interval) != 2:
        raise ValueError("an interval must contain exactly two endpoints")
    start, end = float(interval[0]), float(interval[1])
    if not isfinite(start) or not isfinite(end):
        raise ValueError("interval endpoints must be finite")
    if end < start:
        raise ValueError("interval end must not precede its start")
    return start, end


def merge_intervals(
    intervals: Iterable[Sequence[float]], *, tolerance: float = 1e-9
) -> list[Interval]:
    """Return a sorted, disjoint union of closed intervals."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    ordered = sorted((_checked_interval(item) for item in intervals))
    if not ordered:
        return []
    merged = [ordered[0]]
    for start, end in ordered[1:]:
        previous_start, previous_end = merged[-1]
        if start <= previous_end + tolerance:
            merged[-1] = previous_start, max(previous_end, end)
        else:
            merged.append((start, end))
    return merged


def interval_measure(
    intervals: Iterable[Sequence[float]], *, tolerance: float = 1e-9
) -> float:
    """Measure the union, so overlaps are never counted twice."""
    return float(
        sum(end - start for start, end in merge_intervals(intervals, tolerance=tolerance))
    )


def intersection_of_unions(
    unions: Sequence[Iterable[Sequence[float]]], *, tolerance: float = 1e-9
) -> list[Interval]:
    """Intersect several interval unions using a deterministic two-pointer sweep."""
    if not unions:
        return []
    result = merge_intervals(unions[0], tolerance=tolerance)
    for union in unions[1:]:
        other = merge_intervals(union, tolerance=tolerance)
        intersection: list[Interval] = []
        left_index = right_index = 0
        while left_index < len(result) and right_index < len(other):
            left = result[left_index]
            right = other[right_index]
            start = max(left[0], right[0])
            end = min(left[1], right[1])
            if start <= end + tolerance:
                intersection.append((start, max(start, end)))
            if left[1] < right[1]:
                left_index += 1
            else:
                right_index += 1
        result = merge_intervals(intersection, tolerance=tolerance)
        if not result:
            break
    return result


def deletion_marginals(
    interval_groups: Sequence[Iterable[Sequence[float]]], *, tolerance: float = 1e-9
) -> list[float]:
    """Return union loss after deleting each component group and fully recomputing."""
    normalized = [merge_intervals(group, tolerance=tolerance) for group in interval_groups]
    full_measure = interval_measure(
        (interval for group in normalized for interval in group), tolerance=tolerance
    )
    marginals: list[float] = []
    for omitted in range(len(normalized)):
        reduced = interval_measure(
            (
                interval
                for index, group in enumerate(normalized)
                if index != omitted
                for interval in group
            ),
            tolerance=tolerance,
        )
        marginals.append(max(0.0, full_measure - reduced))
    return marginals
