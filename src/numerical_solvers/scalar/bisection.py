"""Bisecția pentru ecuații scalare f(x) = 0."""

import math

from ..result import SolveResult


def bisection(f, a, b, tol_x=1e-10, max_iter=100):
    """Rezolvă f(x) = 0 pe [a, b], unde f continuă și f(a)f(b) < 0."""
    if not a < b:
        raise ValueError("Trebuie a < b.")

    fa = f(a)
    fb = f(b)

    if not math.isfinite(fa) or not math.isfinite(fb):
        raise ValueError("Valori nefinite la capete.")

    if fa == 0:
        return SolveResult(a, 0, abs(fa), [], "f(a) = 0")

    if fb == 0:
        return SolveResult(b, 0, abs(fb), [], "f(b) = 0")

    if (fa > 0) == (fb > 0):
        raise ValueError("Capetele trebuie să aibă semne opuse.")

    history = []

    for k in range(1, max_iter + 1):
        c = a + (b - a) / 2

        if (b - a) / 2 <= tol_x:
            residual = abs(f(c))
            return SolveResult(
                c, k, residual, history,
                "lățimea intervalului ≤ tol_x",
            )

        if c == a or c == b:
            raise RuntimeError("Stagnare numerică.")

        fc = f(c)

        if not math.isfinite(fc):
            raise ValueError("Funcția a produs o valoare nefinită.")

        history.append({"k": k, "a": a, "b": b, "c": c, "f_c": fc})

        if fc == 0:
            return SolveResult(c, k, 0.0, history, "f(c) = 0")

        if (fa > 0) != (fc > 0):
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError("Limita de iterații a fost atinsă.")
