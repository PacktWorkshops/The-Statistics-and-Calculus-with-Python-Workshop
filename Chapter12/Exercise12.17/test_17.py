import unittest
import sys
import import_ipynb
from Using_Eulers_Method_to_Evaluate_a_Function import *

class Test(unittest.TestCase):
    
    def test_euler(self):
        self.assertAlmostEqual(euler(0,1,0.3,0.001),1.487,3)

if __name__ == '__main__':
    unittest.main()
