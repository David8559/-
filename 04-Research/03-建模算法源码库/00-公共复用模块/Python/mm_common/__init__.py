"""Small, tested utilities shared by mathematical-modeling projects."""

from .intervals import (
    Interval,
    deletion_marginals,
    intersection_of_unions,
    interval_measure,
    merge_intervals,
)
from .optimization import (
    CoordinateRefinementResult,
    EvolutionResult,
    coordinate_refine_unit_cube,
    differential_evolution_maximize,
)
from .roots import RootResult, bisect_sign_change
from .validation import ConstraintViolationReport, constraint_violation_report

__all__ = [
    "ConstraintViolationReport",
    "CoordinateRefinementResult",
    "EvolutionResult",
    "Interval",
    "RootResult",
    "bisect_sign_change",
    "constraint_violation_report",
    "coordinate_refine_unit_cube",
    "deletion_marginals",
    "differential_evolution_maximize",
    "intersection_of_unions",
    "interval_measure",
    "merge_intervals",
]
