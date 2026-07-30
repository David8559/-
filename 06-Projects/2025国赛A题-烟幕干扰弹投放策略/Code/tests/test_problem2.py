"""Regression, constraint, and geometry tests for Problem 2."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from problem1_model import cylinder_surface_points  # noqa: E402
from problem2_model import (  # noqa: E402
    MAX_FUSE_DELAY,
    MISSILE_ARRIVAL_TIME,
    Strategy,
    baseline_problem1_strategy,
    burst_point,
    centerline_proxy_duration,
    cloud_center_for,
    decision_from_strategy,
    drop_point,
    exact_full_cylinder_intervals,
    interval_duration,
    sampled_effective_intervals,
    strategy_from_decision,
    validate_strategy,
)


class Problem2ModelTests(unittest.TestCase):
    def test_baseline_points_match_problem1(self) -> None:
        strategy = baseline_problem1_strategy()
        np.testing.assert_allclose(
            drop_point(strategy), [17620.0, 0.0, 1800.0], atol=1e-10
        )
        np.testing.assert_allclose(
            burst_point(strategy), [17188.0, 0.0, 1736.496], atol=1e-9
        )

    def test_decision_round_trip(self) -> None:
        strategy = Strategy(
            heading_rad=-2.8,
            speed_mps=95.0,
            drop_time_s=2.4,
            fuse_delay_s=4.2,
        )
        recovered = strategy_from_decision(decision_from_strategy(strategy))
        self.assertAlmostEqual(recovered.heading_rad, strategy.heading_rad)
        self.assertAlmostEqual(recovered.speed_mps, strategy.speed_mps)
        self.assertAlmostEqual(recovered.drop_time_s, strategy.drop_time_s)
        self.assertAlmostEqual(recovered.fuse_delay_s, strategy.fuse_delay_s)

    def test_decision_parameterization_is_feasible(self) -> None:
        for decision in (
            [-np.pi, 70.0, 0.0, 0.0],
            [0.0, 140.0, MISSILE_ARRIVAL_TIME, 1.0],
            [2.5, 100.0, 8.0, 0.6],
        ):
            strategy = strategy_from_decision(decision)
            validate_strategy(strategy)
            self.assertGreaterEqual(strategy.drop_time_s, 0.0)
            self.assertLessEqual(strategy.fuse_delay_s, MAX_FUSE_DELAY)
            self.assertGreaterEqual(burst_point(strategy)[2], -1e-9)

    def test_invalid_speed_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_strategy(Strategy(0.0, 60.0, 1.0, 1.0))

    def test_cloud_descends_three_metres_per_second(self) -> None:
        strategy = baseline_problem1_strategy()
        start = cloud_center_for(strategy, strategy.burst_time_s)
        later = cloud_center_for(strategy, strategy.burst_time_s + 7.0)
        np.testing.assert_allclose(later - start, [0.0, 0.0, -21.0])

    def test_sampled_interval_interpolation(self) -> None:
        times = np.array([0.0, 1.0, 2.0, 3.0])
        distances = np.array([12.0, 8.0, 8.0, 12.0])
        intervals = sampled_effective_intervals(times, distances, radius=10.0)
        self.assertEqual(len(intervals), 1)
        self.assertAlmostEqual(intervals[0].start, 0.5)
        self.assertAlmostEqual(intervals[0].end, 2.5)

    def test_baseline_full_cylinder_duration_regression(self) -> None:
        points = cylinder_surface_points(n_theta=360)
        intervals = exact_full_cylinder_intervals(
            baseline_problem1_strategy(), points, scan_step=0.01
        )
        self.assertAlmostEqual(interval_duration(intervals), 1.391643, places=5)

    def test_baseline_proxy_is_close_to_centerline_result(self) -> None:
        decision = decision_from_strategy(baseline_problem1_strategy())
        self.assertAlmostEqual(centerline_proxy_duration(decision, step=0.01), 1.435, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
