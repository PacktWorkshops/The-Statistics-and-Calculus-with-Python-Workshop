import unittest
import sys
import import_ipynb
from Solving_Mixture_Problems_Part_4 import *

class Test(unittest.TestCase):
    
    def test_salt_content(self):
        self.assertAlmostEqual(salt_content(15,18,1200,0,15,10),15.94,2)

if __name__ == '__main__':
    unittest.main()
