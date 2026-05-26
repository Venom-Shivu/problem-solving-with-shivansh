# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Get length
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head

        step = 1

        while step < n:
            prev = dummy
            curr = dummy.next

            while curr:

                # Left list
                left = curr

                # Right list
                right = curr
                for _ in range(step - 1):
                    if right and right.next:
                        right = right.next

                if not right:
                    break

                curr = right.next
                right.next = None
                right = curr

                # Next chunk
                for _ in range(step - 1):
                    if curr and curr.next:
                        curr = curr.next

                nextStart = None
                if curr:
                    nextStart = curr.next
                    curr.next = None

                # Merge
                l1, l2 = left, right

                while l1 and l2:
                    if l1.val <= l2.val:
                        prev.next = l1
                        l1 = l1.next
                    else:
                        prev.next = l2
                        l2 = l2.next
                    prev = prev.next

                prev.next = l1 if l1 else l2

                while prev.next:
                    prev = prev.next

                curr = nextStart

            step *= 2

        return dummy.next