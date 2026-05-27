from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        
        # Build mapping: pair -> possible tops
        mp = defaultdict(list)
        for pattern in allowed:
            mp[pattern[:2]].append(pattern[2])

        @lru_cache(None)
        def dfs(row):
            # Reached top
            if len(row) == 1:
                return True

            candidates = []

            # Generate possible characters for next row
            for i in range(len(row) - 1):
                pair = row[i:i+2]

                if pair not in mp:
                    return False

                candidates.append(mp[pair])

            # Backtrack to build next row
            def build(idx, path):
                if idx == len(candidates):
                    return dfs("".join(path))

                for ch in candidates[idx]:
                    path.append(ch)
                    if build(idx + 1, path):
                        return True
                    path.pop()

                return False

            return build(0, [])

        return dfs(bottom)