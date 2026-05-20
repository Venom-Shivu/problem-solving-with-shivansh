# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):

        lessDummy = ListNode(0)
        greaterDummy = ListNode(0)

        less = lessDummy
        greater = greaterDummy

        while head:

            if head.val < x:

                less.next = head
                less = less.next

            else:

                greater.next = head
                greater = greater.next

            head = head.next

        # Important:
        # terminate greater list
        greater.next = None

        # Connect lists
        less.next = greaterDummy.next

        return lessDummy.next