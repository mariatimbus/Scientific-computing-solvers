"""Solverse numerice pentru ecuații și sisteme neliniare."""

from .result import SolveResult
from .scalar import bisection, fixed_point, newton, secant
from .systems import newton_system

__all__ = [
    "SolveResult",
    "bisection",
    "fixed_point",
    "newton",
    "secant",
    "newton_system",
]
