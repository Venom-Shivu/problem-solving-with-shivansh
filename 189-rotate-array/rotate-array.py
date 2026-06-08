from typing import List
from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        if k == 0:
            return

        for start in range(gcd(n, k)):
            current = start
            prev = nums[start]

            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt

                if current == start:
                    break