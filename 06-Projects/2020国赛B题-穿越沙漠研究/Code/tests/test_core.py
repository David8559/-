import sys
import unittest
from pathlib import Path


CODE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_ROOT / "src"))

from desert_core import Action, FIRST_LEVEL_CONFIG, State, Weather, advance, buy, terminal_cash
from graph_reconstruction import infer_edges, load_distance_matrix, validate


class GraphReconstructionTests(unittest.TestCase):
    def test_b078_distance_matrix_closes_exactly(self):
        nodes, matrix = load_distance_matrix()
        edges = infer_edges(nodes, matrix)
        validate(nodes, matrix, edges)
        self.assertEqual(len(nodes), 25)
        self.assertEqual(len(edges), 40)
        self.assertIn((1, 2), edges)
        self.assertIn((1, 6), edges)
        self.assertNotIn((1, 7), edges)


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


if __name__ == "__main__":
    unittest.main()

