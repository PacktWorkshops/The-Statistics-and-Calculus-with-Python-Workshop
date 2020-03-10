import unittest
import sys
import import_ipynb
from Salt_Content import *

class Test(unittest.TestCase):
    
    def test_salt_content1(self):
        self.assertAlmostEqual(salt_content1(39),469.259,3)
    def test_salt_content(self):
        self.assertAlmostEqual(salt_content(39),470.745,3)

if __name__ == '__main__':
    unittest.main()
