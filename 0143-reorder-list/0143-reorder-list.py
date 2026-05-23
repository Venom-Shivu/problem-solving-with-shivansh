class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge both halves
        first = head
        second = prev

        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2