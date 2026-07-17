# dsa/binary_search/01_binary_search.py

def binary_search_brute(nums, target):
    """Linear scan — correct, but doesn't use the fact that nums is sorted."""
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1
    # Time:  O(n) — checks every element in the worst case
    # Space: O(1)


def binary_search(nums, target):
    """nums is sorted, so every guess eliminates HALF the remaining search
    space instead of one element at a time."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1     # target must be to the right — discard the left half
        else:
            right = mid - 1    # target must be to the left — discard the right half
    return -1
    # Time:  O(log n) — the search space halves every iteration
    # Space: O(1) — two pointers, no extra structure


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9, 12, 20, 33]
    cases = [
        (9, 4),
        (-10, 0),
        (33, 7),
        (6, -1),
        (100, -1),
    ]
    for target, expected in cases:
        result = binary_search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  binary_search(nums, {target}) -> {result}")
