class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        # Step 1: Insert copied nodes
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head

        # Step 2: Set random pointers
        while curr:
            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        curr = head
        copy_head = head.next

        # Step 3: Separate lists
        while curr:
            copy = curr.next

            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head