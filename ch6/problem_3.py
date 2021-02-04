class Stream:
    pass

## TESTS BEGIN HERE

import sys
sys.path.insert(0, '..')
from phoenix_test.matchers import FailedAssertion, Assertion, assert_that
from phoenix_test.test import Test
sys.path.remove('..')


class StreamTests(Test):
    def test_to_list(self):
        assert_that(
            Stream(["holy", "forking", "shirtballs"]).as_list()) \
            .equals(["holy", "forking", "shirtballs"])

    def test_map(self):
        assert_that(
            Stream(["holy", "forking", "shirtballs"]) \
                .map(lambda x: str.capitalize(x)) \
                .as_list()
        ).equals(["Holy", "Forking", "Shirtballs"])

    def test_filter(self):
        assert_that(
            Stream(["holy", "forking", "shirtballs"]) \
                .filter(lambda x: len(x) < 9) \
                .as_list()
        ).equals(["holy", "forking"])

    def test_filter(self):
        assert_that(
            Stream(["holy", "forking", "shirtballs"]) \
                .reduce(lambda x, y: x + y)
        ).equals("holyforkingshirtballs")

    def test_the_whole_flow(self):
        assert_that(
            Stream(["holy", "forking", "shirtballs"]) \
                .map(lambda x: str.capitalize(x)) \
                .filter(lambda x: len(x) < 9) \
                .reduce(lambda x, y: x + y)
        ).equals("HolyForking")


StreamTests().run()