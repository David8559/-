"""Tests for the problem-4 spiral–biarc–spiral path."""

from __future__ import annotations

import sys
import unittest
from math import hypot, isclose
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR / "src"))

from turning_path import (  # noqa: E402
    TURNING_RADIUS,
    build_turning_geometry,
    fixed_endpoint_arc_length,
    path_point,
)


class TurningPathTests(unittest.TestCase):
    def setUp(self) -> None:
        self.geometry = build_turning_geometry()

    def test_endpoint_and_radius_ratio_geometry(self) -> None:
        geometry = self.geometry
        self.assertTrue(
            isclose(
                hypot(geometry.entry_x, geometry.entry_y),
                TURNING_RADIUS,
                abs_tol=1.0e-13,
            )
        )
        self.assertTrue(
            isclose(geometry.exit_x, -geometry.entry_x, abs_tol=1.0e-14)
        )
        self.assertTrue(
            isclose(geometry.exit_y, -geometry.entry_y, abs_tol=1.0e-14)
        )
        self.assertTrue(
            isclose(
                geometry.first_radius / geometry.second_radius,
                2.0,
                abs_tol=1.0e-14,
            )
        )
        center_distance = hypot(
            geometry.second_center_x - geometry.first_center_x,
            geometry.second_center_y - geometry.first_center_y,
        )
        self.assertTrue(
            isclose(
                center_distance,
                geometry.radius_sum,
                abs_tol=1.0e-13,
            )
        )

    def test_path_is_position_and_tangent_continuous(self) -> None:
        geometry = self.geometry
        joins = (0.0, geometry.first_length, geometry.total_arc_length)
        for join in joins:
            left = path_point(join - 1.0e-7, geometry)
            right = path_point(join + 1.0e-7, geometry)
            self.assertLess(hypot(left.x - right.x, left.y - right.y), 3e-7)
            self.assertLess(
                hypot(
                    left.tangent_x - right.tangent_x,
                    left.tangent_y - right.tangent_y,
                ),
                3e-7,
            )

    def test_tangent_is_unit_length(self) -> None:
        geometry = self.geometry
        samples = (
            -100.0,
            0.0,
            0.5 * geometry.first_length,
            geometry.first_length,
            0.5 * (
                geometry.first_length + geometry.total_arc_length
            ),
            geometry.total_arc_length,
            100.0,
        )
        for s in samples:
            point = path_point(s, geometry)
            self.assertTrue(
                isclose(
                    hypot(point.tangent_x, point.tangent_y),
                    1.0,
                    abs_tol=2.0e-14,
                )
            )

    def test_circular_turn_stays_inside_turning_space(self) -> None:
        geometry = self.geometry
        for index in range(1001):
            s = geometry.total_arc_length * index / 1000.0
            point = path_point(s, geometry)
            self.assertLessEqual(
                hypot(point.x, point.y),
                TURNING_RADIUS + 2.0e-13,
            )

    def test_fixed_endpoint_radius_split_does_not_change_length(self) -> None:
        baseline = self.geometry.total_arc_length
        for fraction in (0.2, 0.4, 0.5, 2.0 / 3.0, 0.8):
            self.assertTrue(
                isclose(
                    fixed_endpoint_arc_length(fraction, self.geometry),
                    baseline,
                    abs_tol=2.0e-14,
                )
            )


if __name__ == "__main__":
    unittest.main()
