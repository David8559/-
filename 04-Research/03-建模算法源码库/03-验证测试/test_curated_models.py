"""Persistent smoke tests for the 25 callable Python model-library branches."""

from __future__ import annotations

import sys
import unittest
from importlib.util import find_spec
from pathlib import Path

import numpy as np

LIBRARY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LIBRARY / "01-Python实现代码" / "模型完整代码"))
sys.path.insert(0, str(LIBRARY / "01-Python实现代码" / "优化求解代码"))

from evaluation_models import (  # noqa: E402
    ahp_weights,
    entropy_weights,
    fuzzy_comprehensive_evaluation,
    grey_relational_grade,
    topsis,
)
from forecast_models import (  # noqa: E402
    arima_forecast,
    gm11,
    linear_regression_ols,
    simple_exponential_smoothing,
)
from metaheuristics import (  # noqa: E402
    ant_colony_tsp,
    genetic_algorithm,
    particle_swarm,
    simulated_annealing,
)
from network_dynamics_models import (  # noqa: E402
    diffuse_1d_explicit,
    maximum_flow_minimum_cut,
    minimum_spanning_tree,
    mm1_metrics,
    shortest_path,
    simulate_logistic,
    simulate_sir,
)
from optimization_models import (  # noqa: E402
    greedy_interval_scheduling,
    solve_linear_program,
    solve_milp,
    weighted_sum_multiobjective,
    zero_one_knapsack,
)

HAS_NETWORKX = find_spec("networkx") is not None
HAS_SCIPY = find_spec("scipy") is not None
HAS_STATSMODELS = find_spec("statsmodels") is not None


class EvaluationModelTests(unittest.TestCase):
    def test_five_evaluation_branches(self) -> None:
        weights, ratio, consistent = ahp_weights([[1.0, 2.0], [0.5, 1.0]])
        np.testing.assert_allclose(weights, [2 / 3, 1 / 3])
        self.assertEqual(ratio, 0.0)
        self.assertTrue(consistent)

        entropy = entropy_weights([[1.0, 1.0], [2.0, 4.0], [4.0, 8.0]])
        self.assertAlmostEqual(float(entropy.sum()), 1.0)

        scores, order = topsis([[1.0, 3.0], [2.0, 2.0], [3.0, 1.0]], [0.5, 0.5])
        self.assertEqual(scores.shape, (3,))
        self.assertEqual(set(order.tolist()), {0, 1, 2})

        grades = grey_relational_grade([[1.0, 2.0], [0.0, 0.0]], [1.0, 2.0])
        self.assertAlmostEqual(float(grades[0]), 1.0)

        fuzzy = fuzzy_comprehensive_evaluation(
            [0.4, 0.6], [[0.8, 0.2], [0.3, 0.7]]
        )
        np.testing.assert_allclose(fuzzy, [0.5, 0.5])


class ForecastModelTests(unittest.TestCase):
    def test_three_numpy_forecast_branches(self) -> None:
        beta, fitted, residual = linear_regression_ols([0.0, 1.0, 2.0], [1.0, 3.0, 5.0])
        np.testing.assert_allclose(beta, [1.0, 2.0], atol=1e-12)
        np.testing.assert_allclose(fitted, [1.0, 3.0, 5.0], atol=1e-12)
        np.testing.assert_allclose(residual, 0.0, atol=1e-12)

        smoothed, forecast = simple_exponential_smoothing([1.0, 3.0, 5.0], 0.5)
        self.assertTrue(np.isnan(smoothed[0]))
        self.assertAlmostEqual(forecast, 3.5)

        grey = gm11([2.0, 2.4, 2.9, 3.5, 4.2], horizon=2)
        self.assertEqual(np.asarray(grey["forecast"]).shape, (2,))
        self.assertTrue(np.isfinite(grey["posterior_ratio_C"]))

    @unittest.skipUnless(HAS_STATSMODELS, "statsmodels is not installed")
    def test_arima_branch(self) -> None:
        series = 10.0 + 0.2 * np.arange(36) + np.sin(np.arange(36) / 3.0)
        arima = arima_forecast(series, (1, 1, 0), 2)
        self.assertEqual(np.asarray(arima["mean"]).shape, (2,))
        self.assertEqual(np.asarray(arima["interval_95"]).shape, (2, 2))


