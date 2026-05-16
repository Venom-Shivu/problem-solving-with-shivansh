class Solution:
    def lengthOfLongestSubstring(self, s):

        # Dictionary to track last seen position
        seen = {}

        # Left pointer for sliding window
        left = 0

        # Stores maximum length found
        max_length = 0

        # Traverse string using right pointer
        for right, char in enumerate(s):

            # If character already exists inside current window,
            # move left pointer ahead
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            # Update latest index of character
            seen[char] = right

            # Calculate current window length
            current_length = right - left + 1

            # Update maximum length
            max_length = max(max_length, current_length)

        return max_length