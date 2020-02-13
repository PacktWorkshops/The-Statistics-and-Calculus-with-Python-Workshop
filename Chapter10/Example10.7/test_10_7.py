import unittest
import sys
import import_ipynb
from Maximum_Minimum import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(10),732.85)

    def test_derivative(self):
        self.assertAlmostEqual(derivative(f,3),11.4,1)


if __name__ == '__main__':
    unittest.main()
