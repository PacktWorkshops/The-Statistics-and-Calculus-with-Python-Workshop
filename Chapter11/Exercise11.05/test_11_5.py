import unittest
import sys
import import_ipynb
from Finding_the_Length_of_an_Archimedean_Spiral import *

class Test(unittest.TestCase):
    
    def test_r(self):
        self.assertAlmostEqual(r(pi),5.38,2)

    def test_opposite(self):
        self.assertAlmostEqual(opposite(r(0),r(0.0001),0.0001),0.0002,4)

    def test_trap_integral(self):
        self.assertAlmostEqual(spiral(r,0,2*pi),41.5,1)


if __name__ == '__main__':
    unittest.main()
