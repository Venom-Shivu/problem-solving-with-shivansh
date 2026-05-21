class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level = root

        while level and level.left:
            curr = level

            while curr:
                left = curr.left
                right = curr.right

                left.next = right

                if curr.next:
                    right.next = curr.next.left

                curr = curr.next

            level = level.left

        return root