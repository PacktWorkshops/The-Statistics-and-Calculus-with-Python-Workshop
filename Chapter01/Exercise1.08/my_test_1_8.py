import unittest
from ipynb.fs.full.Testing_for_Concurrency import Counter


class Test(unittest.TestCase):
    def always_true(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # unittest.main()
    sample_counter = Counter(10)
    sample_counter.run()
