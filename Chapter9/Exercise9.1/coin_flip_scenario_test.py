import unittest
import random

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample_size = 100000000
        #Action
        result_list = []
        for i in range(sample_size):
            result = random.randint(0, 1)
            result_list.append(result)
        # compile results
        num_of_heads = sum(result_list)
        avg_of_heads = float(num_of_heads) / sample_size
        #Assert
        self.assertAlmostEqual(avg_of_heads,0.50,places=2)
        
        
if __name__ == '__main__':
    unittest.main()
