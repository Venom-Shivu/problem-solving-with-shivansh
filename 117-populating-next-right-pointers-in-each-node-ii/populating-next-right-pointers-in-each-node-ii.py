class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        dummy = Node(0)

        while curr:
            tail = dummy
            dummy.next = None

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = curr.left

                if curr.right:
                    tail.next = curr.right
                    tail = curr.right

                curr = curr.next

            curr = dummy.next

        return root