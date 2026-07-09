# range()
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

# enumerate()
prices = [7, 1, 5, 3, 6, 4]
for i, price in enumerate(prices):
    print(f"day {i}: ${price}")

# zip()
tickers = ["AAA", "BBB", "CCC"]
values = [10, 20, 30]
for ticker, price in zip(tickers, values):
    print(f"{ticker}: ${price}")

# break via early return
def first_negative(nums):
    for n in nums:
        if n < 0:
            return n
    return None

print(first_negative([3, 5, -2, 8]))

# continue
def sum_positive(nums):
    total = 0
    for n in nums:
        if n < 0:
            continue
        total += n
    return total

print(sum_positive([3, -5, 2, -8, 1]))

# while
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("liftoff")

countdown(3)

# for...else
def has_pair_summing_to(nums, target_sum):
    for i, a in enumerate(nums):
        for b in nums[i + 1:]:
            if a + b == target_sum:
                return True
    return False

print(has_pair_summing_to([1, 2, 3, 4], 7))
