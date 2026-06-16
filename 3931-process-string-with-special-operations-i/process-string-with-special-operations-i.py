class Solution:
    def processStr(self, s: str) -> str:
        r = ""
        for c in s:
            r = r + c if c.isalpha() else r[:-1] if c == "*" else r * 2 if c == "#" else r[::-1]
        return r