#!/usr/bin/env python
# coding: utf-8

# ## Problem 0
# 
# This is the very first problem, and since collections of items in programming are often zero-indexed, we'll call it Problem Zero. You don't have to write code for this problem, but you do need to _read_ code and understand what it is doing.
# 
# The other problems ask you to write code. To help you make sure your code is working, we have provided you with some tests in this file. Here is a test function that we will use to check your code against some examples:

# In[ ]:


def test(function, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        expected = example[-1]
        actual = function(*example[:-1])

        if expected == actual: 
            passed += 1
        else:
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.")


# For Problem 0, open the file called `problem_0.md` and explain what this function is doing by answering the following questions:
# 
# 1. What are the arguments and what types do these arguments need to have for this function to work?
# 1. Walk us through the code line by line. What is happening here?
# 1. Does this function have a return value? How do you know?

# ## Problem 1
# 
# Write a function called `find_twos` that accepts two strings of integers separated by commas and returns a list of integers that appear in both strings and have the digit 2 in them. There should be no duplicates in the output list. Make sure the program works when the lists have different lengths. The list should present the integers in the order that they appear in the _first_ string.
# 
# When you've done Problem 1 correctly, running the following cell should produce "10/10 examples worked as expected."
# 
# For example:
# 
# If you have the following inputs in your function:
# 
# "1, 2, 20,22, 44, 99"
# "3,5, 22, 100, 44, 2"
# 
# The output should be [2, 22]
# 
# There should be no duplicates in your ouput.
# 
# (**Note**: Unfortunately every time you make changes to your `problem_X.py` files, you have to rerun the kernel in this file to get the test to register the new code. We know, it's annoying. We're looking for a reliable fix. In the meantime, go to Kernel > Restart and run your test on your new and improved code!)

# In[ ]:


from problem_1 import find_twos

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


# ## Problem 2
# 
# Write a function called `expand_letter_ranges` that accepts a comma-separated string of letters or letter ranges, and returns a sorted list of all the letters with the ranges expanded into individual letters. The input letters can be either lowercase or uppercase, but each string in the output list should be uppercase. It is not necessary to perform any error checking (ranges that are backwards, non-character input, etc.).
#     
# Note that there are built-in functions, `ord()` and `chr()`, that can convert single characters to integers and vice versa.
# 
# When you've done it right, running the test in the following cell should produce "5/5 examples worked as expected."
# 
# If your function has the following input:
# "b-D,z,m-q,n,C-E"
# 
# Then this is the expected output:
# ['B', 'C', 'D', 'E', 'M', 'N', 'O', 'P', 'Q', 'Z']

# In[ ]:


from problem_2 import expand_letter_ranges

expand_letter_ranges_examples = [
    ("", []),
    ("a-f", ['A','B','C','D','E','F']),
    ("b-D,z,m-q,n,C-E", ['B','C','D','E','M','N','O','P','Q','Z']),
    ("q,r,a,t,v,y,z", ['A','Q','R','T','V','Y','Z']),
    ("b-D,z,m-q,n,C-E", ['B','C','D','E','M','N','O','P','Q','Z']),
]

test(function=expand_letter_ranges, examples=expand_letter_ranges_examples)


# ## Problem 3
# 
# Write a function called `mean` that accepts a whitespace separated string of numbers (integers or floats) and returns their mean. 
# 
# For example, if your function in put was:
# "1 2 3"
# 
# The expected output would be:
# 2.0
# 
# For this problem, you may want to use the built-in `sum()` function, which returns the sum of values in an iterable (such as a list).
# 
# When you've done it right, running the test in the following cell should produce "5/5 examples worked as expected."

# In[ ]:


from problem_3 import mean

mean_examples = [
    ("", 0.0),
    ("1", 1.0),
    ("1 2 3", 2.0),
    ("1 2 3", 2.0),
    ("1 2 3", 2.0),
]

test(function=mean, examples=mean_examples)


# ## Problem 4
# 
# What digits (1 through 9) can replace the letters A, B, and C such that the following equation is true?
# 
# ABC = A×B×C × (A + B + C)
# 
# For example, if A is 1, B is 2, and C is 3 and E is 3, the equation would be:
# 
# 123 ≠ 1×2×3×(1 + 2 + 3) = 36
# 
# so 1, 2, and 3 are clearly not a solution. Rather than solving this problem with your raw brainpower, write a program that checks each combination of digits and returns a collection of the numbers for which it is satisfied, along with their result.
# 
# For this problem please create a function called `find_numbers` that returns a list of the solutions. Each list item should be in the format:
# 
# 'For A, B, and C, the equation solution is ABC'
# 
# When you've solved it correctly, the below cell should print "Great job! You got it!"

# In[ ]:


from problem_4 import find_numbers

solution = [
    'For 1, 3, and 5, the equation solution is 135',
    'For 1, 4, and 4, the equation solution is 144'
]

if find_numbers() == solution:
    print("Great job! You got it!")
else:
    print("Whoops. Try Again.")


# ## Problem 5
# 
# Write a function called `find_day` that takes a collection of dates as slash-separated strings with the month first, then the day, then the year, and returns a collection of the same size with the day of the week on which each of those dates fell, in order.
# 
# There is some implementation advice waiting for you in the `problem_5` file, but first, here's the test:

# In[ ]:


from problem_5 import find_day

find_day_examples = [
    ([""], ["Invalid Entry"]),
    (["/"], ["Invalid Entry"]),
    (["------"], ["Invalid Entry"]),
    (["2/29/2019"], ["Invalid Entry"]),
    (["45/2/1900"], ["Invalid Entry"]),
    (["-1/2/1900"], ["Invalid Entry"]),
    (["02/-2/2019"], ["Invalid Entry"]),
    (["12/43/2018"], ["Invalid Entry"]),
    (["3-4-2020"], ["Invalid Entry"]),
    (["07/4/2008"], ["Friday"]),
    (["01/08/2020"], ["Wednesday"]),
    (["01/8/1900"], ["Monday"]),
    (["02/21/2008"], ["Thursday"]),
    (["02/28/2020", "01/08/2020", "02/29/2020"], ["Friday", "Wednesday", "Saturday"]),
    (["02/28/2020", "01/08/2020", "02/29/2020"], ["Friday", "Wednesday", "Saturday"])

]

test(function=find_day, examples=find_day_examples)


# ## Problem 6
# 
# Write a function called `power_status` that takes in a power grid, represented as a list of the statuses of several homes as a collection ("status" meaning whether their power is working or not), and a _section_ of that grid, represented as two tuples.
# 
# The function then returns a list of booleans indicating the power status for each home in that sector.
# 
# There is some implementation advice waiting for you in the `problem_6` file, but first, here's the test:

# In[ ]:


from problem_6 import power_status

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

