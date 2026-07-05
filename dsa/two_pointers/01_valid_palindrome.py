# Day 5 — Valid Palindrome
# NeetCode: https://neetcode.io/problems/valid-palindrome
# Difficulty: Easy | Category: Two Pointers
#
# Problem:
#   Given a string `s`, return True if it's a palindrome after
#   considering only alphanumeric characters and ignoring case,
#   False otherwise.


# --- Approach 1: Brute Force ---
# Time: O(n) | Space: O(n) — builds a cleaned copy of the string
def is_palindrome_brute(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


# --- Approach 2: Two-Pointer (Optimal) ---
# Time: O(n) | Space: O(1) — no extra copy of the string
#
# Walk from both ends toward the middle. Skip non-alphanumeric
# characters on either side, then compare. Any mismatch means it's
# not a palindrome; pointers crossing means every pair matched.
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

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
        ("aa", True),
        ("", True),
    ]
    print("Valid Palindrome — Two-Pointer")
    print("-" * 40)
    for s, expected in cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] is_palindrome({s!r}) = {result}  (expected {expected})")
