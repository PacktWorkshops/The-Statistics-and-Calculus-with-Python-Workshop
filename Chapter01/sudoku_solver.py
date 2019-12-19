from copy import deepcopy


class Solver:
    def __init__(self, input_path):
        # Read in the input file and initialize the puzzle
        with open(input_path, 'r') as f:
            lines = f.readlines()

        self.cells = [list(map(int, line.split(','))) for line in lines]

    # Print out the initial puzzle or solution in a nice format.
    def display_cell(self):
        print('-' * 23)

        for i in range(9):
            for j in range(9):
                print(self.cells[i][j], end=' ')

                if j % 3 == 2:
                    print('|', end=' ')
            print()

            if i % 3 == 2:
                print('-' * 23)
        print()

    # Functions to find a solution.
    def solve(self):
        # True/False for whether a number is present in a row, column, or quadrant.
        def get_presence(cells):
            present_in_row = [{num: False for num in range(1, 10)}
                              for _ in range(9)]
            present_in_col = [{num: False for num in range(1, 10)}
                              for _ in range(9)]
            present_in_quad = [{num: False for num in range(1, 10)}
                               for _ in range(9)]

            for row_id in range(9):
                for col_id in range(9):
                    temp_val = cells[row_id][col_id]
                    # If a cell is not empty, update the corresponding row,
                    # column, and quadrant.
                    if temp_val > 0:
                        present_in_row[row_id][temp_val] = True
                        present_in_col[col_id][temp_val] = True
                        present_in_quad[row_id // 3 * 3 + col_id // 3][temp_val] = True

            return present_in_row, present_in_col, present_in_quad

        # A dictionary for empty locations and their possible values.
        def get_possible_values(cells):
            present_in_row, present_in_col, present_in_quad = get_presence(cells)
            possible_values = {}

            for row_id in range(9):
                for col_id in range(9):
                    temp_val = cells[row_id][col_id]
                    if temp_val == 0:
                        possible_values[(row_id, col_id)] = []

                        # If a number is not present in the same row, column,
                        # or quadrant as an empty cell, add it to the list of
                        # possible values of that cell.
                        for num in range(1, 10):
                            if (not present_in_row[row_id][num]) \
                                    and (not present_in_col[col_id][num]) \
                                    and (not present_in_quad[row_id // 3 * 3 + col_id // 3][num]):
                                possible_values[(row_id, col_id)].append(num)

            return possible_values

        # Fill in empty cells that have only one possible value.
        def simple_update(cells):
            update_again = False
            possible_values = get_possible_values(cells)

            for row_id, col_id in possible_values:
                if len(possible_values[(row_id, col_id)]) == 1:
                    update_again = True
                    cells[row_id][col_id] = possible_values[(row_id, col_id)][0]

            # Recursively update with potentially new possible values.
            if update_again:
                cells = simple_update(cells)

            return cells

        # Recursively solve the puzzle
        def recur_solve(cells):
            cells = simple_update(cells)
            possible_values = get_possible_values(cells)
            if len(possible_values) == 0:
                return cells  # return when all cells are filled

            # Find the empty cell with fewest possible values.
            fewest_num_values = 10
            for row_id, col_id in possible_values:
                if len(possible_values[(row_id, col_id)]) == 0:
                    return False  # return if an empty is invalid
                if len(possible_values[(row_id, col_id)]) < fewest_num_values:
                    fewest_num_values = len(possible_values[(row_id, col_id)])
                    target_location = (row_id, col_id)

            for value in possible_values[target_location]:
                dup_cells = deepcopy(cells)
                dup_cells[target_location[0]][target_location[1]] = value
                potential_sol = recur_solve(dup_cells)

                # Return immediately when a valid solution is found.
                if potential_sol:
                    return potential_sol

            return False  # return if no valid solution is found

        print('Initial puzzle:')
        self.display_cell()

        final_solution = recur_solve(self.cells)
        if final_solution is False:
            print('A solution cannot be found.')
        else:
            self.cells = final_solution
            print('Final solution:')
            self.display_cell()


if __name__ == '__main__':
    solver = Solver('sudoku_input/sudoku_input_2.txt')
    solver.solve()
