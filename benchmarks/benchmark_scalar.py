"""Benchmark pentru metodele scalare; salvează tabelul în results/tables/."""

import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from numerical_solvers.scalar import bisection, fixed_point, newton, secant

from problems import SCALAR_PROBLEMS


def run_method(method_name, problem):
    f = problem["f"]

    if method_name == "bisection":
        a, b = problem["bracket"]
        return lambda: bisection(f, a, b)
    if method_name == "newton":
        return lambda: newton(f, problem["df"], problem["x0"])
    if method_name == "secant":
        x0, x1 = problem["secant_start"]
        return lambda: secant(f, x0, x1)
    if method_name == "fixed_point":
        if problem["g"] is None:
            return None
        return lambda: fixed_point(problem["g"], f, problem["x0"])

    raise ValueError(f"Metodă necunoscută: {method_name}")


def main():
    methods = ["bisection", "newton", "secant", "fixed_point"]
    rows = []

    for problem in SCALAR_PROBLEMS:
        for method_name in methods:
            runner = run_method(method_name, problem)
            if runner is None:
                continue

            start = time.perf_counter()
            try:
                result = runner()
                elapsed = time.perf_counter() - start
                rows.append({
                    "problem": problem["name"],
                    "method": method_name,
                    "iterations": result.iterations,
                    "residual": result.residual,
                    "error": abs(result.root - problem["root"]),
                    "time_s": elapsed,
                    "reason": result.reason,
                })
            except RuntimeError as error:
                rows.append({
                    "problem": problem["name"],
                    "method": method_name,
                    "iterations": None,
                    "residual": None,
                    "error": None,
                    "time_s": time.perf_counter() - start,
                    "reason": f"eșec: {error}",
                })

    table = pd.DataFrame(rows)
    print(table.to_string(index=False))

    output = Path(__file__).resolve().parents[1] / "results" / "tables"
    output.mkdir(parents=True, exist_ok=True)
    table.to_csv(output / "scalar_benchmark.csv", index=False)
    print(f"\nTabel salvat în {output / 'scalar_benchmark.csv'}")


if __name__ == "__main__":
    main()
