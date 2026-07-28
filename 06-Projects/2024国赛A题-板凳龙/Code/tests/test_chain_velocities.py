"""Tests for analytical handle-velocity recursion."""

from __future__ import annotations

import sys
import unittest
from math import hypot, isclose
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    first_bench_distances,
    solve_handle_positions,
    solve_handle_states,
)
from geometry import head_state  # noqa: E402


class ChainVelocityTests(unittest.TestCase):
    def test_head_state_is_preserved(self) -> None:
        head = head_state(180.0)
        state = solve_handle_states(head, first_bench_distances(3))[0]
        self.assertEqual(state.index, 0)
        self.assertTrue(isclose(state.theta, head.theta, abs_tol=1.0e-15))
        self.assertTrue(
            isclose(state.theta_rate, head.theta_rate, abs_tol=1.0e-15)
        )
        self.assertTrue(isclose(state.vx, head.vx, abs_tol=1.0e-15))
        self.assertTrue(isclose(state.vy, head.vy, abs_tol=1.0e-15))

    def test_differentiated_chord_constraints(self) -> None:
        distances = first_bench_distances(3)
        for time in (0.0, 60.0, 180.0, 300.0):
            states = solve_handle_states(head_state(time), distances)
            for previous, current in zip(states, states[1:]):
                residual = (
                    (current.x - previous.x) * (current.vx - previous.vx)
                    + (current.y - previous.y) * (current.vy - previous.vy)
                )
                self.assertLess(abs(residual), 1.0e-12)

    def test_velocity_matches_centred_difference(self) -> None:
        distances = first_bench_distances(3)
        step = 1.0e-3
        for time in (1.0, 60.0, 180.0, 299.0):
            states = solve_handle_states(head_state(time), distances)
            before = solve_handle_positions(
                head_state(time - step).theta,
                distances,
            )
            after = solve_handle_positions(
                head_state(time + step).theta,
                distances,
            )
            for state, point_before, point_after in zip(
                states,
                before,
                after,
            ):
                numerical_vx = (point_after.x - point_before.x) / (2.0 * step)
                numerical_vy = (point_after.y - point_before.y) / (2.0 * step)
                error = hypot(
                    state.vx - numerical_vx,
                    state.vy - numerical_vy,
                )
                self.assertLess(error, 1.0e-8)

    def test_speeds_are_finite_and_positive(self) -> None:
        distances = first_bench_distances(3)
        for time in range(0, 301):
            states = solve_handle_states(head_state(float(time)), distances)
            for state in states:
                self.assertGreater(state.speed, 0.0)
                self.assertTrue(isclose(state.speed, hypot(state.vx, state.vy)))


if __name__ == "__main__":
    unittest.main()
