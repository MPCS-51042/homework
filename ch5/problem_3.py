from problem_2 import Fraction

## TESTS BELOW USE THE FRACTION CLASS FROM
## THE PREVIOUS PROBLEM.
## PLEASE MAKE CODE CHANGES THERE.

import sys
sys.path.insert(0, '..')
from test_runners import Test
sys.path.remove('..')

fraction_examples = [
    ((Fraction(1, 2) + 1), Fraction(3, 2)),
    ((Fraction(3, 4) - 0.125), Fraction(5, 8)),
    ((Fraction(6, 2) * 5), Fraction(15, 1)),
    ((Fraction(4, 5) / 0.4), Fraction(2, 1)),
    ((0.5 + Fraction(1, 3)), Fraction(5, 6)),
    ((1 - Fraction(1, 8)), Fraction(7, 8)),
    ((3 * Fraction(4, 3)), Fraction(4, 1)),
    ((0.8 / Fraction(3, 1)), Fraction(4, 15)),
]

Test(examples=fraction_examples).equivalence()