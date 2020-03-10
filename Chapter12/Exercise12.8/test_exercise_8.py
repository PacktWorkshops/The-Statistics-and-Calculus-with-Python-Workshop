import unittest
import sys
import import_ipynb
from Salt_Content import *

class Test(unittest.TestCase):
    
    def test_salt_content(self):
        self.assertAlmostEqual(salt_content(60,900,100,20,3,3),705.2,1)

if __name__ == '__main__':
    unittest.main()
