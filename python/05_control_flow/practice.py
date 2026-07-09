# if / elif / else
age = 17
if age >= 18:
    status = "adult"
elif age >= 13:
    status = "teen"
else:
    status = "child"
print(status)

# Ternary expressions
status = "adult" if age >= 18 else "minor"
label = "even" if age % 2 == 0 else "odd"
print(status, label)

# Truthy / falsy
prices = []
if prices:
    print("has prices")
else:
    print("no prices")

count = 0
if count:
    print("count is truthy")
else:
    print("count is falsy, even though it's a valid value")

# match statement
def describe_status_code(code):
    match code:
        case 200 | 201 | 204:
            return "success"
        case 400 | 404 | 422:
            return "client error"
        case 500:
            return "server error"
        case _:
            return "unknown"

for code in [200, 404, 500, 999]:
    print(code, "->", describe_status_code(code))

# match with destructuring
def describe_point(point):
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on the x-axis at {x}"
        case (0, y):
            return f"on the y-axis at {y}"
        case (x, y):
            return f"at ({x}, {y})"

for p in [(0, 0), (5, 0), (0, 5), (3, 4)]:
    print(p, "->", describe_point(p))
