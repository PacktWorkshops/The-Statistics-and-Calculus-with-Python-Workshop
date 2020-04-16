import unittest
import scipy.stats as st
import import_ipynb
from twosampTTest import *

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample1 = [452,874,554,447,356,754,558,574,664,682,547,435,245]
        sample2 = [546,547,774,465,459,665,467,365,589,534,456,651,654,665,546,537]
        #Action
        result = st.ttest_ind(sample1,sample2,equal_var = False)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 4) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(-0.1514,0.8813))
        
        
if __name__ == '__main__':
    unittest.main()
