class Solution(object):

    def combinationSum2(self, candidates, target):

        candidates.sort()

        result = []

        def backtrack(start, remaining, path):

            # Valid combination found
            if remaining == 0:
                result.append(path[:])
                return

            # Target exceeded
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted,
                # no need to continue further
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Move to next index
                # because one element can be used only once
                backtrack(i + 1,
                          remaining - candidates[i],
                          path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])

        return result