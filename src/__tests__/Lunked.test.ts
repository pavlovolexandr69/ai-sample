import { hasCycle } from '../Lunked';

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

describe('hasCycle', () => {
    test('should return false for empty list', () => {
        expect(hasCycle(null)).toBe(false);
    });

    test('should return false for single node', () => {
        const node = new ListNode(1);
        expect(hasCycle(node)).toBe(false);
    });

    test('should return false for linear linked list', () => {
        const node1 = new ListNode(1);
        const node2 = new ListNode(2);
        const node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        expect(hasCycle(node1)).toBe(false);
    });

    test('should return true for circular linked list', () => {
        const node1 = new ListNode(1);
        const node2 = new ListNode(2);
        const node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;
        node3.next = node1;
        expect(hasCycle(node1)).toBe(true);
    });

    test('should return true for cycle in middle of list', () => {
        const node1 = new ListNode(1);
        const node2 = new ListNode(2);
        const node3 = new ListNode(3);
        const node4 = new ListNode(4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node2;
        node4.next = null;
        expect(hasCycle(node1)).toBe(true);
    });

    test('should handle large circular list', () => {
        let current = new ListNode(1);
        const head = current;
        for (let i = 2; i <= 1000; i++) {
            current.next = new ListNode(i);
            current = current.next;
        }
        current.next = head;
        expect(hasCycle(head)).toBe(true);
    });
});
