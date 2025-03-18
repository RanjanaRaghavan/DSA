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
    public int pairSum(ListNode head) {

        //Hare Tortoise 
        ListNode hare = head;
        ListNode tortoise = head;

        while(hare != null && hare.next != null){
            hare = hare.next.next;
            tortoise = tortoise.next;
        }

        //Reverse LinkedList
        ListNode prev = null;
        ListNode curr = tortoise;

        while(curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        //calculate max_val
        int max_val = 0;
        ListNode start = head;

        while(prev != null){

            max_val = Math.max(max_val, prev.val + start.val);
            prev = prev.next;
            start = start.next;
        }

        return max_val;
        
    }
}