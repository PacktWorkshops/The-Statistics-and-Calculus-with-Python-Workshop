import unittest
import sys
import import_ipynb
from Growth_Rate import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(pert,0,2,52.5/42),0.02479,5)

if __name__ == '__main__':
    unittest.main()
