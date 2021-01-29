class Pitch:
    pass

## TESTS BELOW

import sys
sys.path.insert(0, '..')
from test_runners import Test
sys.path.remove('..')

pitch_errors = [
    ("Pitch('c$4')", ValueError),
    ("Pitch('C9')", ValueError),
    ("Pitch('w#4')", ValueError),
    ("Pitch('c♭4 ')", ValueError),
    ("Pitch('aa♭4')", ValueError),
    ("Pitch('C4') + 4.5", TypeError),
    ("Pitch('C4') - (lambda x: int(x))", TypeError),
    ("Pitch('C4') > 'C4'", TypeError),
    ("Pitch('C4') < 'C6'", TypeError),
    ("Pitch('C4') >= 'A4'", TypeError),
]

Test(examples=pitch_errors, test_class=Pitch).pitch_errors()