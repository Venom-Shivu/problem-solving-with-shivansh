class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Stores longest palindrome found
        result = ""

        # Tracks maximum palindrome length
        maxLen = 0

        # Treat every character as center
        for i in range(len(s)):

            # ---------- Odd Length Palindrome ----------
            left = right = i

            # Expand outward while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:

                # Update answer if longer palindrome found
                if (right - left + 1) > maxLen:
                    result = s[left:right + 1]
                    maxLen = right - left + 1

                left -= 1
                right += 1

            # ---------- Even Length Palindrome ----------
            left = i
            right = i + 1

            # Expand outward while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:

                # Update answer if longer palindrome found
                if (right - left + 1) > maxLen:
                    result = s[left:right + 1]
                    maxLen = right - left + 1

                left -= 1
                right += 1

        return result