class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Precompute palindrome table
        dp = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2 or dp[start + 1][end - 1]
                ):
                    dp[start][end] = True

        result = []
        path = []

        def dfs(start):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result