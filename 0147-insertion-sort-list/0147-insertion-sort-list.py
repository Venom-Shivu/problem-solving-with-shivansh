# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)   # Start of sorted list
        curr = head

        while curr:
            prev = dummy
            nxt = curr.next   # Save next node

            # Find insertion position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert current node
            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next