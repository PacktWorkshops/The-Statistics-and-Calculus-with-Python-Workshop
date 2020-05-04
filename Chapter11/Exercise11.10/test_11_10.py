import unittest
import sys
import import_ipynb
from Calculating_the_Value_of_π_Using_Eulers_Expression import *

class Test(unittest.TestCase):
    
    def test_arctan(self):
        self.assertAlmostEqual(sqrt(6*sum([1/(i**2) for i in range(1,n+1)])),3.14159,5)

if __name__ == '__main__':
    unittest.main()
