#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 
# In the Swift programming language, the [Array](https://developer.apple.com/documentation/swift/array) datatype (somewhat equivalent to Python's `list`) has a number of methods which `list` in Python does not have. For this problem, you are to write a subclass of `list` that provides some of these methods.
# 
# ### Specifications
# 
# - The class should be named `SwiftArray` and should inherit from the built-in `list` class.
# - The `allSatisfy(predicate)` method tests whether all items in the list satisfy a given _predicate_ (function of one argument that returns a Boolean value).
# - The `drop(predicate)` method returns a list containing only elements of the original list that do not satisfy the given predicate. As with the `allSatisfy` method, the predicate is a function taking one argument and returning a Boolean value. Elements in the returned list should be in the same order they appear in the SwiftArray.
# - The `min(by)` method returns the minimum element in the list. The `by` argument should take a default value of `None`, in which case elements are compared using their value directly. The `by` argument allows a non-default comparison to be made between elements; it should be a function taking two arguments and returning `True` if the first argument should be ordered before its second argument and `False` otherwise.
# - The `partition(predicate)` method reorders the elements of the list such that all elements that match the given predicate are after all element the elements that don't match. Note that this is an in-place operation, i.e., it should not return a new list. This method also returns the index of the first element in the reordered list that matches the predicate.
# 
# ### Example Interaction
# 
# ```pycon
# >>> x = SwiftArray([1, -3, 10, 5])
# >>> x.allSatisfy(lambda v: isinstance(v, int))
# True
# >>> def even(v):
# ...     return v % 2 == 0
# >>> x.drop(even)
# [1, -3, 5]
# >>> x.min()
# -3
# >>> x.min(lambda a, b: abs(a) < abs(b))
# 1
# >>> x.min(lambda a, b: a > b)
# 10
# >>> first = x.partition(lambda v: v < 0)
# >>> x
# [1, 10, 5, -3]
# >>> x[first]
# -3
# ```

# In[ ]:


import sys
sys.path.insert(0, '..')
from course_utils import Test
sys.path.remove('..')

from problem_1 import SwiftArray

partition_test = SwiftArray([1, 2, 3, 4])
partition_test.partition(lambda x: x < 2)

swift_array_examples = [
    (str(isinstance(SwiftArray([33]), list)), "True"),
    (str(isinstance(SwiftArray([33]), SwiftArray)), "True"),
    (str(SwiftArray([1, 2, 3, 4]).allSatisfy(lambda x: x < 3)), "False"),
    (str(SwiftArray([1, 2, 3, 4]).allSatisfy(lambda x: type(x) == int)), "True"),
    (SwiftArray([1, 2, 3, 4]).drop(lambda x: x < 3), [3, 4]),
    (SwiftArray([1, 2, -1, 4]).min(), -1),
    (SwiftArray(['bb','a','ccc']).min(lambda x, y: len(x) < len(y)), "a"),
    (SwiftArray([1, 2, 3, 4]).partition(lambda x: x < 2), 3),
    (partition_test, [2, 3, 4, 1])
]

Test(examples = swift_array_examples).equivalence()


