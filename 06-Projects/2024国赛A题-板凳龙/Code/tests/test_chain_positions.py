"""Tests for the fixed-chord handle recursion."""

from __future__ import annotations

import sys
import unittest
from math import hypot, isclose
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    BODY_HANDLE_DISTANCE,
    HEAD_HANDLE_DISTANCE,
    chord_distance_squared,
    first_bench_distances,
    solve_handle_positions,
)
from geometry import head_state  # noqa: E402


class ChainPositionTests(unittest.TestCase):
    def test_three_bench_distance_constraints(self) -> None:
        expected = [
            HEAD_HANDLE_DISTANCE,
            BODY_HANDLE_DISTANCE,
            BODY_HANDLE_DISTANCE,
        ]
        for time in (0.0, 60.0, 180.0, 300.0):
            points = solve_handle_positions(
                head_state(time).theta,
                first_bench_distances(3),
            )
            self.assertEqual(len(points), 4)
            for index, distance in enumerate(expected, start=1):
                actual = hypot(
                    points[index].x - points[index - 1].x,
                    points[index].y - points[index - 1].y,
                )
                self.assertTrue(isclose(actual, distance, abs_tol=1.0e-12))

    def test_parameters_are_strictly_outward(self) -> None:
        for time in range(0, 301):
            points = solve_handle_positions(
                head_state(float(time)).theta,
                first_bench_distances(3),
            )
            theta_values = [point.theta for point in points]
            self.assertEqual(theta_values, sorted(theta_values))
            self.assertEqual(len(theta_values), len(set(theta_values)))

    def test_selected_root_is_the_nearest_root(self) -> None:
        previous = head_state(300.0).theta
        points = solve_handle_positions(previous, [HEAD_HANDLE_DISTANCE])
        root = points[1].theta
        target_squared = HEAD_HANDLE_DISTANCE**2

        # All sampled points strictly between the handles remain inside the
        # target circle, so the chosen crossing is the first one.
        for step in range(1, 100):
            theta = previous + (root - previous) * step / 100.0
            self.assertLess(
                chord_distance_squared(previous, theta),
                target_squared,
            )

    def test_distance_formula_matches_cartesian_distance(self) -> None:
        points = solve_handle_positions(
            head_state(0.0).theta,
            first_bench_distances(3),
        )
        for previous, current in zip(points, points[1:]):
            formula = chord_distance_squared(previous.theta, current.theta)
            cartesian = (current.x - previous.x) ** 2 + (
                current.y - previous.y
            ) ** 2
            self.assertTrue(isclose(formula, cartesian, abs_tol=1.0e-13))


if __name__ == "__main__":
    unittest.main()

