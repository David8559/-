"""Representative tests for the complete 224-handle problem-1 chain."""

from __future__ import annotations

import sys
import unittest
from math import hypot
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import (  # noqa: E402
    PROBLEM1_HANDLE_COUNT,
    problem1_handle_distances,
    solve_handle_states,
)
from geometry import head_state  # noqa: E402


class FullChainTests(unittest.TestCase):
    def test_problem1_distance_vector_shape(self) -> None:
        distances = problem1_handle_distances()
        self.assertEqual(len(distances), PROBLEM1_HANDLE_COUNT - 1)
        self.assertEqual(distances[0], 2.86)
        self.assertTrue(all(distance == 1.65 for distance in distances[1:]))

    def test_complete_chain_at_representative_times(self) -> None:
        distances = problem1_handle_distances()
        for time in (0.0, 150.0, 300.0):
            states = solve_handle_states(head_state(time), distances)
            self.assertEqual(len(states), PROBLEM1_HANDLE_COUNT)
            for previous, current, expected in zip(
                states,
                states[1:],
                distances,
            ):
                self.assertGreater(current.theta, previous.theta)
                actual = hypot(
                    current.x - previous.x,
                    current.y - previous.y,
                )
                self.assertLess(abs(actual - expected), 1.0e-11)
                self.assertGreater(current.speed, 0.0)


if __name__ == "__main__":
    unittest.main()
