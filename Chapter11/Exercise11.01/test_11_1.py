import unittest
import sys
import import_ipynb
from Finding_the_Length_of_a_Curve import *

class Test(unittest.TestCase):
    
    def test_circle(self):
        self.assertAlmostEqual(circle(0.2),0.98,2)

    def test_derivative(self):
        self.assertAlmostEqual(derivative(circle,0.2),-0.2,1)

    def test_trap_integral(self):
        self.assertAlmostEqual(trap_integral(circle,0.2,0.3,100),0.0978,4)

    def test_curve_length(self):
        self.assertAlmostEqual(curve_length2 (circle,-1,1),3.14,2)


if __name__ == '__main__':
    unittest.main()
