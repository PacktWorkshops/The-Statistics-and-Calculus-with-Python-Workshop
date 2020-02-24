import unittest
import sys
import import_ipynb
from Curve_Length3 import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(1),3.1)

    def test_derivative(self):
        self.assertEqual(round(derivative(f,2),2),73.55)

    def test_trap_integral(self):
        self.assertEqual(round(trap_integral(f,1,2,100),1),9.9)

    def test_curve_length(self):
        self.assertEqual(round(curve_length2(f,-2,1),1),9.6)


if __name__ == '__main__':
    unittest.main()
