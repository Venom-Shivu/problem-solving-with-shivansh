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
        ans = INF

        # ---------- Water preprocessing ----------
        water = sorted(zip(waterStartTime, waterDuration))
        m = len(water)

        ws = [0] * m
        wd = [0] * m

        for i, (s, d) in enumerate(water):
            ws[i] = s
            wd[i] = d

        suffix_water = [0] * m
        suffix_water[-1] = ws[-1] + wd[-1]

        for i in range(m - 2, -1, -1):
            cur = ws[i] + wd[i]
            nxt = suffix_water[i + 1]
            suffix_water[i] = cur if cur < nxt else nxt

        land_finish = sorted(ls + ld for ls, ld in zip(landStartTime, landDuration))

        ptr = 0
        best_duration = INF

        for t in land_finish:

            while ptr < m and ws[ptr] <= t:
                if wd[ptr] < best_duration:
                    best_duration = wd[ptr]
                ptr += 1

            if best_duration != INF:
                cand = t + best_duration
                if cand < ans:
                    ans = cand

            if ptr < m:
                cand = suffix_water[ptr]
                if cand < ans:
                    ans = cand

        # ---------- Land preprocessing ----------
        land = sorted(zip(landStartTime, landDuration))
        n = len(land)

        ls = [0] * n
        ld = [0] * n

        for i, (s, d) in enumerate(land):
            ls[i] = s
            ld[i] = d

        suffix_land = [0] * n
        suffix_land[-1] = ls[-1] + ld[-1]

        for i in range(n - 2, -1, -1):
            cur = ls[i] + ld[i]
            nxt = suffix_land[i + 1]
            suffix_land[i] = cur if cur < nxt else nxt

        water_finish = sorted(ws0 + wd0 for ws0, wd0 in zip(waterStartTime, waterDuration))

        ptr = 0
        best_duration = INF

        for t in water_finish:

            while ptr < n and ls[ptr] <= t:
                if ld[ptr] < best_duration:
                    best_duration = ld[ptr]
                ptr += 1

            if best_duration != INF:
                cand = t + best_duration
                if cand < ans:
                    ans = cand

            if ptr < n:
                cand = suffix_land[ptr]
                if cand < ans:
                    ans = cand

        return ans