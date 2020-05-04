import unittest
import sys
import import_ipynb
from Finding_the_Area_of_a_3D_Surface_Part_1 import *

class Test(unittest.TestCase):
    
    def test_cross(self):
        self.assertEqual(cross([2,3,4],[5,6,7]),[-3, 6, -3])

    def test_mag(self):
        self.assertAlmostEqual(mag([1,2,-3]),3.7,1)

    def test_partial_d(self):
        self.assertAlmostEqual(partial_d(surface,'x',0.1,0.2,10),4.36,2)

    def test_surface(self):
        self.assertAlmostEqual(surface(1,2),7.87,2)

    def test_area(self):
        self.assertAlmostEqual(area(surface,-1,1,-1,1),27.98,2)


if __name__ == '__main__':
    unittest.main()
