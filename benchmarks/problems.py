"""Probleme de test cu soluții cunoscute pentru benchmarkuri."""

import math

import numpy as np


def cubic(x):
    return x**3 - 2*x - 5


def cubic_df(x):
    return 3*x**2 - 2


def quadratic(x):
    return x**2 - x - 2


def quadratic_g(x):
    return math.sqrt(x + 2)


def cosine(x):
    return math.cos(x) - x


def cosine_df(x):
    return -math.sin(x) - 1


def cosine_g(x):
    return math.cos(x)


def exponential(x):
    return math.exp(-x) - x


def exponential_df(x):
    return -math.exp(-x) - 1


def exponential_g(x):
    return math.exp(-x)


SCALAR_PROBLEMS = [
    {
        "name": "x^3 - 2x - 5",
        "f": cubic,
        "df": cubic_df,
        "g": None,
        "bracket": (2.0, 3.0),
        "x0": 2.0,
        "secant_start": (2.0, 3.0),
        "root": 2.0945514815423265,
    },
    {
        "name": "x^2 - x - 2",
        "f": quadratic,
        "df": lambda x: 2*x - 1,
        "g": quadratic_g,
        "bracket": (1.0, 3.0),
        "x0": 1.5,
        "secant_start": (1.0, 3.0),
        "root": 2.0,
    },
    {
        "name": "cos(x) - x",
        "f": cosine,
        "df": cosine_df,
        "g": cosine_g,
        "bracket": (0.0, 1.0),
        "x0": 0.5,
        "secant_start": (0.0, 1.0),
        "root": 0.7390851332151607,
    },
    {
        "name": "exp(-x) - x",
        "f": exponential,
        "df": exponential_df,
        "g": exponential_g,
        "bracket": (0.0, 1.0),
        "x0": 0.5,
        "secant_start": (0.0, 1.0),
        "root": 0.5671432904097838,
    },
]


def circle_parabola_F(z):
    x, y = z
    return np.array([
        x**2 + y**2 - 1,
        x**2 - y,
    ], dtype=float)


def circle_parabola_J(z):
    x, y = z
    return np.array([
        [2*x, 2*y],
        [2*x, -1],
    ], dtype=float)


_Y_ROOT = (np.sqrt(5.0) - 1) / 2

SYSTEM_PROBLEMS = [
    {
        "name": "x^2 + y^2 = 1, x^2 = y",
        "F": circle_parabola_F,
        "J": circle_parabola_J,
        "starts": [[1, 1], [0.5, 0.5], [-1, 1]],
        "roots": [
            np.array([np.sqrt(_Y_ROOT), _Y_ROOT]),
            np.array([-np.sqrt(_Y_ROOT), _Y_ROOT]),
        ],
    },
]
