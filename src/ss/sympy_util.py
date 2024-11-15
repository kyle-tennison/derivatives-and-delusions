import sympy as sp

from sympy import solve, diff, integrate, Eq, symbols, simplify
from IPython.display import display, Markdown

__all__ = ['solve', 'diff', 'integrate', 'Eq', 'symbols', 'simplify']

def solve_eoe(eqns: list, solve_for: tuple|list):
    """Solve a list of expressions at all equal zero."""
    return solve([Eq(e, 0) for e in eqns], solve_for)

def plot(*args, **kwargs):
    """Plot an expression and automatically center axes."""
    sp.plot(*args, axis_center=(0,0), **kwargs)

def fprint(string: str):
    """Display in jupyter with markdown."""
    display(Markdown(string))