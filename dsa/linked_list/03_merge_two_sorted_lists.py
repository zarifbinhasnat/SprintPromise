# Problem: Merge Two Sorted Lists (Easy · Linked List)
# https://neetcode.io/problems/merge-two-sorted-linked-lists
#
# Given the heads of two sorted linked lists, merge them into one sorted linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists_brute(l1, l2):
    """Brute force: collect all values, sort, rebuild.
    Time:  O((n+m) log(n+m))
    Space: O(n+m)
    """
    values = []
    for node in (l1, l2):
        while node:
            values.append(node.val)
            node = node.next
    values.sort()
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def merge_two_lists(l1, l2):
    """Optimal: two-pointer merge with a dummy head, reuses existing nodes.
    Time:  O(n+m)
    Space: O(1)
    """
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    for a, b, expected in cases:
        result = to_list(merge_two_lists(from_list(a), from_list(b)))
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  merge_two_lists({a}, {b}) -> {result}")
