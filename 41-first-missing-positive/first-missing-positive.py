class Solution(object):

    def firstMissingPositive(self, nums):

        n = len(nums)

        # Place every number at its correct index
        i = 0

        while i < n:

            current = nums[i]

            correct_index = current - 1

            # Place current number correctly if possible
            if (1 <= current <= n and
                    nums[i] != nums[correct_index]):

                nums[i], nums[correct_index] = \
                    nums[correct_index], nums[i]

            else:
                i += 1

        # Find first missing positive
        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1