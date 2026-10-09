"""Benchmark pentru Newton pe sisteme; salvează tabelul în results/tables/."""

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from numerical_solvers.systems import newton_system

from problems import SYSTEM_PROBLEMS


def main():
    rows = []

    for problem in SYSTEM_PROBLEMS:
        for start_point in problem["starts"]:
            started = time.perf_counter()
            try:
                result = newton_system(
                    problem["F"], problem["J"], start_point
                )
                elapsed = time.perf_counter() - started
                rows.append({
                    "problem": problem["name"],
                    "start": str(start_point),
                    "iterations": result.iterations,
                    "residual": result.residual,
                    "error": min(
                        np.linalg.norm(result.root - root, ord=np.inf)
                        for root in problem["roots"]
                    ),
                    "time_s": elapsed,
                    "reason": result.reason,
                })
            except RuntimeError as error:
                rows.append({
                    "problem": problem["name"],
                    "start": str(start_point),
                    "iterations": None,
                    "residual": None,
                    "error": None,
                    "time_s": time.perf_counter() - started,
                    "reason": f"eșec: {error}",
                })

    table = pd.DataFrame(rows)
    print(table.to_string(index=False))

    output = Path(__file__).resolve().parents[1] / "results" / "tables"
    output.mkdir(parents=True, exist_ok=True)
    table.to_csv(output / "systems_benchmark.csv", index=False)
    print(f"\nTabel salvat în {output / 'systems_benchmark.csv'}")


if __name__ == "__main__":
    main()
