import unittest
import sys
import import_ipynb
from Factorial_Series import *

class Test(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(factorial(5),120)


if __name__ == '__main__':
    unittest.main()
