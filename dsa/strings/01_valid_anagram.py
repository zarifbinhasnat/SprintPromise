# Day 2 — Valid Anagram
# NeetCode: https://neetcode.io/problems/valid-anagram
# Difficulty: Easy | Category: Strings
#
# Problem:
#   Given two strings s and t, return True if t is an anagram of s,
#   meaning both strings use exactly the same characters with the
#   same frequency (just rearranged), and False otherwise.


# --- Approach 1: Sorting ---
# Time: O(n log n) | Space: O(n)
def is_anagram_sort(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


# --- Approach 2: Hash Map / Frequency Count (Optimal) ---
# Time: O(n) | Space: O(1) — at most 26 lowercase letters
#
# Key insight: same dict pattern as Two Sum. Count every char in s,
# then walk t decrementing counts. If anything goes negative or a
# leftover count remains, they aren't anagrams.
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]

    return len(counts) == 0


# --- Tests ---
if __name__ == "__main__":
    cases = [
        ("anagram", "nagaram", True),
        ("rat",     "car",     False),
        ("",        "",        True),
        ("listen",  "silent",  True),
        ("aacc",    "ccac",    False),
    ]
    print("Valid Anagram — Hash Map Solution")
    print("-" * 35)
    for s, t, expected in cases:
        result = is_anagram(s, t)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] is_anagram({s!r}, {t!r}) = {result}  (expected {expected})")
