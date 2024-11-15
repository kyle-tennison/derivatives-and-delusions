from random import choice
from despair.sympy_util import (
    solve,
    diff,
    integrate,
    Eq,
    symbols,
    simplify,
    solve_eoe,
    plot,
    fprint,
    Piecewise,
    exp_max,
    exp_arr,
)
import numpy as np
import sympy as sp

__all__ = [
    "solve",
    "diff",
    "integrate",
    "Eq",
    "symbols",
    "simplify",
    "solve_eoe",
    "plot",
    "fprint",
    "sp",
    "Piecewise",
    "exp_max",
    "exp_arr",
    "np",
]

beer = lambda: print("beer")
splendid = lambda: print(choice(["yeah pretty splendid", "not splendid no"]))