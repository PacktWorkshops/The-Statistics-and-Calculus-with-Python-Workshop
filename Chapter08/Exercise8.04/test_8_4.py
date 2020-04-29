import unittest
import import_ipynb
import numpy as np
import scipy.stats as stats


class Test(unittest.TestCase):
	def setUp(self):
		import Using_the_Normal_Distribution_in_Education
		self.exercise = Using_the_Normal_Distribution_in_Education

	def test_X(self):
		X = self.exercise.X_rv
		result = X.ppf(0.5)
		self.assertEqual(result, 100.0)

if __name__ == '__main__':
	unittest.main()
	