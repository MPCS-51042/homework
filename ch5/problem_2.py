from numbers import Rational
import math
from math import gcd, lcm

class Fraction:
    pass

## TESTS BELOW

import sys
sys.path.insert(0, '..')
from test_runners import Test
sys.path.remove('..')

fraction_examples = [
    (Fraction(6, 4), Fraction(3, 2)),
    (Fraction(1, -2), Fraction(-1, 2)),
    ((Fraction(1, 2) + Fraction(1, 3)), Fraction(5, 6)),
    ((Fraction(3, 4) - Fraction(1, 8)), Fraction(5, 8)),
    ((Fraction(6, 2) * Fraction(4, 3)), Fraction(4, 1)),
    ((Fraction(4, 5) / Fraction(3, 1)), Fraction(4, 15)),
]

Test(examples=fraction_examples).equivalence()
