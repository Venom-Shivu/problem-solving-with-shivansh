from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        INF = 10**18

        def calc(start1, dur1, start2, dur2):
            rides = sorted(zip(start2, dur2))
            m = len(rides)

            s = [0] * m
            d = [0] * m

            for i in range(m):
                s[i], d[i] = rides[i]

            suf = [0] * m
            suf[-1] = s[-1] + d[-1]

            for i in range(m - 2, -1, -1):
                cur = s[i] + d[i]
                nxt = suf[i + 1]
                suf[i] = cur if cur < nxt else nxt

            finish = [start1[i] + dur1[i] for i in range(len(start1))]
            finish.sort()

            ptr = 0
            best_dur = INF
            ans = INF

            for t in finish:

                while ptr < m and s[ptr] <= t:
                    if d[ptr] < best_dur:
                        best_dur = d[ptr]
                    ptr += 1

                if best_dur != INF:
                    v = t + best_dur
                    if v < ans:
                        ans = v

                if ptr < m and suf[ptr] < ans:
                    ans = suf[ptr]

            return ans

        a = calc(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        b = calc(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return a if a < b else b