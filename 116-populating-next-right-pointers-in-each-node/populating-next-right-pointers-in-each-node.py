class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            curr = leftmost

            while curr:
                # Connect left -> right
                curr.left.next = curr.right

                # Connect across parents
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftmost = leftmost.left

        return root