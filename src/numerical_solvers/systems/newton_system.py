"""Metoda Newton pentru sisteme neliniare F(z) = 0."""

import numpy as np

from ..result import SolveResult


def newton_system(F, J, z0, tol_x=1e-10, tol_f=1e-10, max_iter=100):
    """Rezolvă F(z) = 0 prin J_F(z_k) s_k = -F(z_k), z_{k+1} = z_k + s_k."""
    z = np.array(z0, dtype=float)
    history = []

    for k in range(1, max_iter + 1):
        residual = F(z)

        if not np.all(np.isfinite(residual)):
            raise RuntimeError("Reziduu nefinit.")

        residual_norm = np.linalg.norm(residual, ord=np.inf)

        if residual_norm <= tol_f:
            return SolveResult(z, k - 1, residual_norm, history, "reziduu ≤ tol_f")

        jacobian = J(z)

        if not np.all(np.isfinite(jacobian)):
            raise RuntimeError("Jacobian nefinit.")

        try:
            correction = np.linalg.solve(jacobian, -residual)
        except np.linalg.LinAlgError as error:
            raise RuntimeError(
                "Sistemul liniar nu poate fi rezolvat."
            ) from error

        z_new = z + correction

        if not np.all(np.isfinite(z_new)):
            raise RuntimeError("Aproximație nefinită.")

        step = np.linalg.norm(z_new - z, ord=np.inf)

        history.append({
            "k": k,
            "z": z_new.copy(),
            "residual": residual_norm,
            "step": step,
        })

        if step <= tol_x:
            new_residual = F(z_new)

            if (
                np.all(np.isfinite(new_residual))
                and np.linalg.norm(new_residual, ord=np.inf) <= tol_f
            ):
                return SolveResult(
                    z_new, k,
                    np.linalg.norm(new_residual, ord=np.inf),
                    history, "pas mic și reziduu mic",
                )

            raise RuntimeError("Pas mic, dar reziduu prea mare.")

        z = z_new

    raise RuntimeError("Limita de iterații a fost atinsă.")
