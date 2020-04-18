import unittest
import statistics as st
import numpy as np

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        calc_means = 10000000
        sample_size = 30
        #Action
        mean_list = []
        for j in range(calc_means):
            # initialize the variables to track our results
            sample_list = []
            for i in range(sample_size):
                draw = np.random.exponential(1)
                sample_list.append(draw)
            sample_mean = sum(sample_list) / sample_size
            mean_list.append(sample_mean)

        #Assert
        self.assertAlmostEqual(st.mean(mean_list),1,places=2)
        
        
if __name__ == '__main__':
    unittest.main()
