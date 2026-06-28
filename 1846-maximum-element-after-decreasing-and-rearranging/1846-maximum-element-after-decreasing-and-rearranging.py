from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)

        for x in arr:
            cnt[min(x, n)] += 1

        ans = 0
        for x in range(1, n + 1):
            ans = min(ans + cnt[x], x)

        return ans