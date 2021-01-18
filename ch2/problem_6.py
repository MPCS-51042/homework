from test import test

def power_status(grid, row_bounds, col_bounds):
    '''
    Determines the status of the homes within a sector. A sector is defined by a row  and column
    boundary. A row boundary is a tuple of two integers from ([0, nRows), [0, nRows)) and the column
    boundary is a tuple of two integers ([0, nColumns), [0, nColumns)), where nRows is equal to the
    number of rows in the grid and nColumns is equal to the number of columns in the grid. Make note
    the upper-bound is exclusive!

    Based on the boundary specified, the function returns a list indicating the power status of the
    homes within the bounds of the sector. Order in the list does matter! Start at the top-left of the
    sector and work your way down towards the bottom-right corner. You increase by in the columns. Once
    you finish with a row then you move to the next row (i.e., increase by 1).

    You can assume the the first component of the boundary is always less than the second component.

    Inputs:
        grid(list of list of bools): the status of the homes
        row_bounds(tuple of ints): the row boundary for the sector
        col_bounds(tuple of ints): the column boundary for the sector

    Outputs:
        Returns a list of booleans indicating the power status of the homes within the bounds of the sector.

    '''
    pass

neighborhood_grid = [
    [True,  True,  True],
    [True,  False, False],
    [False, True,  True]
]

power_status_examples = [
    (neighborhood_grid, (0, 1), (0, 2), [True, True]),
    (neighborhood_grid, (0, 2), (0, 2), [True, True, True, False]),
    (neighborhood_grid, (0, 2), (1, 3), [True, True, False, False]),
    (neighborhood_grid, (1, 2), (0, 3), [True, False, False]),
    (neighborhood_grid, (1, 3), (0, 2), [True, False, False, True]),
    (neighborhood_grid, (1, 3), (1, 3), [False, False, True, True]),
    (neighborhood_grid, (2, 3), (0, 1), [False]),
    (neighborhood_grid, (2, 3), (0, 3), [False, True, True]),
    (neighborhood_grid, (0, 3), (0, 3), [True, True, True, True, False, False, False, True, True]),
    (neighborhood_grid, (0, 3), (0, 2), [True, True, True, False, False, True]),
    (neighborhood_grid, (0, 3), (1, 3), [True, True, False, False, True, True]),
    (neighborhood_grid, (0, 3), (2, 3), [True, False, True]),
]

test(function=power_status, examples=power_status_examples)


