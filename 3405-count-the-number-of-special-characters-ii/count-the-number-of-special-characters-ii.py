class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLower = [-1] * 26
        firstUpper = [-1] * 26

        for i, ch in enumerate(word):
            o = ord(ch)

            # lowercase a-z
            if 97 <= o <= 122:
                lastLower[o - 97] = i
            else:  # uppercase A-Z
                idx = o - 65
                if firstUpper[idx] == -1:
                    firstUpper[idx] = i

        ans = 0

        for i in range(26):
            # must exist in BOTH lower and upper
            if (lastLower[i] != -1 and
                firstUpper[i] != -1 and
                lastLower[i] < firstUpper[i]):
                ans += 1

        return ans