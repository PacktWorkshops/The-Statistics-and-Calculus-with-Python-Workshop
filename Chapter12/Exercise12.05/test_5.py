import unittest
import sys
import import_ipynb
from Becoming_a_Millionaire import *

class Test(unittest.TestCase):
    
    def test_amount(self):
        self.assertAlmostEqual(amount(10000,0.08,60,365),1214465.26,2)
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(amount,50,60,1000000),57.57,2)

if __name__ == '__main__':
    unittest.main()
