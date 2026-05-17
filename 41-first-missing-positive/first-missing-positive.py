class Solution(object):

    def firstMissingPositive(self, nums):

        n = len(nums)
        i = 0

        while i < n:

            v = nums[i]

            if 1 <= v <= n and nums[v - 1] != v:

                nums[i], nums[v - 1] = nums[v - 1], nums[i]

            else:
                i += 1

        i = 0

        while i < n:

            if nums[i] != i + 1:
                return i + 1

            i += 1

        return n + 1