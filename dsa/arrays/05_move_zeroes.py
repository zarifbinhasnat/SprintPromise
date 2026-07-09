def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums


if __name__ == "__main__":
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0],               [0]),
        ([1, 2, 3],         [1, 2, 3]),
        ([0, 0, 1],         [1, 0, 0]),
        ([],                []),
    ]
    for nums, expected in cases:
        result = move_zeroes(list(nums))
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  move_zeroes({nums}) -> {result}")
