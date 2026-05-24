# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(float('-inf'))
        dummy.next = head

        lastSorted = head
        curr = head.next

        while curr:

            # Already in correct position
            if lastSorted.val <= curr.val:
                lastSorted = curr

            else:
                # Find insertion position
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next

                # Remove curr
                lastSorted.next = curr.next

                # Insert curr
                curr.next = prev.next
                prev.next = curr

            curr = lastSorted.next

        return dummy.next