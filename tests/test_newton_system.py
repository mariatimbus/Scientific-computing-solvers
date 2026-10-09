"""Teste pentru Newton pe sisteme: rădăcini cunoscute și primul pas de pe hârtie."""

import numpy as np
import pytest

from numerical_solvers.systems import newton_system


def F(z):
    x, y = z
    return np.array([
        x**2 + y**2 - 1,
        x**2 - y,
    ], dtype=float)


def J(z):
    x, y = z
    return np.array([
        [2*x, 2*y],
        [2*x, -1],
    ], dtype=float)


# y = x^2 și x^2 + y^2 = 1 dau y = (sqrt(5) - 1) / 2.
Y_ROOT = (np.sqrt(5.0) - 1) / 2
POSITIVE_ROOT = np.array([np.sqrt(Y_ROOT), Y_ROOT])


class TestNewtonSystem:
    def test_root_circle_parabola(self):
        result = newton_system(F, J, [1, 1])
        assert result.root == pytest.approx(POSITIVE_ROOT, abs=1e-9)
        assert result.residual < 1e-10

    def test_first_step_matches_paper(self):
        # F(1,1) = (1, 0); 2 s_x + 2 s_y = -1, 2 s_x - s_y = 0
        # dă s = (-1/6, -1/3), deci z_1 = (5/6, 2/3).
        result = newton_system(F, J, [1, 1])
        assert result.history[0]["z"] == pytest.approx([5 / 6, 2 / 3], abs=1e-12)

    def test_negative_branch(self):
        result = newton_system(F, J, [-1, 1])
        assert result.root == pytest.approx(
            [-POSITIVE_ROOT[0], POSITIVE_ROOT[1]], abs=1e-9
        )

    def test_singular_jacobian_raises(self):
        # J(0, 0) este singular, iar F(0, 0) = (-1, 0).
        with pytest.raises(RuntimeError, match="Sistemul liniar"):
            newton_system(F, J, [0, 0])

    def test_history_records_residual_and_step(self):
        result = newton_system(F, J, [1, 1])
        first = result.history[0]
        assert first["residual"] == pytest.approx(1.0)
        assert first["step"] == pytest.approx(1 / 3)
