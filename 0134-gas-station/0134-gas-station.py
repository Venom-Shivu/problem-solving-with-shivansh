class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = total = tank = 0
        n = len(gas)

        for i in range(n):
            diff = gas[i] - cost[i]

            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1