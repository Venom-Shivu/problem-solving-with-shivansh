class Solution:
    def grayCode(self, n: int):

        size = 1 << n

        return [i ^ (i >> 1) for i in range(size)]