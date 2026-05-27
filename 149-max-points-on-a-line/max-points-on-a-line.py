from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):

        n = len(points)

        if n <= 2:
            return n

        ans = 0
        pts = points

        for i in range(n):

            # Remaining points cannot beat answer
            if ans >= n - i:
                break

            x1, y1 = pts[i]

            slopes = {}

            local_max = 0

            for j in range(i + 1, n):

                x2, y2 = pts[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    key = (1, 0)

                elif dy == 0:
                    key = (0, 1)

                else:

                    g = gcd(dx, dy)

                    dx //= g
                    dy //= g

                    # Normalize sign
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    key = (dy, dx)

                val = slopes.get(key, 0) + 1

                slopes[key] = val

                if val > local_max:
                    local_max = val

            if local_max + 1 > ans:
                ans = local_max + 1

        return ans