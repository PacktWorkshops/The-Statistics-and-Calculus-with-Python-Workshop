import unittest
import random

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample_size = 10000000
        #Action
        num_of_heads = 0
        heads_list = []
        trials_list = []
        freq_list = []
        # create a for loop and collect the results in a list
        for i in range(1,sample_size+1):
            result = random.randint(0, 1)
            if result == 1:
                num_of_heads += 1
            avg_of_heads = float(num_of_heads) / i
            heads_list.append(num_of_heads)
            trials_list.append(i)
            freq_list.append(avg_of_heads)
        #Assert
        self.assertAlmostEqual(avg_of_heads,0.50,places=2)
        
        
if __name__ == '__main__':
    unittest.main()
