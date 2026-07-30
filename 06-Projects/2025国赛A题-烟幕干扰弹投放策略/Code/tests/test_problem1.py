"""Regression and boundary tests for Problem 1."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from problem1_model import (  # noqa: E402
    BURST_POINT,
    BURST_TIME,
    CLOUD_LIFETIME,
    CLOUD_RADIUS,
    DROP_POINT,
    DROP_TIME,
    FY1_INITIAL,
    M1_INITIAL,
    TRUE_TARGET_CENTER,
    basic_results,
    bomb_position,
    centerline_distance,
    cloud_center,
    drone_position,
    missile_cloud_sphere_crossings,
    missile_arrival_time,
    missile_position,
    point_to_segment_distance,
)


class Problem1ModelTests(unittest.TestCase):
    def test_initial_positions(self) -> None:
        np.testing.assert_allclose(missile_position(0.0), M1_INITIAL, atol=1e-12)
        np.testing.assert_allclose(drone_position(0.0), FY1_INITIAL, atol=1e-12)

    def test_drop_point_and_release_continuity(self) -> None:
        np.testing.assert_allclose(DROP_POINT, [17620.0, 0.0, 1800.0], atol=1e-12)
        np.testing.assert_allclose(bomb_position(DROP_TIME), DROP_POINT, atol=1e-12)

    def test_burst_time_and_point(self) -> None:
        self.assertAlmostEqual(BURST_TIME, 5.1, places=12)
        np.testing.assert_allclose(
            BURST_POINT, [17188.0, 0.0, 1736.496], atol=1e-9
        )

    def test_cloud_descent(self) -> None:
        np.testing.assert_allclose(cloud_center(BURST_TIME), BURST_POINT, atol=1e-12)
        np.testing.assert_allclose(
            cloud_center(BURST_TIME + 10.0),
            BURST_POINT + [0.0, 0.0, -30.0],
            atol=1e-12,
        )

    def test_missile_arrival(self) -> None:
        arrival = missile_arrival_time()
        np.testing.assert_allclose(missile_position(arrival), [0.0, 0.0, 0.0], atol=1e-9)

    def test_analytic_cloud_sphere_exit_matches_interval_end(self) -> None:
        crossings = missile_cloud_sphere_crossings()
        result = basic_results(n_theta=360)
        interval_end = result["full_cylinder_intervals_s"][0][1]
        self.assertAlmostEqual(float(crossings[-1]), float(interval_end), places=8)

    def test_point_to_segment_projection(self) -> None:
        distance, projection = point_to_segment_distance(
            np.array([0.5, 1.0, 0.0]),
            np.array([0.0, 0.0, 0.0]),
            np.array([1.0, 0.0, 0.0]),
        )
        self.assertAlmostEqual(float(distance), 1.0)
        self.assertAlmostEqual(float(projection), 0.5)

    def test_centerline_interval_boundaries(self) -> None:
        result = basic_results(n_theta=360)
        start, end = result["centerline_intervals_s"][0]
        self.assertAlmostEqual(centerline_distance(start), CLOUD_RADIUS, places=7)
        self.assertAlmostEqual(centerline_distance(end), CLOUD_RADIUS, places=7)
        self.assertLess(centerline_distance(0.5 * (start + end)), CLOUD_RADIUS)
        self.assertGreater(centerline_distance(start - 1e-3), CLOUD_RADIUS)
        self.assertGreater(centerline_distance(end + 1e-3), CLOUD_RADIUS)

    def test_effective_interval_inside_cloud_lifetime(self) -> None:
        result = basic_results(n_theta=360)
        for start, end in result["full_cylinder_intervals_s"]:
            self.assertGreaterEqual(start, BURST_TIME)
            self.assertLessEqual(end, BURST_TIME + CLOUD_LIFETIME)
            self.assertGreater(end, start)

    def test_cylinder_sampling_convergence(self) -> None:
        coarse = basic_results(n_theta=720)["full_cylinder_duration_s"]
        fine = basic_results(n_theta=1440)["full_cylinder_duration_s"]
        self.assertLess(abs(float(coarse) - float(fine)), 2e-4)

    def test_full_cylinder_is_not_more_permissive_than_centerline(self) -> None:
        result = basic_results(n_theta=720)
        self.assertLessEqual(
            float(result["full_cylinder_duration_s"]),
            float(result["centerline_duration_s"]),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
