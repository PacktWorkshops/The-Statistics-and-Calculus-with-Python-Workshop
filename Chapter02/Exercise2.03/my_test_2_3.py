import unittest
import import_ipynb

import pandas as pd


class Test(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Carol', 'Dan', 'Eli', 'Fran'],
            'class': ['FY', 'SO', 'SR', 'SO', 'JR', 'SR'],
            'gpa': [90, 93, 97, 89, 95, 92],
            'num_classes': [4, 3, 4, 4, 3, 2],
            'female_flag': [True, False, True, False, False, True]
        })

        self.df = pd.concat([self.df.drop('class', axis=1),
                             pd.get_dummies(self.df['class'])], axis=1)

        import The_Student_Dataset
        self.exercise = The_Student_Dataset

    def test_final_df(self):
        pd.testing.assert_frame_equal(self.df, self.exercise.student_df)


if __name__ == '__main__':
    unittest.main()
