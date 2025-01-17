class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

Represents a solution to a problem.
class Solution:
# Determines whether a linked list contains a cycle.
    
#     This function takes a `ListNode` object representing the head of a linked list, and returns `True` if the list contains a cycle, and `False` otherwise.
    
#     The algorithm uses the "slow" and "fast" pointer technique to detect a cycle. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle, the two pointers will eventually meet. If there is no cycle, the fast pointer will reach the end of the list (i.e., `fast` or `fast.next` becomes `None`).
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Handle empty list or single node
        if not head or not head.next:
            return False
        
        # Initialize two pointers - slow and fast
        slow = head
        fast = head.next
        
        # Move slow pointer by 1 and fast pointer by 2
        while slow != fast:
            # If fast reaches end, there's no cycle
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        # If we exit the while loop, it means slow == fast, indicating a cycle
        return True
    