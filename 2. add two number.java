/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }    // initialization
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead; // result linked list starts from the dummy head
        ListNode n1 = l1;
        ListNode n2 = l2;
        int carry = 0;
        
        while ((n1 != null) || (n2 != null)){ //one of the linked list not ended
            int x,y = 0;
            if (n1 != null){
                x = n1.val;
            } else {
                x = 0;
            }
            if (n2 != null) {
                y = n2.val;
            } else{
                y = 0;
            }
            int sum = 0;
            sum = carry + x + y;
            int newValue = sum % 10;
            ListNode newNode = new ListNode(newValue);
            curr.next = newNode;
            // update
            carry = sum / 10;
            curr = curr.next;   
            if (n1 != null) {
                n1 = n1.next;
            }
            if (n2 != null) {
                n2  = n2.next;
            }
        }
        // two linked list ended, if the previous sum > 10, we have to deal carry
        if (carry > 0) {
            curr.next  = new ListNode(carry);
        }
        
        return dummyHead.next;       // the function of dummyHead: do not need  to write special conditions for the head value, regard 
                                     //it as a normal node 
    }
}