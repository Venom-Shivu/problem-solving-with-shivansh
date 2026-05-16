class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        currentRow = 0
        direction = -1

        for char in s:

            rows[currentRow] += char

            # Change direction at top or bottom
            if currentRow == 0 or currentRow == numRows - 1:
                direction *= -1

            currentRow += direction

        return "".join(rows)