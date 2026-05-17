class Solution(object):

    def multiply(self, num1, num2):

        # Quick zero handling
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        # Maximum possible digits = n + m
        result = [0] * (n + m)

        # Multiply from right to left
        for i in xrange(n - 1, -1, -1):

            d1 = ord(num1[i]) - 48

            for j in xrange(m - 1, -1, -1):

                d2 = ord(num2[j]) - 48

                product = d1 * d2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                # Store digit
                result[pos2] = total % 10

                # Carry
                result[pos1] += total / 10

        # Build final string
        start = 0

        # Skip leading zeros
        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(str(x) for x in result[start:])