class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        ans = float('inf')

        land = [(s, s + d, d) for s, d in zip(landStartTime, landDuration)]
        water = [(s, s + d, d) for s, d in zip(waterStartTime, waterDuration)]

        for ls, lf, ld in land:
            for ws, wf, wd in water:

                finish1 = (lf if lf > ws else ws) + wd
                finish2 = (wf if wf > ls else ls) + ld

                if finish1 < ans:
                    ans = finish1

                if finish2 < ans:
                    ans = finish2

        return ans