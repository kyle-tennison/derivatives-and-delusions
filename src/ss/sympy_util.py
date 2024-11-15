import sympy as sp
import numpy as np

from sympy import solve, diff, integrate, Eq, symbols, simplify, Piecewise
from IPython.display import display, Markdown

__all__ = ['solve', 'diff', 'integrate', 'Eq', 'symbols', 'simplify', 'Piecewise']

def solve_eoe(eqns: list, solve_for: tuple|list) -> tuple:
    """Solve a list of expressions at all equal zero."""
    sol = solve([Eq(e, 0) for e in eqns], solve_for)
    return tuple(sol[i] for i in solve_for)


def plot(*args, **kwargs):
    """Plot an expression and automatically center axes."""
    sp.plot(*args, axis_center=(0,0), **kwargs)

def fprint(string: str):
    """Display in jupyter with markdown."""
    display(Markdown(string.replace('\n', '\n\n')))

def exp_max(f, var, interval: tuple[int, int], num_points=1024):
    arr = exp_arr(f, var, interval, num_points)
    return arr.max()

def exp_min(f, var, interval: tuple[int, int], num_points=1024):
    arr = exp_arr(f, var, interval, num_points)
    return arr.min()

def exp_arr(exp, var, interval: tuple[int, int], n: int=1024, exclude_NaN: bool=True) ->np.ndarray:
    """Create a numpy array from an expression by sweeping a value over an interval."""


    def _inner_iter():
        for p in np.linspace(*interval, n):
            val = float(exp.subs(var, p).evalf())

            if exclude_NaN and np.isnan(val):
                continue
            yield val


    return np.array([i for i in _inner_iter()], dtype=float)
