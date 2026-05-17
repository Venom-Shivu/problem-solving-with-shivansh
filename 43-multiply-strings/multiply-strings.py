class Solution(object):

    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        for i in xrange(n - 1, -1, -1):

            d1 = ord(num1[i]) - 48

            for j in xrange(m - 1, -1, -1):

                total = d1 * (ord(num2[j]) - 48)

                p1 = i + j
                p2 = i + j + 1

                total += res[p2]

                res[p2] = total % 10
                res[p1] += total / 10

        # Skip leading zeros
        i = 0

        while res[i] == 0:
            i += 1

        # Faster conversion
        return ''.join(map(str, res[i:]))