# ## Problem 2: Chicago Public Libraries
# 
# In this problem, we're going to continue exploring [open data](https://data.cityofchicago.org) from the City of Chicago, except this time we're going to take advantage of object-oriented programming to build the foundation for a hypothetical "library application". We have provided you with a CSV file with data on each public library in Chicago including its name, hours of operation, address, website, and location. You are asked to write three classes that will allow a user to easily interact with this data.
# 
# ### Specifications
# 
# The specifications below indicate what classes/methods must be implemented to receive full credit. However, you should feel free to implement helper methods/functions if you find doing so to be useful.
# 
# #### Library Class
# 
# - Write a class named `Library`, each instance of which represents a single public library in Chicago.
# - The `__init__(self, data)` method should receive a dictionary corresponding to a row in the CSV file (see suggested CSV reading code in City Class). In its body, it should create the following attributes:
# 
#   - `self.name` -- name of the library
#   - `self.hours` -- hours of operation (it's up to you how you want to store this data)
#   - `self.address` -- street address of the library
#   - `self.city` -- what city the library is in
#   - `self.state` -- what state the library is in
#   - `self.zip` -- the ZIP code of the library
#   - `self.phone` -- the phone number of the library
#   - `self.url` -- the URL for the library's website
#   - `self.location` -- the location of the library as an instance of
#     `Coordinate` (see specifications in Coordinate Class
# 
# - The `open_website(self)` method should open the website of the library using the [webbrowser.open_new_tab()](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new_tab) function from the standard library.
# - The `is_open(self, time)` method should accept an instance of [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) and return a boolean indicating whether the library is open.
# - The `distance(self, coord)` method should accept an instance of `Coordinate` and return the distance in miles "as the crow flies" from the specified location to the library. See the description below for how to calculate distances using latitudes/longitudes.
# - The `full_address(self)` method should return a multi-line string (that is, a string with a newline character within it) with the street address, city, state, and ZIP code of the library
# 
# #### Coordinate Class
# 
# - The `Coordinate` class stores a latitude/longitude pair indicating a physical location on Earth.
# - The `__init__(self, latitude, longitude)` method should accept two floats that represent the latitude and longitude in radians.
# - `Coordinate.fromdegrees(cls, latitude, longitude)` should be a `@classmethod` that accepts two floats representing the latitude and longitude in degrees and returns an instance of `Coordinate`.
# - The `distance(self, coord)` method should accept another instance of `Coordinate` and calculate the distance in miles to it from the current instance.
# - The `as_degrees(self)` method should return a tuple of the latitude and longitude in degrees.
# - The `show_map(self)` method should open up Google Maps on a web browser with a point placed on the latitude/longitude. The URL you can use for this is `http://maps.google.com/maps?q=<latitude>,<longitude>` where `<latitude>` and `<longitude>` have been replaced by the corresponding decimal degrees.
# 
# #### City Class
# 
# - The `City` class stores a list of libraries in the city.
# - The `__init__(self, filename)` method accepts a filename for the CSV file in which our library data is stored. It should create an attribute called `libraries` that is a list of `Library` instances. To iterate over the rows in the CSV file, you can use the following code:
# 
# ```python
# import csv
# 
# with open(filename, 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         ...
# ```
# 
# - The `nearest_library(self, coord)` method accepts an instance of `Coordinate` and returns the `Library` instance that is closest to the given coordinates.
# 
# #### Calculating distance between points
# 
# Since the library locations are given as latitude/longitude coordinates, we need a way to calculate distance given two such pairs. One recommended way to do this is using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula), which is
# 
# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a65dbbde43ff45bacd2505fcf32b44fc7dcd8cc0" width="600px" />
# 
# where `d` is the distance between the two points, `r` is the radius of the Earth (use 3961 miles), φ1, φ2 are the latitude of point 1 and latitude of point 2 (in radians), λ1, λ2 are the longitude of point 1 and longitude of point 2 (in radians). Note that the data you are given is in degrees, not radians, so make sure you [convert it](https://en.wikipedia.org/wiki/Radian#Conversion_between_radians_and_degrees) first.
# 
# ### Example Interaction
# 
# The example below shows an example interaction with these classes at a Python console. Note that for this example, I've implemented a [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) method in the `Library` and `Coordinate` classes to get a nice string representation; feel free to do the same if you wish.
# 
# ```pycon
# >>> chicago = City('libraries.csv')
# >>> chicago.libraries[:5]
# [Library(Albany Park),
#  Library(Altgeld),
#  Library(Archer Heights),
#  Library(Austin),
#  Library(Austin-Irving)]
# >>> [x for x in chicago.libraries if x.name.startswith('N')]
# [Library(Near North),
#  Library(North Austin),
#  Library(North Pulaski),
#  Library(Northtown)]
# >>> the_bean = Coordinate.fromdegrees(41.8821512, -87.6246838)
# >>> chicago.nearest_library(the_bean)
# Library(Harold Washington-HWLC)
# >>> time = datetime(2017, 10, 9, 20, 30)
# >>> [x for x in chicago.libraries if x.is_open(time)]
# [Library(Harold Washington-HWLC),
#  Library(Sulzer Regional),
#  Library(Woodson Regional)]
# >>> austin = chicago.libraries[3]
# >>> print(austin.full_address())
# 5615 W. Race Avenue
# CHICAGO, IL 60644
# >>> austin.location
# Coordinate(41.889272153514526, -87.76571186722818)
# ```

# In[ ]:




