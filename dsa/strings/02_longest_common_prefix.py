def longest_common_prefix(strs):
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]


if __name__ == "__main__":
    cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"],    ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        ([""],                          ""),
        (["a"],                         "a"),
        ([],                            ""),
    ]
    for strs, expected in cases:
        result = longest_common_prefix(strs)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  longest_common_prefix({strs!r}) -> {result!r}")
