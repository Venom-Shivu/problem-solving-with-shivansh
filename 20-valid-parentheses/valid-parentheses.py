class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # Opening bracket
            if ch not in mapping:
                stack.append(ch)

            else:

                # Stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False

                stack.pop()

        return len(stack) == 0