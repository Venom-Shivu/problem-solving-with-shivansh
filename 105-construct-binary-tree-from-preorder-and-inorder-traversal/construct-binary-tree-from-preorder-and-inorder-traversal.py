class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v: i for i, v in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def build(left, right):
            if left > right:
                return None

            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)