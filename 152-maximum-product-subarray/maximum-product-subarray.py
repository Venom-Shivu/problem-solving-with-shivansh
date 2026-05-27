class Solution:
    def maxProduct(self, nums):
        max_prod = min_prod = ans = nums[0]

        for x in nums[1:]:

            # Negative flips max/min
            if x < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(x, x * max_prod)
            min_prod = min(x, x * min_prod)

            ans = max(ans, max_prod)

        return ans