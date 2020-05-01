import unittest
import import_ipynb
import numpy as np

class Test(unittest.TestCase):
	def setUp(self):
		import Calculate_Average_Wins_in_Roulette
		self.exercise = Calculate_Average_Wins_in_Roulette

	def test_roulette(self):
		roulette = self.exercise.roulette
		result = roulette(1)
		self.assertIn(result, [i for i in range(37)])

	def test_payoff(self):
		payoff = self.exercise.payoff
		result_1 = payoff(1, units=1)
		result_2 = payoff(25, units=1)
		self.assertEqual(result_1, -1)
		self.assertEqual(result_2, 1)
		
if __name__ == '__main__':
	unittest.main()
	