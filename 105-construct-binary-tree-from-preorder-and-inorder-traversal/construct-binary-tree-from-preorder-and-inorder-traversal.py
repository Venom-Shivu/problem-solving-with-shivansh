class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_idx = 0

        def build(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            # Current root
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root = TreeNode(root_val)

            # Root position in inorder
            mid = inorder_map[root_val]

            # Build left then right
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)