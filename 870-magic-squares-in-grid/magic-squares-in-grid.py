class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])

        def isMagic(r, c):

            # Center of a valid 3x3 magic square is always 5
            if grid[r+1][c+1] != 5:
                return False

            # Check distinct numbers 1-9
            nums = set()

            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]

                    if val < 1 or val > 9:
                        return False

                    nums.add(val)

            if len(nums) != 9:
                return False

            # Rows
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != 15:
                    return False

            # Columns
            for j in range(3):
                if (grid[r][c+j] +
                    grid[r+1][c+j] +
                    grid[r+2][c+j]) != 15:
                    return False

            # Diagonals
            if (grid[r][c] +
                grid[r+1][c+1] +
                grid[r+2][c+2]) != 15:
                return False

            if (grid[r][c+2] +
                grid[r+1][c+1] +
                grid[r+2][c]) != 15:
                return False

            return True

        ans = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    ans += 1

        return ans