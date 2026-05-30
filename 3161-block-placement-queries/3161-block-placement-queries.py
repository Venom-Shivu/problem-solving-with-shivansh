from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries):
        mx = max(q[1] for q in queries)

        obstacles = SortedList([0, mx + 1])

        # Add all obstacles first
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        n = mx + 3

        seg = [0] * (4 * n)

        def update(idx, val, node, l, r):
            if l == r:
                seg[node] = val
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(idx, val, node * 2, l, mid)
            else:
                update(idx, val, node * 2 + 1, mid + 1, r)

            seg[node] = max(seg[node * 2], seg[node * 2 + 1])

        def query(L, R, node, l, r):
            if L > r or R < l:
                return 0

            if L <= l and r <= R:
                return seg[node]

            mid = (l + r) // 2

            return max(
                query(L, R, node * 2, l, mid),
                query(L, R, node * 2 + 1, mid + 1, r)
            )

        arr = list(obstacles)

        for i in range(1, len(arr)):
            update(arr[i], arr[i] - arr[i - 1], 1, 0, n)

        ans = []

        for q in reversed(queries):

            if q[0] == 2:

                x, sz = q[1], q[2]

                idx = obstacles.bisect_right(x)
                prev = obstacles[idx - 1]

                best = query(0, prev, 1, 0, n)
                best = max(best, x - prev)

                ans.append(best >= sz)

            else:

                x = q[1]

                idx = obstacles.index(x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                update(right, right - left, 1, 0, n)
                update(x, 0, 1, 0, n)

                obstacles.remove(x)

        return ans[::-1]