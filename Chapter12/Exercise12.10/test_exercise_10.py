import unittest
import sys
import import_ipynb
from Euler import *

class Test(unittest.TestCase):
    
    def test_euler(self):
        self.assertAlmostEqual(euler(0,1,0.3,0.001),1.487,3)

if __name__ == '__main__':
    unittest.main()
