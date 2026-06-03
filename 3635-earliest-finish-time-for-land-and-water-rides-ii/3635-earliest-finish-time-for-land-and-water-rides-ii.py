from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        INF = float('inf')

        # ---------- Water preprocessing ----------
        water = sorted(zip(waterStartTime, waterDuration))
        ws = [x[0] for x in water]
        wd = [x[1] for x in water]

        m = len(water)

        prefWaterDur = [0] * m
        prefWaterDur[0] = wd[0]

        for i in range(1, m):
            prefWaterDur[i] = min(prefWaterDur[i - 1], wd[i])

        suffWaterFinish = [0] * m
        suffWaterFinish[-1] = ws[-1] + wd[-1]

        for i in range(m - 2, -1, -1):
            suffWaterFinish[i] = min(
                suffWaterFinish[i + 1],
                ws[i] + wd[i]
            )

        ans = INF

        # ---------- Land -> Water ----------
        for ls, ld in zip(landStartTime, landDuration):

            t = ls + ld

            idx = bisect_right(ws, t) - 1

            if idx >= 0:
                ans = min(ans, t + prefWaterDur[idx])

            if idx + 1 < m:
                ans = min(ans, suffWaterFinish[idx + 1])

        # ---------- Land preprocessing ----------
        land = sorted(zip(landStartTime, landDuration))
        ls = [x[0] for x in land]
        ld = [x[1] for x in land]

        n = len(land)

        prefLandDur = [0] * n
        prefLandDur[0] = ld[0]

        for i in range(1, n):
            prefLandDur[i] = min(prefLandDur[i - 1], ld[i])

        suffLandFinish = [0] * n
        suffLandFinish[-1] = ls[-1] + ld[-1]

        for i in range(n - 2, -1, -1):
            suffLandFinish[i] = min(
                suffLandFinish[i + 1],
                ls[i] + ld[i]
            )

        # ---------- Water -> Land ----------
        for ws0, wd0 in zip(waterStartTime, waterDuration):

            u = ws0 + wd0

            idx = bisect_right(ls, u) - 1

            if idx >= 0:
                ans = min(ans, u + prefLandDur[idx])

            if idx + 1 < n:
                ans = min(ans, suffLandFinish[idx + 1])

        return ans