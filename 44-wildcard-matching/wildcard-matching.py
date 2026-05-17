class Solution(object):

    def isMatch(self, s, p):

        i = 0
        j = 0

        star = -1
        match = 0

        n = len(s)
        m = len(p)

        while i < n:

            # Direct match or '?'
            if j < m and (p[j] == s[i] or p[j] == '?'):

                i += 1
                j += 1

            # Found '*'
            elif j < m and p[j] == '*':

                star = j
                match = i

                j += 1

            # Previous '*' exists → backtrack
            elif star != -1:

                j = star + 1

                match += 1
                i = match

            else:
                return False

        # Remaining pattern should all be '*'
        while j < m and p[j] == '*':
            j += 1

        return j == m