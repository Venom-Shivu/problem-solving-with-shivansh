class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return

            # pruning
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return ans