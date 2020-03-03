import unittest
import import_ipynb
import numpy as np
import scipy.stats as stats


class Test(unittest.TestCase):
	def setUp(self):
		import exercise_8_3
		self.exercise = exercise_8_3

	def test_X(self):
		X = self.exercise.X_rv
		result = X.ppf(0.5)
		self.assertEqual(result, 100.0)

if __name__ == '__main__':
	unittest.main()
	