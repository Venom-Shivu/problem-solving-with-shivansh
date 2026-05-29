class Solution:
    def minElement(self, nums):
        ans = 46  # max digit sum for <=10000 is 1+0+0+0+0 = 1, for safety use >45

        for x in nums:
            s = 0

            while x:
                s += x % 10
                x //= 10

            if s < ans:
                ans = s

        return ans