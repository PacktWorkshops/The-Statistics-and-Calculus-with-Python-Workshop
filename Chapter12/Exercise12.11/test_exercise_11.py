import unittest
import sys
import import_ipynb
from Projectile import *

class Test(unittest.TestCase):
    
    def test_bin_search(self):
        self.assertAlmostEqual(bin_search(dy,1.25,1.3,0),1.253,3)

    def test_position(self):
        self.assertEqual(position(-2,3,1.145),(0.031374484385746366, 14.515587014923222))

if __name__ == '__main__':
    unittest.main()
