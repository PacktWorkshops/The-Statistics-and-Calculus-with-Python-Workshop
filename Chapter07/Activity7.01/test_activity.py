import unittest
import import_ipynb
import pandas as pd

class Test(unittest.TestCase):
	def setUp(self):
		import Activity
		self.exercise = Activity
		self.games = self.exercise.games

	def test_df_dim(self):
		dim_games = self.exercise.games.shape
		self.assertEqual(dim_games, (4311, 18))

	def test_value_impute_languages(self):
		imputed_series = self.games['languages'].fillna('EN')
		pd.testing.assert_series_equal(imputed_series, self.exercise.games['languages'])
		
	def test_multilingual_series(self):
		number_of_languages = self.games['languages'].str.split(',').apply(lambda x: len(x))
		multilingual = number_of_languages == 1
		multilingual = multilingual.astype(int).map({0:'multilingual', 1:'monolingual'})
		multilingual.name = 'multilingual'
		pd.testing.assert_series_equal(multilingual, self.exercise.games['multilingual'])


if __name__ == '__main__':
	unittest.main()
	