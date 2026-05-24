# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)  # start of sorted list
        curr = head
        
        while curr:
            prev = dummy
            
            # find position to insert
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # save next node
            nxt = curr.next
            
            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            # move forward
            curr = nxt
        
        return dummy.next
        