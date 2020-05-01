import unittest
import sys
import import_ipynb
from Runge_Kutta import *

class Test(unittest.TestCase):
    
    def test_deriv(self):
        self.assertEqual(deriv(7,24),625)

if __name__ == '__main__':
    unittest.main()
