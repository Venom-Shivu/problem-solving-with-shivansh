from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def dfs(a, b):

            # Exact match
            if a == b:
                return True

            # Different character counts
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):

                # No swap case
                if (
                    dfs(a[:i], b[:i]) and
                    dfs(a[i:], b[i:])
                ):
                    return True

                # Swap case
                if (
                    dfs(a[:i], b[n-i:]) and
                    dfs(a[i:], b[:n-i])
                ):
                    return True

            return False

        return dfs(s1, s2)