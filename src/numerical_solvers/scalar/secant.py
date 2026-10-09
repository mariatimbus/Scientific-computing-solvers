"""Metoda secantei pentru ecuații scalare f(x) = 0."""

import math

from ..result import SolveResult


def secant(f, x0, x1, tol_x=1e-10, tol_f=1e-10, max_iter=100):
    """Rezolvă f(x) = 0 fără derivată, din două aproximații inițiale."""
    f0 = f(x0)
    f1 = f(x1)

    if not math.isfinite(f0) or not math.isfinite(f1):
        raise RuntimeError("Valori inițiale nefinite.")

    if abs(f0) <= tol_f:
        return SolveResult(x0, 0, abs(f0), [], "reziduu inițial ≤ tol_f")

    if abs(f1) <= tol_f:
        return SolveResult(x1, 0, abs(f1), [], "reziduu inițial ≤ tol_f")

    history = []

    for k in range(1, max_iter + 1):
        denominator = f1 - f0

        if denominator == 0:
            raise RuntimeError("Numitorul secantei este zero.")

        x2 = x1 - f1 * (x1 - x0) / denominator

        if not math.isfinite(x2):
            raise RuntimeError("Aproximație nefinită.")

        f2 = f(x2)

        if not math.isfinite(f2):
            raise RuntimeError("Reziduu nefinit.")

        history.append({"k": k, "x": x2, "f_x": f2})

        if abs(f2) <= tol_f:
            return SolveResult(x2, k, abs(f2), history, "reziduu ≤ tol_f")

        if abs(x2 - x1) <= tol_x:
            raise RuntimeError("Pas mic, dar reziduu prea mare.")

        x0, x1 = x1, x2
        f0, f1 = f1, f2

    raise RuntimeError("Limita de iterații a fost atinsă.")
