# python/10_lambdas_map_filter/practice.py

# lambda — anonymous one-expression function
square = lambda n: n * n
print(square(5))

# Lambdas as key functions — this is the whole reason they're worth learning
nums = [5, 2, 8, 1, 9]
print(sorted(nums, key=lambda n: -n))

stocks = [{"ticker": "AAA", "price": 42}, {"ticker": "BBB", "price": 10}]
print(sorted(stocks, key=lambda s: s["price"]))

# map() — apply a function to every element
prices = [10, 20, 30]
doubled = list(map(lambda p: p * 2, prices))
print(doubled)

# filter() — keep only elements where the function returns True
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

# Comprehension vs lambda+map/filter — the comprehension usually wins for
# simple cases (Day 9); lambda earns its keep specifically as a key function
evens_comp = [n for n in nums if n % 2 == 0]
print(evens_comp == evens)
