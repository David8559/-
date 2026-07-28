"""Solve the minimum feasible spiral pitch for problem 3."""

from __future__ import annotations

import argparse
import json
import sys
from math import ceil
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR / "src"))

from pitch_feasibility import (  # noqa: E402
    critical_pitch_for_pair,
    global_clearance,
    minimum_pair_clearance_over_path,
    sampled_global_path_minimum,
)


CRITICAL_PAIR = (0, 19)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--global-scan-intervals", type=int, default=480)
    args = parser.parse_args()

    critical_pitch, low_result, high_result = critical_pitch_for_pair(
        *CRITICAL_PAIR,
        low_pitch=0.45,
        high_pitch=0.46,
    )
    critical_result = minimum_pair_clearance_over_path(
        critical_pitch,
        *CRITICAL_PAIR,
    )
    critical_global = global_clearance(
        critical_result.theta,
        critical_pitch,
    )

    below = minimum_pair_clearance_over_path(
        critical_pitch - 1.0e-6,
        *CRITICAL_PAIR,
    )
    above = minimum_pair_clearance_over_path(
        critical_pitch + 1.0e-6,
        *CRITICAL_PAIR,
    )
    rounded_six_decimal = round(critical_pitch, 6)
    rounded_result = minimum_pair_clearance_over_path(
        rounded_six_decimal,
        *CRITICAL_PAIR,
    )
    safe_six_decimal = ceil(critical_pitch * 1.0e6) / 1.0e6
    safe_six_decimal_result = minimum_pair_clearance_over_path(
        safe_six_decimal,
        *CRITICAL_PAIR,
    )
    sampled_global = sampled_global_path_minimum(
        critical_pitch,
        intervals=args.global_scan_intervals,
    )

    if (
        critical_global.first_index,
        critical_global.second_index,
    ) != CRITICAL_PAIR:
        raise RuntimeError("the assumed critical pair is not globally active")
    if below.margin >= 0.0 or above.margin <= 0.0:
        raise RuntimeError("the pitch perturbation does not bracket contact")

    payload = {
        "criticalPitchM": critical_pitch,
        "criticalPair": list(CRITICAL_PAIR),
        "criticalThetaRad": critical_result.theta,
        "criticalHeadRadiusM": critical_result.head_radius,
        "criticalPairMarginM": critical_result.margin,
        "criticalGlobalMarginM": critical_global.margin,
        "pitchLowerBoundM": low_result.pitch,
        "pitchUpperBoundM": high_result.pitch,
        "lowerBoundMarginM": low_result.margin,
        "upperBoundMarginM": high_result.margin,
        "oneMicrometreBelowMarginM": below.margin,
        "oneMicrometreAboveMarginM": above.margin,
        "roundedSixDecimalPitchM": rounded_six_decimal,
        "roundedSixDecimalMarginM": rounded_result.margin,
        "safeSixDecimalPitchM": safe_six_decimal,
        "safeSixDecimalMarginM": safe_six_decimal_result.margin,
        "sampledGlobalIntervals": args.global_scan_intervals,
        "sampledGlobalMinimum": {
            "marginM": sampled_global.margin,
            "thetaRad": sampled_global.theta,
            "headRadiusM": sampled_global.head_radius,
            "pair": [
                sampled_global.first_index,
                sampled_global.second_index,
            ],
        },
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"critical_pitch={critical_pitch:.12f} m")
    print(f"critical_pair={CRITICAL_PAIR}")
    print(f"critical_theta={critical_result.theta:.12f} rad")
    print(f"critical_head_radius={critical_result.head_radius:.12f} m")
    print(f"critical_pair_margin={critical_result.margin:+.3e} m")
    print(f"critical_global_margin={critical_global.margin:+.3e} m")
    print(
        "one_micrometre_pitch_bracket="
        f"[{below.margin:+.3e}, {above.margin:+.3e}] m"
    )
    print(
        "six_decimal_reporting="
        f"rounded {rounded_six_decimal:.6f} m "
        f"(margin {rounded_result.margin:+.3e} m); "
        f"safe {safe_six_decimal:.6f} m "
        f"(margin {safe_six_decimal_result.margin:+.3e} m)"
    )
    print(
        "sampled_global_minimum="
        f"{sampled_global.margin:+.3e} m at "
        f"r={sampled_global.head_radius:.6f} m, "
        f"pair=({sampled_global.first_index}, "
        f"{sampled_global.second_index})"
    )
    print(args.json_output.resolve())


if __name__ == "__main__":
    main()
