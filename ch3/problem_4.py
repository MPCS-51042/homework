def taxes_owed(income):
    '''
        This function takes in an income as an integer or float and
        returns taxes owed as a float, truncated at two digits.

        Inputs:
            income (integer or float)

        Output:
            taxes owed (float)
        '''
    pass

#TESTS BELOW

from test import test

tax_examples = [
    (40000, 0.0),
    (42000, 40.0),
    (70000, 900.0),
    (100000, 2600.0),
    (125000, 4450.0),
    (187000, 10910.0),
    (238000, 18100.0),
    (1000000, 170400.0),
]

if __name__ == '__main__':
    test(function=taxes_owed, examples=tax_examples)

