import unittest
import import_ipynb
import pandas as pd

class Test(unittest.TestCase):
	def setUp(self):
		import Using_a_String_Column_to_Produce_a_Numerical_Column
		self.exercise = Using_a_String_Column_to_Produce_a_Numerical_Column
		self.games = self.exercise.games2


	def test_df_dim(self):
		dim_games_2 = self.exercise.games2.shape
		self.assertEqual(dim_games_2, (4311, 16))

	def test_value_counts_languages(self):
		value_counts_lang = self.games['languages'].fillna('EN').value_counts().loc['EN']
		self.assertEqual(value_counts_lang, 2558)
		
	def test_num_of_languages(self):
		filled_series = self.games['languages'].fillna('EN')
		target_series = filled_series.str.split(',').apply(lambda x: len(x))
		target_series.name = 'n_languages'
		pd.testing.assert_series_equal(target_series, self.games['n_languages'])


if __name__ == '__main__':
	unittest.main()
	