class Solution:
    def maximumGap(self, nums):

        if len(nums) < 2:
            return 0

        nums.sort()

        ans = 0
        nums_local = nums

        for i in range(1, len(nums_local)):

            diff = nums_local[i] - nums_local[i - 1]

            if diff > ans:
                ans = diff

        return ans