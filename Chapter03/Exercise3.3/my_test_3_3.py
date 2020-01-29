import unittest
import ipynb
from ipynb.fs.full.Model_Selection import X, y, X_train, X_test, y_train, y_test

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split


class Test(unittest.TestCase):
    def setUp(self):
        self.X, self.y = make_blobs(
            n_samples=10000,
            centers=[(-2, 2), (0, 0), (2, 2)],
            shuffle=False,
            random_state=0
        )
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, shuffle=True, random_state=0
        )

    def test_data(self):
        np.testing.assert_equal(self.X, X)
        np.testing.assert_equal(self.y, y)

    def test_split_data(self):
        np.testing.assert_equal(self.X_train, X_train)
        np.testing.assert_equal(self.X_test, X_test)

        np.testing.assert_equal(self.y_train, y_train)
        np.testing.assert_equal(self.y_test, y_test)


if __name__ == '__main__':
    unittest.main()
