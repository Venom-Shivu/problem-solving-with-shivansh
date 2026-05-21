class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        node_stack = [root]
        sum_stack = [targetSum - root.val]

        while node_stack:
            node = node_stack.pop()
            remain = sum_stack.pop()

            if not node.left and not node.right and remain == 0:
                return True

            if node.right:
                node_stack.append(node.right)
                sum_stack.append(remain - node.right.val)

            if node.left:
                node_stack.append(node.left)
                sum_stack.append(remain - node.left.val)

        return False