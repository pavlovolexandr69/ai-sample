import unittest
from typing import Optional
from Linked import ListNode, Solution

class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.hasCycle(None))

    def test_single_node(self):
        head = ListNode(1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_two_nodes_no_cycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        self.assertFalse(self.solution.hasCycle(head))

    def test_cycle_in_two_nodes(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node2.next = head
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_in_multiple_nodes(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        self.assertTrue(self.solution.hasCycle(head))

    def test_long_list_no_cycle(self):
        head = ListNode(1)
        current = head
        for i in range(2, 1000):
            current.next = ListNode(i)
            current = current.next
        self.assertFalse(self.solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main()
