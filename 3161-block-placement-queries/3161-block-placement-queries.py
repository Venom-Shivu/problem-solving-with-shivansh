from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries):

        mx = max(q[1] for q in queries)

        obs = SortedList([0, mx + 1])

        for q in queries:
            if q[0] == 1:
                obs.add(q[1])

        size = mx + 2

        n = 1
        while n < size:
            n <<= 1

        seg = [0] * (2 * n)

        def update(pos, val):
            p = pos + n
            seg[p] = val

            p >>= 1

            while p:
                left = seg[p << 1]
                right = seg[p << 1 | 1]
                seg[p] = left if left > right else right
                p >>= 1

        def query(l, r):
            l += n
            r += n

            res = 0

            while l <= r:

                if l & 1:
                    if seg[l] > res:
                        res = seg[l]
                    l += 1

                if not (r & 1):
                    if seg[r] > res:
                        res = seg[r]
                    r -= 1

                l >>= 1
                r >>= 1

            return res

        arr = list(obs)

        for i in range(1, len(arr)):
            update(arr[i], arr[i] - arr[i - 1])

        ans = []

        for q in reversed(queries):

            if q[0] == 2:

                x = q[1]
                sz = q[2]

                idx = obs.bisect_right(x)

                prev = obs[idx - 1]

                best = query(0, prev)

                gap = x - prev

                if gap > best:
                    best = gap

                ans.append(best >= sz)

            else:

                x = q[1]

                idx = obs.bisect_left(x)

                left = obs[idx - 1]
                right = obs[idx + 1]

                update(right, right - left)
                update(x, 0)

                obs.remove(x)

        ans.reverse()
        return ans