class NetworkDynamicsTests(unittest.TestCase):
    @unittest.skipUnless(HAS_NETWORKX, "networkx is not installed")
    def test_three_networkx_branches(self) -> None:
        edges = [("a", "b", 1.0), ("b", "c", 2.0), ("a", "c", 5.0)]
        path, length = shortest_path(edges, "a", "c")
        self.assertEqual(path, ["a", "b", "c"])
        self.assertEqual(length, 3.0)

        tree, weight = minimum_spanning_tree(edges)
        self.assertEqual(len(tree), 2)
        self.assertEqual(weight, 3.0)

        flow = maximum_flow_minimum_cut(
            [("s", "a", 3.0), ("a", "t", 2.0), ("s", "t", 1.0)], "s", "t"
        )
        self.assertEqual(flow["max_flow"], 3.0)
        self.assertEqual(flow["min_cut"], 3.0)

    def test_mm1_and_explicit_diffusion_branches(self) -> None:
        queue = mm1_metrics(2.0, 3.0)
        self.assertAlmostEqual(queue["utilization_rho"], 2 / 3)
        self.assertAlmostEqual(queue["mean_time_system_W"], 1.0)

        diffusion = diffuse_1d_explicit([0.0, 0.0, 1.0, 0.0, 0.0], 1.0, 1.0, 0.25, 3)
        self.assertEqual(diffusion.shape, (4, 5))
        np.testing.assert_allclose(diffusion[:, [0, -1]], 0.0)

    @unittest.skipUnless(HAS_SCIPY, "scipy is not installed")
    def test_two_scipy_dynamics_branches(self) -> None:
        times = np.linspace(0.0, 2.0, 9)
        sir = simulate_sir(0.3, 0.1, (990.0, 10.0, 0.0), times)
        self.assertTrue(sir.success)
        np.testing.assert_allclose(sir.y.sum(axis=0), 1000.0, rtol=1e-8)

        logistic = simulate_logistic(0.4, 100.0, 10.0, times)
        self.assertTrue(logistic.success)
        self.assertGreater(logistic.y[0, -1], logistic.y[0, 0])


class OptimizationModelTests(unittest.TestCase):
    @unittest.skipUnless(HAS_SCIPY, "scipy is not installed")
    def test_two_scipy_optimization_branches(self) -> None:
        linear = solve_linear_program([-1.0], a_ub=[[1.0]], b_ub=[2.0], bounds=[(0.0, None)])
        self.assertAlmostEqual(float(linear["x"][0]), 2.0)

        from scipy.optimize import Bounds

        integer = solve_milp(
            [-1.0],
            [[1.0]],
            [-np.inf],
            [2.5],
            integrality=[1],
            variable_bounds=Bounds([0.0], [np.inf]),
        )
        self.assertAlmostEqual(float(integer["x"][0]), 2.0)

    def test_three_dependency_free_optimization_branches(self) -> None:
        scalar = weighted_sum_multiobjective(
            [lambda x: x[0] ** 2, lambda x: (x[0] - 2.0) ** 2], [0.25, 0.75], [1.0]
        )
        self.assertAlmostEqual(scalar, 1.0)

        value, chosen = zero_one_knapsack([6.0, 10.0, 12.0], [1, 2, 3], 5)
        self.assertEqual(value, 22.0)
        self.assertEqual(chosen, [1, 2])

        selected = greedy_interval_scheduling(
            [(0.0, 2.0, "a"), (1.0, 3.0, "b"), (2.0, 4.0, "c")]
        )
        self.assertEqual([item[2] for item in selected], ["a", "c"])


class MetaheuristicTests(unittest.TestCase):
    @staticmethod
    def sphere(x: np.ndarray) -> float:
        return float(np.sum(x**2))

    def test_four_metaheuristic_branches(self) -> None:
        bounds = [[-2.0, 2.0], [-2.0, 2.0]]
        _, ga_value, _ = genetic_algorithm(
            self.sphere, bounds, population_size=30, generations=50, seed=11
        )
        _, pso_value, _ = particle_swarm(
            self.sphere, bounds, particles=25, iterations=50, seed=11
        )
        _, sa_value, _ = simulated_annealing(
            self.sphere, [1.0, -1.0], bounds, iterations=400, seed=11
        )
        self.assertLess(ga_value, 0.05)
        self.assertLess(pso_value, 0.01)
        self.assertLess(sa_value, 0.2)

        square = np.array(
            [[0.0, 1.0, np.sqrt(2.0), 1.0], [1.0, 0.0, 1.0, np.sqrt(2.0)],
             [np.sqrt(2.0), 1.0, 0.0, 1.0], [1.0, np.sqrt(2.0), 1.0, 0.0]]
        )
        route, length, _ = ant_colony_tsp(square, ants=15, iterations=30, seed=11)
        self.assertEqual(len(route), 5)
        self.assertAlmostEqual(length, 4.0)


if __name__ == "__main__":
    unittest.main()
