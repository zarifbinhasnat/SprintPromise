# python/05_control_flow/practice.py

age = 20
if age < 13:
    category = "child"
elif age < 20:
    category = "teen"
else:
    category = "adult"
print(category)

# Ternary expression — same if/else, one line
label = "adult" if age >= 20 else "minor"
print(label)

# match statement — structural pattern matching (Python 3.10+)
status_code = 404
match status_code:
    case 200:
        print("OK")
    case 400 | 404:
        print("Client error")
    case code if code >= 500:
        print("Server error")
    case _:
        print("Unknown")

# Truthy / falsy values — 0, "", None, [], {} are all falsy
for value in [0, "", None, [], {}, "hi", [1], 1]:
    print(value, "->", "truthy" if value else "falsy")

text = "  "
if not text.strip():
    print("text is empty or whitespace-only")
