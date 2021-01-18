def find_numbers():
    '''
        This function computes the combinations of the numbers, 1 through 9, for which

        ABC = A*B*C*(A+B+C)
    '''

solution = [
    'For 1, 3, and 5, the equation solution is 135',
    'For 1, 4, and 4, the equation solution is 144'
]

if find_numbers() == solution:
    print("Great job! You got it!")
else:
    print("Whoops. Try Again.")

