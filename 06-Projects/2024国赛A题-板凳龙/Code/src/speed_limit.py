"""Continuous speed-ratio optimization on the problem-4 turning path."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from path_chain import PathHandleState, solve_path_handle_states
from turning_path import TurningGeometry


@dataclass(frozen=True)
class SpeedEvaluation:
    """Maximum unit-head-speed response at one head path coordinate."""

    head_s: float
    maximum_ratio: float
    handle_index: int
    handle_s: float
    handle_segment: str


@dataclass(frozen=True)
class ScalarMaximum:
    """Deterministic one-dimensional maximum result."""

    x: float
    value: float
    iterations: int
    bracket_width: float


def evaluate_speed_ratio(
    head_s: float,
    handle_distances: Iterable[float],
    geometry: TurningGeometry,
) -> SpeedEvaluation:
    """Return the largest handle speed for unit head speed."""

    states = solve_path_handle_states(
        head_s,
        handle_distances,
        geometry,
        head_speed=1.0,
    )
    active = max(states, key=lambda state: (state.speed, -state.index))
    return SpeedEvaluation(
        head_s=head_s,
        maximum_ratio=active.speed,
        handle_index=active.index,
        handle_s=active.s,
        handle_segment=active.segment,
    )


def handle_speed_ratio(
    head_s: float,
    handle_index: int,
    handle_distances: Iterable[float],
    geometry: TurningGeometry,
) -> float:
    """Return one handle's speed ratio for unit head speed."""

    states = solve_path_handle_states(
        head_s,
        handle_distances,
        geometry,
        head_speed=1.0,
    )
    if not 0 <= handle_index < len(states):
        raise IndexError("handle index is outside the solved chain")
    return states[handle_index].speed


def golden_section_maximum(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    *,
    x_tolerance: float = 1.0e-10,
    max_iterations: int = 200,
) -> ScalarMaximum:
    """Maximize a locally unimodal scalar function on a closed interval."""

    if not lower < upper:
        raise ValueError("lower must be strictly less than upper")
    if x_tolerance <= 0.0:
        raise ValueError("x_tolerance must be positive")

    inverse_phi = (5.0**0.5 - 1.0) / 2.0
    left = lower
    right = upper
    c = right - inverse_phi * (right - left)
    d = left + inverse_phi * (right - left)
    fc = function(c)
    fd = function(d)

    iterations = 0
    while (
        right - left > x_tolerance * max(1.0, abs(c), abs(d))
        and iterations < max_iterations
    ):
        if fc < fd:
            left = c
            c = d
            fc = fd
            d = left + inverse_phi * (right - left)
            fd = function(d)
        else:
            right = d
            d = c
            fd = fc
            c = right - inverse_phi * (right - left)
            fc = function(c)
        iterations += 1

    candidates = (
        (left, function(left)),
        (c, fc),
        (d, fd),
        (right, function(right)),
        (
            0.5 * (left + right),
            function(0.5 * (left + right)),
        ),
    )
    best_x, best_value = max(candidates, key=lambda pair: pair[1])
    return ScalarMaximum(
        x=best_x,
        value=best_value,
        iterations=iterations,
        bracket_width=right - left,
    )


def maximum_chord_and_rate_errors(
    states: list[PathHandleState],
    handle_distances: Iterable[float],
) -> tuple[float, float]:
    """Return maximum chord and differentiated-constraint residuals."""

    maximum_chord_error = 0.0
    maximum_rate_residual = 0.0
    for front, rear, distance in zip(
        states,
        states[1:],
        handle_distances,
    ):
        delta_x = rear.x - front.x
        delta_y = rear.y - front.y
        chord = (delta_x * delta_x + delta_y * delta_y) ** 0.5
        maximum_chord_error = max(
            maximum_chord_error,
            abs(chord - distance),
        )
        maximum_rate_residual = max(
            maximum_rate_residual,
            abs(
                delta_x * (rear.vx - front.vx)
                + delta_y * (rear.vy - front.vy)
            ),
        )
    return maximum_chord_error, maximum_rate_residual
