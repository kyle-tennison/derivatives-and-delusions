# derivatives and despair

hail mary tools for engineering students when we're thoroughly screwed

### overview

really just some quality of life wrappers around `sympy`, `numpy` and `matplotlib`
that are useful for solving evil annoying problems


### installation

```
python -m pip install sleepless-solutions
```


### usage

```python
from ss import *


x, y, z = syms("x, y, z")

all_of_my_homework_problems_that_i_hate = [
    2*x + 4*y + z, # == 0
    4

]
```