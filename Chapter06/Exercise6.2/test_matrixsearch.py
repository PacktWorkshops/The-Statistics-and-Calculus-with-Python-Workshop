import numpy as np
import matrixsearch
import uniitest

class Test(uniitest.TestCase):

    def test_matrixsearch(self):
        matrix = [
          [7,  10,  15, 18],
          [25, 29, 35, 47],
          [56, 78, 85, 104]
        ]
        value = 78
        # Check for edge cases
        self.assertIsNotNone(matrix)
        self.assertIsNotNone(value)
        result = False
        if value is None or not matrix:
                result = False

        # Initialize the variables
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end   = row * col - 1

        # Logic for binary search within a sorted matrix
        while start <= end:
            mid = (start + end) / 2
            pointer = matrix[mid/col][mid%col]
            print(mid/col, mid%col)

            if pointer == value:
                result = True
            elif pointer < value:
                start = mid + 1
            else:
                end = mid - 1
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
