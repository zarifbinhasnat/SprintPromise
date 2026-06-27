# Day 1 — Two Sum
# NeetCode: https://neetcode.io/problems/two-sum
# Difficulty: Easy | Category: Arrays
#
# Problem:
#   Given an array of integers `nums` and an integer `target`,
#   return indices of the two numbers that add up to target.
#   Exactly one solution exists. Cannot reuse the same element.


# --- Approach 1: Brute Force ---
# Time: O(n²) | Space: O(1)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# --- Approach 2: Hash Map (Optimal) ---
# Time: O(n) | Space: O(n)
#
# Key insight: for each num, the complement needed is (target - num).
# Store each number's index in a dict. On each step, check if the
# complement was already seen. One pass is enough.
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# --- Tests ---
if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9,  [0, 1]),
        ([3, 2, 4],      6,  [1, 2]),
        ([3, 3],         6,  [0, 1]),
        ([1, 5, 3, 2],   4,  [2, 3]),
    ]
    print("Two Sum — Hash Map Solution")
    print("-" * 35)
    for nums, target, expected in cases:
        result = two_sum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] two_sum({nums}, {target}) = {result}  (expected {expected})")
