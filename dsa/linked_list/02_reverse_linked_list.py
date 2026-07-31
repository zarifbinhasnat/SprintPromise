# Problem: Reverse Linked List (Easy · Linked List)
# https://neetcode.io/problems/reverse-a-linked-list
#
# Given the head of a singly linked list, reverse it in place and return the new head.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_brute(head):
    """Brute force: collect values, rebuild a new chain in reverse order.
    Time:  O(n)
    Space: O(n)
    """
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    dummy = ListNode()
    curr = dummy
    for v in reversed(values):
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def reverse_list(head):
    """Optimal: iterative, in place, three pointers.
    Time:  O(n)
    Space: O(1)
    """
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def from_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    for values, expected in cases:
        head = from_list(values)
        result = to_list(reverse_list(head))
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  reverse_list({values}) -> {result}")
