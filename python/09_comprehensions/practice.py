# Nested comprehension — flatten
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(flat)

# Nested comprehension — build a grid
grid = [[r * c for c in range(3)] for r in range(3)]
print(grid)

# Generator expression — lazy evaluation
squares_gen = (n * n for n in range(1_000_000))
print(next(squares_gen))
print(sum(n * n for n in range(10)))

# Comprehension vs. map/filter
nums = [1, 2, 3, 4, 5]
evens_comp = [n for n in nums if n % 2 == 0]
evens_mapfilter = list(filter(lambda n: n % 2 == 0, nums))
print(evens_comp, evens_mapfilter)

# When a comprehension is too dense — readable loop instead
result = []
for x in range(10):
    if x % 2 != 0:
        continue
    for y in range(10):
        if y % 3 != 0 or x == y:
            continue
        result.append(x * y)
print(result)
