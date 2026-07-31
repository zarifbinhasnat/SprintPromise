class Stock:
    def __init__(self, ticker: str, prices: list[int]):
        self.ticker = ticker
        self.prices = prices          # goes through the setter below, even in __init__

    @property
    def prices(self) -> list[int]:
        return self._prices

    @prices.setter
    def prices(self, value: list[int]):
        if not all(isinstance(p, (int, float)) and p >= 0 for p in value):
            raise ValueError("all prices must be non-negative numbers")
        self._prices = value

    @property
    def latest_price(self) -> int:
        return self._prices[-1] if self._prices else 0


acme = Stock("ACME", [10, 20, 30])
print(acme.prices)          # [10, 20, 30]
print(acme.latest_price)    # 30

acme.prices = [15, 25]
print(acme.latest_price)    # 25

try:
    acme.prices = [-5]
except ValueError as e:
    print(f"caught: {e}")

try:
    acme.latest_price = 100
except AttributeError as e:
    print(f"caught: {e}")
