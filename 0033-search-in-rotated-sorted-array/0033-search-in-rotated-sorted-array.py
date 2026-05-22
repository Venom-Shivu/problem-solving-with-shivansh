class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            val = nums[mid]

            if val == target:
                return mid

            # Left half sorted
            if nums[left] <= val:
                if nums[left] <= target < val:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half sorted
            else:
                if val < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1