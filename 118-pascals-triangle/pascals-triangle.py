class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            prev = result[-1]

            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]

            result.append(row)

        return result[:numRows]