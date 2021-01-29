class SwiftArray:
    pass


## TESTS BELOW

import sys
sys.path.insert(0, '..')
from test_runners import Test
sys.path.remove('..')

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


