class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(node, remain):
            if not node:
                return

            val = node.val
            path.append(val)
            remain -= val

            left = node.left
            right = node.right

            if not left and not right:
                if remain == 0:
                    ans.append(path.copy())
            else:
                if left:
                    dfs(left, remain)
                if right:
                    dfs(right, remain)

            path.pop()

        dfs(root, targetSum)
        return ans