# Scientific Computing Solvers

Proiect pentru metode numerice de rezolvare a ecuațiilor neliniare și sistemelor de ecuații neliniare.

## Structură

```
scientific-computing-solvers/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── theory/                    # Notițe teoretice
│
├── exercises/                 # Exerciții
│   ├── solutions/             # Soluții scrise
│   │
│   └── implementations/       # Implementări per exercițiu
│       ├── exercise_01.py
│       ├── exercise_02.py
│
├── src/
│   └── numerical_solvers/     # Pachetul de solvere numerice
│       ├── __init__.py
│       ├── result.py
│       │
│       ├── scalar/            # Metode scalare
│       │   ├── __init__.py
│       │   ├── bisection.py
│       │   ├── fixed_point.py
│       │   ├── newton.py
│       │   └── secant.py
│       │
│       └── systems/           # Metode pentru sisteme
│           ├── __init__.py
│           └── newton_system.py
│
├── benchmarks/                # Benchmark-uri și probleme de test
│   ├── problems.py
│   ├── benchmark_scalar.py
│   └── benchmark_systems.py
│
├── results/                   # Rezultate generate
│   ├── tables/
│   └── figures/
│
├── notes/                     # Jurnal de cercetare
│   ├── research_log.md
│   └── questions.md
│
└── tests/                     # Teste unitare
    ├── test_scalar_solvers.py
    └── test_newton_system.py
```

## Folosire

```bash
pip install -r requirements.txt
python -m pytest tests/
```

Exemplu:

```python
import sys
sys.path.insert(0, "src")

from numerical_solvers.scalar import newton

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

result = newton(f, df, x0=2)
print(result.summary())
# root=2.094551481542327  iterations=4  residual=8.882e-16  reason='reziduu ≤ tol_f'
```

Fiecare solver returnează un `SolveResult` cu: `root` (aproximația finală),
`iterations` (numărul de iterații), `residual` (reziduul final),
`history` (înregistrările pe fiecare iterație) și `reason` (motivul opririi).
Eșecurile semnalează prin excepții (`ValueError`/`RuntimeError`).

Benchmarkuri:

```bash
python benchmarks/benchmark_scalar.py    # salvează results/tables/scalar_benchmark.csv
python benchmarks/benchmark_systems.py   # salvează results/tables/systems_benchmark.csv
```
