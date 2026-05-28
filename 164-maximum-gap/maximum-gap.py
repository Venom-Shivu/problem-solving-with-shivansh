class Solution:
    def maximumGap(self, nums):

        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        size = max(1, (mx - mn) // (n - 1))
        cnt = (mx - mn) // size + 1

        buckets = [[-1, -1] for _ in range(cnt)]

        # fill buckets
        for x in nums:

            idx = (x - mn) // size

            b = buckets[idx]

            if b[0] == -1:
                b[0] = x
                b[1] = x
            else:
                if x < b[0]:
                    b[0] = x
                elif x > b[1]:
                    b[1] = x

        ans = 0
        prev = mn

        # compute gaps
        for bmin, bmax in buckets:

            if bmin == -1:
                continue

            gap = bmin - prev

            if gap > ans:
                ans = gap

            prev = bmax

        return ans