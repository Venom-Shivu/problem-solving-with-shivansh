from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def f(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)
            L = len(s)

            @cache
            def dp(pos, tight, started, seen, a, b):
                if pos == L:
                    return 1, 0

                limit = ord(s[pos]) - 48 if tight else 9

                total_cnt = 0
                total_sum = 0

                for d in range(limit + 1):
                    nt = tight and d == limit

                    if not started:
                        if d == 0:
                            cnt, sm = dp(pos + 1, nt, 0, 0, 10, 10)
                        else:
                            cnt, sm = dp(pos + 1, nt, 1, 1, 10, d)

                        total_cnt += cnt
                        total_sum += sm

                    elif seen == 1:
                        cnt, sm = dp(pos + 1, nt, 1, 2, b, d)
                        total_cnt += cnt
                        total_sum += sm

                    else:
                        add = (
                            (b > a and b > d)
                            or
                            (b < a and b < d)
                        )

                        cnt, sm = dp(pos + 1, nt, 1, 2, b, d)

                        total_cnt += cnt
                        total_sum += sm + add * cnt

                return total_cnt, total_sum

            return dp(0, 1, 0, 0, 10, 10)[1]

        return f(num2) - f(num1 - 1)