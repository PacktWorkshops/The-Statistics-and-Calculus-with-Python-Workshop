import unittest
import sys
import import_ipynb
from Curve_Length import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(5),10)

    def test_derivative(self):
        self.assertEqual(round(derivative(f,1),1),2.0)

    def test_trap_integral(self):
        self.assertEqual(round(trap_integral(f,0,1,10),1),1.0)

    def test_curve_length(self):
        self.assertEqual(round(curve_length(f,0,2,1000),1),4.5)


if __name__ == '__main__':
    unittest.main()
