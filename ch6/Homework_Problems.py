#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 
# Write a class named `Fraction` that represents a rational number (a number that can be expressed as the quotient of two integers). It is required to implement the following methods:
# 
# - The `__init__(self, numerator, denominator)` method should accept integer values for the `numerator` and `denominator` arguments and set instance attributes of the same name. If the `denominator` is 0, raise a `ZeroDivisionError` exception. Use the [math.gcd](https://docs.python.org/3/library/math.html#math.gcd) function to find the greatest common divisor (GCD) of the numerator and denominator and then divide each of them by it to "normalize" the fraction. For example, the fraction 28/20 will get normalized to 7/5 since the GCD of 28 and 20 is 4:
# 
#    ```pycon
#    >>> x = Fraction(28, 20)
#    >>> x
#    Fraction(7, 5)
#    ```
# - Implement the basic binary operators (`+`, `-`, `*`, `/`) so that a `Fraction` can combined with either another fraction or an integer. All methods should return a new `Fraction`. Note that you may need to implement "reversed" operators for arithmetic with integers to fully work.
# - The `__neg__` method should return a new `Fraction` instance with the numerator negated.
# - The `__repr__` method should return a string of the form `Fraction(a, b)` where a and b are the numerator and denominator, respectively.
# - The `__eq__` method should should return a boolean indicating that both the numerator and denominator of any two fractions are identical

# The below should print `Fraction(5, 6)` and then raise a `ZeroDivisionError`

# In[ ]:


from problem_1 import Fraction
print(Fraction(1, 2) + Fraction(1, 3))
Fraction(4, 0)


# *NOTE*: In order for the test runner to work, the numerator and denominator attribtues must be named `numerator` and `denominator`

# In[ ]:


import sys
sys.path.insert(0, '..')
from course_utils import Test
sys.path.remove('..')

from problem_1 import Fraction

fraction_examples = [
    (Fraction(6, 4), Fraction(3, 2)),
    (Fraction(1, -2), Fraction(-1, 2)),
    ((Fraction(1, 2) + Fraction(1, 3)), Fraction(5, 6)),
    ((Fraction(3, 4) - Fraction(1, 8)), Fraction(5, 8)),
    ((Fraction(6, 2) * Fraction(4, 3)), Fraction(4, 1)),
    ((Fraction(4, 5) / Fraction(3, 1)), Fraction(4, 15)),
]

Test(examples=fraction_examples).equivalence()


# ## Problem 2
# 
# Make the fraction addition method work with floats and integers:
# 
# ```
# __repr__(Frac(1, 2) + 1) = Fraction(3/2)
# __repr__(Frac(1, 2) + 1.0) = Fraction(3/2)
# __repr__(Frac(1, 2) + 0.6) = Fraction(11/10)
# __repr__(3.2 + Frac(3, 2) = Fraction(47/10)
# ```

# In[ ]:


import sys
sys.path.insert(0, '..')
from course_utils import Test
sys.path.remove('..')

from problem_2 import Fraction

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


