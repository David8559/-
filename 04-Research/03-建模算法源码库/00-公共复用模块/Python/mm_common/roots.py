"""Bracket-preserving scalar root finding for event and threshold times."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class RootResult:
    root: float
    value: float
    iterations: int
    left: float
    right: float


def _finite_value(function: Callable[[float], float], point: float) -> float:
    value = float(function(point))
    if not isfinite(value):
        raise ValueError(f"function is not finite at x={point!r}")
    return value


def bisect_sign_change(
    function: Callable[[float], float],
    left: float,
    right: float,
    *,
    x_tolerance: float = 1e-10,
    value_tolerance: float = 1e-12,
    max_iterations: int = 200,
) -> RootResult:
    """Find a bracketed root while retaining the final sign-change interval."""
    left, right = float(left), float(right)
    if not isfinite(left) or not isfinite(right) or right < left:
        raise ValueError("a finite ordered bracket is required")
    if x_tolerance <= 0.0 or value_tolerance < 0.0 or max_iterations < 1:
        raise ValueError("invalid bisection tolerances or iteration limit")
    left_value = _finite_value(function, left)
    right_value = _finite_value(function, right)
    if abs(left_value) <= value_tolerance:
        return RootResult(left, left_value, 0, left, left)
    if abs(right_value) <= value_tolerance:
        return RootResult(right, right_value, 0, right, right)
    if left_value * right_value > 0.0:
        raise ValueError("the endpoints do not bracket a sign change")
    midpoint = left
    midpoint_value = left_value
    for iteration in range(1, max_iterations + 1):
        midpoint = 0.5 * (left + right)
        midpoint_value = _finite_value(function, midpoint)
        if abs(midpoint_value) <= value_tolerance or right - left <= x_tolerance:
            return RootResult(midpoint, midpoint_value, iteration, left, right)
        if left_value * midpoint_value <= 0.0:
            right, right_value = midpoint, midpoint_value
        else:
            left, left_value = midpoint, midpoint_value
    raise RuntimeError("bisection did not converge within max_iterations")
