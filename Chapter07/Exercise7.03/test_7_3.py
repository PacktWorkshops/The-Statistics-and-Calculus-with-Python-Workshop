import unittest
import import_ipynb
import pandas as pd


class Test(unittest.TestCase):
	def setUp(self):
		import Practicing_EDA
		self.exercise = Practicing_EDA
		self.games = self.exercise.games

	def test_round_price(self):
	# covers point 2
		rounded_series = self.exercise.games['price'].round()
		pd.testing.assert_series_equal(rounded_series, self.exercise.games['price'])
		#self.assertEqual(rounded_series, self.exercise.games['price'])

	def test_cat_price(self):
	# covers point 4
		true_result = self.exercise.games['price'] == 0
		true_result = true_result.astype(int).map({0:'paid', 1:'free'})
		true_result.name = 'cat_price'
		user_result = self.exercise.games['cat_price']
		pd.testing.assert_series_equal(user_result, true_result)
		#self.assertAlmostEqual(user_result, true_result)


if __name__ == '__main__':
	unittest.main()
	