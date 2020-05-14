import unittest
import sys
import import_ipynb
from Calculating_Interest import *

class Test(unittest.TestCase):
    
    def test_amount1(self):
        self.assertEqual(amount1(3500,0.02,1),70.0)

    def test_amount(self):
        self.assertEqual(amount(3500,0.02,1,1),3570.0)

if __name__ == '__main__':
    unittest.main()
