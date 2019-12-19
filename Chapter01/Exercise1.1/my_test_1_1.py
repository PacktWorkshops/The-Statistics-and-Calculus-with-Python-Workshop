import unittest
from io import StringIO
import sys

import import_ipynb


class Test(unittest.TestCase):
    def setUp(self):
        import Divisibility_with_Conditionals
        self.exercise = Divisibility_with_Conditionals

        if self.exercise.x % 6 == 0:
            self.truth = 'x is divisible by 6'
        elif self.exercise.x % 2 == 0:
            self.truth = 'x is divisible by 2'
        elif self.exercise.x % 3 == 0:
            self.truth = 'x is divisible by 3'
        else:
            self.truth = 'x is not divisible by 2 or 3'

    # def test_x(self):
    #     self.assertEqual(self.exercise.x, 12)

    def test_truth(self):
        with open('output.txt', 'r') as f:
            data = f.readline()

        self.assertEqual(self.truth, data)

if __name__ == '__main__':
    unittest.main()
