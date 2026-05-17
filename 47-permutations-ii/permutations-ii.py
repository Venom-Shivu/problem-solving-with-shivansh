class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Step 1: Sorting is crucial. It puts duplicates side-by-side
        nums.sort()
        
        n = len(nums)
        used = [False] * n
        
        def backtrack(current_path):
            # Base case: if our path is the same length as nums, we're done
            if len(current_path) == n:
                res.append(current_path[:])
                return
            
            for i in range(n):
                # If we already used this specific index in our current path, move on
                if used[i]:
                    continue
                
                # Step 2: The Duplicate Skip Logic
                # If this number is the same as the previous one AND the previous
                # one isn't currently being used, skip this iteration.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Step 3: Standard backtracking: Mark it, add it, recurse, then undo
                used[i] = True
                current_path.append(nums[i])
                
                backtrack(current_path)
                
                # Undo everything so the next loop can try a different number
                current_path.pop()
                used[i] = False
                
        backtrack([])
        return res