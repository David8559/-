"""Auditable core rules for the 2020 CUMCM B desert game.

This module intentionally separates rules from a particular solver. It can be
used by dynamic programming, Monte Carlo simulation, or an MDP implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Weather(str, Enum):
    SUNNY = "sunny"
    HOT = "hot"
    SANDSTORM = "sandstorm"


class Action(str, Enum):
    REST = "rest"
    MOVE = "move"
    MINE = "mine"


@dataclass(frozen=True)
class GameConfig:
    deadline: int
    capacity: int
    water_weight: int
    food_weight: int
    water_price: int
    food_price: int
    mine_income: int
    consumption: dict[Weather, tuple[int, int]]

    def load(self, water: int, food: int) -> int:
        return water * self.water_weight + food * self.food_weight


@dataclass(frozen=True)
class State:
    day: int
    node: int
    water: int
    food: int
    cash: int


@dataclass(frozen=True)
class Transition:
    state: State
    action: Action
    target: int | None = None


def buy(
    config: GameConfig,
    state: State,
    water: int,
    food: int,
    *,
    price_multiplier: int,
) -> State:
    """Buy non-negative integer boxes at start (1x) or village (2x)."""
    if water < 0 or food < 0:
        raise ValueError("purchase quantities must be non-negative")
    new_water, new_food = state.water + water, state.food + food
    cost = price_multiplier * (water * config.water_price + food * config.food_price)
    if cost > state.cash:
        raise ValueError("insufficient cash")
    if config.load(new_water, new_food) > config.capacity:
        raise ValueError("capacity exceeded")
    return State(state.day, state.node, new_water, new_food, state.cash - cost)


def advance(
    config: GameConfig,
    state: State,
    weather: Weather,
    action: Action,
    *,
    target: int | None = None,
    adjacent: bool = False,
    at_mine: bool = False,
) -> State:
    """Advance one day; the caller supplies graph and node-type facts explicitly."""
    if state.day >= config.deadline:
        raise ValueError("deadline reached")
    if action is Action.MOVE:
        if weather is Weather.SANDSTORM:
            raise ValueError("cannot move during a sandstorm")
        if target is None or not adjacent:
            raise ValueError("move target must be adjacent")
        factor = 2
        next_node = target
        income = 0
    elif action is Action.MINE:
        if not at_mine:
            raise ValueError("mining is only legal at a mine")
        factor = 3
        next_node = state.node
        income = config.mine_income
    else:
        factor = 1
        next_node = state.node
        income = 0
    base_water, base_food = config.consumption[weather]
    water_cost, food_cost = factor * base_water, factor * base_food
    if state.water < water_cost or state.food < food_cost:
        raise ValueError("insufficient resources")
    return State(
        day=state.day + 1,
        node=next_node,
        water=state.water - water_cost,
        food=state.food - food_cost,
        cash=state.cash + income,
    )


def terminal_cash(config: GameConfig, state: State) -> float:
    """Unused resources are refunded at half the base price at the destination."""
    return state.cash + 0.5 * (
        state.water * config.water_price + state.food * config.food_price
    )


FIRST_LEVEL_CONFIG = GameConfig(
    deadline=30,
    capacity=1200,
    water_weight=3,
    food_weight=2,
    water_price=5,
    food_price=10,
    mine_income=1000,
    consumption={
        Weather.SUNNY: (5, 7),
        Weather.HOT: (8, 6),
        Weather.SANDSTORM: (10, 10),
    },
)

