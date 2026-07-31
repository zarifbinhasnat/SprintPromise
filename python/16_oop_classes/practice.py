class Stock:
    def __init__(self, ticker: str, prices: list[int]):
        self.ticker = ticker
        self.prices = prices

    def total_value(self) -> int:
        return sum(self.prices)


acme = Stock("ACME", [10, 20, 30])
zed = Stock("ZED", [5, 5])

print(acme.ticker, acme.total_value())   # ACME 60
print(zed.ticker, zed.total_value())     # ZED 10

acme.prices.append(40)
print(acme.total_value())   # 100
print(zed.total_value())    # 10 — untouched, independent state


class StockNode:
    def __init__(self, ticker: str, prices: list[int], next: "StockNode | None" = None):
        self.ticker = ticker
        self.prices = prices
        self.next = next

    def total_value(self) -> int:
        return sum(self.prices)


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


n1 = StockNode("ACME", [10, 20])
n2 = StockNode("ZED", [5, 5])
n1.next = n2
print(has_cycle(n1))   # False

n2.next = n1            # manually create a cycle
print(has_cycle(n1))   # True
