import unittest
import scipy.stats as st
import import_ipynb
from Activity import *

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
        
    def test2(self):
        #Assume
        sample1 = [452,874,554,447,356,754,558,574,664,682,547,435,245]
        sample2 = [546,547,774,465,459,665,467,365,589,534,456,651,654,665,546,537]
        #Action
        result = st.ttest_ind(sample1,sample2,equal_var = False)
        result2 = tuple(map(lambda x: isinstance(x, float) and round(x, 4) or x, result))
        #Assert
        self.assertSequenceEqual(result2,(-0.1514,0.8813))
        
    def test3(self):
        #Assume
        x = [1,2,3,4,5]
        x = np.array(x).reshape(-1,1)
        y = [1,2,1.3,3.75,2.25]
        #Action
        model = lm.LinearRegression()
        model.fit(x,y)
        coeff = float(model.coef_)
        intercept = float(model.intercept_)
        #Assert
        self.assertEqual(round(intercept,3), 0.785)
        self.assertEqual(round(coeff,3), 0.425)
        
        
if __name__ == '__main__':
    unittest.main()
        
