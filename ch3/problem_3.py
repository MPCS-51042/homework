def fill_completions(fd):
    pass


def find_completions(prefix, c_dict):
    pass


def main():
    pass

if __name__ == '__main__':
    main()

## TESTS BELOW

issues = 0

import os
print(os.getcwd())
with open("./articles.txt", "r") as f:
    c_dict = fill_completions(f)

if (c_dict == None) or (len(c_dict) != 354):
    issues += 1
    print("Looks like your dictionary length is not 354 items long.")

if find_completions("za", c_dict) != {'zara', 'zakharova', 'zapad'}:
    issues += 1
    print("Looks like the za prefix did not return the correct results of {'zakharova', 'zapad', 'zara'}.")

if find_completions("lum", c_dict) != {'lumley', 'lump', 'lumet'}:
    issues += 1
    print("Looks like the za prefix did not return the correct results of {'lumley', 'lump', 'lumet'}.")

if find_completions("multis", c_dict) != set():
    issues += 1
    print("Looks like the multis prefix did not return the correct response of an empty set.")

print(f"{4 - issue_counter} out of 4 checks succeeded.")

