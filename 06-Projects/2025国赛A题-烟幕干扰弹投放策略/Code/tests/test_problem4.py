"""Constraint and geometry tests for Problem 4."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from problem4_model import (  # noqa: E402
    DECISION_DIMENSION,
    DRONE_IDS,
    DRONE_INITIALS,
    DroneBombStrategy,
    MultiDroneStrategy,
    burst_point,
    cylinder_surface_points,
    decode_decision,
    drop_point,
    encode_strategy,
    exact_multi_drone_intervals,
    intervals_duration,
    seed_strategies,
    validate_bomb_strategy,
)


class Problem4ModelTests(unittest.TestCase):
    def test_decision_dimension_and_drone_order(self) -> None:
        strategy = decode_decision(np.full(DECISION_DIMENSION, 0.25))
        self.assertEqual(tuple(bomb.drone_id for bomb in strategy.bombs), DRONE_IDS)

    def test_seed_round_trip(self) -> None:
        for decision in seed_strategies():
            strategy = decode_decision(decision)
            recovered = decode_decision(encode_strategy(strategy))
            for expected, actual in zip(strategy.bombs, recovered.bombs):
                self.assertEqual(expected.drone_id, actual.drone_id)
                self.assertAlmostEqual(expected.heading_rad, actual.heading_rad)
                self.assertAlmostEqual(expected.speed_mps, actual.speed_mps)
                self.assertAlmostEqual(expected.drop_time_s, actual.drop_time_s)
                self.assertAlmostEqual(expected.fuse_delay_s, actual.fuse_delay_s)

    def test_zero_drop_points_are_drone_initials(self) -> None:
        for drone_id in DRONE_IDS:
            strategy = DroneBombStrategy(drone_id, 0.0, 100.0, 0.0, 0.0)
            np.testing.assert_allclose(
                drop_point(strategy), DRONE_INITIALS[drone_id], atol=1e-12
            )
            np.testing.assert_allclose(
                burst_point(strategy), DRONE_INITIALS[drone_id], atol=1e-12
            )

    def test_burst_vertical_displacement(self) -> None:
        strategy = DroneBombStrategy("FY2", 0.0, 100.0, 1.0, 2.0)
        expected = np.array([12300.0, 1400.0, 1400.0 - 19.6])
        np.testing.assert_allclose(burst_point(strategy), expected, atol=1e-12)

    def test_invalid_low_altitude_fuse_is_rejected(self) -> None:
        strategy = DroneBombStrategy("FY3", 0.0, 100.0, 0.0, 20.0)
        with self.assertRaises(ValueError):
            validate_bomb_strategy(strategy)

    def test_multi_strategy_requires_all_three_drones(self) -> None:
        decision = np.full(DECISION_DIMENSION, 0.25)
        strategy = decode_decision(decision)
        self.assertIsInstance(strategy, MultiDroneStrategy)
        self.assertEqual(len(strategy.bombs), 3)

    def test_reported_strategy_regression(self) -> None:
        strategy = MultiDroneStrategy(
            (
                DroneBombStrategy(
                    "FY1",
                    np.radians(6.945852317258661),
                    140.0,
                    0.0,
                    0.7390456916109627,
                ),
                DroneBombStrategy(
                    "FY2",
                    np.radians(280.19192130188935),
                    119.7465028251595,
                    5.612725805244697,
                    5.869072353881609,
                ),
                DroneBombStrategy(
                    "FY3",
                    np.radians(78.24891581523705),
                    132.66917535866548,
                    21.390227030047182,
                    2.422908693922376,
                ),
            )
        )
        target_points = cylinder_surface_points(n_theta=48, n_z=5, n_r=4)
        individual, union = exact_multi_drone_intervals(
            strategy, target_points, scan_step=0.01
        )
        self.assertEqual([len(intervals) for intervals in individual], [1, 1, 1])
        self.assertEqual(len(union), 3)
        # The compact 48-angle test grid is intentionally coarser than the
        # 1440-angle reporting grid, but it must preserve the same strategy basin.
        self.assertAlmostEqual(intervals_duration(union), 11.63332987867295, places=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
