import unittest
import sys
import import_ipynb
from Find_the_Quickest_Route import *

class Test(unittest.TestCase):
    
    def test_t(self):
        self.assertEqual(t(0),3.8)

    def test_derivative(self):
        self.assertAlmostEqual(derivative(t,0),-0.2,1)


if __name__ == '__main__':
    unittest.main()
