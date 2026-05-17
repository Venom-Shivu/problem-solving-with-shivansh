class Solution(object):

    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        # Precompute digits once
        a = [ord(c) - 48 for c in num1]
        b = [ord(c) - 48 for c in num2]

        for i in xrange(n - 1, -1, -1):

            ai = a[i]
            ri = res

            for j in xrange(m - 1, -1, -1):

                pos = i + j + 1

                total = ai * b[j] + ri[pos]

                ri[pos] = total % 10
                ri[pos - 1] += total / 10

        # Skip leading zeros
        i = 0

        while res[i] == 0:
            i += 1

        # Faster than map(str,...)
        return ''.join(chr(x + 48) for x in res[i:])