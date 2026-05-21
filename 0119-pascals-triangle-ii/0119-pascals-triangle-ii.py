class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        value = 1

        for k in range(1, rowIndex + 1):
            value = value * (rowIndex - k + 1) // k
            row.append(value)

        return row