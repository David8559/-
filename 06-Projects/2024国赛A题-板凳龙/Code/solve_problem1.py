"""Solve all 224 handle states at integer seconds from 0 through 300.

The script validates the full chain at full precision, then writes a compact
JSON intermediate for the official result1.xlsx template builder.  Stored
table values are rounded to six decimals only after validation.
"""

from __future__ import annotations

import argparse
import json
import sys
from math import hypot, isfinite
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    PROBLEM1_HANDLE_COUNT,
    problem1_handle_distances,
    solve_handle_states,
)
from geometry import head_state  # noqa: E402


def six_decimal_value(value: float) -> float:
    """Round for the official table and avoid a displayed negative zero."""

    rounded = round(value, 6)
    return 0.0 if rounded == 0.0 else rounded


def solve_problem1() -> tuple[dict[str, object], dict[str, float]]:
    """Return official-table rows and full-precision validation metrics."""

    times = list(range(301))
    distances = problem1_handle_distances()
    position_rows = [[] for _ in range(2 * PROBLEM1_HANDLE_COUNT)]
    speed_rows = [[] for _ in range(PROBLEM1_HANDLE_COUNT)]

    maximum_chord_error = 0.0
    maximum_constraint_rate_residual = 0.0
    minimum_speed = float("inf")
    maximum_speed = 0.0
    minimum_theta_gap = float("inf")

    for time in times:
        states = solve_handle_states(head_state(float(time)), distances)
        if len(states) != PROBLEM1_HANDLE_COUNT:
            raise RuntimeError(
                f"expected {PROBLEM1_HANDLE_COUNT} states, got {len(states)}"
            )

        for index, state in enumerate(states):
            values = (
                state.theta,
                state.theta_rate,
                state.x,
                state.y,
                state.vx,
                state.vy,
                state.speed,
            )
            if not all(isfinite(value) for value in values):
                raise RuntimeError(
                    f"non-finite state at t={time} s, handle P_{index}"
                )
            position_rows[2 * index].append(six_decimal_value(state.x))
            position_rows[2 * index + 1].append(six_decimal_value(state.y))
            speed_rows[index].append(six_decimal_value(state.speed))
            minimum_speed = min(minimum_speed, state.speed)
            maximum_speed = max(maximum_speed, state.speed)

        for index, (previous, current, expected_distance) in enumerate(
            zip(states, states[1:], distances),
            start=1,
        ):
            theta_gap = current.theta - previous.theta
            if theta_gap <= 0.0:
                raise RuntimeError(
                    f"non-outward parameter order at t={time} s, P_{index}"
                )
            minimum_theta_gap = min(minimum_theta_gap, theta_gap)

            actual_distance = hypot(
                current.x - previous.x,
                current.y - previous.y,
            )
            maximum_chord_error = max(
                maximum_chord_error,
                abs(actual_distance - expected_distance),
            )
            constraint_rate_residual = abs(
                (current.x - previous.x) * (current.vx - previous.vx)
                + (current.y - previous.y) * (current.vy - previous.vy)
            )
            maximum_constraint_rate_residual = max(
                maximum_constraint_rate_residual,
                constraint_rate_residual,
            )

    table_data: dict[str, object] = {
        "times": times,
        "positionRows": position_rows,
        "speedRows": speed_rows,
    }
    metrics = {
        "maximumChordErrorM": maximum_chord_error,
        "maximumConstraintRateResidualM2PerS": (
            maximum_constraint_rate_residual
        ),
        "minimumSpeedMPerS": minimum_speed,
        "maximumSpeedMPerS": maximum_speed,
        "minimumThetaGapRad": minimum_theta_gap,
    }
    return table_data, metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json-output",
        type=Path,
        required=True,
        help="Path for the six-decimal workbook intermediate.",
    )
    args = parser.parse_args()

    table_data, metrics = solve_problem1()
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    payload = {**table_data, "validation": metrics}
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    print(f"handles={PROBLEM1_HANDLE_COUNT}")
    print("times=301 (0-300 s)")
    for key, value in metrics.items():
        print(f"{key}={value:.12e}")
    print(args.json_output.resolve())


if __name__ == "__main__":
    main()
