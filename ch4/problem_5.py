from collections import OrderedDict, namedtuple
from functools import wraps

def lru_cache(maxsize=0):
    pass

## TESTS BELOW
import sys
sys.path.append("..")
from test_runners import Test, first_digit
sys.path.remove('..')

import math
import cmath

@lru_cache(maxsize=2)
def solve_quadratic(a, b, c):
    """Solve the equation ax^2 + bx + c = 0"""
    quad = b*b - 4*a*c
    sqrt = cmath.sqrt if quad < 0 else math.sqrt
    x1 = (-b + sqrt(quad))/(2*a)
    x2 = (-b - sqrt(quad))/(2*a)
    return x1, x2

# NOTE: Because the cache is storing state, earlier tests influence later ones
#       Which means commenting out some tests will affect others
#       IE These tests are NOT independent
cache_test_flow = [
    (solve_quadratic(1, -5, 6), (3.0, 2.0)),
    (solve_quadratic(1, -6, 9), (3.0, 3.0)),
    (solve_quadratic(2, 2, 1), ((-0.5+0.5j), (-0.5-0.5j))),
    (solve_quadratic(1, -6, 9), (3.0, 3.0)),
    (solve_quadratic(1, -5, 6), (3.0, 2.0)),
    (str(solve_quadratic.cache_info()), 'CacheInfo(hits=1, misses=4, maxsize=2, currsize=2)')
]

Test(examples=cache_test_flow).equivalence()

