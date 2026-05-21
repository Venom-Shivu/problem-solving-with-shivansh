class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left

                while prev.right:
                    prev = prev.right

                # Rewire pointers
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right