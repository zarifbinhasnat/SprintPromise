# python/12_recursion/practice.py

# Every recursive function needs two things: a base case (when to stop) and
# a recursive case (how to shrink the problem toward that base case).
def countdown(n):
    if n <= 0:            # base case
        print("liftoff")
        return
    print(n)
    countdown(n - 1)      # recursive case — same function, smaller input


countdown(3)

# Recursion vs iteration — same result, different mental model
def sum_to_n_recursive(n):
    if n == 0:
        return 0
    return n + sum_to_n_recursive(n - 1)


def sum_to_n_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_to_n_recursive(5), sum_to_n_iterative(5))

# Tracing the call stack by hand for sum_to_n_recursive(3):
#   sum_to_n_recursive(3) calls sum_to_n_recursive(2) calls sum_to_n_recursive(1)
#   calls sum_to_n_recursive(0) -> returns 0
#   -> 1 + 0 = 1
#   -> 2 + 1 = 3
#   -> 3 + 3 = 6
# Nothing gets ADDED until the base case returns and the calls unwind —
# that's the part that trips people up: the work happens on the way back up.

# Naive recursive Fibonacci — no memo — to show WHY it gets slow
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(8)])
# fib(5) alone re-solves fib(3) twice and fib(2) three times — no memory of
# work already done. That repeated-subproblem waste is exactly what Day 12's
# DSA problem (Climbing Stairs) runs into, and what Day 13 fixes with memoization.
