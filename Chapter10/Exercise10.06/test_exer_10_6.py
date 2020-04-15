import unittest
import sys
import import_ipynb
from The_Optimal_Can import *

class Test(unittest.TestCase):
    
    def test_derivative(self):
        self.assertAlmostEqual(derivative(surf_area,4.835),0.0078,4)

    def test_surf_area(self):
        self.assertAlmostEqual(surf_area(5),220.5,1)


if __name__ == '__main__':
    unittest.main()
