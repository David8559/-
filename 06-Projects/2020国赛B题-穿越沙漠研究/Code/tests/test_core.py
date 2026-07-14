import sys
import unittest
from pathlib import Path


CODE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_ROOT / "src"))

from desert_core import Action, FIRST_LEVEL_CONFIG, State, Weather, advance, buy, terminal_cash
from b078_core import (
    B078_FIRST_SPECIAL_MAP,
    B078_FIRST_WEATHER,
    floyd_warshall,
    reconstruct_path,
    sample_weather,
    solve_mining_backtracking,
    solve_no_mining,
)
from graph_reconstruction import infer_edges, load_distance_matrix, validate


class GraphReconstructionTests(unittest.TestCase):
    def test_b078_level4_distance_matrix_closes_exactly(self):
        nodes, matrix = load_distance_matrix()
        edges = infer_edges(nodes, matrix)
        validate(nodes, matrix, edges)
        self.assertEqual(len(nodes), 25)
        self.assertEqual(len(edges), 40)
        self.assertIn((1, 2), edges)
        self.assertIn((1, 6), edges)
        self.assertNotIn((1, 7), edges)

    def test_floyd_reconstructs_path(self):
        adjacency = (
            (0, 1, 0, 0),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (0, 0, 1, 0),
        )
        distance, next_hop = floyd_warshall(adjacency)
        self.assertEqual(distance[0][3], 3)
        self.assertEqual(reconstruct_path(next_hop, 0, 3), [0, 1, 2, 3])


class DesertRuleTests(unittest.TestCase):
    def test_start_purchase_and_move_consumption(self):
        initial = State(day=0, node=1, water=0, food=0, cash=10_000)
        stocked = buy(FIRST_LEVEL_CONFIG, initial, 20, 20, price_multiplier=1)
        moved = advance(
            FIRST_LEVEL_CONFIG,
            stocked,
            Weather.SUNNY,
            Action.MOVE,
            target=2,
            adjacent=True,
        )
        self.assertEqual((moved.day, moved.node, moved.water, moved.food), (1, 2, 10, 6))

    def test_sandstorm_blocks_move(self):
        state = State(day=0, node=1, water=100, food=100, cash=0)
        with self.assertRaises(ValueError):
            advance(
                FIRST_LEVEL_CONFIG,
                state,
                Weather.SANDSTORM,
                Action.MOVE,
                target=2,
                adjacent=True,
            )

    def test_mining_and_terminal_refund(self):
        state = State(day=1, node=18, water=100, food=100, cash=500)
        mined = advance(
            FIRST_LEVEL_CONFIG,
            state,
            Weather.SUNNY,
            Action.MINE,
            at_mine=True,
        )
        self.assertEqual((mined.water, mined.food, mined.cash), (85, 79, 1500))
        self.assertEqual(terminal_cash(FIRST_LEVEL_CONFIG, mined), 2107.5)


class B078AlgorithmTests(unittest.TestCase):
    def test_no_mining_reproduces_paper_baseline(self):
        result = solve_no_mining(FIRST_LEVEL_CONFIG, B078_FIRST_WEATHER, distance=3)
        self.assertEqual((result.initial_water, result.initial_food, result.score), (42, 38, 9410))

    def test_mining_backtracking_reproduces_10470(self):
        result = solve_mining_backtracking(
            FIRST_LEVEL_CONFIG,
            B078_FIRST_SPECIAL_MAP,
            B078_FIRST_WEATHER,
        )
        self.assertEqual(result.score, 10470)
        self.assertEqual((result.initial_water, result.initial_food), (178, 333))
        self.assertEqual(result.final_state.day, 24)
        self.assertEqual(result.final_state.node, B078_FIRST_SPECIAL_MAP.end)

    def test_weather_sampling_is_reproducible(self):
        first = sample_weather(10, (17 / 30, 1 / 3, 1 / 10), seed=2020)
        second = sample_weather(10, (17 / 30, 1 / 3, 1 / 10), seed=2020)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
