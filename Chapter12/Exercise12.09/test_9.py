import unittest
import sys
import import_ipynb
from Measuring_the_Age_of_a_Historical_Artifact import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(pert,-2,0,0.5),-0.00012,5)

    def test_bin_search2(self):
        self.assertAlmostEqual(bin_search2(pert,1,100000,0.91),779.6,1)

if __name__ == '__main__':
    unittest.main()
