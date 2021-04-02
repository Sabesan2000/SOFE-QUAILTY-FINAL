from parameterized import parameterized
from datetime import datetime
import unittest
import sys

class TestSequence(unittest.TestCase):

    @parameterized.expand([
        ["foo", "a", "a", ],
        ["bar", "a", "b"],
        ["lee", "b", "b"],
    ])
    def test_thing(self, name, a, b):
        unittest.TestCase.assertEqual(self, first=a, second=b, msg=name)


if __name__ == '__main__':
    with open(f'DynamicTestData/t-{datetime.now().strftime("%Y-%m-%dT%H%M%S")}.txt', "w") as output:
        runner = unittest.TextTestRunner(output)
        unittest.main(testRunner=runner)
