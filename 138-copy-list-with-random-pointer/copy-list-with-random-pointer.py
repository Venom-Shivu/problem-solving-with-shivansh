class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        # Insert copied nodes
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt)
            curr = nxt

        curr = head

        # Assign random pointers
        while curr:
            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        curr = head
        copy_head = head.next

        # Separate lists
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next

            if curr:
                copy.next = curr.next

        return copy_head