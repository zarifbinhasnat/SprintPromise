class Stock:
    def __init__(self, ticker: str, prices: list[int]):
        self.ticker = ticker
        self.prices = prices

    def total_value(self) -> int:
        return sum(self.prices)

    @classmethod
    def from_dict(cls, data: dict) -> "Stock":
        return cls(data["ticker"], data["prices"])

    @staticmethod
    def is_valid_ticker(ticker: str) -> bool:
        return ticker.isupper() and ticker.isalpha()

    def __repr__(self) -> str:
        return f"Stock(ticker={self.ticker!r}, total_value={self.total_value()})"


acme = Stock.from_dict({"ticker": "ACME", "prices": [10, 20, 30]})
print(acme)                              # Stock(ticker='ACME', total_value=60)
print(Stock.is_valid_ticker("ACME"))     # True
print(Stock.is_valid_ticker("acme123"))  # False


class StockNode:
    def __init__(self, ticker: str, prices: list[int], next: "StockNode | None" = None):
        self.ticker = ticker
        self.prices = prices
        self.next = next

    def __repr__(self) -> str:
        return f"StockNode({self.ticker!r})"


def reverse_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


n1 = StockNode("ACME", [10, 20])
n2 = StockNode("ZED", [5])
n3 = StockNode("MID", [7, 7])
n1.next, n2.next = n2, n3

node = reverse_list(n1)
while node:
    print(node)
    node = node.next
# StockNode('MID')
# StockNode('ZED')
# StockNode('ACME')
