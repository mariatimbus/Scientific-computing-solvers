"""Metoda Newton pentru ecuații scalare f(x) = 0."""

import math

from ..result import SolveResult


def newton(f, df, x0, tol_x=1e-10, tol_f=1e-10, max_iter=100):
    """Rezolvă f(x) = 0 prin x_{k+1} = x_k - f(x_k)/f'(x_k)."""
    x = x0
    history = []

    for k in range(1, max_iter + 1):
        fx = f(x)

        if not math.isfinite(fx):
            raise RuntimeError("Valoare nefinită a funcției.")

        if abs(fx) <= tol_f:
            return SolveResult(x, k - 1, abs(fx), history, "reziduu ≤ tol_f")

        dfx = df(x)

        if not math.isfinite(dfx) or dfx == 0:
            raise RuntimeError("Derivata nu permite calculul pasului.")

        correction = -fx / dfx
        x_new = x + correction

        if not math.isfinite(x_new):
            raise RuntimeError("Pasul a produs o valoare nefinită.")

        history.append({
            "k": k,
            "x": x_new,
            "fx": fx,
            "dfx": dfx,
            "step": abs(correction),
        })

        if abs(x_new - x) <= tol_x:
            residual = f(x_new)

            if math.isfinite(residual) and abs(residual) <= tol_f:
                return SolveResult(
                    x_new, k, abs(residual), history,
                    "pas mic și reziduu mic",
                )

            raise RuntimeError("Pas mic, dar reziduu prea mare.")

        x = x_new

    raise RuntimeError("Limita de iterații a fost atinsă.")
