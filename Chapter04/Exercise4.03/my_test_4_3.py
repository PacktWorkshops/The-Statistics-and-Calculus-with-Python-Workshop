import unittest
import ipynb
from ipynb.fs.full.Introduction_to_Break_Even_Analysis import sols, sols1

from sympy.solvers import solve
from sympy import Symbol


class Test(unittest.TestCase):
    def setUp(self):
        self.x = Symbol('x')

    def test_fixed_price(self):
        self.assertEqual(
            solve(8.99 * self.x - 6.56 * self.x - 1312.13, self.x),
            sols
        )

    def test_fixed_n_burgers(self):
        self.assertEqual(
            solve(400 * self.x - 3936.13, self.x),
            sols1
        )

if __name__ == '__main__':
    unittest.main()
