def unique():
    pass

## TESTS BELOW

from ..test_runners import Test, first_digit

unique_examples = [
#     ('', []),
    ('aaadddpppzzzaaa', ['a', 'd', 'p', 'z']),
    ((10, 1, 100, 2019, 2, 25), first_digit, [10, 2019]),
    (('True and 1', '0 or True', '15 + 5', '4 * 5'), eval, ['True and 1', '15 + 5']),
    ((3, 'Chance', 'Kendrick', chr, 25, eval), type, [3, 'Chance', chr])
]

Test(examples=unique_examples, function=unique).generator_function()
