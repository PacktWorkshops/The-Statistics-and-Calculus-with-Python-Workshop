import unittest
import import_ipynb

import random


class Test(unittest.TestCase):
    def setUp(self):
        import Finding_the_Maximum
        self.exercise = Finding_the_Maximum

    def test_simple(self):
        self.assertEqual((1, 3), self.exercise.get_max([1, 3, 2]))
        self.assertEqual((3, 3), self.exercise.get_max([1, 3, 2, 3]))

    def test_random(self):
        def get_max(my_list):
            running_max_index = 0

            # Iterate over index-value pairs.
            for index, item in enumerate(my_list):
                if item >= my_list[running_max_index]:
                    running_max_index = index

            return running_max_index, my_list[running_max_index]

        for _ in range(10):
            temp_list = [random.randrange(1, 50, 1) for __ in range(50)]
            self.assertEqual(get_max(temp_list), self.exercise.get_max(temp_list))


if __name__ == '__main__':
    unittest.main()
