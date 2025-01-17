function hasCycle(head: ListNode | null): boolean {
    // Handle empty list or single node
    if (!head || !head.next) {
        return false;
    }
    
    let slow: ListNode | null = head;
    let fast: ListNode | null = head.next;
    
    while (slow !== fast) {
        if (!fast || !fast.next) {
            return false;
        }
        
        slow = slow!.next;
        fast = fast.next.next;
    }
    
    return true;
}