from test import test

def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    pass

## TESTS BELOW

expand_letter_ranges_examples = [
    ("", []),
    ("a-f", ['A','B','C','D','E','F']),
    ("b-D,z,m-q,n,C-E", ['B','C','D','E','M','N','O','P','Q','Z']),
    ("q,r,a,t,v,y,z", ['A','Q','R','T','V','Y','Z']),
    ("b-D,z,m-q,n,C-E", ['B','C','D','E','M','N','O','P','Q','Z']),
]

test(function=expand_letter_ranges, examples=expand_letter_ranges_examples)