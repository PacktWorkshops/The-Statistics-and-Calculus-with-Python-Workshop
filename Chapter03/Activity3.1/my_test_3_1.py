import unittest
import ipynb
from ipynb.fs.full.Analyzing_the_Communities_and_Crimes_Dataset import df, \
    group_state_df, crime_df, filtered_df

import pandas as pd
import numpy as np


class Test(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('CommViolPredUnnormalizedData.txt')
        self.df = self.df.replace('?', np.nan)
        self.df = self.df.rename(columns={'racepctblack': 'racePctBlack'})

        races = ['Black', 'White', 'Asian', 'Hisp']

        for race in races:
            self.df['raceCnt' + race] = (self.df['population']
                * self.df['racePct' + race]).astype(int)

        self.group_state_df = self.df.groupby('state')
        self.crime_df = self.df[[
            'burglPerPop', 'larcPerPop', 'autoTheftPerPop', 'arsonsPerPop',
            'nonViolPerPop'
        ]]
        self.filtered_df = self.df[[
            'PctPopUnderPov', 'PctLess9thGrade', 'PctUnemployed',
            'ViolentCrimesPerPop', 'nonViolPerPop'
        ]]

    def test_main_df(self):
        pd.testing.assert_frame_equal(self.df, df)

    def test_other_dfs(self):
        pd.testing.assert_frame_equal(self.group_state_df.sum(), group_state_df.sum())
        pd.testing.assert_frame_equal(self.crime_df, crime_df)
        pd.testing.assert_frame_equal(self.filtered_df, filtered_df)


if __name__ == '__main__':
    unittest.main()
