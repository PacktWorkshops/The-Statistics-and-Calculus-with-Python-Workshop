import unittest
import import_ipynb
import numpy as np
import scipy.stats as stats

class Test(unittest.TestCase):
	def setUp(self):
		import Checking_If_a_Random_Variable_Follows_a_Binomial_Distribution
		self.exercise = Checking_If_a_Random_Variable_Follows_a_Binomial_Distribution

	def test_Z(self):
		Z = self.exercise.Z_rv
		prob_1 = Z.pmf(1)
		Z_true = stats.binom(n = 12, p = 0.04)
		test_value = Z_true.pmf(1)
		self.assertEqual(prob_1, test_value)

		
if __name__ == '__main__':
	unittest.main()
	