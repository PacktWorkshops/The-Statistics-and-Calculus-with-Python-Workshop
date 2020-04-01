import unittest


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.small_params = 5
        self.med_params = 5000
        self.large_params = 10000

    def test_small(self):
        small_counter = Counter(self.small_params)
        small_counter.run()
        self.assertEqual(small_counter.value, self.small_params)

    def test_med(self):
        med_counter = Counter(self.med_params)
        med_counter.run()
        self.assertEqual(med_counter.value, self.med_params)

    def test_large(self):
        large_counter = Counter(self.large_params)
        large_counter.run()
        self.assertEqual(large_counter.value, self.large_params)


if __name__ == '__main__':
    unittest.main()
