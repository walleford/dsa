# each row is sorted array.
# each array is smaller than the next array, 
# so entire matrix is sorted

# time: O(log(m*n))
# space: O(1)
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // 2][mid % n]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid -1
    return False