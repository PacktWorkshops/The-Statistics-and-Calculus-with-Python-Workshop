import unittest
import sys
import import_ipynb
from Calculating_the_Time_of_Death import *

class Test(unittest.TestCase):
    
    def test_pert(self):
        self.assertAlmostEqual(pert(33.6,-0.4055,3),9.95,2)

if __name__ == '__main__':
    unittest.main()
