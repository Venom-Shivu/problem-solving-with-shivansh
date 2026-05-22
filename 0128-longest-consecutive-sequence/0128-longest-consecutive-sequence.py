class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                curr = num
                length = 1

                while (curr := curr + 1) in s:
                    length += 1

                if length > longest:
                    longest = length

        return longest