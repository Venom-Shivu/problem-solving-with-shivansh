class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = [False] * n
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)

        count = 0

        def backtrack(row):

            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):

                d1 = row - col + n
                d2 = row + col

                if cols[col] or diag1[d1] or diag2[d2]:
                    continue

                cols[col] = True
                diag1[d1] = True
                diag2[d2] = True

                backtrack(row + 1)

                cols[col] = False
                diag1[d1] = False
                diag2[d2] = False

        backtrack(0)

        return count