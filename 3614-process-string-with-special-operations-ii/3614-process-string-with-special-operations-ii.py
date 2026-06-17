class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lens = [0] * (n + 1)

        for i, c in enumerate(s):
            cur = lens[i]

            if 'a' <= c <= 'z':
                lens[i + 1] = cur + 1
            elif c == '*':
                lens[i + 1] = max(0, cur - 1)
            elif c == '#':
                lens[i + 1] = cur * 2
            else:  # %
                lens[i + 1] = cur

        if k >= lens[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            prev = lens[i]
            cur = lens[i + 1]

            if 'a' <= c <= 'z':
                if k == prev:
                    return c

            elif c == '*':
                pass

            elif c == '#':
                k %= prev

            else:  # %
                k = cur - 1 - k

        return '.'