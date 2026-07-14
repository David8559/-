"""Clean-room implementation of the core algorithms described in paper B078.

The paper splits the deterministic problem into two cases:

1. no mining: Floyd shortest path + minimum required initial purchase;
2. mining: bounded depth-first search among special nodes, with retroactive
   village replenishment and pruning.

This module preserves that structure while replacing the scan-damaged C++ and
MATLAB listings with typed, testable Python.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, replace
from math import inf
from typing import Iterable, Sequence

from desert_core import GameConfig, Weather


@dataclass(frozen=True)
class SpecialMap:
    names: tuple[str, ...]
    kinds: tuple[str, ...]
    distances: tuple[tuple[int, ...], ...]
    start: int
    end: int

    def allowed_destinations(self, node: int) -> tuple[int, ...]:
        """B078's directed decision table, expressed by semantic node type."""
        allowed = {
            "start": {"village", "mine", "end"},
            "village": {"mine", "end"},
            "mine": {"village", "end"},
            "end": set(),
        }[self.kinds[node]]
        return tuple(i for i, kind in enumerate(self.kinds) if kind in allowed)


@dataclass(frozen=True)
class SearchState:
    day: int
    node: int
    water: int
    food: int
    cash: int
    # Capacity that may still be filled retroactively at the most recent village.
    village_reserve: int


@dataclass(frozen=True)
class AuditRow:
    day: int
    location: str
    action: str
    weather: str
    cash: int
    water: int
    food: int


@dataclass(frozen=True)
class StrategyResult:
    score: float
    initial_water: int
    initial_food: int
    final_state: SearchState
    audit: tuple[AuditRow, ...]


def floyd_warshall(adjacency: Sequence[Sequence[int]]) -> tuple[list[list[float]], list[list[int | None]]]:
    """Return all-pairs shortest distances and a next-hop matrix."""
    n = len(adjacency)
    distance = [[0.0 if i == j else (1.0 if adjacency[i][j] else inf) for j in range(n)] for i in range(n)]
    next_hop: list[list[int | None]] = [
        [j if i != j and adjacency[i][j] else None for j in range(n)] for i in range(n)
    ]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                candidate = distance[i][k] + distance[k][j]
                if candidate < distance[i][j]:
                    distance[i][j] = candidate
                    next_hop[i][j] = next_hop[i][k]
    return distance, next_hop


def reconstruct_path(next_hop: Sequence[Sequence[int | None]], start: int, end: int) -> list[int]:
    if start == end:
        return [start]
    if next_hop[start][end] is None:
        return []
    path = [start]
    while start != end:
        next_node = next_hop[start][end]
        if next_node is None:
            return []
        start = next_node
        path.append(start)
    return path


def _consume(
    config: GameConfig,
    state: SearchState,
    water_need: int,
    food_need: int,
) -> SearchState | None:
    """Consume resources, buying any shortage from the last village at 2x.

    This is the readable equivalent of B078's `nm` variable: after leaving a
    village, unused capacity is retained as a reserve. If a later leg reveals a
    shortage, the algorithm backtracks conceptually and purchases exactly that
    shortage at the village.
    """
    water_shortage = max(0, water_need - state.water)
    food_shortage = max(0, food_need - state.food)
    reserve_weight = water_shortage * config.water_weight + food_shortage * config.food_weight
    purchase_cost = 2 * (
        water_shortage * config.water_price + food_shortage * config.food_price
    )
    if reserve_weight > state.village_reserve or purchase_cost > state.cash:
        return None
    return replace(
        state,
        water=max(0, state.water - water_need),
        food=max(0, state.food - food_need),
        cash=state.cash - purchase_cost,
        village_reserve=state.village_reserve - reserve_weight,
    )


def _travel(
    config: GameConfig,
    special_map: SpecialMap,
    weather: Sequence[Weather],
    state: SearchState,
    target: int,
    audit: tuple[AuditRow, ...],
) -> tuple[SearchState, tuple[AuditRow, ...]] | None:
    steps_required = special_map.distances[state.node][target]
    steps = 0
    current = state
    rows = list(audit)
    while steps < steps_required:
        if current.day >= min(config.deadline, len(weather)):
            return None
        today = weather[current.day]
        moving = today is not Weather.SANDSTORM
        factor = 2 if moving else 1
        base_water, base_food = config.consumption[today]
        consumed = _consume(config, current, factor * base_water, factor * base_food)
        if consumed is None:
            return None
        if moving:
            steps += 1
        arrived = steps == steps_required
        current = replace(consumed, day=consumed.day + 1, node=target if arrived else state.node)
        rows.append(
            AuditRow(
                day=current.day,
                location=special_map.names[target] if arrived else f"前往{special_map.names[target]}({steps}/{steps_required})",
                action="移动" if moving else "沙暴停留",
                weather=today.value,
                cash=current.cash,
                water=current.water,
                food=current.food,
            )
        )
    if special_map.kinds[target] == "village":
        free_capacity = config.capacity - config.load(current.water, current.food)
        current = replace(current, village_reserve=free_capacity)
    return current, tuple(rows)


def minimum_travel_requirements(
    config: GameConfig,
    weather: Sequence[Weather],
    distance: int,
) -> tuple[int, int, int]:
    """Resource boxes and calendar days needed to complete `distance` moves."""
    steps = water = food = day = 0
    while steps < distance:
        if day >= min(config.deadline, len(weather)):
            raise ValueError("the destination cannot be reached before the deadline")
        today = weather[day]
        moving = today is not Weather.SANDSTORM
        factor = 2 if moving else 1
        base_water, base_food = config.consumption[today]
        water += factor * base_water
        food += factor * base_food
        steps += int(moving)
        day += 1
    return water, food, day


