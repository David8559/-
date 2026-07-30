"""Constraint and interval tests for Problem 3."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from problem1_model import EffectiveInterval, cylinder_surface_points  # noqa: E402
from problem3_model import (  # noqa: E402
    MIN_DROP_GAP,
    MultiBombStrategy,
    decode_decision,
    encode_strategy,
    exact_multi_bomb_intervals,
    intervals_duration,
    merge_intervals,
    overlap_duration,
    seed_strategies,
    validate_multi_strategy,
)


class Problem3ModelTests(unittest.TestCase):
    def test_decoding_enforces_drop_gap(self) -> None:
        strategy = decode_decision(np.zeros(8))
        self.assertGreaterEqual(
            strategy.drop_times_s[1] - strategy.drop_times_s[0], MIN_DROP_GAP
        )
        self.assertGreaterEqual(
            strategy.drop_times_s[2] - strategy.drop_times_s[1], MIN_DROP_GAP
        )

    def test_seed_round_trip(self) -> None:
        for decision in seed_strategies():
            strategy = decode_decision(decision)
            recovered = decode_decision(encode_strategy(strategy))
            self.assertAlmostEqual(recovered.heading_rad, strategy.heading_rad)
            self.assertAlmostEqual(recovered.speed_mps, strategy.speed_mps)
            np.testing.assert_allclose(
                recovered.drop_times_s, strategy.drop_times_s, atol=1e-12
            )
            np.testing.assert_allclose(
                recovered.fuse_delays_s, strategy.fuse_delays_s, atol=1e-12
            )

    def test_invalid_drop_gap_is_rejected(self) -> None:
        strategy = MultiBombStrategy(
            heading_rad=0.0,
            speed_mps=100.0,
            drop_times_s=(0.0, 0.5, 2.0),
            fuse_delays_s=(1.0, 1.0, 1.0),
        )
        with self.assertRaises(ValueError):
            validate_multi_strategy(strategy)

    def test_interval_union(self) -> None:
        intervals = [
            EffectiveInterval(1.0, 3.0),
            EffectiveInterval(2.5, 4.0),
            EffectiveInterval(5.0, 6.0),
        ]
        merged = merge_intervals(intervals)
        self.assertEqual(
            merged,
            [EffectiveInterval(1.0, 4.0), EffectiveInterval(5.0, 6.0)],
        )
        self.assertAlmostEqual(intervals_duration(merged), 4.0)

    def test_overlap_duration(self) -> None:
        individual = [
            [EffectiveInterval(1.0, 3.0)],
            [EffectiveInterval(2.0, 4.0)],
            [EffectiveInterval(5.0, 6.0)],
        ]
        union = merge_intervals(
            interval for intervals in individual for interval in intervals
        )
        self.assertAlmostEqual(overlap_duration(individual, union), 1.0)

    def test_final_schedule_complete_cylinder_regression(self) -> None:
        strategy = MultiBombStrategy(
            heading_rad=np.radians(9.23648438557577),
            speed_mps=103.59649265282755,
            drop_times_s=(0.0, 1.0, 2.0),
            fuse_delays_s=(0.005101962649377057, 0.0, 0.0),
        )
        points = cylinder_surface_points(n_theta=48, n_z=5, n_r=4)
        individual, union = exact_multi_bomb_intervals(
            strategy, points, scan_step=0.01
        )
        self.assertAlmostEqual(intervals_duration(union), 6.4014, places=3)
        self.assertEqual(individual[2], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
