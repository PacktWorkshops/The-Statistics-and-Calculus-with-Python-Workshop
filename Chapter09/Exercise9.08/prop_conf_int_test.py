import unittest
import import_ipynb
from prop_conf_int import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        p_hat = 0.52
        n = 500
        con_lvl = 0.95
        #Action
        result = prop_confidenct_interval(p_hat,n,con_lvl)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 3) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(0.476,0.564))
        
        
if __name__ == '__main__':
    unittest.main()
