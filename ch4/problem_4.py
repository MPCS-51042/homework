def accepts():
    pass

# TESTS BELOW

from ..test_runners import Test

@accepts(int, int)
def sum(a, b): return a + b
@accepts(type(lambda x: int(x)))
def return_func(func): return func
@accepts(str)
def uppercase(string): return string.upper()
@accepts(str, int)
def multiply_string(s, n): return s * n
@accepts(float)
def square_float(val): return val * val
@accepts(str, str, str)
def concat_three(a, b, c): return a + b + c

accepts_examples = [
    (return_func(uppercase), uppercase),
    (uppercase('all gas no brakes'), 'ALL GAS NO BRAKES'),
    (multiply_string('and on ', 3), 'and on and on and on '),
    (square_float(5.0), 25.0),
    (concat_three('wake ', 'up ', 'samurai'), 'wake up samurai')
]

Test(examples=accepts_examples).equivalence()


