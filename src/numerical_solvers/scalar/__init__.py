"""Metode scalare pentru ecuații neliniare f(x) = 0."""

from .bisection import bisection
from .fixed_point import fixed_point
from .newton import newton
from .secant import secant

__all__ = ["bisection", "fixed_point", "newton", "secant"]
