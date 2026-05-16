class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        n = len(nums)

        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            x = nums[i]

            l = i + 1
            r = n - 1

            while l < r:

                total = x + nums[l] + nums[r]

                # Better answer found
                if abs(total - target) < abs(best - target):
                    best = total

                if total < target:
                    l += 1

                elif total > target:
                    r -= 1

                else:
                    return target

        return best