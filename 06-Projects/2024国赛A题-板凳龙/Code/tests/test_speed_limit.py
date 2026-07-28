"""Tests for the continuous problem-5 speed-limit search."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import problem1_handle_distances  # noqa: E402
from path_chain import solve_path_handle_states  # noqa: E402
from speed_limit import (  # noqa: E402
    evaluate_speed_ratio,
    golden_section_maximum,
)
from turning_path import build_turning_geometry  # noqa: E402


class SpeedLimitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.geometry = build_turning_geometry()
        self.distances = problem1_handle_distances()

    def test_golden_section_maximum_on_known_parabola(self) -> None:
        result = golden_section_maximum(
            lambda value: 7.0 - (value - 1.25) ** 2,
            -2.0,
            4.0,
        )
        self.assertAlmostEqual(result.x, 1.25, delta=5.0e-8)
        self.assertAlmostEqual(result.value, 7.0, delta=1.0e-13)

    def test_handle_speeds_scale_linearly_with_head_speed(self) -> None:
        unit = solve_path_handle_states(
            14.48,
            self.distances,
            self.geometry,
            head_speed=1.0,
        )
        scaled = solve_path_handle_states(
            14.48,
            self.distances,
            self.geometry,
            head_speed=1.25,
        )
        for baseline, changed in zip(unit, scaled):
            self.assertAlmostEqual(
                changed.speed,
                1.25 * baseline.speed,
                delta=2.0e-13,
            )

    def test_continuous_neighborhood_exceeds_integer_samples(self) -> None:
        integer_left = evaluate_speed_ratio(
            14.0,
            self.distances,
            self.geometry,
        )
        interior = evaluate_speed_ratio(
            14.48,
            self.distances,
            self.geometry,
        )
        integer_right = evaluate_speed_ratio(
            15.0,
            self.distances,
            self.geometry,
        )
        self.assertGreater(interior.maximum_ratio, 1.60)
        self.assertGreater(
            interior.maximum_ratio,
            integer_left.maximum_ratio + 0.18,
        )
        self.assertGreater(
            interior.maximum_ratio,
            integer_right.maximum_ratio + 0.18,
        )

    def test_refined_problem5_peak_is_locally_maximal(self) -> None:
        result = golden_section_maximum(
            lambda head_s: evaluate_speed_ratio(
                head_s,
                self.distances,
                self.geometry,
            ).maximum_ratio,
            14.4,
            14.55,
            x_tolerance=1.0e-9,
        )
        self.assertGreater(result.value, 1.604)
        self.assertGreater(result.x, 14.45)
        self.assertLess(result.x, 14.51)
        for offset in (-1.0e-4, 1.0e-4):
            neighbor = evaluate_speed_ratio(
                result.x + offset,
                self.distances,
                self.geometry,
            )
            self.assertLessEqual(
                neighbor.maximum_ratio,
                result.value + 2.0e-11,
            )

    def test_primary_domain_contains_complete_turn_transition(self) -> None:
        entry = solve_path_handle_states(
            0.0,
            self.distances,
            self.geometry,
        )
        exit_state = solve_path_handle_states(
            400.0,
            self.distances,
            self.geometry,
        )
        self.assertTrue(
            all(state.segment == "inward-spiral" for state in entry)
        )
        self.assertTrue(
            all(state.segment == "outward-spiral" for state in exit_state)
        )


if __name__ == "__main__":
    unittest.main()
