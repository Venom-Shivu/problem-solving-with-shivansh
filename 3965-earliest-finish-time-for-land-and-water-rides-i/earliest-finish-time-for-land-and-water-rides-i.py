class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            land_finish = ls + ld

            for ws, wd in zip(waterStartTime, waterDuration):
                water_finish = ws + wd

                ans = min(
                    ans,
                    max(land_finish, ws) + wd,
                    max(water_finish, ls) + ld
                )

        return ans