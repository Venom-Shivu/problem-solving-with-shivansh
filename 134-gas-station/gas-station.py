class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            total += g - c

            if tank < 0:
                start = i + 1
                tank = 0

        return -1 if total < 0 else start