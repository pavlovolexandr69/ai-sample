public class Solution {
    
/// <summary>
    /// Determines whether the linked list represented by the given head node contains a cycle.
    /// </summary>
    /// <param name="head">The head node of the linked list to check for a cycle.</param>
    /// <returns>True if the linked list contains a cycle, false otherwise.</returns>
        public bool HasCycle(ListNode head) {
        if (head == null || head.next == null)
            return false;
            
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast)
                return true;
        }
        
        return false;
    }
}