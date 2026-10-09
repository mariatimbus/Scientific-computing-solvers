"""Teste pentru solvere scalare: rădăcini cunoscute, primii pași de pe hârtie, eșecuri."""

import math

import pytest

from numerical_solvers.scalar import bisection, fixed_point, newton, secant


def f_cubic(x):
    return x**3 - 2*x - 5


def df_cubic(x):
    return 3*x**2 - 2


def f_quadratic(x):
    return x**2 - x - 2


def g_quadratic(x):
    return math.sqrt(x + 2)


CUBIC_ROOT = 2.0945514815423265


class TestBisection:
    def test_root_cubic(self):
        result = bisection(f_cubic, 2, 3)
        # Bisecția garantează eroarea în x, nu reziduul:
        # |c - rădăcină| ≤ (b - a)/2 ≤ tol_x.
        assert result.root == pytest.approx(CUBIC_ROOT, abs=1e-10)
        assert abs(result.root - CUBIC_ROOT) <= 1e-10
        assert result.iterations > 0
        assert result.reason

    def test_first_step_matches_paper(self):
        # f(2) = -1, f(3) = 16, primul mijloc este 2.5.
        result = bisection(f_cubic, 2, 3)
        assert result.history[0]["c"] == pytest.approx(2.5)
        assert result.history[0]["f_c"] > 0

    def test_error_interval_halves(self):
        result = bisection(f_cubic, 2, 3)
        widths = [h["b"] - h["a"] for h in result.history]
        assert all(
            widths[i + 1] == pytest.approx(widths[i] / 2)
            for i in range(len(widths) - 1)
        )

    def test_same_sign_bracket_raises(self):
        with pytest.raises(ValueError, match="semne opuse"):
            bisection(f_cubic, 3, 4)

    def test_exact_endpoint_returned(self):
        result = bisection(lambda x: x - 2, 2, 3)
        assert result.root == 2
        assert result.iterations == 0

    def test_max_iter_exhausted_raises(self):
        with pytest.raises(RuntimeError, match="iterații"):
            bisection(f_cubic, 2, 3, tol_x=0.0, max_iter=3)


class TestFixedPoint:
    def test_root_quadratic(self):
        result = fixed_point(g_quadratic, f_quadratic, 1.5)
        assert result.root == pytest.approx(2.0, abs=1e-9)
        assert result.residual < 1e-10

    def test_first_step_matches_paper(self):
        # x_1 = g(1.5) = sqrt(3.5)
        result = fixed_point(g_quadratic, f_quadratic, 1.5)
        assert result.history[0]["x"] == pytest.approx(math.sqrt(3.5))

    def test_non_finite_iteration_raises(self):
        with pytest.raises(RuntimeError, match="nefinit"):
            fixed_point(lambda x: math.inf, f_quadratic, 1.5)


class TestNewton:
    def test_root_cubic(self):
        result = newton(f_cubic, df_cubic, 2)
        assert result.root == pytest.approx(CUBIC_ROOT, abs=1e-9)
        assert result.residual < 1e-10

    def test_first_step_matches_paper(self):
        # f(2) = -1, f'(2) = 10, deci x_1 = 2 - (-1)/10 = 2.1.
        result = newton(f_cubic, df_cubic, 2)
        assert result.history[0]["x"] == pytest.approx(2.1)
        assert result.history[0]["fx"] == pytest.approx(-1.0)
        assert result.history[0]["dfx"] == pytest.approx(10.0)

    def test_zero_derivative_raises(self):
        # f(1) = 0.5, f'(1) = 0.
        with pytest.raises(RuntimeError, match="Derivata"):
            newton(lambda x: (x - 1)**3 + 0.5, lambda x: 3*(x - 1)**2, 1.0)

    def test_initial_root_returns_zero_iterations(self):
        result = newton(f_quadratic, lambda x: 2*x - 1, 2.0)
        assert result.root == pytest.approx(2.0)
        assert result.iterations == 0
        assert result.reason == "reziduu ≤ tol_f"


class TestSecant:
    def test_root_cubic(self):
        result = secant(f_cubic, 2, 3)
        assert result.root == pytest.approx(CUBIC_ROOT, abs=1e-9)
        assert result.residual < 1e-10

    def test_first_step_matches_paper(self):
        # f(2) = -1, f(3) = 16, deci x_2 = 3 - 16 * (3-2)/(16-(-1)) = 35/17.
        result = secant(f_cubic, 2, 3)
        assert result.history[0]["x"] == pytest.approx(35 / 17)

    def test_zero_denominator_raises(self):
        with pytest.raises(RuntimeError, match="Numitorul"):
            secant(lambda x: 1.0, 0.0, 1.0)
