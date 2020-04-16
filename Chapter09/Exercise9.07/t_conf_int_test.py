import unittest
import import_ipynb
from t_conf_int import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        data = [2,3,5,6,9]
        con_lvl = 0.95
        #Action
        result = t_confidence_interval(data,con_lvl)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(1.60,8.40))
        
        
if __name__ == '__main__':
    unittest.main()
