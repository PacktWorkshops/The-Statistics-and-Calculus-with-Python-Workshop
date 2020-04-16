import unittest
import random

class Test(unittest.TestCase):
    
    def test1(self):
        #Assume
        sample_size = 10000000
        bet = 1
        #Action
        net_money = 0
        wins = 0
        money_track = []
        trials_track = []
        
        # create a for loop and collect the results in a list
        for i in range(1,sample_size+1):
            result = random.randint(1,38)
            #an odd number means we land on red, with the exception of 37, which means 0
            if result % 2 == 1 and result != 37:
                net_money += bet
                wins += 1
            else:
                net_money -= bet
            money_track.append(net_money/i)
            trials_track.append(i)
        #Assert
        self.assertAlmostEqual(net_money/sample_size,-0.05263157894736842,places=2)
        
        
if __name__ == '__main__':
    unittest.main()
