import unittest
import sys
import import_ipynb
from Maximum_Circle_to_Cone_Volume import *

class Test(unittest.TestCase):
    
    def test_derivative(self):
        self.assertAlmostEqual(derivative(v,1.15),0.0005,4)

    def test_surf_area(self):
        self.assertAlmostEqual(v(3),0.2438,4)


if __name__ == '__main__':
    unittest.main()