# ## Problem 3
# 
# In music, the [pitch](https://en.wikipedia.org/wiki/Pitch_(music)) of a note refers to how high or low the note is. For this problem, you will write a `Pitch` class that represents a musical pitch as identified by a musical note name and a number identifying the pitch's octave. It's easiest to think about pitches by looking at a piano. A piano features a repeating group of 12 keys, 7 of which are white and 5 of which are black:
# 
# <img src="https://imgur.com/TrCgpIL.jpg" width="200">
# 
# The white keys are ordered as C, D, E, F, G, A, and B. After B comes C in the next repeating group of 12 keys. Some pairs of white keys have a black key in between that is denoted either by a sharp (♯) or a flat (♭). Sharp means "higher in pitch", so C♯ is above C. Flat means "lower in pitch", so D♭ is below D. That is, we can refer to the black key between C and D as either C♯ or D♭.
# 
# Since pianos have 88 keys in total, all the notes appear multiple times. In order to refer to a specific key on the piano, it's necessary to say not only the name of the note (e.g., F) but also which group of 12 keys it appears in. One common system for identifying a specific key (or pitch) is called [scientific pitch notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation) (SPN). In SPN, we identify the name of the note along with what *octave* it appears in:
# 
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Piano_Frequencies.svg/2560px-Piano_Frequencies.svg.png" width=700>
# 
# The note colored in cyan is C in octave 4, so we refer to it as C4; the first note in octave 5 is C5, and so on. Some final terminology: the distance between two adjacent notes (e.g., C and C♯, E and F, G♯ and A, etc.) on a piano is called a *semitone*. Note that two white keys that have a black key in between are not considered adjacent, so C and D are two semitones apart, not one.
# 
# ### Specifications
# 
# Your `Pitch` class will represent a musical pitch as identified by the note name and what octave it appears in (see picture above). To make the class useful, you are to overload several operators to perform arithmetic operations on it.
# 
# - The `Pitch` constructor should take a single argument as a string in SPN format, e.g. "D#2". For simplicity, notes with a flat are not to be used. The constructor should work whether a lowercase or uppercase note name is used. Passing a string that is not valid should raise a `ValueError`.
# - After an instance is constructed, it should have two attributes `octave` and `semitone`.
#   - The `octave` attribute is an `int` that represents which octave the pitch appears in.
#   - The `semitone` attribute is also an `int` that represents which note within an octave the pitch is. You should assign the value 0 to C, 1 to C#, 2 to D, and so on until you get to 11 for B.
# - Adding or subtracting an integer, N, to a `Pitch` is to return a new pitch that is N semitones higher or lower, respectively. Augmented addition (`+=`) and subtraction (`-=`) should modify the `Pitch` object in-place.
# - Subtracting two `Pitch` objects should return the number of semitones separating them as an `int`.
# - The `frequency()` method should return the [frequency](https://en.wikipedia.org/wiki/Frequency#Sound) of the pitch as a `float` in units of hertz (Hz). To determine the frequency, we can use the fact that A4 (the yellow note on the picture above) has a frequency of exactly 440 Hz. The frequency of any other note can be determined as
# 
# 
# frequency = 440 * 2 <sup>(semitones between self and A4)/12</sup>
# 
#   where `x` is the number of semitones separating the note from A4. For example, C5 is three semitones above A4, so its frequency can be determined by substituting 3 for `x` in the equation. Notes that are lower than A4 will have negative values for `x`.
# - The `from_frequency` method should be a `@classmethod` that takes a single argument, a frequency in Hz as a `float`, and returns the nearest `Pitch`. This allows us to construct a `Pitch` object only knowing the frequency rather than its representation in SPN. This can be done be inverting the equation above to solve for `x`. Since this will give a `float` for `x`, find the nearest integer using the [round](https://docs.python.org/3/library/functions.html#round) built-in function and then return the `Pitch` that is that many semitones away from A4 (since the frequency of A4 is 440 Hz).
# - Comparing two `Pitch` objects should return the result of comparing their frequencies. All comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`) should work for the object. If you'd like you can use the [functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering) class decorator which allows you to define only two of the comparison operators and provides your class with the remainder.
# - Trying to add, subtract, or compare a `Pitch` object with another object that doesn't make sense should raise a `TypeError` exception. This can be achieved through use of the `NotImplemented` singleton.
# - The `__repr__()` method should return the pitch in SPN as a string.
# 
# ### Note:
# You should construct your class with a bias first towards having neither sharps nor flats (if a white key) and then towards only using sharps (in music, we might determine this based on the key, but for a pitch in isolation, we need to have rules. As such, while your class must be able to parse `d♭2` or `F♭4`, printing them would yield `C#2` and `E4`, respectively.
# 

# ### Error Tests

# In[ ]:


import sys
sys.path.insert(0, '..')
from course_utils import Test
sys.path.remove('..')

from problem_3 import Pitch

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


# ### Functional Tests

# In[ ]:


import sys
sys.path.insert(0, '..')
from course_utils import Test
sys.path.remove('..')

from problem_3 import Pitch

pitch_examples = [
    (Pitch('d♭2'), Pitch('C#2')),
    (Pitch('d♭2').__repr__(), 'C#2'),
    (Pitch('F♭4'), Pitch('E4')),
    (Pitch('c#2').__repr__(), 'C#2'),
    (Pitch('G6').octave, 6),
    (Pitch('D3').semitone, 2),
    (Pitch('A3') + 4, Pitch('C#4')),
    (Pitch('C#4') - 5, Pitch('G#3')),
    ((Pitch('C7') += 4).semitone, 0),
    ((Pitch('C7') += 4).octave, 7),
    ((Pitch('C7') -= 4).semitone, 8),
    ((Pitch('c7') -= 4).octave, 6),
    (Pitch('c4') - Pitch('C3'), 12),
    (Pitch('G#2') - Pitch('F#3'), -10),
    (Pitch('A5').frequency(), 880.0),
    (Pitch.from_frequency(170), Pitch('F3')),
    (str(Pitch('A4') == Pitch('A4')), 'True'),
    (str(Pitch('A4') != Pitch('A4')), 'False'),
    (str(Pitch('A5') >= Pitch('A4')), 'True'),
    (str(Pitch('c#3') < Pitch('A4')), 'True'),   
    (str(Pitch('A4') <= Pitch('A4')), 'True'),
    (str(Pitch('d♭2') > Pitch('c#2')), 'False')
]

Test(examples=pitch_examples).equivalence()

