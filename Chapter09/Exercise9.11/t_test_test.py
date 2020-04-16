import unittest
import import_ipynb
from t_test import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample = [159,155,157,125,103,122,101,82,228,199,195,110,191,151,119,119,112,87,190,87]
        hypoth_value = 130
        sig_level = .05
        test_type = 'upper'
        #Action
        result = t_test(sample, hypoth_value, sig_level, test_type)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 4) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(0.9956,0.166))
        
        
if __name__ == '__main__':
    unittest.main()
