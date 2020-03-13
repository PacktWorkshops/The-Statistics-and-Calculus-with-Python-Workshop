import unittest
import ipynb
from ipynb.fs.full.Multi_Var_Break_Even_Analysis import profits_976, \
    profits_999, profits, COST_PER_BURGER, FIXED_COST, AVG_TOWN_BUDGET

import numpy as np


class Test(unittest.TestCase):
    def test_fixed_price_976(self):
        xs = [i for i in range(300, 501)]

        self.assertEqual(
            [Test.get_profit(x, 9.76) for x in xs],
            profits_976
        )

    def test_fixed_price_999(self):
        xs = [i for i in range(300, 501)]

        self.assertEqual(
            [Test.get_profit(x, 9.99) for x in xs],
            profits_999
        )

    def test_profit_matrix(self):
        xs = [i for i in range(300, 501, 2)]
        ys = np.linspace(5, 10, 100)

        self.assertEqual(
            [[Test.get_profit(x, y) for y in ys] for x in xs],
            profits
        )

    @staticmethod
    def get_profit(x, y):
        demand = AVG_TOWN_BUDGET / y
        if x > demand:
            return AVG_TOWN_BUDGET - x * COST_PER_BURGER - FIXED_COST

        return x * (y - COST_PER_BURGER) - FIXED_COST


if __name__ == '__main__':
    unittest.main()
