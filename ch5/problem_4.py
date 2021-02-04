from functools import wraps, total_ordering
from math import log2
from numbers import Integral
import re

class Pitch:
    pass

## TESTS BELOW

import sys
sys.path.insert(0, '..')
from test_runners import Test
sys.path.remove('..')

pitch_errors = [
    ("Pitch('c$4')", ValueError),
    ("Pitch('w#4')", ValueError),
    ("Pitch('C4') + 4.5", TypeError),
    ("Pitch('C4') - (lambda x: int(x))", TypeError),
    ("Pitch('C4') > 'C4'", TypeError),
    ("Pitch('C4') < 'C6'", TypeError),
    ("Pitch('C4') >= 'A4'", TypeError),
]

Test(examples=pitch_errors, test_class=Pitch).pitch_errors()

pitch_examples = [
    (Pitch('c#2').__repr__(), 'C#2'),
    (Pitch('G6').octave, 6),
    (Pitch('D3').semitone, 2),
    (Pitch('A3') + 4, Pitch('C#4')),
    (Pitch('C#4') - 5, Pitch('G#3')),
    ((Pitch('C7') + 4).semitone, 4),
    ((Pitch('C7') + 4).octave, 7),
    ((Pitch('C7') - 4).semitone, 8),
    ((Pitch('c7') - 4).octave, 6),
    (Pitch('c4') - Pitch('C3'), 12),
    (Pitch('G#2') - Pitch('F#3'), -10),
    (Pitch('A5').frequency(), 880.0),
    (Pitch.from_frequency(170), Pitch('F3')),
    (str(Pitch('A4') == Pitch('A4')), 'True'),
    (str(Pitch('A4') != Pitch('A4')), 'False'),
    (str(Pitch('A5') >= Pitch('A4')), 'True'),
    (str(Pitch('c#3') < Pitch('A4')), 'True'),
    (str(Pitch('A4') <= Pitch('A4')), 'True')
]

Test(examples=pitch_examples).equivalence()