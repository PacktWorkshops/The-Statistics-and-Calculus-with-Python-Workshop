import unittest
import import_ipynb
from z_conf_int import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        data = [7.5] * 100
        st_dev = 2.3
        con_lvl = 0.95
        #Action
        result = z_confidence_interval(data,st_dev,con_lvl)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(7.05,7.95))
        
        
if __name__ == '__main__':
    unittest.main()
