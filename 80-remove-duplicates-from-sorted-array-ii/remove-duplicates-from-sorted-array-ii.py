class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # k is the write-index
        k = 0
        
        # Iterating directly over elements is faster than range(len(nums))
        for x in nums:
            # We allow the element if:
            # 1. We have written fewer than 2 elements (k < 2)
            # 2. The current element x is different from the one written two steps ago
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
                
        return k