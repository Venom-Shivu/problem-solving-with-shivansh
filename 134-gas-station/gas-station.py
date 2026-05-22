class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = i = 0

        for g, c in zip(gas, cost):
            diff = g - c

            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

            i += 1

        return start if total >= 0 else -1