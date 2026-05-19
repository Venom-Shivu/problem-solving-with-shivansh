class Solution:
    def plusOne(self, digits):
        
        n = len(digits)
        
        # Traverse from last digit
        for i in range(n - 1, -1, -1):
            
            # If digit < 9
            # just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9
            # becomes 0 due to carry
            digits[i] = 0
        
        # If all digits were 9
        return [1] + digits