class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = {}

        def dfs(i, j):

            # Already computed
            if (i, j) in dp:
                return dp[(i, j)]

            # Pattern fully used
            if j == len(p):
                return i == len(s)

            # Current characters match?
            match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                dp[(i, j)] = (
                    dfs(i, j + 2) or
                    (match and dfs(i + 1, j))
                )

                return dp[(i, j)]

            # Normal matching
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return dfs(0, 0)