# Day 1 — Variables, Data Types & Type Conversion
# Run: python python/01_variables_datatypes/practice.py

# --- Primitive Types ---
name = "Hasnat"
age = 22
gpa = 3.8
is_student = True

print("=== Primitives ===")
print(f"Name: {name}, Age: {age}, GPA: {gpa}, Student: {is_student}")
print(f"Types: {type(name)}, {type(age)}, {type(gpa)}, {type(is_student)}")

# --- Type Conversion ---
print("\n=== Type Conversion ===")
age_str = str(age)
print(f"str(22) = '{age_str}' — type: {type(age_str)}")
print(f"int('42') = {int('42')} — type: {type(int('42'))}")
print(f"float('3.14') = {float('3.14')}")
print(f"bool(0) = {bool(0)},  bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}, bool('hi') = {bool('hi')}")

# --- f-strings ---
print("\n=== f-strings ===")
print(f"Hello, {name}! You are {age} years old.")
print(f"GPA rounded: {gpa:.1f}")   # format to 1 decimal

# --- Truthy / Falsy ---
print("\n=== Truthy / Falsy ===")
falsy_values = [0, 0.0, "", [], {}, None, False]
for val in falsy_values:
    print(f"bool({repr(val)}) = {bool(val)}")

# --- Dict Preview (used in DSA block) ---
print("\n=== Dict Preview ===")
scores = {"math": 95, "cs": 99, "physics": 88}
print(f"scores['cs'] = {scores['cs']}")
print(f"Keys: {list(scores.keys())}")
print(f"Values: {list(scores.values())}")

# Challenge: try these yourself
# 1. Create a variable for your full name, birth year, and city
# 2. Print a sentence using f-string combining all three
# 3. Convert your birth year to a string and concatenate " is my birth year"
