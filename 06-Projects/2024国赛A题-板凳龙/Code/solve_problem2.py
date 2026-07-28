"""Find the first physical-bench collision and export its handle states."""

from __future__ import annotations

import argparse
import json
import sys
from math import floor, hypot, isfinite
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    PROBLEM1_HANDLE_COUNT,
    problem1_handle_distances,
    solve_handle_states,
)
from collision import (  # noqa: E402
    CollisionClearance,
    bench_rectangles,
    first_nonadjacent_collision,
    minimum_nonadjacent_clearance,
)
from geometry import head_state  # noqa: E402


def six_decimal_value(value: float) -> float:
    """Round for the official table and avoid a displayed negative zero."""

    rounded = round(value, 6)
    return 0.0 if rounded == 0.0 else rounded


def state_and_clearance(time: float):
    """Return the complete chain state and minimum physical clearance."""

    states = solve_handle_states(
        head_state(time),
        problem1_handle_distances(),
    )
    clearance = minimum_nonadjacent_clearance(bench_rectangles(states))
    return states, clearance


def find_first_collision(
    *,
    scan_start: int = 0,
    scan_stop: int = 1000,
    time_tolerance: float = 1.0e-12,
) -> tuple[float, float, CollisionClearance, CollisionClearance]:
    """Bracket by integer seconds, then bisect the first sign change."""

    _, previous = state_and_clearance(float(scan_start))
    if previous.is_collision:
        raise RuntimeError("the chain is already colliding at scan_start")

    low = float(scan_start)
    high = float("nan")
    high_clearance = previous
    for integer_time in range(scan_start + 1, scan_stop + 1):
        _, current = state_and_clearance(float(integer_time))
        if current.is_collision:
            high = float(integer_time)
            low = float(integer_time - 1)
            high_clearance = current
            break
        previous = current
    else:
        raise RuntimeError("no collision found in the scan interval")

    low_clearance = previous
    while high - low > time_tolerance:
        middle = 0.5 * (low + high)
        _, middle_clearance = state_and_clearance(middle)
        if middle_clearance.is_collision:
            high = middle
            high_clearance = middle_clearance
        else:
            low = middle
            low_clearance = middle_clearance

    critical_time = 0.5 * (low + high)
    return critical_time, low, low_clearance, high_clearance


def validate_critical_state(states) -> dict[str, float]:
    """Validate full-chain geometry and velocity at the critical time."""

    distances = problem1_handle_distances()
    if len(states) != PROBLEM1_HANDLE_COUNT:
        raise RuntimeError("critical state does not contain 224 handles")

    maximum_chord_error = 0.0
    maximum_constraint_rate_residual = 0.0
    minimum_speed = float("inf")
    maximum_speed = 0.0
    minimum_theta_gap = float("inf")

    for state in states:
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
            raise RuntimeError("critical state contains a non-finite value")
        minimum_speed = min(minimum_speed, state.speed)
        maximum_speed = max(maximum_speed, state.speed)

    for previous, current, distance in zip(
        states,
        states[1:],
        distances,
    ):
        theta_gap = current.theta - previous.theta
        if theta_gap <= 0.0:
            raise RuntimeError("critical state has non-outward parameters")
        minimum_theta_gap = min(minimum_theta_gap, theta_gap)
        actual_distance = hypot(
            current.x - previous.x,
            current.y - previous.y,
        )
        maximum_chord_error = max(
            maximum_chord_error,
            abs(actual_distance - distance),
        )
        maximum_constraint_rate_residual = max(
            maximum_constraint_rate_residual,
            abs(
                (current.x - previous.x) * (current.vx - previous.vx)
                + (current.y - previous.y) * (current.vy - previous.vy)
            ),
        )

    return {
        "maximumChordErrorM": maximum_chord_error,
        "maximumConstraintRateResidualM2PerS": (
            maximum_constraint_rate_residual
        ),
        "minimumSpeedMPerS": minimum_speed,
        "maximumSpeedMPerS": maximum_speed,
        "minimumThetaGapRad": minimum_theta_gap,
    }


def dense_collision_scan(
    stop_time: float,
    *,
    step: float = 0.25,
) -> tuple[float, float, tuple[int, int]]:
    """Confirm the first sampled collision on a denser time grid."""

    if step <= 0.0:
        raise ValueError("dense scan step must be positive")

    previous_time = 0.0
    sample_index = 0
    while True:
        time = sample_index * step
        states = solve_handle_states(
            head_state(time),
            problem1_handle_distances(),
        )
        pair = first_nonadjacent_collision(bench_rectangles(states))
        if pair is not None:
            return previous_time, time, pair
        if time > stop_time + step:
            raise RuntimeError("dense scan did not reach a collision sample")
        previous_time = time
        sample_index += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", type=Path, required=True)
    args = parser.parse_args()

    critical_time, safe_bound, safe_clearance, collision_clearance = (
        find_first_collision()
    )
    states, critical_clearance = state_and_clearance(critical_time)
    metrics = validate_critical_state(states)
    safe_six_decimal_time = floor(critical_time * 1.0e6) / 1.0e6
    _, safe_six_decimal_clearance = state_and_clearance(
        safe_six_decimal_time
    )
    _, before_clearance = state_and_clearance(critical_time - 1.0e-6)
    _, after_clearance = state_and_clearance(critical_time + 1.0e-6)
    dense_safe_time, dense_collision_time, dense_pair = dense_collision_scan(
        critical_time,
        step=0.25,
    )

    rows = [
        [
            six_decimal_value(state.x),
            six_decimal_value(state.y),
            six_decimal_value(state.speed),
        ]
        for state in states
    ]
    payload = {
        "criticalTime": critical_time,
        "safeBoundTime": safe_bound,
        "safeSixDecimalTime": safe_six_decimal_time,
        "collisionPair": [
            critical_clearance.first_index,
            critical_clearance.second_index,
        ],
        "criticalMarginM": critical_clearance.margin,
        "safeBoundMarginM": safe_clearance.margin,
        "collisionBoundMarginM": collision_clearance.margin,
        "safeSixDecimalMarginM": safe_six_decimal_clearance.margin,
        "marginOneMicrosecondBeforeM": before_clearance.margin,
        "marginOneMicrosecondAfterM": after_clearance.margin,
        "denseScanStepS": 0.25,
        "denseSafeUntilS": dense_safe_time,
        "denseFirstCollisionSampleS": dense_collision_time,
        "denseCollisionPair": list(dense_pair),
        "rows": rows,
        "validation": metrics,
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    print(f"critical_time={critical_time:.12f} s")
    print(
        "collision_pair="
        f"({critical_clearance.first_index}, "
        f"{critical_clearance.second_index})"
    )
    print(f"critical_margin={critical_clearance.margin:.3e} m")
    print(
        "safe_six_decimal_time="
        f"{safe_six_decimal_time:.6f} s, "
        f"margin={safe_six_decimal_clearance.margin:.3e} m"
    )
    print(
        "one_microsecond_bracket="
        f"[{before_clearance.margin:.3e}, "
        f"{after_clearance.margin:.3e}] m"
    )
    print(
        "dense_scan="
        f"safe through {dense_safe_time:.2f} s, "
        f"collision at {dense_collision_time:.2f} s, "
        f"pair={dense_pair}"
    )
    for key, value in metrics.items():
        print(f"{key}={value:.12e}")
    print(args.json_output.resolve())


if __name__ == "__main__":
    main()
