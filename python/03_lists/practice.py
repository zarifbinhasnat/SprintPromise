# Day 3 — Lists: Slicing, Mutation & When a List Beats a Dict
# Run: python python/03_lists/practice.py

# --- Creating & Indexing ---
nums = [5, 3, 8, 1, 9]
print("=== Indexing ===")
print(f"nums[0] = {nums[0]}, nums[-1] = {nums[-1]}")
print(f"nums[1:3] = {nums[1:3]}")   # same slicing rules as strings

# --- Mutation: lists change in place, strings never do ---
print("\n=== Mutation ===")
nums.append(12)
print(f"after append(12): {nums}")
nums.pop()
print(f"after pop(): {nums}")
nums.pop(0)
print(f"after pop(0): {nums}")
nums.insert(0, 100)
print(f"after insert(0, 100): {nums}")

# --- Sorting ---
print("\n=== Sorting ===")
unsorted = [5, 3, 8, 1, 9]
print(f"sorted() (new list):     {sorted(unsorted)} — original untouched: {unsorted}")
unsorted.sort()
print(f".sort() (in place):      {unsorted}")
unsorted.sort(reverse=True)
print(f".sort(reverse=True):     {unsorted}")

# --- Membership check: O(n) for a list ---
print("\n=== Membership (O(n)) ===")
big_list = list(range(1000))
print(f"999 in big_list: {999 in big_list}  (scans up to 1000 elements)")

# --- Same check with a set: O(1) average ---
print("\n=== Membership via set (O(1) avg) ===")
big_set = set(big_list)
print(f"999 in big_set: {999 in big_set}  (hash lookup, no scan)")

# --- The pattern for today's DSA problem ---
print("\n=== Seen-set pattern ===")
values = [1, 2, 3, 2, 5]
seen = set()
has_dup = False
for v in values:
    if v in seen:
        has_dup = True
        break
    seen.add(v)
print(f"values={values} -> has_dup={has_dup}")

# Challenge: try these yourself
# 1. Given a list of numbers, remove duplicates while preserving order
#    (hint: build a new list, checking against a seen set)
# 2. Time the difference between `x in a_list` and `x in a_set` for 100k items
