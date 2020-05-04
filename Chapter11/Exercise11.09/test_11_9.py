import unittest
import sys
import import_ipynb
from Machin_Series import *

class Test(unittest.TestCase):
    
    def test_arctan(self):
        self.assertAlmostEqual(arctan(1/2,10),0.46,2)

if __name__ == '__main__':
    unittest.main()
