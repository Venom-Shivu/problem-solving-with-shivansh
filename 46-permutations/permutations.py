class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        def solve(index):
            # Step 1: If we've reached the end, we've got a full permutation
            if index == n:
                # We need to append a copy (nums[:]) otherwise it gets modified later
                result.append(nums[:])
                return
            
            # Step 2: Try every available number for the current position
            for i in range(index, n):
                
                # Step 3: Swap the current index with the loop index
                # This 'fixes' a number at the current position
                nums[index], nums[i] = nums[i], nums[index]
                
                # Step 4: Move to the next position in the array
                solve(index + 1)
                
                # Step 5: Backtrack! Swap them back so the next loop iteration 
                # starts with the original array order
                nums[index], nums[i] = nums[i], nums[index]
        
        solve(0)
        return result