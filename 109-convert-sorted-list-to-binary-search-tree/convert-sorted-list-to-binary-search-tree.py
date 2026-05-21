class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        def build(left, right):
            nonlocal head

            if left > right:
                return None

            mid = (left + right) // 2

            left_child = build(left, mid - 1)

            root = TreeNode(head.val)
            root.left = left_child

            head = head.next

            root.right = build(mid + 1, right)

            return root

        return build(0, n - 1)