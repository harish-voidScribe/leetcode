/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head1) {
        ListNode slow = head1;
        ListNode fast = head1;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode head2 = slow.next;
        slow.next = null;

        ListNode prev = null;
        while (head2 != null) {
            ListNode temp = head2.next;
            head2.next = prev;
            prev = head2;
            head2 = temp;
        }

        head2 = prev;

        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        while (head1 != null || head2 != null) {
            curr.next = head1;
            head1 = head1.next;
            curr = curr.next;
            curr.next = null;

            if (head2 != null) {
                curr.next = head2;
                head2 = head2.next;
                curr = curr.next;
                curr.next = null;
            }
        }
        head1 = dummy.next;
    }
}
