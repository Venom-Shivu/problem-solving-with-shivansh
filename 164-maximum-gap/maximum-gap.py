class Solution:
    def maximumGap(self, nums):

        n = len(nums)

        if n < 2:
            return 0

        nums.sort()

        ans = 0
        prev = nums[0]

        for i in range(1, n):

            gap = nums[i] - prev

            if gap > ans:
                ans = gap

            prev = nums[i]

        return ans