import unittest
import import_ipynb

import numpy as np
import math


class Test(unittest.TestCase):
    def setUp(self):
        import Timing_Vectorization_in_NumPy
        self.exercise = Timing_Vectorization_in_NumPy

    def for_add_truth(self):
        return [item + 1 for item in self.exercise.my_list]

    def vec_add_truth(self):
        return self.exercise.my_array + 1

    def for_mul_truth(self):
        return [item * 2 for item in self.exercise.my_list]

    def vec_mul_truth(self):
        return self.exercise.my_array * 2

    def for_sqrt_truth(self):
        return [math.sqrt(item) for item in self.exercise.my_list]

    def vec_sqrt_truth(self):
        return np.sqrt(self.exercise.my_array)

    def test_add(self):
        self.assertEqual(self.for_add_truth(), self.exercise.for_add())
        np.testing.assert_equal(self.vec_add_truth(), self.exercise.vec_add())

    def test_mul(self):
        self.assertEqual(self.for_mul_truth(), self.exercise.for_mul())
        np.testing.assert_equal(self.vec_mul_truth(), self.exercise.vec_mul())

    def test_sqrt(self):
        self.assertEqual(self.for_sqrt_truth(), self.exercise.for_sqrt())
        np.testing.assert_equal(self.vec_sqrt_truth(), self.exercise.vec_sqrt())


if __name__ == '__main__':
    unittest.main()