def solve_no_mining(
    config: GameConfig,
    weather: Sequence[Weather],
    distance: int,
    *,
    initial_cash: int = 10_000,
) -> StrategyResult:
    water, food, days = minimum_travel_requirements(config, weather, distance)
    if config.load(water, food) > config.capacity:
        raise ValueError("minimum supplies exceed carrying capacity")
    cash = initial_cash - water * config.water_price - food * config.food_price
    if cash < 0:
        raise ValueError("minimum supplies exceed initial cash")
    final = SearchState(days, 1, 0, 0, cash, 0)
    return StrategyResult(cash, water, food, final, ())


def _full_capacity_purchases(config: GameConfig, initial_cash: int) -> Iterable[tuple[int, int, int]]:
    """Enumerate B078's full-load initial purchases without duplicate pairs."""
    for water in range(config.capacity // config.water_weight + 1):
        remaining = config.capacity - water * config.water_weight
        if remaining % config.food_weight:
            continue
        food = remaining // config.food_weight
        cash = initial_cash - water * config.water_price - food * config.food_price
        if cash >= 0:
            yield water, food, cash


def solve_mining_backtracking(
    config: GameConfig,
    special_map: SpecialMap,
    weather: Sequence[Weather],
    *,
    initial_cash: int = 10_000,
    refund_rate: float = 1.0,
) -> StrategyResult:
    """B078-style bounded DFS over special nodes and mine actions.

    `refund_rate=1.0` mirrors the appendix C++ terminal expression. Pass 0.5 to
    enforce the literal problem statement's half-price terminal refund.
    """
    best: StrategyResult | None = None
    memo: dict[tuple[int, int, int, int, int], int] = {}

    def dfs(
        state: SearchState,
        initial_water: int,
        initial_food: int,
        audit: tuple[AuditRow, ...],
    ) -> None:
        nonlocal best
        key = (state.day, state.node, state.water, state.food, state.village_reserve)
        if memo.get(key, -1) >= state.cash:
            return
        memo[key] = state.cash

        if special_map.kinds[state.node] == "end":
            score = state.cash + refund_rate * (
                state.water * config.water_price + state.food * config.food_price
            )
            candidate = StrategyResult(score, initial_water, initial_food, state, audit)
            if best is None or candidate.score > best.score:
                best = candidate
            return
        if state.day >= min(config.deadline, len(weather)):
            return

        # Even mining every remaining day cannot beat the incumbent.
        if best is not None:
            optimistic = (
                state.cash
                + (config.deadline - state.day) * config.mine_income
                + refund_rate * (state.water * config.water_price + state.food * config.food_price)
            )
            if optimistic <= best.score:
                return

        for target in special_map.allowed_destinations(state.node):
            travelled = _travel(config, special_map, weather, state, target, audit)
            if travelled is not None:
                next_state, next_audit = travelled
                dfs(next_state, initial_water, initial_food, next_audit)

        if special_map.kinds[state.node] == "mine":
            today = weather[state.day]
            base_water, base_food = config.consumption[today]
            for action, factor, income in (
                ("挖矿", 3, config.mine_income),
                ("矿山停留", 1, 0),
            ):
                consumed = _consume(config, state, factor * base_water, factor * base_food)
                if consumed is None:
                    continue
                next_state = replace(consumed, day=consumed.day + 1, cash=consumed.cash + income)
                row = AuditRow(
                    day=next_state.day,
                    location=special_map.names[state.node],
                    action=action,
                    weather=today.value,
                    cash=next_state.cash,
                    water=next_state.water,
                    food=next_state.food,
                )
                dfs(next_state, initial_water, initial_food, audit + (row,))

    for water, food, cash in _full_capacity_purchases(config, initial_cash):
        initial = SearchState(0, special_map.start, water, food, cash, 0)
        first_row = AuditRow(0, special_map.names[special_map.start], "起点购买", "", cash, water, food)
        dfs(initial, water, food, (first_row,))

    if best is None:
        raise ValueError("no feasible mining strategy found")
    return best


def sample_weather(
    days: int,
    probabilities: tuple[float, float, float],
    *,
    seed: int | None = None,
) -> tuple[Weather, ...]:
    rng = random.Random(seed)
    return tuple(
        rng.choices(
            (Weather.SUNNY, Weather.HOT, Weather.SANDSTORM),
            weights=probabilities,
            k=days,
        )
    )


B078_FIRST_WEATHER = tuple(
    {
        1: Weather.SUNNY,
        2: Weather.HOT,
        3: Weather.SANDSTORM,
    }[value]
    for value in (
        2, 2, 1, 3, 1,
        2, 3, 1, 2, 2,
        3, 2, 1, 2, 2,
        2, 3, 3, 2, 2,
        1, 1, 2, 1, 3,
        2, 1, 1, 2, 2,
    )
)


B078_FIRST_SPECIAL_MAP = SpecialMap(
    names=("起点1", "村庄15", "矿山12", "终点27"),
    kinds=("start", "village", "mine", "end"),
    distances=(
        (0, 6, 8, 3),
        (6, 0, 2, 3),
        (8, 2, 0, 5),
        (3, 3, 5, 0),
    ),
    start=0,
    end=3,
)
