import unittest
import import_ipynb

import random


class Test(unittest.TestCase):
    def setUp(self):
        import The_Tower_of_Hanoi
        self.exercise = The_Tower_of_Hanoi

    def test_simple(self):
        self.assertEqual(7, self.exercise.solve(3))
        self.assertEqual(63, self.exercise.solve(6))

    def test_random(self):
        for _ in range(10):
            temp_n = random.randrange(1, 20, 1)
            self.assertEqual(2 ** temp_n - 1, self.exercise.solve(temp_n))


if __name__ == '__main__':
    unittest.main()
