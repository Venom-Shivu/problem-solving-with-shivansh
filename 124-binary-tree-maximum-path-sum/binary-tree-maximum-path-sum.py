class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current = node.val + left + right
            max_sum = max(max_sum, current)

            return node.val + max(left, right)

        dfs(root)
        return max_sum