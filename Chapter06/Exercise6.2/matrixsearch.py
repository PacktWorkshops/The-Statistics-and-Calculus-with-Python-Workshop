matrix = [
  [7,  10,  15, 18],
  [25, 29, 35, 47],
  [56, 78, 85, 104]
]

def matrixsearch(matrix, value):
    # Check for edge cases
    if value is None or not matrix:
            return False

    # Initialize the variables
    row = len(matrix)
    col = len(matrix[0])
    start = 0
    end   = row * col - 1

    # Logic for binary search within a sorted matrix
    while start <= end:
        mid = int((start + end) / 2)
        pointer = matrix[int(mid/col)][int(mid%col)]
        print(int(mid/col), int(mid%col))

        if pointer == value:
            return True
        elif pointer < value:
            start = mid + 1
        else:
            end = mid - 1
    return False

sol = matrixsearch(matrix, 78)
print(sol)
# Output: True
