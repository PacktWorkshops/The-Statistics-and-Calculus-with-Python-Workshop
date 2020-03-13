import unittest
import ipynb
from ipynb.fs.full.Matrix_Solution import solve_eq_sys

import numpy as np


class Test(unittest.TestCase):
    def test_real(self):
        coeff_matrix = np.array([
            [1, 3, -2],
            [3, 5, 6],
            [2, 4, 3]
        ])

        c = np.array([1, 31, 19])

        np.testing.assert_array_almost_equal(
            solve_eq_sys(coeff_matrix, c),
            np.array([1.0, 2.0, 3.0])
        )

    def test_singular(self):
        coeff_matrix = np.array([
            [1, 3, -2],
            [3, 5, 6],
            [2, 6, -4]
        ])

        c = np.array([1, 31, 19])

        self.assertFalse(solve_eq_sys(coeff_matrix, c))


if __name__ == '__main__':
    unittest.main()
