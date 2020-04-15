import unittest
import sys
import import_ipynb
from The_Box_Problem import *

class Test(unittest.TestCase):
    
    def test_derivative(self):
        self.assertAlmostEqual(derivative(v,1.811),-0.01,2)

    def test_v(self):
        self.assertAlmostEqual(v(1.811),96.77,2)


if __name__ == '__main__':
    unittest.main()
