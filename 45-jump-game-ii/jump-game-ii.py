class Solution(object):

    def jump(self, nums):

        n = len(nums)

        # Already at last index
        if n <= 1:
            return 0

        jumps = 0
        currentEnd = 0
        farthest = 0

        # No need to process last index
        for i in xrange(n - 1):

            # Farthest reachable index
            if i + nums[i] > farthest:
                farthest = i + nums[i]

            # Current jump range finished
            if i == currentEnd:

                jumps += 1
                currentEnd = farthest

        return jumps