class Solution:
    def maximumGap(self, nums):

        n = len(nums)

        if n < 2:
            return 0

        minVal = min(nums)
        maxVal = max(nums)

        if minVal == maxVal:
            return 0

        bucketSize = max(1, (maxVal - minVal) // (n - 1))
        bucketCount = (maxVal - minVal) // bucketSize + 1

        bucketsMin = [float('inf')] * bucketCount
        bucketsMax = [float('-inf')] * bucketCount
        used = [False] * bucketCount

        # place numbers into buckets
        for num in nums:

            idx = (num - minVal) // bucketSize

            bucketsMin[idx] = min(bucketsMin[idx], num)
            bucketsMax[idx] = max(bucketsMax[idx], num)

            used[idx] = True

        ans = 0
        prevMax = minVal

        # compute maximum gap
        for i in range(bucketCount):

            if not used[i]:
                continue

            ans = max(ans, bucketsMin[i] - prevMax)

            prevMax = bucketsMax[i]

        return ans