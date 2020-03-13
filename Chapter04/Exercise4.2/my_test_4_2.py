import unittest


class Test(unittest.TestCase):
    def always_true(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
