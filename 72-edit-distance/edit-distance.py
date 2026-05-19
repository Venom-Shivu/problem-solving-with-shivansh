class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        # previous row
        prev = list(range(n + 1))

        for i in range(1, m + 1):

            curr = [i] * (n + 1)

            for j in range(1, n + 1):

                # characters same
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]

                else:
                    curr[j] = 1 + min(
                        prev[j],      # delete
                        curr[j - 1],  # insert
                        prev[j - 1]   # replace
                    )

            prev = curr

        return prev[n]