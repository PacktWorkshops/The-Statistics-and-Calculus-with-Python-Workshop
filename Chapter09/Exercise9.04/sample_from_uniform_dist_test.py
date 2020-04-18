import unittest
import random
import statistics as st

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        calc_means = 10000000
        sample_size = 30
        #Action
        mean_list = []
       # run our loop and collect a sample
        for j in range(calc_means):
            # initialize the variables to track our results
            sample_list = []
            for i in range(sample_size):
                sample_list.append(random.randint(0, 100))
            sample_mean = sum(sample_list) / sample_size
            mean_list.append(sample_mean)
        #Assert
        self.assertAlmostEqual(st.mean(mean_list),50,places=2)
        
        
if __name__ == '__main__':
    unittest.main()
