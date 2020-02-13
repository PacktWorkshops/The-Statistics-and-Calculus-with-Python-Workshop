import unittest
import sys
import import_ipynb
from Integral import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(2),4)

    def test_integral(self):
        self.assertAlmostEqual(integral(f,0,1,100),0.3283,3)


if __name__ == '__main__':
    unittest.main()
