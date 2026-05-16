class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        n = len(s)
        i = 0

        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # Sign handling
        sign = 1

        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i += 1

        num = 0

        while i < n:

            c = s[i]

            # Faster digit check than isdigit()
            if c < '0' or c > '9':
                break

            digit = ord(c) - 48

            # Overflow check
            if num > 214748364 or (
                num == 214748364 and digit > 7
            ):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit

            i += 1

        return sign * num