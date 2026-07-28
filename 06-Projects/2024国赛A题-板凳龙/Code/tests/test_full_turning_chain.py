"""Full-chain smoke tests on representative problem-4 times."""

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
)
from collision import bench_rectangles, minimum_nonadjacent_clearance  # noqa: E402
from path_chain import solve_path_handle_states  # noqa: E402
from turning_path import build_turning_geometry  # noqa: E402


class FullTurningChainTests(unittest.TestCase):
    def test_complete_chain_at_all_problem4_output_times(self) -> None:
        geometry = build_turning_geometry()
        distances = problem1_handle_distances()
        for time in range(-100, 101):
            states = solve_path_handle_states(
                float(time),
                distances,
                geometry,
            )
            self.assertEqual(len(states), PROBLEM1_HANDLE_COUNT)
            for front, rear, distance in zip(
                states,
                states[1:],
                distances,
            ):
                self.assertLess(rear.s, front.s)
                self.assertAlmostEqual(
                    hypot(rear.x - front.x, rear.y - front.y),
                    distance,
                    delta=1.0e-11,
                )
            clearance = minimum_nonadjacent_clearance(
                bench_rectangles(states)
            )
            self.assertGreater(clearance.margin, 0.0)


if __name__ == "__main__":
    unittest.main()
