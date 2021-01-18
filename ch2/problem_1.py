from test import test

def find_twos(string_1, string_2):
    '''
        This function takes in two strings that only contains integers, commas and whitespace and
        returns a list of integers, where each integer,

           1. Appears in both strings
           2. Contains a 2 as a digit in the number.

        Inputs:
            str1, str2 (string): strings that contains integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

        Output:
            A list of integers, where the list contents is described by above. The returned list must not contain duplicates.
        '''
    pass

## TESTS BELOW

find_twos_examples = [
    ("", "", []),
    ("1", "1, 3", []),
    ("2", "", []),
    ("2", "1, 3", []),
    ("2", "2", [2]),
    ("2", "12", []),
    ("12", "2, 12", [12]),
    ("1, 3, 5, 12, 7, 200", "2, 6, 9, 200, 5", [200]),
    ("1, 2, 20, 22, 44, 99", "3, 5, 22, 100, 44, 2", [2, 22]),
    ("1,2, 20,22, 44, 99", "3,5, 22, 100, 44, 2", [2, 22]),
    ("1,2, 20,22, 22,44, 20, 99", "3,5, 22, 100, 44, 2", [2, 22]),
    ("1, 2, 20, 22", "3, 2, 20, 22", [2, 20, 22]),
]

test(function=find_twos, examples=find_twos_examples)
