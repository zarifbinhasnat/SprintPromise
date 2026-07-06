# dsa/two_pointers/01_valid_palindrome.py

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


if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("0P", False),
        ("Was it a car or a cat I saw?", True),
    ]
    for s, expected in cases:
        result = is_palindrome(s)
        status_label = "PASS" if result == expected else "FAIL"
        print(f"[{status_label}]  is_palindrome({s!r}) -> {result}")
