class Solution(object):

    def isMatch(self, s, p):

        n = len(s)
        m = len(p)

        dp = [False] * (m + 1)

        dp[0] = True

        # Handle patterns like ****
        for j in xrange(m):

            if p[j] == '*':
                dp[j + 1] = dp[j]

        for i in xrange(n):

            prev = dp[0]

            dp[0] = False

            for j in xrange(m):

                temp = dp[j + 1]

                if p[j] == '*':

                    dp[j + 1] = dp[j + 1] or dp[j]

                else:

                    dp[j + 1] = prev and (
                        p[j] == s[i] or p[j] == '?'
                    )

                prev = temp

        return dp[m]