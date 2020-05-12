import unittest
import sys
import import_ipynb
from Solving_Mixture_Problems_Part_2 import *

class Test(unittest.TestCase):
    
    def test_salt_content1(self):
        self.assertAlmostEqual(salt_content1(5*60),183.0769,4)
    def test_salt_content(self):
        self.assertAlmostEqual(salt_content(300,100,10000,0.4,20,10),183.0769,4)

if __name__ == '__main__':
    unittest.main()
