import unittest
import sys
import import_ipynb
from Finding_Where_the_Predator_Catches_the_Prey import *

class Test(unittest.TestCase):
    
    def test_dist(self):
        self.assertEqual(dist(1,1,4,5),5.0)

    def test_position(self):
        self.assertEqual(towards(1,1,2,2.732),[0.5000110003630132, 0.8660190526287391])

    def test_chase(self):
        self.assertAlmostEqual(chase(),24.0,1)

if __name__ == '__main__':
    unittest.main()
