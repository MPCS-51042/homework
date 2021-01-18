def maketuple():
    pass

## TESTS BELOW
import sys
sys.path.append("..")
from test_runners import Test, first_digit
sys.path.remove('..')

@maketuple
def return_func(func): return func
@maketuple
def return_func_array(): return [int, eval, chr]
@maketuple
def uppercase(string): return string.upper()
@maketuple
def square(val): return val * val
@maketuple
def square_multi(*args): return [val * val for val in args]
@maketuple
def arbitrary_multi(*args, func=int): return [func(arg) for arg in args]

maketuple_examples = [
    (return_func(int), (int,)),
    (return_func_array(), (int, eval, chr)),
    (uppercase('im calm'), ('I', 'M', ' ', 'C', 'A', 'L', 'M')),
    (square(5), (25,)),
    (square_multi(1, 2, 3, 4, 5), (1, 4, 9, 16, 25)),
    (arbitrary_multi('wake', 'up', func=uppercase), (('W', 'A', 'K', 'E'), ('U', 'P')))
]

Test(examples=maketuple_examples).equivalence()

