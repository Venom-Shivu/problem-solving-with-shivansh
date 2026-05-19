class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n

        # Starting cell
        dp[0] = 1

        for i in range(m):

            for j in range(n):

                # Obstacle
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0

                # Add left path
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]