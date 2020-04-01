import unittest
import nbformat


class Test(unittest.TestCase):
    def setUp(self):
        nb = nbformat.read('The_N_Queens_Problem.ipynb', as_version=4)
        for cell in nb.cells:
            if len(cell.outputs) > 0:
                output_text = cell.outputs[0].text
                break

        output_lines = output_text.split('\n')[1: -1]
        self.board = [list(map(int, row[: -1].split(' ')))
                      for row in output_lines]

    def test_attack(self):
        def check_row_wise(board, row, col):
            for i in range(row):
                if board[i][col] == 1:
                    return False

            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 1:
                    return False

            for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
                if board[i][j] == 1:
                    return False

            return True

        for row_id in range(len(self.board)):
            for col_id in range(len(self.board)):
                if self.board[row_id][col_id] == 1:
                    self.assertTrue(check_row_wise(self.board, row_id, col_id))


if __name__ == '__main__':
    unittest.main()
