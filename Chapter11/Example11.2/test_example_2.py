import unittest
import sys
import import_ipynb
from Curve_Length2 import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertAlmostEqual(f(0.2),0.98,2)

    def test_derivative(self):
        self.assertAlmostEqual(derivative(f,0.1),-0.1,2)

    def test_trap_integral(self):
        self.assertAlmostEqual(trap_integral(f,0,0.5,10),0.528,3)

    def test_curve_length(self):
        with self.assertRaises(ValueError):
            curve_length(f,-1,1,100)


if __name__ == '__main__':
    unittest.main()
