/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {

    public ListNode mergeKLists(ListNode[] lists) {

        // Min Heap based on node values
        PriorityQueue<ListNode> minHeap =
                new PriorityQueue<>((a, b) -> a.val - b.val);

        // Put first node of every list into heap
        for (ListNode node : lists) {
            if (node != null) {
                minHeap.offer(node);
            }
        }

        // Dummy node to build answer list
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        // Process heap
        while (!minHeap.isEmpty()) {

            // Get smallest node
            ListNode smallest = minHeap.poll();

            // Attach to result
            tail.next = smallest;
            tail = tail.next;

            // If next node exists, push into heap
            if (smallest.next != null) {
                minHeap.offer(smallest.next);
            }
        }

        return dummy.next;
    }
}