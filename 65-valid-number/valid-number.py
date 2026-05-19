class Solution:
    def isNumber(self, s: str) -> bool:
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, ch in enumerate(s):
            
            # Digit
            if ch.isdigit():
                seen_digit = True
            
            # Sign
            elif ch in ['+', '-']:
                
                # Sign only allowed:
                # 1. At beginning
                # 2. Right after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            # Decimal point
            elif ch == '.':
                
                # Dot not allowed after e/E
                # Only one dot allowed
                if seen_dot or seen_e:
                    return False
                
                seen_dot = True
            
            # Exponent
            elif ch in ['e', 'E']:
                
                # Only one e allowed
                # Must have digit before e
                if seen_e or not seen_digit:
                    return False
                
                seen_e = True
                
                # Need digits after e
                seen_digit = False
            
            else:
                return False
        
        return seen_digit