"""Regression tests for the problem-1 dragon-head trajectory."""

from __future__ import annotations

import sys
import unittest
from math import isclose, pi
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from geometry import (  # noqa: E402
    DEFAULT_PITCH,
    DEFAULT_THETA_INITIAL,
    head_state,
    spiral_arc_primitive,
    spiral_scale,
)


class HeadTrajectoryTests(unittest.TestCase):
    def test_initial_geometry_and_direction(self) -> None:
        state = head_state(0.0)
        self.assertTrue(isclose(state.theta, 32.0 * pi, abs_tol=1.0e-12))
        self.assertTrue(isclose(state.x, 8.8, abs_tol=1.0e-12))
        self.assertTrue(isclose(state.y, 0.0, abs_tol=1.0e-12))
        self.assertLess(state.vy, 0.0)
        self.assertTrue(isclose(state.speed, 1.0, abs_tol=1.0e-12))

    def test_arc_length_balance(self) -> None:
        initial = spiral_arc_primitive(DEFAULT_THETA_INITIAL)
        for time in (0.0, 60.0, 120.0, 180.0, 240.0, 300.0):
            state = head_state(time)
            travelled = initial - spiral_arc_primitive(state.theta)
            self.assertTrue(isclose(travelled, time, abs_tol=1.0e-10))

    def test_theta_decreases_and_radius_matches(self) -> None:
        previous_theta = float("inf")
        b = spiral_scale(DEFAULT_PITCH)
        for time in range(0, 301):
            state = head_state(float(time))
            self.assertLess(state.theta, previous_theta)
            self.assertTrue(
                isclose(
                    (state.x * state.x + state.y * state.y) ** 0.5,
                    b * state.theta,
                    abs_tol=1.0e-12,
                )
            )
            previous_theta = state.theta

    def test_primitive_derivative(self) -> None:
        b = spiral_scale(DEFAULT_PITCH)
        for theta in (1.0, 10.0, 32.0 * pi):
            step = 1.0e-5
            numerical = (
                spiral_arc_primitive(theta + step)
                - spiral_arc_primitive(theta - step)
            ) / (2.0 * step)
            expected = b * (1.0 + theta * theta) ** 0.5
            self.assertTrue(isclose(numerical, expected, rel_tol=1.0e-9))


if __name__ == "__main__":
    unittest.main()

