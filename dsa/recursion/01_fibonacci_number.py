# dsa/recursion/01_fibonacci_number.py

def fib_brute(n):
    """Same shape as Day 12's climb_stairs_brute — two calls per level."""
    if n <= 1:
        return n
    return fib_brute(n - 1) + fib_brute(n - 2)
    # Time:  O(2^n) — call tree doubles at every level
    # Space: O(n) — recursion depth


def fib_memo(n, cache=None):
    """Same recursion, but every result is stored the first time it's
    computed and looked up instead of recomputed after that."""
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
    # Time:  O(n) — each fib_memo(k) does its own work exactly once
    # Space: O(n) — cache dict + recursion depth


if __name__ == "__main__":
    cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
    ]
    for n, expected in cases:
        result = fib_memo(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  fib_memo({n}) -> {result}")
