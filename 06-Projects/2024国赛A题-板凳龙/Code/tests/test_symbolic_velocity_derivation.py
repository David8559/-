"""Exact symbolic check of the fixed-chord velocity recursion."""

from __future__ import annotations

import unittest

import sympy as sp


class SymbolicVelocityDerivationTests(unittest.TestCase):
    def test_velocity_recursion_follows_from_chord_constraint(self) -> None:
        delta_x, delta_y = sp.symbols("Delta_x Delta_y", real=True)
        previous_vx, previous_vy = sp.symbols(
            "v_previous_x v_previous_y",
            real=True,
        )
        tangent_x, tangent_y = sp.symbols(
            "q_prime_i_x q_prime_i_y",
            real=True,
        )
        theta_rate = sp.symbols("theta_rate_i", real=True)

        differentiated_constraint = (
            delta_x * (tangent_x * theta_rate - previous_vx)
            + delta_y * (tangent_y * theta_rate - previous_vy)
        )
        solution = sp.solve(
            sp.Eq(differentiated_constraint, 0),
            theta_rate,
        )[0]
        expected = (
            delta_x * previous_vx + delta_y * previous_vy
        ) / (delta_x * tangent_x + delta_y * tangent_y)

        self.assertEqual(sp.simplify(solution - expected), 0)
        self.assertEqual(
            sp.simplify(
                differentiated_constraint.subs(theta_rate, solution)
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
