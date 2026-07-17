# python/13_memoization/practice.py

import time
from functools import lru_cache

# Manual memoization — a dict that remembers every (input -> output) pair
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result
    return result


print(fib_memo(30))   # instant — naive recursive fib(30) would be noticeably slow

# functools.lru_cache — the same idea, one decorator, no cache dict to manage
@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


print(fib_lru(30))

# Proving the speedup — naive vs memoized on the same input
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


start = time.perf_counter()
fib_naive(28)
naive_time = time.perf_counter() - start

start = time.perf_counter()
fib_lru(28)
memo_time = time.perf_counter() - start

print(f"naive: {naive_time:.4f}s, memoized: {memo_time:.6f}s")
# The memoized version is dramatically faster — it does O(n) work total
# because each fib_lru(k) only ever runs its own body ONCE, no matter how
# many places call it.

# A gotcha: lru_cache keys on the exact arguments passed — mutable arguments
# (like a list) aren't hashable and will raise a TypeError. Only use it on
# functions whose arguments are hashable (ints, strings, tuples).
