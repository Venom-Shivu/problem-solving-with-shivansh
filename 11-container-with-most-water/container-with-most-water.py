class Solution:
    def maxArea(self, height) -> int:

        l = 0
        r = len(height) - 1

        ans = 0

        while l < r:

            hl = height[l]
            hr = height[r]

            width = r - l

            if hl < hr:

                area = hl * width

                if area > ans:
                    ans = area

                l += 1

            else:

                area = hr * width

                if area > ans:
                    ans = area

                r -= 1

        return ans