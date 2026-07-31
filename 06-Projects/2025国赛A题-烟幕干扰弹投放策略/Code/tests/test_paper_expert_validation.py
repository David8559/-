"""Tests for the paper-expert Monte Carlo validation companion."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from build_submission import latex_inline_to_text  # noqa: E402
from run_paper_expert_validation import run_monte_carlo, summarize


class PaperExpertValidationTests(unittest.TestCase):
    def test_inline_latex_is_readable_in_word(self) -> None:
        cases = {
            r"\boldsymbol M_j(t)": "M_j(t)",
            r"\widehat\lambda=\min(1,\max(0,\lambda^*))": "λ̂=min(1,max(0,λ*))",
            r"j\in\{1,2,3\}": "j∈{1,2,3}",
            r"10^{-7}": "10⁻⁷",
            r"-\boldsymbol M_{j0}/\|\boldsymbol M_{j0}\|_2": "-M_j0/‖M_j0‖_2",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                converted = latex_inline_to_text(source)
                self.assertEqual(converted, expected)
                self.assertNotIn("\\", converted)

    def test_monte_carlo_is_reproducible(self) -> None:
        first = run_monte_carlo(samples=8, seed=1234, step=0.1, n_theta=12)
        second = run_monte_carlo(samples=8, seed=1234, step=0.1, n_theta=12)
        np.testing.assert_allclose(first.duration_s, second.duration_s)

    def test_summary_has_physical_probabilities(self) -> None:
        result = run_monte_carlo(samples=8, seed=4321, step=0.1, n_theta=12)
        report = summarize(result, seed=4321)
        self.assertGreaterEqual(report["probability_positive"], 0.0)
        self.assertLessEqual(report["probability_positive"], 1.0)
        self.assertGreaterEqual(report["standard_deviation_s"], 0.0)


if __name__ == "__main__":
    unittest.main()
