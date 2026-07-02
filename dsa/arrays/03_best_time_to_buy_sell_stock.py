# Day 4 — Best Time to Buy and Sell Stock
# NeetCode: https://neetcode.io/problems/best-time-to-buy-and-sell-stock
# Difficulty: Easy | Category: Arrays
#
# Problem:
#   You are given an array `prices` where prices[i] is the price of a
#   stock on day i. Choose a single day to buy and a later day to sell
#   to maximize profit. Return the max profit, or 0 if none is possible.


# --- Approach 1: Brute Force ---
# Time: O(n²) | Space: O(1)
def max_profit_brute(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > best:
                best = profit
    return best


# --- Approach 2: One-Pass Greedy (Optimal) ---
# Time: O(n) | Space: O(1)
#
# Walk the array once, tracking the lowest price seen so far. At every
# day, the best possible sale is "today's price minus the lowest price
# I've seen up to now" — so update the running minimum and the running
# max profit in the same pass.
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best_profit = max(best_profit, price - min_price)
    return best_profit


# --- Tests ---
if __name__ == "__main__":
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1],    0),
        ([2, 4, 1],          2),
        ([],                 0),
        ([5],                0),
    ]
    print("Best Time to Buy and Sell Stock — One-Pass Greedy")
    print("-" * 40)
    for prices, expected in cases:
        result = max_profit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] max_profit({prices}) = {result}  (expected {expected})")
