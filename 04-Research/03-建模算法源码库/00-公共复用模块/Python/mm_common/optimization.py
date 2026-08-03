"""Deterministic optimization helpers with explicit feasibility protection."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from math import isfinite

import numpy as np

Objective = Callable[[np.ndarray], float]
Feasibility = Callable[[np.ndarray], bool]


@dataclass(frozen=True)
class EvolutionResult:
    decision: np.ndarray
    score: float
    history_best: np.ndarray
    history_mean_feasible: np.ndarray
    evaluations: int
    feasible_evaluations: int


@dataclass(frozen=True)
class CoordinateRefinementResult:
    decision: np.ndarray
    score: float
    history_best: np.ndarray
    evaluations: int


def _unit_vector(decision: Sequence[float], dimension: int) -> np.ndarray:
    vector = np.asarray(decision, dtype=float)
    if vector.shape != (dimension,) or not np.all(np.isfinite(vector)):
        raise ValueError("decision must be a finite one-dimensional vector")
    if np.any(vector < 0.0) or np.any(vector > 1.0):
        raise ValueError("decision must lie in the unit cube")
    return vector.copy()


def differential_evolution_maximize(
    objective: Objective,
    *,
    dimension: int,
    seed: int,
    population_size: int = 40,
    generations: int = 100,
    mutation: float = 0.75,
    crossover: float = 0.90,
    feasible: Feasibility | None = None,
    initial_decisions: Sequence[Sequence[float]] = (),
    incumbent: Sequence[float] | None = None,
) -> EvolutionResult:
    """Maximize on ``[0,1]^d`` using DE/rand/1/bin and an incumbent guard."""
    if dimension < 1 or population_size < 4 or generations < 0:
        raise ValueError("invalid dimension, population size, or generation count")
    if not 0.0 < mutation <= 2.0 or not 0.0 <= crossover <= 1.0:
        raise ValueError("invalid mutation or crossover parameter")
    rng = np.random.default_rng(seed)
    population = rng.random((population_size, dimension))
    seeds = list(initial_decisions)
    if incumbent is not None:
        seeds.insert(0, incumbent)
    for index, decision in enumerate(seeds[:population_size]):
        population[index] = _unit_vector(decision, dimension)

    evaluations = feasible_evaluations = 0

    def evaluate(decision: np.ndarray) -> float:
        nonlocal evaluations, feasible_evaluations
        evaluations += 1
        if feasible is not None and not bool(feasible(decision)):
            return -np.inf
        feasible_evaluations += 1
        score = float(objective(decision))
        return score if isfinite(score) else -np.inf

    scores = np.asarray([evaluate(candidate) for candidate in population])
    if incumbent is not None and not np.isfinite(scores[0]):
        raise ValueError("incumbent must be feasible and have a finite score")
    if not np.any(np.isfinite(scores)):
        raise RuntimeError("initial population contains no feasible finite solution")

    history_best = [float(np.max(scores))]
    finite_scores = scores[np.isfinite(scores)]
    history_mean = [float(np.mean(finite_scores))]
    for _ in range(generations):
        for index in range(population_size):
            pool = np.delete(np.arange(population_size), index)
            a, b, c = rng.choice(pool, size=3, replace=False)
            mutant = np.clip(
                population[a] + mutation * (population[b] - population[c]), 0.0, 1.0
            )
            mask = rng.random(dimension) < crossover
            mask[rng.integers(0, dimension)] = True
            trial = np.where(mask, mutant, population[index])
            trial_score = evaluate(trial)
            if trial_score >= scores[index]:
                population[index], scores[index] = trial, trial_score
        history_best.append(float(np.max(scores)))
        finite_scores = scores[np.isfinite(scores)]
        history_mean.append(float(np.mean(finite_scores)))

    best = int(np.argmax(scores))
    return EvolutionResult(
        decision=population[best].copy(),
        score=float(scores[best]),
        history_best=np.asarray(history_best),
        history_mean_feasible=np.asarray(history_mean),
        evaluations=evaluations,
        feasible_evaluations=feasible_evaluations,
    )


def coordinate_refine_unit_cube(
    decision: Sequence[float],
    objective: Objective,
    *,
    feasible: Feasibility | None = None,
    initial_step: float = 0.10,
    minimum_step: float = 1e-5,
    max_rounds: int = 200,
) -> CoordinateRefinementResult:
    """Coordinate search that never replaces a feasible incumbent by an invalid point."""
    current = np.asarray(decision, dtype=float)
    if current.ndim != 1:
        raise ValueError("decision must be one-dimensional")
    current = _unit_vector(current, len(current))
    if initial_step <= 0.0 or minimum_step <= 0.0 or max_rounds < 1:
        raise ValueError("invalid refinement settings")
    if feasible is not None and not bool(feasible(current)):
        raise ValueError("initial decision must be feasible")
    current_score = float(objective(current))
    if not isfinite(current_score):
        raise ValueError("initial score must be finite")
    evaluations = 1
    step = float(initial_step)
    history = [current_score]
    for _ in range(max_rounds):
        improved = False
        for axis in range(len(current)):
            for direction in (-1.0, 1.0):
                candidate = current.copy()
                candidate[axis] = np.clip(candidate[axis] + direction * step, 0.0, 1.0)
                if feasible is not None and not bool(feasible(candidate)):
                    continue
                candidate_score = float(objective(candidate))
                evaluations += 1
                if isfinite(candidate_score) and candidate_score > current_score + 1e-12:
                    current, current_score = candidate, candidate_score
                    improved = True
        history.append(current_score)
        if not improved:
            step *= 0.5
        if step <= minimum_step:
            break
    return CoordinateRefinementResult(
        decision=current,
        score=current_score,
        history_best=np.asarray(history),
        evaluations=evaluations,
    )
