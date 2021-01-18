from problem_4 import taxes_owed
import csv

def total_impact(strategy):
    '''
        This function takes in a tax strategy as a string and
        returns a tuple of tax_revenue and poverty_burden.

        Inputs:
            tax strategy (string)

        Output:
            tax_revenue and poverty_burden (tuple, float and integer)
        '''
    pass

## TESTS BELOW

from test import test

impact_examples = [
    ("flat_rate", (146450.0, 13, 55450.0)),
    ("graduated_rate", (300300.0, 8, 36000.0)),
]

test(function=total_impact, examples=impact_examples)
