# Problem: Linked List Cycle (Easy · Linked List)
# https://neetcode.io/problems/linked-list-cycle-detection
#
# Given the head of a singly linked list, determine whether it contains a cycle.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle_brute(head):
    """Brute force: track visited nodes in a set.
    Time:  O(n)
    Space: O(n)
    """
    seen = set()
    node = head
    while node:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False


def has_cycle(head):
    """Optimal: Floyd's tortoise and hare.
    Time:  O(n)
    Space: O(1)
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def build_cyclic_list(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
    ]
    for values, pos, expected in cases:
        head = build_cyclic_list(values, pos)
        result = has_cycle(head)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  has_cycle({values}, pos={pos}) -> {result}")
