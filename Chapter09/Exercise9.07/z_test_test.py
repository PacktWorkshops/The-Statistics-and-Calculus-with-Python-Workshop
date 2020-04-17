import unittest
import import_ipynb
from z_test import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample = [80.94]*25
        pop_st_dev = 11.6
        hypoth_value = 85
        sig_level = .05
        test_type = 'lower'
        #Action
        result = z_test(sample, pop_st_dev, hypoth_value, sig_level, test_type)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 4) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(-1.75,0.0401))
        
        
if __name__ == '__main__':
    unittest.main()
