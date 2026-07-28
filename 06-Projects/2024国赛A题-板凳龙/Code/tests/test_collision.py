"""Tests for oriented-rectangle bench collision detection."""

from __future__ import annotations

import sys
import unittest
from math import isclose
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from chain import problem1_handle_distances, solve_handle_states  # noqa: E402
from collision import (  # noqa: E402
    BENCH_WIDTH,
    BODY_BENCH_LENGTH,
    HEAD_BENCH_LENGTH,
    BenchRectangle,
    bench_rectangles,
    first_nonadjacent_collision,
    minimum_nonadjacent_clearance,
    rectangle_separation_margin,
)
from geometry import head_state  # noqa: E402


def axis_aligned_rectangle(
    index: int,
    center_x: float,
    center_y: float,
    half_length: float = 1.0,
    half_width: float = 0.5,
) -> BenchRectangle:
    return BenchRectangle(
        index=index,
        center_x=center_x,
        center_y=center_y,
        axis_x=1.0,
        axis_y=0.0,
        normal_x=0.0,
        normal_y=1.0,
        half_length=half_length,
        half_width=half_width,
    )


class CollisionTests(unittest.TestCase):
    def test_axis_aligned_separation_touch_and_overlap(self) -> None:
        first = axis_aligned_rectangle(0, 0.0, 0.0)
        separated = axis_aligned_rectangle(2, 3.0, 0.0)
        touching = axis_aligned_rectangle(2, 2.0, 0.0)
        overlapping = axis_aligned_rectangle(2, 1.5, 0.0)

        self.assertTrue(
            isclose(
                rectangle_separation_margin(first, separated),
                1.0,
                abs_tol=1.0e-15,
            )
        )
        self.assertTrue(
            isclose(
                rectangle_separation_margin(first, touching),
                0.0,
                abs_tol=1.0e-15,
            )
        )
        self.assertTrue(
            isclose(
                rectangle_separation_margin(first, overlapping),
                -0.5,
                abs_tol=1.0e-15,
            )
        )

    def test_adjacent_benches_are_excluded(self) -> None:
        rectangles = [
            axis_aligned_rectangle(0, 0.0, 0.0),
            axis_aligned_rectangle(1, 0.0, 0.0),
            axis_aligned_rectangle(2, 5.0, 0.0),
        ]
        clearance = minimum_nonadjacent_clearance(rectangles)
        self.assertEqual(
            (clearance.first_index, clearance.second_index),
            (0, 2),
        )
        self.assertGreater(clearance.margin, 0.0)

    def test_physical_bench_dimensions_and_initial_clearance(self) -> None:
        states = solve_handle_states(
            head_state(0.0),
            problem1_handle_distances(),
        )
        rectangles = bench_rectangles(states)
        self.assertEqual(len(rectangles), 223)
        self.assertTrue(
            isclose(rectangles[0].half_length * 2.0, HEAD_BENCH_LENGTH)
        )
        self.assertTrue(
            isclose(rectangles[1].half_length * 2.0, BODY_BENCH_LENGTH)
        )
        self.assertTrue(
            isclose(rectangles[0].half_width * 2.0, BENCH_WIDTH)
        )
        self.assertGreater(
            minimum_nonadjacent_clearance(rectangles).margin,
            0.0,
        )

    def test_problem2_collision_is_bracketed_by_integer_seconds(self) -> None:
        distances = problem1_handle_distances()
        before = minimum_nonadjacent_clearance(
            bench_rectangles(
                solve_handle_states(head_state(412.0), distances)
            )
        )
        after = minimum_nonadjacent_clearance(
            bench_rectangles(
                solve_handle_states(head_state(413.0), distances)
            )
        )
        self.assertGreater(before.margin, 0.0)
        self.assertLessEqual(after.margin, 0.0)
        self.assertEqual(
            (before.first_index, before.second_index),
            (0, 8),
        )
        self.assertEqual(
            (after.first_index, after.second_index),
            (0, 8),
        )
        before_rectangles = bench_rectangles(
            solve_handle_states(head_state(412.0), distances)
        )
        after_rectangles = bench_rectangles(
            solve_handle_states(head_state(413.0), distances)
        )
        self.assertIsNone(first_nonadjacent_collision(before_rectangles))
        self.assertEqual(
            first_nonadjacent_collision(after_rectangles),
            (0, 8),
        )


if __name__ == "__main__":
    unittest.main()
