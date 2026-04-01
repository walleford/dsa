def search_matrix(matrix, target):
    # start at top right, if matrix value is bigger, go left
    # if matrix value is smaller, go down
    row, col = 0, len(matrix[0]) - 1

    # basically, until the row reaches the index
    # of the last row and until the column reaches
    # the first value in the row
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        # if val is the target we are done
        if val == target:
            return True
        # if value is greater than target, go left
        elif val > target:
            col -= 1
        # if val is less than target, go down
        else:
            row += 1

    return False