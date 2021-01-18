from problem_4 import taxes_owed

def inflection_point():
    '''
        This function returns a float representing the income at which
        Townsville's graduated income tax would be higher than a flat
        5% income tax.
    '''
    pass

## TESTS BELOW

inflection_income = inflection_point()

if inflection_income == 163334.0:
    print(f"Yep, ${inflection_income} is the income at which someone starts paying more in graduated income tax than with the flat rate.")
else:
    print("Nope, try again.")

