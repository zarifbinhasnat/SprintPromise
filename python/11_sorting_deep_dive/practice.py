# python/11_sorting_deep_dive/practice.py

nums = [5, 2, 8, 1, 9]

# sorted() returns a NEW list, leaves the original untouched
new_list = sorted(nums)
print(nums, new_list)

# .sort() sorts IN PLACE and returns None — don't do `nums = nums.sort()`
nums_copy = nums.copy()
result = nums_copy.sort()
print(nums_copy, result)

# Stability: elements with EQUAL keys keep their original relative order
students = [("Dee", 85), ("Amy", 90), ("Cal", 85), ("Bob", 90)]
by_score = sorted(students, key=lambda s: s[1])
print(by_score)  # Dee still comes before Cal — both scored 85, original order kept

# Multi-key sort with tuples — score DESC, name ASC as the tiebreaker
ranked = sorted(students, key=lambda s: (-s[1], s[0]))
print(ranked)  # ties broken ALPHABETICALLY: Amy before Bob, Cal before Dee

# reverse=True flips the whole comparison but stability still applies to the
# ORIGINAL input order — ties are NOT re-sorted alphabetically, they just
# keep showing up in the order they were already in
ranked_reverse_true = sorted(students, key=lambda s: s[1], reverse=True)
print(ranked_reverse_true)  # Amy before Bob (original order) but Dee before Cal (original order, not alphabetical)
