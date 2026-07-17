# python/14_type_hints/practice.py

from typing import Optional

# Type hints document what a function expects and returns — Python doesn't
# enforce them at runtime, but tools (mypy, your editor, FastAPI itself) do.
def add(a: int, b: int) -> int:
    return a + b


print(add(2, 3))
# print(add("2", "3"))   # Python still runs this fine — hints are NOT enforced
#                         # at runtime, they're documentation + tooling only.

# Collection types — what's INSIDE the list/dict, not just "a list"
def total_price(prices: list[int]) -> int:
    return sum(prices)


def ticker_lookup(prices_by_ticker: dict[str, list[int]]) -> list[str]:
    return list(prices_by_ticker.keys())


print(total_price([10, 20, 30]))
print(ticker_lookup({"ACME": [10, 20], "ZED": [5]}))

# Optional[X] means "X or None" — the same thing as `X | None`.
# It documents a real branch every caller has to handle.
def find_ticker(tickers: list[str], target: str) -> Optional[int]:
    for i, ticker in enumerate(tickers):
        if ticker == target:
            return i
    return None


index = find_ticker(["ACME", "ZED"], "ZED")
if index is not None:          # the hint is WHY this check exists
    print(f"found at index {index}")

# Why FastAPI leans on these so heavily: every route parameter and response
# model you've written since Day 3 (StockIn, `stock_id: int`, `List[int]`)
# has been a type hint. FastAPI reads them at import time to build request
# validation, response schemas, AND the interactive Swagger docs — the hints
# aren't just documentation there, they're the entire mechanism.
