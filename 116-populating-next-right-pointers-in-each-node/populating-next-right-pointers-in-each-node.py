class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr_level = root

        while curr_level and curr_level.left:
            node = curr_level

            while node:
                node.left.next = node.right

                nxt = node.next
                if nxt:
                    node.right.next = nxt.left

                node = nxt

            curr_level = curr_level.left

        return root