"""Solve problem 4 on the spiral–biarc–spiral turning path."""

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
)
from collision import bench_rectangles, minimum_nonadjacent_clearance  # noqa: E402
from path_chain import solve_path_handle_states  # noqa: E402
from turning_path import build_turning_geometry  # noqa: E402


START_TIME = -100
STOP_TIME = 100
KEY_TIMES = (-100, -50, 0, 50, 100)
KEY_INDICES = (0, 1, 51, 101, 151, 201, 223)


def six_decimal_value(value: float) -> float:
    """Round for the official table and suppress displayed negative zero."""

    rounded = round(value, 6)
    return 0.0 if rounded == 0.0 else rounded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", type=Path, required=True)
    args = parser.parse_args()

    geometry = build_turning_geometry()
    distances = problem1_handle_distances()
    all_states = []
    maximum_chord_error = 0.0
    maximum_constraint_rate_residual = 0.0
    minimum_speed = float("inf")
    maximum_speed = 0.0
    maximum_speed_time = float("nan")
    maximum_speed_index = -1
    minimum_path_gap = float("inf")
    minimum_clearance = float("inf")
    minimum_clearance_time = float("nan")
    minimum_clearance_pair = (-1, -1)

    for time in range(START_TIME, STOP_TIME + 1):
        states = solve_path_handle_states(
            float(time),
            distances,
            geometry,
        )
        if len(states) != PROBLEM1_HANDLE_COUNT:
            raise RuntimeError("problem-4 state does not contain 224 handles")

        for state in states:
            values = (
                state.s,
                state.x,
                state.y,
                state.vx,
                state.vy,
                state.speed,
            )
            if not all(isfinite(value) for value in values):
                raise RuntimeError("problem-4 state contains a non-finite value")
            minimum_speed = min(minimum_speed, state.speed)
            if state.speed > maximum_speed:
                maximum_speed = state.speed
                maximum_speed_time = float(time)
                maximum_speed_index = state.index

        for front, rear, distance in zip(states, states[1:], distances):
            path_gap = front.s - rear.s
            if path_gap <= 0.0:
                raise RuntimeError("problem-4 handle order is not decreasing")
            minimum_path_gap = min(minimum_path_gap, path_gap)
            chord = hypot(rear.x - front.x, rear.y - front.y)
            maximum_chord_error = max(
                maximum_chord_error,
                abs(chord - distance),
            )
            rate_residual = abs(
                (rear.x - front.x) * (rear.vx - front.vx)
                + (rear.y - front.y) * (rear.vy - front.vy)
            )
            maximum_constraint_rate_residual = max(
                maximum_constraint_rate_residual,
                rate_residual,
            )

        clearance = minimum_nonadjacent_clearance(
            bench_rectangles(states)
        )
        if clearance.margin < minimum_clearance:
            minimum_clearance = clearance.margin
            minimum_clearance_time = float(time)
            minimum_clearance_pair = (
                clearance.first_index,
                clearance.second_index,
            )
        all_states.append(states)

    position_rows: list[list[float]] = []
    speed_rows: list[list[float]] = []
    for handle_index in range(PROBLEM1_HANDLE_COUNT):
        position_rows.append(
            [
                six_decimal_value(states[handle_index].x)
                for states in all_states
            ]
        )
        position_rows.append(
            [
                six_decimal_value(states[handle_index].y)
                for states in all_states
            ]
        )
        speed_rows.append(
            [
                six_decimal_value(states[handle_index].speed)
                for states in all_states
            ]
        )

    key_rows = {}
    for time in KEY_TIMES:
        states = all_states[time - START_TIME]
        key_rows[str(time)] = [
            {
                "index": index,
                "x": six_decimal_value(states[index].x),
                "y": six_decimal_value(states[index].y),
                "speed": six_decimal_value(states[index].speed),
            }
            for index in KEY_INDICES
        ]

    payload = {
        "times": list(range(START_TIME, STOP_TIME + 1)),
        "positionRows": position_rows,
        "speedRows": speed_rows,
        "keyRows": key_rows,
        "geometry": {
            "boundaryThetaRad": geometry.boundary_theta,
            "entry": [geometry.entry_x, geometry.entry_y],
            "exit": [geometry.exit_x, geometry.exit_y],
            "join": [geometry.join_x, geometry.join_y],
            "firstCenter": [
                geometry.first_center_x,
                geometry.first_center_y,
            ],
            "secondCenter": [
                geometry.second_center_x,
                geometry.second_center_y,
            ],
            "firstRadiusM": geometry.first_radius,
            "secondRadiusM": geometry.second_radius,
            "firstSweepRad": geometry.first_sweep,
            "secondSweepRad": geometry.second_sweep,
            "firstLengthM": geometry.first_length,
            "secondLengthM": geometry.second_length,
            "totalArcLengthM": geometry.total_arc_length,
        },
        "validation": {
            "maximumChordErrorM": maximum_chord_error,
            "maximumConstraintRateResidualM2PerS": (
                maximum_constraint_rate_residual
            ),
            "minimumSpeedMPerS": minimum_speed,
            "maximumSpeedMPerS": maximum_speed,
            "maximumSpeedTimeS": maximum_speed_time,
            "maximumSpeedHandleIndex": maximum_speed_index,
            "minimumPathGapM": minimum_path_gap,
            "minimumCollisionMarginM": minimum_clearance,
            "minimumCollisionMarginTimeS": minimum_clearance_time,
            "minimumCollisionMarginPair": list(minimum_clearance_pair),
        },
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    print(f"first_radius={geometry.first_radius:.12f} m")
    print(f"second_radius={geometry.second_radius:.12f} m")
    print(f"turning_arc_length={geometry.total_arc_length:.12f} m")
    for key, value in payload["validation"].items():
        print(f"{key}={value}")
    print(args.json_output.resolve())


if __name__ == "__main__":
    main()
