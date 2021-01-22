from itertools import product
from pprint import pprint

def full_paths(path_components, base_path='/'):
    pass

## TESTS BELOW

path_components_1 = ['usr', ['lib', 'bin'], 'config', ['x', 'y', 'z']]
expected_1 = [
    '/usr/lib/config/x',
    '/usr/lib/config/y',
    '/usr/lib/config/z',
    '/usr/bin/config/x',
    '/usr/bin/config/y',
    '/usr/bin/config/z'
]

path_components_2 = ['codes', ['python', 'c', 'c++'], ['Makefile']]
base_path = '/home/user/'
expected_2 = [
    '/home/user/codes/python/Makefile',
    '/home/user/codes/c/Makefile',
    '/home/user/codes/c++/Makefile'
]

if not full_paths(path_components_1) == expected_1:
    print(f"Looks like a path component of \n {path_components_1} \n doesn't return the correct solution of \n {expected_1}")

if not full_paths(path_components_2, base_path) == expected_2:
    print(f"Looks like a path component of \n {path_components_2} with a base path of \n {base_path} doesn't return the correct solution of \n {expected_2}")

else:
    print("Looks like your solutions passes our tests! Nice!")

