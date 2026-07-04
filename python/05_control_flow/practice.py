def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(grade(95), grade(82), grade(71), grade(40))

best_profit = 0
profit = 5
best_profit = profit if profit > best_profit else best_profit
print(best_profit)

label = "even" if 4 % 2 == 0 else "odd"
print(label)


def describe(value):
    match value:
        case 0:
            return "zero"
        case int() if value < 0:
            return "negative int"
        case int():
            return "positive int"
        case [first, *rest]:
            return f"list starting with {first}"
        case {"ticker": t}:
            return f"a stock dict for {t}"
        case _:
            return "unknown shape"


print(describe(0))
print(describe(-5))
print(describe(5))
print(describe([1, 2, 3]))
print(describe({"ticker": "SPRINT"}))

falsy_values = [0, 0.0, "", [], {}, set(), None, False]
for v in falsy_values:
    assert not v

prices = []
if prices:
    print("has prices")
else:
    print("no prices yet")
