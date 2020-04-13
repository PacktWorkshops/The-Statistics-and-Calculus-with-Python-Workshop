import unittest
import sys
import import_ipynb
from Tangent_Line import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(1),0)

    def test_derivative(self):
        self.assertAlmostEqual(derivative(f,0.67),-1.33,2)

    def test_point_slope(self):
        self.assertEqual(point_slope(2,1,3),1)


if __name__ == '__main__':
    unittest.main()
