import unittest
import sys
import import_ipynb
from Calculating_Compound_Interest_Part_1 import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(amount,25,30,8000),25.33,2)

    def test_amount(self):
        self.assertAlmostEqual(amount(2000,0.055,25.334,12),8030.9,1)

if __name__ == '__main__':
    unittest.main()
