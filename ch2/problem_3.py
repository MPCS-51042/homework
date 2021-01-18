from test import test

def mean(string_of_numbers):
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    pass

## TESTS BELOW

mean_examples = [
    ("", 0.0),
    ("1", 1.0),
    ("1 2 3", 2.0),
    ("1 2 3", 2.0),
    ("1 2 3", 2.0),
]

test(function=mean, examples=mean_examples)
