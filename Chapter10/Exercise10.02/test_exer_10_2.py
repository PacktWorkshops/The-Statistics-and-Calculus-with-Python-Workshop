import unittest
import sys
import import_ipynb
from Find_the_Area_Under_a_Curve import *

class Test(unittest.TestCase):
    
    def test_f(self):
        self.assertAlmostEqual(trap_integral(f,3,4,100),46.75,2)

    def test_g(self):
        self.assertAlmostEqual(trap_integral(g,0,pi/4,100),2.12,2)

    def test_h(self):
        self.assertAlmostEqual(trap_integral(h,2,4,100),18.4,1)


if __name__ == '__main__':
    unittest.main()
