import unittest
import sys
import import_ipynb
from Trapezoidal_Rule import *

class Test(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(f(3),9)

    def test_trap_integral(self):
        self.assertAlmostEqual(trap_integral(f,0,1,5),0.34,2)


if __name__ == '__main__':
    unittest.main()
