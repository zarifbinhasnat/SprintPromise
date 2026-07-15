# dsa/stack/01_valid_parentheses.py

def is_valid_brute(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""
    # Time:  O(n^2) — up to n/2 passes, each an O(n) replace
    # Space: O(n) — a new string is built on every replace call


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        elif ch in pairs.values():
            stack.append(ch)
    return not stack
    # Time:  O(n) — one pass
    # Space: O(n) — stack holds up to n/2 open brackets


if __name__ == "__main__":
    cases = [
        ("()",       True),
        ("()[]{}",   True),
        ("(]",       False),
        ("([)]",     False),
        ("{[]}",     True),
        ("",         True),
        ("(((",      False),
        ("(())",     True),
    ]
    for s, expected in cases:
        result = is_valid(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  is_valid({s!r}) -> {result}")
