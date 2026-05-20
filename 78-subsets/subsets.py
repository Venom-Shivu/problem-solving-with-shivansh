class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(start):
            ans.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return ans