import unittest
import sys
import import_ipynb
from Finding_the_Minimum_of_a_Surface import *

class Test(unittest.TestCase):
    
    def test_surface(self):
        self.assertAlmostEqual(surface(1,2),0.50,2)

    def test_partial_d(self):
        self.assertAlmostEqual(partial_d(surface,'x',2,2.5),6.22,2)

if __name__ == '__main__':
    unittest.main()
