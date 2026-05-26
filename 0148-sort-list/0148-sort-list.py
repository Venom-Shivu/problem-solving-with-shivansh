# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < length:
            prev = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                mergedHead, mergedTail = self.merge(left, right)

                prev.next = mergedHead
                prev = mergedTail

            size *= 2

        return dummy.next

    # Split list after 'size' nodes
    def split(self, head, size):
        if not head:
            return None

        for _ in range(size - 1):
            if head.next:
                head = head.next
            else:
                break

        second = head.next
        head.next = None
        return second

    # Merge two sorted lists
    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        while tail.next:
            tail = tail.next

        return dummy.next, tail