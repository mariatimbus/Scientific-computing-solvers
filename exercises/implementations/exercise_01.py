"""Exercițiul 1: verificarea legăturii dintre pașii de pe hârtie și cod.

Pentru fiecare metodă scalară afișăm primele iterații și le comparăm cu
calculele manuale. Regula: dacă coincid primii doi-trei pași, algoritmul
este tradus corect și putem rula până la toleranța finală.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from numerical_solvers.scalar import bisection, fixed_point, newton, secant


def f(x):
    return x**3 - 2*x - 5


def df(x):
    return 3*x**2 - 2


def g(x):
    return math.sqrt(x + 2)


def f_quadratic(x):
    return x**2 - x - 2


def main():
    print("=== Bisecție pe [2, 3]; pe hârtie c_1 = 2.5, f(2.5) = 5.125 > 0 ===")
    result = bisection(f, 2, 3)
    for record in result.history[:3]:
        print(f"k={record['k']}  a={record['a']:.10f}  b={record['b']:.10f}  "
              f"c={record['c']:.10f}  f(c)={record['f_c']:.6e}")
    assert result.history[0]["c"] == 2.5
    print(result.summary())

    print("\n=== Newton din x_0 = 2; pe hârtie x_1 = 2.1 ===")
    result = newton(f, df, 2)
    for record in result.history[:3]:
        print(f"k={record['k']}  x={record['x']:.10f}  f(x)={record['fx']:.6e}  "
              f"f'(x)={record['dfx']:.6e}")
    assert result.history[0]["x"] == 2.1
    print(result.summary())

    print("\n=== Secanta din 2, 3; pe hârtie x_2 = 35/17 ≈ 2.0588235294 ===")
    result = secant(f, 2, 3)
    for record in result.history[:3]:
        print(f"k={record['k']}  x={record['x']:.10f}  f(x)={record['f_x']:.6e}")
    assert result.history[0]["x"] == 35 / 17
    print(result.summary())

    print("\n=== Punct fix g(x) = sqrt(x + 2) din 1.5; pe hârtie x_1 = sqrt(3.5) ===")
    result = fixed_point(g, f_quadratic, 1.5)
    for record in result.history[:3]:
        print(f"k={record['k']}  x={record['x']:.10f}  "
              f"pas={record['step']:.6e}  |f(x)|={record['residual']:.6e}")
    assert result.history[0]["x"] == math.sqrt(3.5)
    print(result.summary())

    print("\nPrimii pași coincid cu calculele de pe hârtie.")


if __name__ == "__main__":
    main()
