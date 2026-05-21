class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def dfs(l, r):
            if l > r:
                return None

            mid = (l + r) >> 1   # bit shift slightly faster than //

            node = TreeNode(nums[mid])
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node

        return dfs(0, n - 1)