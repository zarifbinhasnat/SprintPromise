# Day 2 — Strings: Slicing, Methods & Immutability
# Run: python python/02_strings/practice.py

# --- Strings are immutable sequences ---
word = "Sprint"
print("=== Immutability ===")
print(f"word = {word!r}")
print(f"word[0] = {word[0]}, word[-1] = {word[-1]}")
# word[0] = "s"  # would raise TypeError — strings can't be mutated in place

# --- Slicing: [start:stop:step] ---
print("\n=== Slicing ===")
s = "abcdefgh"
print(f"s[2:5]   = {s[2:5]}")     # 'cde'
print(f"s[:3]    = {s[:3]}")      # 'abc'
print(f"s[3:]    = {s[3:]}")      # 'defgh'
print(f"s[::2]   = {s[::2]}")     # 'aceg' — every 2nd char
print(f"s[::-1]  = {s[::-1]}")    # 'hgfedcba' — reverse via slicing

# --- Common methods ---
print("\n=== Methods ===")
raw = "  Hello, World!  "
print(f"strip()      = {raw.strip()!r}")
print(f"lower()      = {raw.lower().strip()!r}")
print(f"replace      = {raw.strip().replace('World', 'Sprint')!r}")
print(f"split()      = {'a,b,c'.split(',')}")
print(f"join()       = {'-'.join(['a', 'b', 'c'])}")

# --- Counting characters (the pattern behind today's DSA problem) ---
print("\n=== Char Frequency ===")
text = "anagram"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(f"freq({text!r}) = {freq}")

# --- sorted() on a string returns a sorted list of chars ---
print(f"sorted('anagram') = {sorted('anagram')}")
print(f"''.join(sorted('anagram')) = {''.join(sorted('anagram'))}")

# Challenge: try these yourself
# 1. Write a one-liner that checks if a string is a palindrome using slicing
# 2. Count vowels in a sentence using a dict
# 3. Reverse the words in "Sprint is fun" (hint: split() + reversed() + join())
