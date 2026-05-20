class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        subset = []

        def backtrack(start):
            ans.append(subset[:])

            for i in range(start, len(nums)):
                # Skip duplicates at same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return ans