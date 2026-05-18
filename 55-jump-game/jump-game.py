class Solution:
    def canJump(self, nums):

        farthest = 0
        last = len(nums) - 1

        for i, jump in enumerate(nums):

            if i > farthest:
                return False

            reach = i + jump

            if reach > farthest:
                farthest = reach

            if farthest >= last:
                return True

        return True