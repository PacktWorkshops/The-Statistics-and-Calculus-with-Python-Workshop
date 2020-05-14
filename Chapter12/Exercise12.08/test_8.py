import unittest
import sys
import import_ipynb
from Measuring_Radioactive_Decay import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(pert,-2,0,0.5),-0.0004332,7)

    def test_pert(self):
        self.assertAlmostEqual(pert(1,-0.0004332,800),0.7071,4)

if __name__ == '__main__':
    unittest.main()
