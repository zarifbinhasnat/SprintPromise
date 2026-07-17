# dsa/stack/02_min_stack.py

class MinStackBrute:
    """push/pop/top are O(1); get_min re-scans the whole stack every call."""

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return min(self.stack)
        # Time:  O(n) per get_min call — full re-scan
        # Space: O(n) — one stack


class MinStack:
    """A second stack tracks the running minimum alongside every push, so
    get_min becomes a lookup instead of a scan."""

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
        # Time:  O(1) for every operation
        # Space: O(n) — two stacks, same height


if __name__ == "__main__":
    ms = MinStack()
    checks = []

    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    checks.append(("get_min() after push(-2,0,-3)", ms.get_min(), -3))

    ms.pop()
    checks.append(("top() after pop()", ms.top(), 0))
    checks.append(("get_min() after pop()", ms.get_min(), -2))

    for label, result, expected in checks:
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  {label} -> {result}")
