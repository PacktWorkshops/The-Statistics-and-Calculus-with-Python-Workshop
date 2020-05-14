import unittest
import sys
import import_ipynb
from Implementing_the_Runge_Kutta_Method import *

class Test(unittest.TestCase):
    
    def test_deriv(self):
        self.assertEqual(deriv(7,24),625)

if __name__ == '__main__':
    unittest.main()
