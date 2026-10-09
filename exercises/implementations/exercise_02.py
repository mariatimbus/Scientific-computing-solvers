"""Exercițiul 2: verificarea primului pas Newton pentru sistemul neliniar.

Sistemul din fișa de probleme:
    x^2 + y^2 - 1 = 0
    x^2 - y = 0

În z_0 = (1, 1): F = (1, 0). Sistemul liniar 2 s_x + 2 s_y = -1,
2 s_x - s_y = 0 dă s = (-1/6, -1/3), deci z_1 = (5/6, 2/3).
Codul trebuie să reproducă exact acest prim pas.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

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


def main():
    result = newton_system(F, J, [1, 1])

    print("=== Istoricul iterațiilor ===")
    for record in result.history:
        z = record["z"]
        print(f"k={record['k']}  z=({z[0]:.10f}, {z[1]:.10f})  "
              f"pas={record['step']:.6e}  reziduu={record['residual']:.6e}")

    z1 = result.history[0]["z"]
    assert np.allclose(z1, [5 / 6, 2 / 3], atol=1e-12), z1
    print("\nPrimul pas coincide cu calculul de mână: z_1 = (5/6, 2/3).")
    print(result.summary())


if __name__ == "__main__":
    main()
