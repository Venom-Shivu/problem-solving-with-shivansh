class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = {}

        # Store prefix -> length
        for num in arr1:
            x = num
            length = len(str(num))

            while x:
                prefixes[x] = length
                x //= 10
                length -= 1

        ans = 0

        for num in arr2:
            x = num

            while x:
                if x in prefixes:
                    ans = max(ans, prefixes[x])
                    break
                x //= 10

        return ans