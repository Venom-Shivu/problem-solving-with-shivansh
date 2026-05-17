class Solution(object):

    def firstMissingPositive(self, nums):

        n = len(nums)

        i = 0

        while i < n:

            val = nums[i]

            # Correct position for current value
            correct = val - 1

            # Valid number and not already placed correctly
            if 1 <= val <= n and nums[correct] != val:

                # Faster manual swap
                temp = nums[correct]
                nums[correct] = val
                nums[i] = temp

            else:
                i += 1

        # Find first missing positive
        for i in xrange(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1