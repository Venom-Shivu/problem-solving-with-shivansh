class Solution:
    def maxProduct(self, nums):

        cur_max = nums[0]
        cur_min = nums[0]

        ans = nums[0]

        for num in nums[1:]:

            # Negative swaps roles
            if num < 0:

                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)

            cur_min = min(num, cur_min * num)

            if cur_max > ans:
                ans = cur_max

        return ans