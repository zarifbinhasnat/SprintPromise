def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == "__main__":
    cases = [
        (list("hello"), list("olleh")),
        (list("Hannah"), list("hannaH")),
        (list("a"), list("a")),
        (list(""), list("")),
        (list("ab"), list("ba")),
    ]
    for s, expected in cases:
        result = reverse_string(list(s))
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  reverse_string({s!r}) -> {result!r}")
