import unittest
import import_ipynb


class Test(unittest.TestCase):
    NUM_SET = {i for i in range(1, 10)}

    def setUp(self):
        import Sudoku_Solver
        self.activity = Sudoku_Solver

    def test_empty(self):
        self.solver = self.activity.Solver('sudoku_input/sudoku_input_1.txt')
        self.solver.solve()
        final_solution = self.solver.cells

        # Check rows.
        for row in final_solution:
            self.assertTrue(Test.check_unique(row))

        # Check columns.
        for i in range(9):
            temp_col = []
            for row in final_solution:
                temp_col.append(row[i])

            self.assertTrue(Test.check_unique(temp_col))

        # Check quadrants.
        for quad_id in range(9):
            temp_quad = []

            for i in range(3):
                for j in range(3):
                    temp_quad.append(final_solution[quad_id // 3 * 3 + i][quad_id % 3 * 3 + j])

            self.assertTrue(Test.check_unique(temp_quad))

    def test_sample(self):
        self.solver = self.activity.Solver('sudoku_input/sudoku_input_2.txt')
        self.solver.solve()
        final_solution = self.solver.cells

        # Check rows.
        for row in final_solution:
            self.assertTrue(Test.check_unique(row))

        # Check columns.
        for i in range(9):
            temp_col = []
            for row in final_solution:
                temp_col.append(row[i])

            self.assertTrue(Test.check_unique(temp_col))

        # Check quadrants.
        for quad_id in range(9):
            temp_quad = []

            for i in range(3):
                for j in range(3):
                    temp_quad.append(final_solution[quad_id // 3 * 3 + i][quad_id % 3 * 3 + j])

            self.assertTrue(Test.check_unique(temp_quad))

    @staticmethod
    def check_unique(num_list):
        return set(num_list) == Test.NUM_SET


if __name__ == '__main__':
    unittest.main()
