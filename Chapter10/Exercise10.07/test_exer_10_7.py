import unittest
import sys
import import_ipynb
from Two_Ships import *

class Test(unittest.TestCase):
    
    def test_derivative(self):
        self.assertAlmostEqual(derivative(d,1.12),-0.5,1)

    def test_surf_area(self):
        self.assertAlmostEqual(d(2),17.9,1)


if __name__ == '__main__':
    unittest.main()
