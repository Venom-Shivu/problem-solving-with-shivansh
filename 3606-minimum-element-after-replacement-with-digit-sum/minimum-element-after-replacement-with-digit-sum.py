class Solution:
    def minElement(self, nums):
        ans = float('inf')

        for x in nums:
            s = 0

            while x:
                s += x % 10
                x //= 10

            if s < ans:
                ans = s

        return ans