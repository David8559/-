"""Regression tests for the cross-project mathematical-modeling utilities."""

from __future__ import annotations

import unittest

import numpy as np

from mm_common import (
    bisect_sign_change,
    constraint_violation_report,
    coordinate_refine_unit_cube,
    deletion_marginals,
    differential_evolution_maximize,
    intersection_of_unions,
    interval_measure,
    merge_intervals,
)


class IntervalTests(unittest.TestCase):
    def test_merge_and_measure_overlap_once(self) -> None:
        intervals = [(2.0, 3.0), (0.0, 1.0), (0.5, 2.0), (5.0, 5.0)]
        self.assertEqual(merge_intervals(intervals), [(0.0, 3.0), (5.0, 5.0)])
        self.assertAlmostEqual(interval_measure(intervals), 3.0)

    def test_intersection_of_unions(self) -> None:
        result = intersection_of_unions(
            [[(0.0, 2.0), (4.0, 7.0)], [(1.0, 5.0)], [(1.5, 4.5)]]
        )
        self.assertEqual(result, [(1.5, 2.0), (4.0, 4.5)])

    def test_deletion_marginals_recompute_union(self) -> None:
        marginals = deletion_marginals([[(0.0, 2.0)], [(1.0, 3.0)], [(4.0, 5.0)]])
        np.testing.assert_allclose(marginals, [1.0, 1.0, 1.0])

    def test_invalid_interval_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            merge_intervals([(2.0, 1.0)])


class RootTests(unittest.TestCase):
    def test_bracketed_root_and_final_bracket(self) -> None:
        result = bisect_sign_change(lambda x: x * x - 2.0, 1.0, 2.0)
        self.assertAlmostEqual(result.root, np.sqrt(2.0), places=9)
        self.assertLessEqual(result.left, np.sqrt(2.0))
        self.assertGreaterEqual(result.right, np.sqrt(2.0))

    def test_endpoint_root(self) -> None:
        result = bisect_sign_change(lambda x: x - 1.0, 1.0, 3.0)
        self.assertEqual(result.iterations, 0)
        self.assertEqual(result.root, 1.0)

    def test_nonbracketed_root_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            bisect_sign_change(lambda x: x * x + 1.0, -1.0, 1.0)


class OptimizationTests(unittest.TestCase):
    @staticmethod
    def objective(x: np.ndarray) -> float:
        return -float(np.sum((x - np.array([0.25, 0.70])) ** 2))

    def test_differential_evolution_is_seed_reproducible(self) -> None:
        first = differential_evolution_maximize(
            self.objective, dimension=2, seed=17, population_size=24, generations=70
        )
        second = differential_evolution_maximize(
            self.objective, dimension=2, seed=17, population_size=24, generations=70
        )
        np.testing.assert_allclose(first.decision, second.decision)
        self.assertGreater(first.score, -1e-5)

    def test_feasibility_and_incumbent_guard(self) -> None:
        incumbent = np.array([0.2, 0.3])
        result = differential_evolution_maximize(
            lambda x: float(np.sum(x)),
            dimension=2,
            seed=9,
            population_size=20,
            generations=40,
            feasible=lambda x: bool(np.sum(x) <= 0.5 + 1e-12),
            incumbent=incumbent,
        )
        self.assertLessEqual(float(np.sum(result.decision)), 0.5 + 1e-12)
        self.assertGreaterEqual(result.score, float(np.sum(incumbent)) - 1e-12)

    def test_coordinate_refinement_improves_without_losing_feasibility(self) -> None:
        result = coordinate_refine_unit_cube(
            [0.0, 0.0],
            self.objective,
            feasible=lambda x: bool(np.sum(x) <= 1.0),
            initial_step=0.2,
        )
        self.assertGreater(result.score, self.objective(np.array([0.0, 0.0])))
        self.assertLessEqual(float(np.sum(result.decision)), 1.0 + 1e-12)


class ValidationTests(unittest.TestCase):
    def test_constraint_report_components(self) -> None:
        report = constraint_violation_report(
            [1.2, -0.1],
            inequalities=[-2.0, 0.03],
            equalities=[-0.02],
            lower_bounds=[0.0, 0.0],
            upper_bounds=[1.0, 1.0],
            tolerance=0.01,
        )
        self.assertAlmostEqual(report.maximum, 0.2)
        self.assertAlmostEqual(report.inequality, 0.03)
        self.assertAlmostEqual(report.equality, 0.02)
        self.assertAlmostEqual(report.lower_bound, 0.1)
        self.assertFalse(report.feasible)

    def test_empty_constraints_are_feasible(self) -> None:
        report = constraint_violation_report([0.4, 0.6])
        self.assertTrue(report.feasible)
        self.assertEqual(report.maximum, 0.0)


if __name__ == "__main__":
    unittest.main()
