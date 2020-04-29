import unittest
import import_ipynb
import pandas as pd
import scipy.stats as stats


class Test(unittest.TestCase):
	def setUp(self):
		import Using_the_Normal_Distribution_in_Finance
		self.exercise = Using_the_Normal_Distribution_in_Finance
		data_path = '../data/MSFT.csv'
		self.msft = pd.read_csv(data_path)
		self.msft.rename(
			columns = lambda x: x.lower().replace(' ', '_'),
			inplace = True
			)
		self.msft['date'] = pd.to_datetime(self.msft['date'])
		self.msft.set_index('date', inplace = True)
		self.msft['returns'] = self.msft['adj_close'].pct_change()
		start_date = '2014-01-01'
		end_date = '2018-12-31'
		self.msft = self.msft.loc[start_date: end_date]

	def test_returns(self):
		user_df = self.exercise.msft
		pd.testing.assert_series_equal(user_df['returns'], self.msft['returns'])
		
		
	def test_shape(self):
		self.assertEqual(self.msft.shape, self.exercise.msft.shape)


	def test_R_rv(self):
		R_mean = self.msft['returns'].mean()
		R_std = self.msft['returns'].std()

		R_rv = stats.norm(
			loc = R_mean,
			scale = R_std
		)
		user_rv = self.exercise.R_rv
		
		self.assertEqual(R_rv.mean(), user_rv.mean())
		

if __name__ == '__main__':
	unittest.main()
	