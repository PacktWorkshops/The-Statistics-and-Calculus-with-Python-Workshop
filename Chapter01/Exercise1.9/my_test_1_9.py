import unittest
import import_ipynb

import random


class Test(unittest.TestCase):
    def setUp(self):
        import Version_Control_with_Git_and_GitHub
        self.exercise = Version_Control_with_Git_and_GitHub

    def add_elements_truth(self, a, b):
        result = []
        for item_a, item_b in zip(a, b):
            result.append(item_a + item_b)

        return result

    def test_simple(self):
        a = [1, 1, 1]
        b = [1, 1, 1]

        self.assertEqual(self.add_elements_truth(a, b),
                         self.exercise.add_elements(a, b))

    def test_random(self):
        for _ in range(10):
            length = random.randrange(1, 10, 1)
            a = [random.randrange(1, 20, 1) for __ in range(length)]
            b = [random.randrange(1, 20, 1) for __ in range(length)]

            self.assertEqual(self.add_elements_truth(a, b),
                             self.exercise.add_elements(a, b))


if __name__ == '__main__':
    unittest.main()
