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
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < n:
            tail = dummy
            cur = dummy.next

            while cur:
                left = cur
                right = self.cut(left, size)
                cur = self.cut(right, size)

                # Merge directly
                while left and right:
                    if left.val <= right.val:
                        tail.next = left
                        left = left.next
                    else:
                        tail.next = right
                        right = right.next
                    tail = tail.next

                tail.next = left if left else right

                while tail.next:
                    tail = tail.next

            size <<= 1

        return dummy.next

    def cut(self, head, size):
        if not head:
            return None

        cur = head
        for _ in range(size - 1):
            if cur.next:
                cur = cur.next
            else:
                break

        nxt = cur.next
        cur.next = None
        return nxt