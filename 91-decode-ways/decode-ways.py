class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        prev2 = 1   # dp[i-2]
        prev1 = 1   # dp[i-1]

        for i in range(1, len(s)):
            curr = 0

            # Single digit decode
            if s[i] != '0':
                curr += prev1

            # Two digit decode
            if '10' <= s[i-1:i+1] <= '26':
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1