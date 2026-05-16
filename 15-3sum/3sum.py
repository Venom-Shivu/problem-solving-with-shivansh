class Solution:
    def threeSum(self, nums):

        nums.sort()

        n = len(nums)
        res = []

        for i in range(n - 2):

            x = nums[i]

            # Skip duplicates
            if i > 0 and x == nums[i - 1]:
                continue

            # No possible solution ahead
            if x > 0:
                break

            l = i + 1
            r = n - 1

            while l < r:

                total = x + nums[l] + nums[r]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:

                    res.append([x, nums[l], nums[r]])

                    lv = nums[l]
                    rv = nums[r]

                    # Skip duplicates aggressively
                    while l < r and nums[l] == lv:
                        l += 1

                    while l < r and nums[r] == rv:
                        r -= 1

        return res