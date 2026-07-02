# Day 4 — Dicts & Sets: Comprehensions, .get(), Set Ops & Nested Structures
# Run: python python/04_dicts_sets/practice.py

# --- Dict comprehensions ---
print("=== Dict Comprehensions ===")
nums = [1, 2, 3, 4, 5]
squares = {n: n * n for n in nums}
print(f"squares = {squares}")

evens_only = {n: n * n for n in nums if n % 2 == 0}
print(f"evens_only = {evens_only}")

# --- .get() vs. [] ---
print("\n=== .get() vs [] ===")
counts = {"a": 3, "b": 1}
print(f"counts.get('a') = {counts.get('a')}")
print(f"counts.get('z') = {counts.get('z')}")            # None, no KeyError
print(f"counts.get('z', 0) = {counts.get('z', 0)}")       # safe default

# The .get() increment pattern — no need to check "in" first
word = "aabbbc"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(f"freq('{word}') = {freq}")

# --- Set comprehensions & operations ---
print("\n=== Set Comprehensions & Operations ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}, b = {b}")
print(f"union (a | b)        = {a | b}")
print(f"intersection (a & b) = {a & b}")
print(f"difference (a - b)   = {a - b}")
print(f"symmetric (a ^ b)    = {a ^ b}")

squares_set = {n * n for n in range(6)}
print(f"squares_set = {squares_set}")

# --- Nested structures ---
print("\n=== Nested Structures ===")
students = {
    "amina": {"grades": [88, 92, 79], "active": True},
    "yusuf": {"grades": [65, 70], "active": False},
}
for name, info in students.items():
    avg = sum(info["grades"]) / len(info["grades"])
    print(f"{name}: avg={avg:.1f}, active={info['active']}")

# list of dicts — the shape most APIs return
records = [
    {"id": 1, "price": 7},
    {"id": 2, "price": 1},
    {"id": 3, "price": 5},
]
prices_by_id = {r["id"]: r["price"] for r in records}
print(f"prices_by_id = {prices_by_id}")

# Challenge: try these yourself
# 1. Given records above, build a set of all ids with price > 3
# 2. Merge two dicts so keys in the second override the first (hint: {**d1, **d2})
