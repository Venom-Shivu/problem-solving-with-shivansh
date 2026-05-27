class Solution:
    def numMagicSquaresInside(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m - 2):
            row0 = grid[r]
            row1 = grid[r + 1]
            row2 = grid[r + 2]

            for c in range(n - 2):

                # center must be 5
                if row1[c + 1] != 5:
                    continue

                a = row0[c]
                b = row0[c+1]
                d = row0[c+2]
                e = row1[c]
                f = row1[c+2]
                g = row2[c]
                h = row2[c+1]
                i = row2[c+2]

                # bitmask uniqueness + range check
                mask = 0

                for x in (a,b,d,e,5,f,g,h,i):
                    if x < 1 or x > 9:
                        mask = -1
                        break

                    bit = 1 << x

                    if mask & bit:
                        mask = -1
                        break

                    mask |= bit

                if mask == -1:
                    continue

                # all sums must be 15
                if (
                    a+b+d == 15 and
                    e+5+f == 15 and
                    g+h+i == 15 and

                    a+e+g == 15 and
                    b+5+h == 15 and
                    d+f+i == 15 and

                    a+5+i == 15 and
                    d+5+g == 15
                ):
                    ans += 1

        return ans