class Solution:
    def maxSubArray(self, nums):

        best = curr = nums[0]

        for num in nums[1:]:

            if curr < 0:
                curr = num
            else:
                curr += num

            if curr > best:
                best = curr

        return best