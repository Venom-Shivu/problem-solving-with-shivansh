class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Build all prefixes from arr1
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        ans = 0

        for num in arr2:
            length = len(str(num))

            while num:
                if num in prefixes:
                    ans = max(ans, length)
                    break

                num //= 10
                length -= 1

        return ans