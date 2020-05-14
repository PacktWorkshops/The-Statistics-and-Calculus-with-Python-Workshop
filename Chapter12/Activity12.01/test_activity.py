import unittest
import sys
import import_ipynb
from Finding_the_Velocity_and_Location_of_a_Particle import *

class Test(unittest.TestCase):
    
    def test_dx(self):
        self.assertEqual(dxist(0),1.0)

    def test_dy(self):
        self.assertAlmostEqual(dy(0),12.6,1)

    def test_speed(self):
        self.assertAlmostEqual(speed(1.0),4.8,1)

if __name__ == '__main__':
    unittest.main()
