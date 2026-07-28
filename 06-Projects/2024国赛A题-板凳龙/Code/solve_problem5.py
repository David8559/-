"""Solve the continuous speed-limit problem on the problem-4 path."""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter


CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import problem1_handle_distances  # noqa: E402
from path_chain import solve_path_handle_states  # noqa: E402
from speed_limit import (  # noqa: E402
    SpeedEvaluation,
    evaluate_speed_ratio,
    golden_section_maximum,
    maximum_chord_and_rate_errors,
)
from turning_path import build_turning_geometry  # noqa: E402


SPEED_LIMIT_M_PER_S = 2.0
SEARCH_START_S = 0.0
SEARCH_STOP_S = 400.0
FINE_GRID_STEP_M = 0.1
LOCAL_SCAN_HALF_WIDTH_M = 0.06
LOCAL_SCAN_STEP_M = 0.001

_WORKER_GEOMETRY = None
_WORKER_DISTANCES = None


def _initialize_worker() -> None:
    global _WORKER_GEOMETRY, _WORKER_DISTANCES
    _WORKER_GEOMETRY = build_turning_geometry()
    _WORKER_DISTANCES = problem1_handle_distances()


def _evaluate_worker(head_s: float) -> tuple[float, float, int, float, str]:
    if _WORKER_GEOMETRY is None or _WORKER_DISTANCES is None:
        _initialize_worker()
    result = evaluate_speed_ratio(
        head_s,
        _WORKER_DISTANCES,
        _WORKER_GEOMETRY,
    )
    return (
        result.head_s,
        result.maximum_ratio,
        result.handle_index,
        result.handle_s,
        result.handle_segment,
    )


def _grid(start: float, stop: float, step: float) -> list[float]:
    count = int(round((stop - start) / step))
    if abs(start + count * step - stop) > 1.0e-10:
        raise ValueError("grid endpoints are not aligned with the step")
    return [start + index * step for index in range(count + 1)]


def _scan(
    values: list[float],
    workers: int,
) -> list[SpeedEvaluation]:
    if workers == 1:
        _initialize_worker()
        rows = [_evaluate_worker(value) for value in values]
    else:
        with ProcessPoolExecutor(
            max_workers=workers,
            initializer=_initialize_worker,
        ) as executor:
            rows = list(
                executor.map(
                    _evaluate_worker,
                    values,
                    chunksize=10,
                )
            )
    return [
        SpeedEvaluation(
            head_s=row[0],
            maximum_ratio=row[1],
            handle_index=row[2],
            handle_s=row[3],
            handle_segment=row[4],
        )
        for row in rows
    ]


def _local_candidate_indices(
    samples: list[SpeedEvaluation],
) -> list[int]:
    candidates = []
    for index in range(1, len(samples) - 1):
        current = samples[index].maximum_ratio
        if (
            current >= samples[index - 1].maximum_ratio
            and current >= samples[index + 1].maximum_ratio
        ):
            candidates.append(index)
    candidates.sort(
        key=lambda index: samples[index].maximum_ratio,
        reverse=True,
    )
    return candidates


def _grid_convergence(
    samples: list[SpeedEvaluation],
) -> list[dict[str, float | int]]:
    rows = []
    for step in (1.0, 0.5, 0.2, 0.1):
        stride = int(round(step / FINE_GRID_STEP_M))
        subset = samples[::stride]
        best = max(subset, key=lambda sample: sample.maximum_ratio)
        rows.append(
            {
                "stepM": step,
                "maximumRatio": best.maximum_ratio,
                "headS": best.head_s,
                "handleIndex": best.handle_index,
            }
        )
    return rows


