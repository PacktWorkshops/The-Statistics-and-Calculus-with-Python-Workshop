import unittest
import sys
import import_ipynb
from Determining_the_Interval_of_Convergence_Part_1 import *

class Test(unittest.TestCase):
    
    def test_mystery_sum(self):
        self.assertAlmostEqual(mystery_sum(-2),-0.25,2)

if __name__ == '__main__':
    unittest.main()
