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
