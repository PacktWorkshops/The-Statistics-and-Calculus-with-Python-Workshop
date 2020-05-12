import unittest
import sys
import import_ipynb
from Calculating_the_Rate_of_Change_in_Temperature import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(pert,-2,0,68),-1.66,2)

    def test_pert(self):
        self.assertAlmostEqual(pert(103,-1.6608851322143892,1),19.6,1)

if __name__ == '__main__':
    unittest.main()
