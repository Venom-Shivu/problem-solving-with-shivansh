# Starting the programming journey 🚀
# Problem: Find two numbers in the list whose sum equals the target

class Solution:
    def twoSum(self, nums, target):
        
        # Dictionary to store numbers we've already seen
        # Format -> {number : index}
        seen = {}
        
        # Loop through each number along with its index
        for i, num in enumerate(nums):
            
            # Instead of checking every pair manually,
            # think: "What number do I need to reach the target?"
            complement = target - num
            
            # If that required number already exists in our dictionary,
            # then we found the answer
            if complement in seen:
                
                # Return index of previous number + current index
                return [seen[complement], i]
            
            # If not found yet,
            # store the current number with its index
            # so future elements can check against it
            seen[num] = i