import unittest
import sys
import import_ipynb
from Interval_of_Convergence2 import *

class Test(unittest.TestCase):
    
    def test_mystery_sum(self):
        self.assertAlmostEqual(mystery_sum(-10),-0.204,3)

if __name__ == '__main__':
    unittest.main()
