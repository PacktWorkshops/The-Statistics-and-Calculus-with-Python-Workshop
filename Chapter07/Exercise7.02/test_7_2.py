import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing


class Test(unittest.TestCase):
	def setUp(self):
		import Calculating_Descriptive_Statistics
		self.exercise = Calculating_Descriptive_Statistics
		self.games = self.exercise.games


	def test_proportion_of_4_5(self):
	# covers points 1 and 5
		boolean_series = self.exercise.games['average_user_rating'] == 4.5
		true_result = boolean_series.mean()
		user_result = self.exercise.proportion_of_ratings_4_5
		self.assertAlmostEqual(user_result, true_result)

if __name__ == '__main__':
	unittest.main()
	