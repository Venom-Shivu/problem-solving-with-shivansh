class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head

        while fast is not None:
            fast = fast.next
            if fast is None:
                return None

            fast = fast.next
            slow = slow.next

            if slow is fast:
                break
        else:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow