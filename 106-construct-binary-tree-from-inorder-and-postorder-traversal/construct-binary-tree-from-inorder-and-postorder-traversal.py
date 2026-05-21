class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v: i for i, v in enumerate(inorder)}
        post_iter = reversed(postorder)

        def build(left, right):
            if left > right:
                return None

            root_val = next(post_iter)
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            # Right first because postorder is consumed backwards
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)