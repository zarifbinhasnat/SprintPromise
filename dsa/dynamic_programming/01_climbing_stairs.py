# dsa/dynamic_programming/01_climbing_stairs.py

def climb_stairs_brute(n):
    """Pure recursion, no memo — every call branches into two more calls."""
    if n <= 2:
        return n
    return climb_stairs_brute(n - 1) + climb_stairs_brute(n - 2)
    # Time:  O(2^n) — the call tree doubles at every level
    # Space: O(n) — recursion depth


def climb_stairs(n):
    """Bottom-up DP — build the answer from the base cases up, one pass."""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2  # ways to reach step 1, ways to reach step 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
    # Time:  O(n) — one pass, no repeated work
    # Space: O(1) — only ever two numbers in flight


if __name__ == "__main__":
    cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]
    for n, expected in cases:
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  climb_stairs({n}) -> {result}")
