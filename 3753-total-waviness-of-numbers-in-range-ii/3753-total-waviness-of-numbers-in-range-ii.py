from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, length_state, last2, last1):
                """
                Returns:
                    (count_numbers, total_waviness)
                """
                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started:
                        if d == 0:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                False,
                                0,
                                10,
                                10,
                            )
                            total_count += cnt
                            total_waviness += wav
                        else:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                1,
                                10,
                                d,
                            )
                            total_count += cnt
                            total_waviness += wav

                    else:
                        if length_state == 1:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                2,
                                last1,
                                d,
                            )
                            total_count += cnt
                            total_waviness += wav

                        else:
                            add = 0
                            if (last1 > last2 and last1 > d) or (
                                last1 < last2 and last1 < d
                            ):
                                add = 1

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                2,
                                last1,
                                d,
                            )

                            total_count += cnt
                            total_waviness += wav + add * cnt

                return (total_count, total_waviness)

            return dp(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)