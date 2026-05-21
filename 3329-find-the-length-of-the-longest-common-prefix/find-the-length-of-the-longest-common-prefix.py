class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Store all prefixes from arr1
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        ans = 0

        # Check prefixes for arr2
        for num in arr2:
            curr = num

            while curr:
                if curr in prefixes:
                    ans = max(ans, len(str(curr)))
                    break
                curr //= 10

        return ans