def _finite_difference_error(
    head_s: float,
    handle_indices: list[int],
    *,
    step: float = 1.0e-5,
) -> float:
    geometry = build_turning_geometry()
    distances = problem1_handle_distances()
    before = solve_path_handle_states(head_s - step, distances, geometry)
    middle = solve_path_handle_states(head_s, distances, geometry)
    after = solve_path_handle_states(head_s + step, distances, geometry)
    maximum_error = 0.0
    for index in handle_indices:
        finite_vx = (after[index].x - before[index].x) / (2.0 * step)
        finite_vy = (after[index].y - before[index].y) / (2.0 * step)
        error = (
            (middle[index].vx - finite_vx) ** 2
            + (middle[index].vy - finite_vy) ** 2
        ) ** 0.5
        maximum_error = max(maximum_error, error)
    return maximum_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument(
        "--workers",
        type=int,
        default=min(8, os.cpu_count() or 1),
    )
    args = parser.parse_args()
    if args.workers <= 0:
        raise ValueError("workers must be positive")

    started = perf_counter()
    fine_grid = _grid(
        SEARCH_START_S,
        SEARCH_STOP_S,
        FINE_GRID_STEP_M,
    )
    samples = _scan(fine_grid, args.workers)
    if len(samples) != len(fine_grid):
        raise RuntimeError("continuous speed scan returned the wrong size")

    candidate_indices = _local_candidate_indices(samples)
    if not candidate_indices:
        raise RuntimeError("continuous speed scan found no local maximum")
    coarse_best = samples[candidate_indices[0]]

    geometry = build_turning_geometry()
    distances = problem1_handle_distances()

    def global_ratio(head_s: float) -> float:
        return evaluate_speed_ratio(
            head_s,
            distances,
            geometry,
        ).maximum_ratio

    refined = golden_section_maximum(
        global_ratio,
        coarse_best.head_s - FINE_GRID_STEP_M,
        coarse_best.head_s + FINE_GRID_STEP_M,
        x_tolerance=1.0e-11,
    )
    refined_evaluation = evaluate_speed_ratio(
        refined.x,
        distances,
        geometry,
    )
    unit_states = solve_path_handle_states(
        refined.x,
        distances,
        geometry,
        head_speed=1.0,
    )
    tie_tolerance = 2.0e-11
    active_handles = [
        state.index
        for state in unit_states
        if refined.value - state.speed <= tie_tolerance
    ]
    active_segments = sorted(
        {unit_states[index].segment for index in active_handles}
    )

    maximum_head_speed = SPEED_LIMIT_M_PER_S / refined.value
    rounded_six = round(maximum_head_speed, 6)
    safe_six = math.floor(maximum_head_speed * 1.0e6) / 1.0e6
    if rounded_six * refined.value <= SPEED_LIMIT_M_PER_S:
        safe_six = rounded_six

    scaled_states = solve_path_handle_states(
        refined.x,
        distances,
        geometry,
        head_speed=maximum_head_speed,
    )
    scaled_maximum = max(state.speed for state in scaled_states)
    maximum_chord_error, maximum_rate_residual = (
        maximum_chord_and_rate_errors(scaled_states, distances)
    )

    local_start = refined.x - LOCAL_SCAN_HALF_WIDTH_M
    local_stop = refined.x + LOCAL_SCAN_HALF_WIDTH_M
    local_grid = _grid(
        local_start,
        local_stop,
        LOCAL_SCAN_STEP_M,
    )
    local_samples = [
        evaluate_speed_ratio(value, distances, geometry)
        for value in local_grid
    ]
    local_best = max(
        local_samples,
        key=lambda sample: sample.maximum_ratio,
    )
    local_deviation = abs(local_best.maximum_ratio - refined.value)

    perturbations = []
    for offset in (-1.0e-3, -1.0e-4, -1.0e-5, 0.0, 1.0e-5, 1.0e-4, 1.0e-3):
        evaluation = evaluate_speed_ratio(
            refined.x + offset,
            distances,
            geometry,
        )
        perturbations.append(
            {
                "offsetM": offset,
                "maximumRatio": evaluation.maximum_ratio,
                "handleIndex": evaluation.handle_index,
            }
        )

    negative_tail = [
        evaluate_speed_ratio(value, distances, geometry)
        for value in _grid(-200.0, 0.0, 10.0)
    ]
    positive_tail = [
        evaluate_speed_ratio(value, distances, geometry)
        for value in _grid(400.0, 800.0, 5.0)
    ]
    negative_tail_max = max(
        negative_tail,
        key=lambda sample: sample.maximum_ratio,
    )
    positive_tail_max = max(
        positive_tail,
        key=lambda sample: sample.maximum_ratio,
    )

    if refined.value <= max(
        negative_tail_max.maximum_ratio,
        positive_tail_max.maximum_ratio,
    ):
        raise RuntimeError("tail-domain check exceeds the refined peak")
    if abs(scaled_maximum - SPEED_LIMIT_M_PER_S) > 2.0e-12:
        raise RuntimeError("scaled maximum speed does not meet the limit")
    if local_deviation > 2.0e-6:
        raise RuntimeError("local dense scan disagrees with refinement")

    top_candidates = [
        samples[index]
        for index in candidate_indices[:20]
    ]
    payload = {
        "model": {
            "speedLimitMPerS": SPEED_LIMIT_M_PER_S,
            "unitHeadSpeedMPerS": 1.0,
            "searchCoordinate": "head path arc length s0",
            "primaryDomainM": [SEARCH_START_S, SEARCH_STOP_S],
            "fineGridStepM": FINE_GRID_STEP_M,
            "sampleCount": len(samples),
            "workers": args.workers,
        },
        "gridConvergence": _grid_convergence(samples),
        "refinedMaximum": {
            "maximumSpeedRatio": refined.value,
            "headSAtMaximumM": refined.x,
            "coarseHeadSM": coarse_best.head_s,
            "coarseMaximumRatio": coarse_best.maximum_ratio,
            "activeHandleIndices": active_handles,
            "activeSegments": active_segments,
            "headSegment": unit_states[0].segment,
            "maximumHeadSpeedMPerS": maximum_head_speed,
            "roundedSixDecimalsMPerS": rounded_six,
            "safeSixDecimalsMPerS": safe_six,
            "maximumSpeedAtSafeSixMPerS": safe_six * refined.value,
            "peakTimeAtMaximumHeadSpeedS": (
                refined.x / maximum_head_speed
            ),
            "goldenIterations": refined.iterations,
            "finalBracketWidthM": refined.bracket_width,
        },
        "validation": {
            "scaledMaximumSpeedMPerS": scaled_maximum,
            "maximumChordErrorM": maximum_chord_error,
            "maximumConstraintRateResidualM2PerS": (
                maximum_rate_residual
            ),
            "finiteDifferenceVelocityErrorMPerS": (
                _finite_difference_error(refined.x, active_handles)
            ),
            "localScanStepM": LOCAL_SCAN_STEP_M,
            "localScanMaximumRatio": local_best.maximum_ratio,
            "localScanHeadSM": local_best.head_s,
            "localScanDeviationFromRefined": local_deviation,
            "negativeTailMaximumRatio": (
                negative_tail_max.maximum_ratio
            ),
            "positiveTailMaximumRatio": (
                positive_tail_max.maximum_ratio
            ),
            "positiveTailMaximumHeadSM": positive_tail_max.head_s,
            "perturbations": perturbations,
        },
        "topGridCandidates": [
            {
                "headS": sample.head_s,
                "maximumRatio": sample.maximum_ratio,
                "handleIndex": sample.handle_index,
                "handleS": sample.handle_s,
                "handleSegment": sample.handle_segment,
            }
            for sample in top_candidates
        ],
        "scan": {
            "headS": [sample.head_s for sample in samples],
            "maximumRatio": [
                sample.maximum_ratio for sample in samples
            ],
            "activeHandleIndex": [
                sample.handle_index for sample in samples
            ],
        },
        "localScan": {
            "headS": [sample.head_s for sample in local_samples],
            "maximumRatio": [
                sample.maximum_ratio for sample in local_samples
            ],
            "activeHandleIndex": [
                sample.handle_index for sample in local_samples
            ],
        },
        "runtimeSeconds": perf_counter() - started,
    }

    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"maximum_speed_ratio={refined.value:.15f}")
    print(f"head_s_at_maximum={refined.x:.12f} m")
    print(f"active_handles={active_handles}")
    print(f"maximum_head_speed={maximum_head_speed:.12f} m/s")
    print(f"safe_six_decimals={safe_six:.6f} m/s")
    print(f"scaled_maximum_speed={scaled_maximum:.12f} m/s")
    print(f"runtime={payload['runtimeSeconds']:.3f} s")
    print(args.json_output.resolve())


if __name__ == "__main__":
    main()
