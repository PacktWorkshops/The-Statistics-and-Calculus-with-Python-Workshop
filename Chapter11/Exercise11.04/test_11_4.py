import unittest
import sys
import import_ipynb
from Finding_the_Length_of_Insulation_in_a_Roll import *

class Test(unittest.TestCase):
    
    def test_r(self):
        self.assertAlmostEqual(r(24*pi),7.6,1)

    def test_opposite(self):
        self.assertAlmostEqual(opposite(r(0),r(0.0001),0.0001),0.0002,4)

    def test_trap_integral(self):
        self.assertAlmostEqual(spiral(r,0,2*pi*23.5),1107.5,1)


if __name__ == '__main__':
    unittest.main()
