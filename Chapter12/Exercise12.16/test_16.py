import unittest
import sys
import import_ipynb
from Solving_Differential_Equations_by_Eulers_Method import *

class Test(unittest.TestCase):
    
    def test_euler(self):
        self.assertEqual(euler(0,1,2,0.5),5.0625)

if __name__ == '__main__':
    unittest.main()
