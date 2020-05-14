import unittest
import sys
import import_ipynb
from Calculating_Compound_Interest_Part_2 import *

class Test(unittest.TestCase):
    
    def test_amount(self):
        self.assertAlmostEqual(amount(1,1,1,360*24*60*60),2.71828,5)

if __name__ == '__main__':
    unittest.main()
