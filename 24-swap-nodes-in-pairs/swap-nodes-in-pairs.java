/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int next, ListNode nextNode) {
 *         this.val = val;
 *         this.next = nextNode;
 *     }
 * }
 */

class Solution {

    public ListNode swapPairs(ListNode head) {

        // Dummy node helps handle head swap easily
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;

        // Need at least 2 nodes to swap
        while (prev.next != null && prev.next.next != null) {

            // Identify nodes to swap
            ListNode first = prev.next;
            ListNode second = first.next;

            // Swapping
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Move prev to next pair
            prev = first;
        }

        return dummy.next;
    }
}