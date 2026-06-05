from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        strs = [str(x) for x in nums]

        def cmp(a, b):
            if a + b > b + a:
                return -1
            return 1 if a + b < b + a else 0

        strs.sort(key=cmp_to_key(cmp))

        if strs[0] == "0":
            return "0"

        return "".join(strs)