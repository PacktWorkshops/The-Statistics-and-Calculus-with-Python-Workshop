import unittest
import sys
import import_ipynb
from Finding_the_Constant import *

class Test(unittest.TestCase):
    
    def test_mystery_constant(self):
        self.assertAlmostEqual(sum([1/factorial(n) for n in range(10000)]),2.71828,5)

if __name__ == '__main__':
    unittest.main()
