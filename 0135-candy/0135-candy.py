class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies = 1
        up = down = peak = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                candies += up + 1

            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                candies += 1

            else:
                up = 0
                down += 1
                candies += down

                if down > peak:
                    candies += 1

        return candies