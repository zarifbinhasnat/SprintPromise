def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)
    return best

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Amina"))
print(greet("Yusuf", greeting="Hi"))

def create_stock(ticker, prices, active=True):
    return {"ticker": ticker, "prices": prices, "active": active}

print(create_stock(ticker="AAA", prices=[1, 2, 3]))

def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)

def is_palindrome(s):
    """Return True if s reads the same forwards and backwards, ignoring case and punctuation."""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))

# The mutable default argument trap — demonstrated, then fixed
def add_ticker_buggy(ticker, seen=[]):
    seen.append(ticker)
    return seen

print(add_ticker_buggy("AAA"))   # ['AAA']
print(add_ticker_buggy("BBB"))   # ['AAA', 'BBB']  <- shared state bug

def add_ticker(ticker, seen=None):
    if seen is None:
        seen = []
    seen.append(ticker)
    return seen

print(add_ticker("AAA"))   # ['AAA']
print(add_ticker("BBB"))   # ['BBB']  <- fixed, fresh list each call
