def vectorize():
    pass

## TESTS BELOW
import sys
sys.path.append("..")
from test_runners import Test, first_digit
sys.path.remove('..')

vectorize_examples = [
    (int, [], []),
    (int, ['55'], [55]),
    (int, ['-1', '0', 100], [-1, 0, 100]),
    (sorted, [['d', 'b', 'a', 'c'], 'albus', [55, -10, 15, 12]], [['a', 'b', 'c', 'd'], ['a', 'b', 'l', 's', 'u'], [-10, 12, 15, 55]]),
    (eval, ['"Wasabi" + "Ginger"', '5 * 10', 'True and False'], ['WasabiGinger', 50, False])
]

Test(examples=vectorize_examples, function=vectorize).passed_function()
