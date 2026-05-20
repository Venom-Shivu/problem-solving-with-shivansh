class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if not curr.left:
                # Process node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                # Find inorder predecessor
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None

                    # Process node
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val