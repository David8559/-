"""Constraint and geometry tests for Problem 5."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from problem5_model import (  # noqa: E402
    DRONE_IDS,
    DRONE_INITIALS,
    MISSILE_ARRIVAL_TIMES,
    MISSILE_IDS,
    BombStrategy,
    DronePlan,
    FleetStrategy,
    burst_point,
    coverage_durations,
    cylinder_surface_points,
    decode_pair_decision,
    drop_point,
    exact_full_intervals_for_bomb,
    intersect_interval_sets,
    missile_position_for,
    plan_is_drop_feasible,
    validate_drone_plan,
    validate_fleet_strategy,
)
from problem1_model import EffectiveInterval  # noqa: E402


class Problem5ModelTests(unittest.TestCase):
    def test_interval_intersection(self) -> None:
        result = intersect_interval_sets(
            [
                [EffectiveInterval(1.0, 5.0), EffectiveInterval(8.0, 9.0)],
                [EffectiveInterval(3.0, 6.0), EffectiveInterval(8.5, 10.0)],
                [EffectiveInterval(4.0, 7.0), EffectiveInterval(8.2, 8.8)],
            ]
        )
        self.assertEqual(
            result,
            [EffectiveInterval(4.0, 5.0), EffectiveInterval(8.5, 8.8)],
        )

    def test_all_objects_are_registered(self) -> None:
        self.assertEqual(DRONE_IDS, ("FY1", "FY2", "FY3", "FY4", "FY5"))
        self.assertEqual(MISSILE_IDS, ("M1", "M2", "M3"))

    def test_missiles_reach_false_target(self) -> None:
        for missile_id in MISSILE_IDS:
            np.testing.assert_allclose(
                missile_position_for(missile_id, MISSILE_ARRIVAL_TIMES[missile_id]),
                np.zeros(3),
                atol=1e-10,
            )

    def test_pair_parameterization_is_feasible(self) -> None:
        for drone_id in DRONE_IDS:
            for missile_id in MISSILE_IDS:
                strategy = decode_pair_decision(
                    np.array([0.25, 0.50, 0.60, 0.40]),
                    drone_id,
                    missile_id,
                )
                self.assertGreaterEqual(strategy.drop_time_s, 0.0)
                self.assertLessEqual(
                    strategy.burst_time_s,
                    MISSILE_ARRIVAL_TIMES[missile_id],
                )

    def test_zero_drop_point_is_drone_initial(self) -> None:
        strategy = BombStrategy("FY5", "M2", 0.3, 100.0, 0.0, 0.0)
        np.testing.assert_allclose(
            drop_point(strategy), DRONE_INITIALS["FY5"], atol=1e-12
        )
        np.testing.assert_allclose(
            burst_point(strategy), DRONE_INITIALS["FY5"], atol=1e-12
        )

    def test_drop_gap_check(self) -> None:
        bombs = (
            BombStrategy("FY4", "M1", 0.2, 100.0, 1.0, 1.0),
            BombStrategy("FY4", "M2", 0.2, 100.0, 1.5, 1.0),
        )
        self.assertFalse(plan_is_drop_feasible(bombs))

    def test_plan_rejects_heading_change(self) -> None:
        plan = DronePlan(
            "FY1",
            (
                BombStrategy("FY1", "M1", 0.2, 100.0, 0.0, 1.0),
                BombStrategy("FY1", "M2", 0.3, 100.0, 2.0, 1.0),
            ),
        )
        with self.assertRaises(ValueError):
            validate_drone_plan(plan)

    def test_final_strategy_is_feasible_and_reproduces_total(self) -> None:
        specifications = {
            "FY1": (
                9.236484,
                103.596493,
                (("M1", 0.0, 0.005102), ("M1", 1.0, 0.0)),
            ),
            "FY2": (
                280.19192130188935,
                119.7465028251595,
                (
                    ("M2", 5.143516652262085, 3.0798293988838052),
                    ("M1", 6.183406181298409, 5.497307360692917),
                ),
            ),
            "FY3": (
                88.90258296798298,
                124.82421440185331,
                (
                    ("M3", 19.79212684488296, 3.321241498187949),
                    ("M1", 21.052143731163717, 3.597930066963999),
                    ("M2", 24.10870664243407, 2.1534035444841346),
                ),
            ),
            "FY4": (
                306.5108628896607,
                138.77828180296348,
                (("M2", 4.666303731936562, 9.563953424618248),),
            ),
            "FY5": (
                115.19024800624231,
                138.89976278423063,
                (("M3", 12.246621631583992, 0.5767295529530098),),
            ),
        }
        plans = []
        for drone_id, (heading_deg, speed_mps, records) in specifications.items():
            bombs = tuple(
                BombStrategy(
                    drone_id,
                    missile_id,
                    float(np.deg2rad(heading_deg)),
                    speed_mps,
                    drop_time_s,
                    fuse_delay_s,
                )
                for missile_id, drop_time_s, fuse_delay_s in records
            )
            plans.append(DronePlan(drone_id, bombs))
        fleet = FleetStrategy(tuple(plans))
        validate_fleet_strategy(fleet)

        target_points = cylinder_surface_points(n_theta=48, n_z=5, n_r=4)
        durations = coverage_durations(
            (
                bomb,
                exact_full_intervals_for_bomb(
                    bomb, target_points, scan_step=0.02
                ),
            )
            for bomb in fleet.bombs
        )
        self.assertTrue(all(value > 6.0 for value in durations.values()))
        self.assertGreater(sum(durations.values()), 30.32)
        self.assertLess(sum(durations.values()), 30.34)


if __name__ == "__main__":
    unittest.main(verbosity=2)
