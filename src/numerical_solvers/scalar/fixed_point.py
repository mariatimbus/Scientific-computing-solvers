"""Iterația de punct fix pentru ecuații scalare f(x) = 0."""

import math

from ..result import SolveResult


def fixed_point(g, f, x0, tol_x=1e-10, tol_f=1e-10, max_iter=200):
    """Rezolvă f(x) = 0 prin x_{k+1} = g(x_k).

    g construiește aproximațiile, f verifică reziduul în ecuația originală.
    """
    x = x0

    if abs(f(x)) <= tol_f:
        return SolveResult(x, 0, abs(f(x)), [], "reziduu inițial ≤ tol_f")

    history = []

    for k in range(1, max_iter + 1):
        x_new = g(x)

        if not math.isfinite(x_new):
            raise RuntimeError("Iterația a produs o valoare nefinită.")

        residual = f(x_new)

        if not math.isfinite(residual):
            raise RuntimeError("Reziduu nefinit.")

        step = abs(x_new - x)

        history.append({"k": k, "x": x_new, "residual": abs(residual), "step": step})

        if step <= tol_x and abs(residual) <= tol_f:
            return SolveResult(
                x_new, k, abs(residual), history,
                "pas mic și reziduu mic",
            )

        if x_new == x:
            raise RuntimeError("Stagnare fără reziduu acceptabil.")

        x = x_new

    raise RuntimeError("Limita de iterații a fost atinsă.")
