"""Tests for the rigid chain on the problem-4 piecewise path."""

from __future__ import annotations

import sys
import unittest
from math import hypot, isfinite
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import first_bench_distances  # noqa: E402
from path_chain import solve_path_handle_states  # noqa: E402
from turning_path import build_turning_geometry  # noqa: E402


class PathChainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.geometry = build_turning_geometry()
        self.distances = first_bench_distances(12)

    def test_chords_order_and_velocity_constraints(self) -> None:
        for head_s in (-100.0, 0.0, 5.0, 10.0, 14.0, 50.0, 100.0):
            states = solve_path_handle_states(
                head_s,
                self.distances,
                self.geometry,
            )
            self.assertEqual(len(states), 13)
            for front, rear, distance in zip(
                states,
                states[1:],
                self.distances,
            ):
                self.assertLess(rear.s, front.s)
                chord = hypot(rear.x - front.x, rear.y - front.y)
                self.assertAlmostEqual(chord, distance, delta=1.0e-11)
                residual = (
                    (rear.x - front.x) * (rear.vx - front.vx)
                    + (rear.y - front.y) * (rear.vy - front.vy)
                )
                self.assertAlmostEqual(residual, 0.0, delta=1.0e-11)
            self.assertTrue(
                all(
                    isfinite(value)
                    for state in states
                    for value in (
                        state.s,
                        state.x,
                        state.y,
                        state.vx,
                        state.vy,
                        state.speed,
                    )
                )
            )

    def test_velocity_matches_centred_difference(self) -> None:
        step = 1.0e-4
        for head_s in (0.5, 8.5, 10.0, 14.5):
            middle = solve_path_handle_states(
                head_s,
                self.distances,
                self.geometry,
            )
            before = solve_path_handle_states(
                head_s - step,
                self.distances,
                self.geometry,
            )
            after = solve_path_handle_states(
                head_s + step,
                self.distances,
                self.geometry,
            )
            for state, left, right in zip(middle, before, after):
                finite_vx = (right.x - left.x) / (2.0 * step)
                finite_vy = (right.y - left.y) / (2.0 * step)
                self.assertLess(
                    hypot(state.vx - finite_vx, state.vy - finite_vy),
                    2.0e-7,
                )


if __name__ == "__main__":
    unittest.main()
