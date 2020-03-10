import unittest
import sys
import import_ipynb
from Monthly_Compounding import *

class Test(unittest.TestCase):
    
    def test_amount(self):
        self.assertAlmostEqual(amount(5000,0.18,1,12),5978.09,2)

if __name__ == '__main__':
    unittest.main()
