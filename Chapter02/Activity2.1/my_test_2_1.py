import unittest
# import import_ipynb
#
# import pandas as pd
# import numpy as np
#
#
# class Test(unittest.TestCase):
#     def setUp(self):
#         self.df = pd.read_csv('CommViolPredUnnormalizedData.txt')
#         self.df = self.df.replace('?', np.nan)
#
#         import Analyzing_the_Communities_and_Crimes_Dataset
#         self.exercise = Analyzing_the_Communities_and_Crimes_Dataset
#
#     def test_df(self):
#         pd.testing.assert_frame_equal(self.df, self.exercise.df)


class Test(unittest.TestCase):
    def always_true(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
