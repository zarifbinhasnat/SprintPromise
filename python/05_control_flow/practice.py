# Day 5 — Control Flow: if/elif/else, Ternary, match, Truthy/Falsy
# Run: python python/05_control_flow/practice.py

# --- if / elif / else ---
print("=== if / elif / else ===")
for score in [95, 82, 60, 40]:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"score={score} -> grade={grade}")

# --- Ternary expressions ---
print("\n=== Ternary Expressions ===")
n = 7
parity = "even" if n % 2 == 0 else "odd"
print(f"{n} is {parity}")

prices = [7, 1, 5, 3, 6, 4]
labeled = [("high" if p >= 5 else "low") for p in prices]
print(f"labeled = {labeled}")

# --- match statement (structural pattern matching, Python 3.10+) ---
print("\n=== match Statement ===")
def describe_status(status_code):
    match status_code:
        case 200 | 201 | 204:
            return "success"
        case 400 | 401 | 403 | 404:
            return "client error"
        case 500:
            return "server error"
        case _:
            return "unknown"

for code in [200, 404, 500, 999]:
    print(f"{code} -> {describe_status(code)}")

# match can also destructure, not just compare literals
def describe_point(point):
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on the x-axis at {x}"
        case (0, y):
            return f"on the y-axis at {y}"
        case (x, y):
            return f"point at ({x}, {y})"

for pt in [(0, 0), (3, 0), (0, -2), (4, 5)]:
    print(f"{pt} -> {describe_point(pt)}")

# --- Truthy / Falsy ---
print("\n=== Truthy / Falsy ===")
values = [0, 1, "", "hi", [], [1], {}, {"a": 1}, None]
for v in values:
    print(f"bool({v!r}) = {bool(v)}")

# The idiomatic way to check "is this empty/missing" — no need for len() == 0
stock_db = {}
if not stock_db:
    print("stock_db is empty (falsy)")

# Challenge: try these yourself
# 1. Write a ternary that labels a NeetCode difficulty as "warmup" if easy, else "grind"
# 2. Rewrite describe_status() using if/elif instead of match — which reads better to you?
