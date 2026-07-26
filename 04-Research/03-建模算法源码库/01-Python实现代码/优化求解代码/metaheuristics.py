"""GA、PSO、SA、ACO 的教学型基础实现。

统一假设目标函数越小越好；随机算法均暴露 seed，并返回收敛历史。
正式比赛至少运行多个随机种子并报告最好值、均值、标准差与预算。
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray


Objective = Callable[[NDArray[np.float64]], float]


def genetic_algorithm(
    objective: Objective,
    bounds: ArrayLike,
    *,
    population_size: int = 80,
    generations: int = 200,
    crossover_rate: float = 0.9,
    mutation_rate: float = 0.1,
    seed: int = 42,
) -> tuple[NDArray[np.float64], float, list[float]]:
    """实数编码 GA：锦标赛选择、算术交叉、高斯变异和精英保留。"""
    rng = np.random.default_rng(seed)
    limits = np.asarray(bounds, dtype=float)
    lower, upper = limits[:, 0], limits[:, 1]
    population = rng.uniform(lower, upper, size=(population_size, len(lower)))
    history: list[float] = []

    for _ in range(generations):
        fitness = np.array([objective(x) for x in population], dtype=float)
        elite = population[int(np.argmin(fitness))].copy()
        history.append(float(fitness.min()))
        children = [elite]
        while len(children) < population_size:
            candidates = rng.integers(0, population_size, size=(2, 3))
            p1 = population[candidates[0, np.argmin(fitness[candidates[0]])]]
            p2 = population[candidates[1, np.argmin(fitness[candidates[1]])]]
            if rng.random() < crossover_rate:
                alpha = rng.random(len(lower))
                child = alpha * p1 + (1 - alpha) * p2
            else:
                child = p1.copy()
            mask = rng.random(len(lower)) < mutation_rate
            child[mask] += rng.normal(0, 0.1 * (upper - lower)[mask])
            children.append(np.clip(child, lower, upper))
        population = np.asarray(children)

    fitness = np.array([objective(x) for x in population], dtype=float)
    best = int(np.argmin(fitness))
    return population[best], float(fitness[best]), history


def particle_swarm(
    objective: Objective,
    bounds: ArrayLike,
    *,
    particles: int = 60,
    iterations: int = 200,
    inertia: float = 0.7,
    cognitive: float = 1.5,
    social: float = 1.5,
    seed: int = 42,
) -> tuple[NDArray[np.float64], float, list[float]]:
    """连续 PSO；采用全局最优拓扑与边界截断。"""
    rng = np.random.default_rng(seed)
    limits = np.asarray(bounds, dtype=float)
    lower, upper = limits[:, 0], limits[:, 1]
    x = rng.uniform(lower, upper, size=(particles, len(lower)))
    v = rng.uniform(-(upper - lower), upper - lower, size=x.shape) * 0.1
    pbest = x.copy()
    pval = np.array([objective(row) for row in x], dtype=float)
    gbest = pbest[int(np.argmin(pval))].copy()
    history: list[float] = []

    for _ in range(iterations):
        r1, r2 = rng.random(x.shape), rng.random(x.shape)
        v = inertia * v + cognitive * r1 * (pbest - x) + social * r2 * (gbest - x)
        x = np.clip(x + v, lower, upper)
        values = np.array([objective(row) for row in x], dtype=float)
        improved = values < pval
        pbest[improved], pval[improved] = x[improved], values[improved]
        gbest = pbest[int(np.argmin(pval))].copy()
        history.append(float(pval.min()))
    return gbest, float(pval.min()), history


def simulated_annealing(
    objective: Objective,
    initial: ArrayLike,
    bounds: ArrayLike,
    *,
    temperature: float = 10.0,
    cooling: float = 0.98,
    iterations: int = 1000,
    step_scale: float = 0.1,
    seed: int = 42,
) -> tuple[NDArray[np.float64], float, list[float]]:
    """连续变量 SA；按 Metropolis 准则接受劣解。"""
    rng = np.random.default_rng(seed)
    limits = np.asarray(bounds, dtype=float)
    lower, upper = limits[:, 0], limits[:, 1]
    current = np.clip(np.asarray(initial, dtype=float), lower, upper)
    current_value = float(objective(current))
    best, best_value = current.copy(), current_value
    history: list[float] = []

    temp = float(temperature)
    for _ in range(iterations):
        candidate = np.clip(
            current + rng.normal(0, step_scale * (upper - lower)), lower, upper
        )
        candidate_value = float(objective(candidate))
        delta = candidate_value - current_value
        if delta <= 0 or rng.random() < np.exp(-delta / max(temp, 1e-12)):
            current, current_value = candidate, candidate_value
        if current_value < best_value:
            best, best_value = current.copy(), current_value
        history.append(best_value)
        temp *= cooling
    return best, best_value, history


def ant_colony_tsp(
    distance: ArrayLike,
    *,
    ants: int = 40,
    iterations: int = 150,
    alpha: float = 1.0,
    beta: float = 3.0,
    evaporation: float = 0.5,
    seed: int = 42,
) -> tuple[list[int], float, list[float]]:
    """对称 TSP 的 Ant System 基线，返回闭合路线、长度与收敛历史。"""
    rng = np.random.default_rng(seed)
    d = np.asarray(distance, dtype=float)
    n = d.shape[0]
    if d.shape != (n, n) or np.any(d < 0) or not np.allclose(d, d.T):
        raise ValueError("distance 必须为非负对称方阵")
    off_diagonal = ~np.eye(n, dtype=bool)
    if not np.allclose(np.diag(d), 0) or np.any(d[off_diagonal] <= 0):
        raise ValueError("distance 对角线必须为 0，非对角元素必须为正")
    heuristic = np.zeros_like(d)
    mask = d > 0
    heuristic[mask] = 1.0 / d[mask]
    pheromone = np.ones_like(d)
    best_route: list[int] = []
    best_length = np.inf
    history: list[float] = []

    for _ in range(iterations):
        routes: list[tuple[list[int], float]] = []
        for _ant in range(ants):
            start = int(rng.integers(n))
            route, unvisited = [start], set(range(n)) - {start}
            while unvisited:
                current = route[-1]
                candidates = np.array(sorted(unvisited))
                desirability = (
                    pheromone[current, candidates] ** alpha
                    * heuristic[current, candidates] ** beta
                )
                if desirability.sum() == 0:
                    nxt = int(rng.choice(candidates))
                else:
                    nxt = int(rng.choice(candidates, p=desirability / desirability.sum()))
                route.append(nxt)
                unvisited.remove(nxt)
            closed = route + [start]
            length = float(sum(d[a, b] for a, b in zip(closed[:-1], closed[1:])))
            routes.append((closed, length))
            if length < best_length:
                best_route, best_length = closed, length
        pheromone *= 1 - evaporation
        for route, length in routes:
            deposit = 1.0 / max(length, np.finfo(float).eps)
            for a, b in zip(route[:-1], route[1:]):
                pheromone[a, b] += deposit
                pheromone[b, a] += deposit
        history.append(best_length)
    return best_route, best_length, history
