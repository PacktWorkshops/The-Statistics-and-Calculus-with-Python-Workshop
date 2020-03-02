import unittest
import import_ipynb
import pandas as pd

class Test(unittest.TestCase):
	def setUp(self):
		import exercise_7_1
		self.exercise = exercise_7_1
		self.games = self.exercise.games


	def test_df_dim(self):
	# covers points 1 and 5
		dim_games_2 = self.exercise.games2.shape
		self.assertEqual(dim_games_2, (4311, 16))

	def test_value_counts_languages(self):
	# covers points 2 and 3
		value_counts_lang = self.games['languages'].fillna('EN').value_counts().loc['EN']
		self.assertEqual(value_counts_lang, 2558)
		
	def test_num_of_languages(self):
	# covers points 4 and 5
		filled_series = self.games['languages'].fillna('EN')
		target_series = filled_series.str.split(',').apply(lambda x: len(x))
		self.assertEqual(target_series.loc[284921427], 17)
		self.assertEqual(target_series.loc[284926400], 1)


if __name__ == '__main__':
	unittest.main()
	