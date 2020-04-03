import unittest
import import_ipynb

import pandas as pd
import numpy as np


class Test(unittest.TestCase):
    def setUp(self):
        self.zero_df = pd.DataFrame(np.zeros((2, 3)),
                                    columns=['col_x', 'col_y', 'col_z'])
        self.old_df = pd.DataFrame({
            'col_x': [1, 1, 2],
            'col_y': [1, 3, 2],
            'col_z': [3, 0, 3]
        })
        self.old_df.index = [0, 2, 5]
        self.df = pd.concat([self.zero_df, self.old_df], axis=0).astype(int)

        import Data_Table_Manipulation
        self.exercise = Data_Table_Manipulation

    def test_zero_df(self):
        pd.testing.assert_frame_equal(self.zero_df, self.exercise.zero_df)

    def test_final_df(self):
        pd.testing.assert_frame_equal(self.df, self.exercise.df)


if __name__ == '__main__':
    unittest.main()
