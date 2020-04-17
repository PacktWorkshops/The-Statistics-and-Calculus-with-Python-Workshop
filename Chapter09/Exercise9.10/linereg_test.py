import unittest
import numpy as np
import sklearn.linear_model as lm
import import_ipynb
from linereg import *

class Test(unittest.TestCase):
    
    def test1(self):
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
