def to_generator(map_or_filter):
    pass

# TESTS BEGIN HERE

import sys
sys.path.insert(0, '..')
from phoenix_test.matchers import FailedAssertion, Assertion, assert_that
from phoenix_test.test import Test
sys.path.remove('..')
import types

class ToGeneratorTest(Test):
    def test_map_to_generator(self):
        g = to_generator(map(lambda x: x + 1, [1, 2, 3, 4, 5]))
        assert_that(type(g)).equals(types.GeneratorType)
        assert_that(list(g)).equals([2, 3, 4, 5, 6])

    def test_filter_to_generator(self):
        g = to_generator(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
        assert_that(type(g)).equals(types.GeneratorType)
        assert_that(list(g)).equals([2, 4])

ToGeneratorTest().run()