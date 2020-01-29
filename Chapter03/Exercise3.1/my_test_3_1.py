import unittest
import ipynb
from ipynb.fs.defs.Min_Max_Scaling import min_max_scale

import numpy as np


class Test(unittest.TestCase):
    def min_max_scale_truth(self, data, a, b):
        data_max = np.max(data)
        data_min = np.min(data)

        return a + (b - a) * (data - data_min) / (data_max - data_min)

    def test_base(self):
        base_array = np.array([1, 2, 3, 4])

        np.testing.assert_equal(
            self.min_max_scale_truth(base_array, 0, 5),
            min_max_scale(base_array, 0, 5)
        )

    def test_random(self):
        random_array = np.random.normal(size=1000)

        np.testing.assert_equal(
            self.min_max_scale_truth(random_array, 0, 10),
            min_max_scale(random_array, 0, 10)
        )


if __name__ == '__main__':
    unittest.main()
