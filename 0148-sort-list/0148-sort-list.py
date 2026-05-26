# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head:
            return None

        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        vals.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next