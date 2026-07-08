# Day 5 — Control Flow: if/elif/else, Ternary Expressions, match & Truthy/Falsy
# Run: python python/05_control_flow/practice.py

print("=== if / elif / else ===")


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


for s in [95, 82, 71, 40]:
    print(f"score={s} -> grade={grade(s)}")

print("\n=== Ternary expressions ===")
n = 7
label = "even" if n % 2 == 0 else "odd"
print(f"{n} is {label}")

nums = [-3, 0, 5, -1, 8]
signs = ["positive" if x > 0 else "non-positive" for x in nums]
print(signs)

print("\n=== match statements (Python 3.10+) ===")


def http_status_label(code):
    match code:
        case 200 | 201 | 204:
            return "success"
        case 400 | 401 | 403 | 404:
            return "client error"
        case 500:
            return "server error"
        case _:
            return "unknown"


for code in [200, 404, 500, 999]:
    print(f"{code} -> {http_status_label(code)}")

print("\n=== Truthy / falsy values ===")
falsy_examples = [0, 0.0, "", [], {}, set(), None, False]
for val in falsy_examples:
    print(f"{val!r:10} -> {'truthy' if val else 'falsy'}")

# The pattern you'll use constantly: guard clauses on emptiness,
# without an explicit "== []" or "== None" comparison.


def first_or_default(items, default=None):
    return items[0] if items else default


print(first_or_default([1, 2, 3]))
print(first_or_default([]))
