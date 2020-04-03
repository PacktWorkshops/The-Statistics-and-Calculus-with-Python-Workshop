import unittest
import ipynb
from ipynb.fs.full.Analyzing_the_Communities_and_Crimes_Dataset import df

import pandas as pd
import numpy as np


class Test(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('CommViolPredUnnormalizedData.txt')
        self.df = self.df.replace('?', np.nan)

    def test_df(self):
        pd.testing.assert_frame_equal(self.df, df)


if __name__ == '__main__':
    unittest.main()
