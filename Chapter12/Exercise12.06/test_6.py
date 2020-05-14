import unittest
import sys
import import_ipynb
from Calculating_the_Population_Growth_Rate_Part_1 import *

class Test(unittest.TestCase):
    
    def test_amount(self):
        self.assertAlmostEqual(amount(21000000,0.04,17.3,1000000),41951845.46,2)
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(pert,1,100,2),17.3,1)

if __name__ == '__main__':
    unittest.main()
