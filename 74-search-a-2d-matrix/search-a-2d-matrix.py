class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            # convert 1D index -> 2D index
            r = mid // cols
            c = mid % cols

            value = matrix[r][c]

            if value == target:
                return True

            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False