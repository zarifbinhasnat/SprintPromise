def max_subarray(nums):
    best = nums[0]
    current = 0
    for n in nums:
        if current < 0:
            current = 0
        current += n
        best = max(best, current)
    return best


if __name__ == "__main__":
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1],                              1),
        ([5, 4, -1, 7, 8],                23),
        ([-1, -2, -3],                    -1),
        ([0, 0, 0],                        0),
    ]
    for nums, expected in cases:
        result = max_subarray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  max_subarray({nums}) -> {result}")
