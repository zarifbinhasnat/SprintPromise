# Day 3 — Contains Duplicate
# NeetCode: https://neetcode.io/problems/contains-duplicate
# Difficulty: Easy | Category: Arrays
#
# Problem:
#   Given an integer array `nums`, return True if any value appears
#   at least twice in the array, and False if every element is distinct.


# --- Approach 1: Brute Force ---
# Time: O(n²) | Space: O(1)
def contains_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# --- Approach 2: Sorting ---
# Time: O(n log n) | Space: O(1) extra (ignoring sort's internal space)
#
# Duplicates end up adjacent after sorting, so one linear pass over
# neighbors is enough to catch them.
def contains_duplicate_sort(nums):
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return True
    return False


# --- Approach 3: Hash Set (Optimal) ---
# Time: O(n) | Space: O(n)
#
# Same "seen" pattern from Two Sum and Valid Anagram: walk the array once,
# and check membership in a set instead of counting frequency — this
# problem only cares about presence, not how many times.
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# --- Tests ---
if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 1],       True),
        ([1, 2, 3, 4],       False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([],                 False),
        ([7],                False),
    ]
    print("Contains Duplicate — Hash Set Solution")
    print("-" * 40)
    for nums, expected in cases:
        result = contains_duplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] contains_duplicate({nums}) = {result}  (expected {expected})")
