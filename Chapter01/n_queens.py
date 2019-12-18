BOARD_SIZE = 8
N = 8


# Print out the board in console.
def display_solution(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=' ')
        print()


# Generate a valid solution.
def generate_solution():
    # Check if a queen can be placed in the position.
    def check_next(board, row, col):
        # Check the current column.
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check the upper-left diagonal.
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check the upper-right diagonal.
        for i, j in zip(range(row, -1, -1), range(col, BOARD_SIZE)):
            if board[i][j] == 1:
                return False

        return True

    # Recursively generate a solution.
    def recur_generate_solution(board, row_id):
        # Return if we have reached the last row.
        if row_id >= N:
            return True

        # Iteratively try out cells in the current row.
        for i in range(BOARD_SIZE):
            if check_next(board, row_id, i):
                board[row_id][i] = 1  # try to place a queen at the current cell

                # Return if a valid solution is found.
                final_board = recur_generate_solution(board, row_id + 1)
                if final_board:
                    return True

                board[row_id][i] = 0  # take the queen out of the current cell

        # When the current board has no valid solutions.
        return False

    # Start out with en empty board.
    my_board = [[0 for _ in range(BOARD_SIZE)] for __ in range(BOARD_SIZE)]
    final_solution = recur_generate_solution(my_board, 0)

    # Display the final solution.
    if final_solution is False:
        print('A solution cannot be found.')
    else:
        print('A solution was found.')
        display_solution(my_board)


if __name__ == '__main__':
    generate_solution()
