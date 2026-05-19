class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 -> move left
            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            # 1 -> already correct
            elif nums[mid] == 1:
                mid += 1

            # 2 -> move right
            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1