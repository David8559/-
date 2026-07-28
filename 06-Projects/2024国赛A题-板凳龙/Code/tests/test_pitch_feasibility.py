"""Tests for the problem-3 pitch-feasibility model."""

from __future__ import annotations

import sys
import unittest
from math import isclose, pi
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from pitch_feasibility import (  # noqa: E402
    INITIAL_THETA,
    TURNING_RADIUS,
    boundary_theta,
    global_clearance,
    minimum_pair_clearance_over_path,
)


class PitchFeasibilityTests(unittest.TestCase):
    def test_boundary_is_on_turning_circle(self) -> None:
        pitch = 0.45
        theta = boundary_theta(pitch)
        self.assertTrue(
            isclose(
                pitch * theta / (2.0 * pi),
                TURNING_RADIUS,
                abs_tol=1.0e-14,
            )
        )
        self.assertLess(theta, INITIAL_THETA)

    def test_pitch_brackets_problem3_contact(self) -> None:
        below = minimum_pair_clearance_over_path(
            0.4503,
            0,
            19,
            coarse_intervals=80,
        )
        above = minimum_pair_clearance_over_path(
            0.4504,
            0,
            19,
            coarse_intervals=80,
        )
        self.assertLess(below.margin, 0.0)
        self.assertGreater(above.margin, 0.0)
        self.assertGreater(below.head_radius, TURNING_RADIUS)
        self.assertGreater(above.head_radius, TURNING_RADIUS)

    def test_critical_pair_is_global_near_contact(self) -> None:
        result = minimum_pair_clearance_over_path(
            0.450337393,
            0,
            19,
            coarse_intervals=100,
        )
        clearance = global_clearance(result.theta, result.pitch)
        self.assertEqual(
            (clearance.first_index, clearance.second_index),
            (0, 19),
        )
        self.assertTrue(
            isclose(clearance.margin, result.margin, abs_tol=1.0e-13)
        )


if __name__ == "__main__":
    unittest.main()
