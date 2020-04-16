import unittest
import statsmodels.stats.proportion as prop
import import_ipynb
from z_prop_test import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        success = 5
        sample = 83
        hypoth = 0.05
        alt = 'two-sided'
        #Action
        result = prop.proportions_ztest(success, sample, hypoth, alt)
        #Assert
        self.assertAlmostEqual(result[0],0.392, places = 3)
        self.assertAlmostEqual(result[1],0.695, places = 3) 
        
if __name__ == '__main__':
    unittest.main()
