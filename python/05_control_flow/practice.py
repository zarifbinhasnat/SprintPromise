# Day 5 — Control Flow: if/elif/else, ternary, match, truthy/falsy

prices = [7, 1, 5, 3, 6, 4]

# --- Truthy/falsy: no more `len(x) > 0` ---
if prices:
    print("prices is non-empty")

empty_list, empty_dict, empty_str, zero = [], {}, "", 0
for value in (empty_list, empty_dict, empty_str, zero, None):
    print(f"{value!r} is truthy: {bool(value)}")

# --- Ternary expression ---
best_profit = 5
verdict = "profitable" if best_profit > 0 else "no profit"
print(verdict)

# --- if/elif/else chain ---
def profit_tier(profit):
    if profit <= 0:
        return "loss"
    elif profit < 5:
        return "small win"
    else:
        return "big win"

for p in (0, 3, 5, 12):
    print(p, "->", profit_tier(p))

# --- match statement (structural pattern matching) ---
def describe_tier(tier):
    match tier:
        case "loss":
            return "sell at a loss or break even"
        case "small win":
            return "modest gain"
        case "big win":
            return "strong gain"
        case _:
            return "unknown tier"

for tier in ("loss", "small win", "big win", "sideways"):
    print(tier, "->", describe_tier(tier))
