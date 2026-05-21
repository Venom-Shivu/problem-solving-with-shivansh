class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        head_ref = [head]
        Tree = TreeNode

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2

            left = build(l, mid - 1)

            node = Tree(head_ref[0].val)
            node.left = left

            head_ref[0] = head_ref[0].next

            node.right = build(mid + 1, r)

            return node

        return build(0, n - 1)