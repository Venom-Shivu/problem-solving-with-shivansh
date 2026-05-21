class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root

        while curr:
            next_head = None
            prev = None

            while curr:
                left = curr.left
                right = curr.right

                if left:
                    if prev:
                        prev.next = left
                    else:
                        next_head = left
                    prev = left

                if right:
                    if prev:
                        prev.next = right
                    else:
                        next_head = right
                    prev = right

                curr = curr.next

            curr = next_head

        return root