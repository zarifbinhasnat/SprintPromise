# Day 5 — Valid Palindrome
# NeetCode: https://neetcode.io/problems/valid-palindrome
# Difficulty: Easy | Category: Two Pointers
#
# Problem:
#   Given a string s, return True if it is a palindrome after
#   converting all uppercase letters to lowercase and removing all
#   non-alphanumeric characters, False otherwise.


# --- Approach 1: Clean + Reverse (Brute Force) ---
# Time: O(n) | Space: O(n) — the cleaned list is a full copy
def is_palindrome_brute(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


# --- Approach 2: Two Pointers (Optimal) ---
# Time: O(n) — each pointer moves at most n times total
# Space: O(1) — two index variables, no extra structure
#
# Key insight: you don't need to build a cleaned copy first. Walk one
# pointer in from each end, skip past anything that isn't alphanumeric,
# and compare in place. The moment two real characters disagree, it's
# not a palindrome — no need to look at the rest of the string.
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


# --- Tests ---
if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("ab_a", True),
    ]
    print("Valid Palindrome — Two Pointer Solution")
    print("-" * 40)
    for s, expected in cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] is_palindrome({s!r}) = {result}  (expected {expected})")
