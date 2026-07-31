# fastapi/18_lifespan_resource_pool/main.py
# Run: uvicorn main:app --reload

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from pydantic import BaseModel


class StockNode:
    def __init__(self, ticker: str, prices: list, next=None):
        self.ticker = ticker
        self.prices = prices
        self.next = next

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, value):
        if not all(isinstance(p, (int, float)) and p >= 0 for p in value):
            raise ValueError("all prices must be non-negative numbers")
        self._prices = value


def merge_two_lists(l1, l2, key=lambda node: node.ticker):
    dummy = StockNode("", [])
    curr = dummy
    while l1 and l2:
        if key(l1) <= key(l2):
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


class ConnectionPool:
    def __init__(self, size: int):
        self._available = [f"conn-{i}" for i in range(size)]

    def acquire(self) -> str:
        if not self._available:
            raise RuntimeError("pool exhausted")
        return self._available.pop()

    def release(self, conn: str) -> None:
        self._available.append(conn)


app_state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_state["pool"] = ConnectionPool(size=3)
    yield
    app_state["pool"] = None


app = FastAPI(title="Sprint Day 18", lifespan=lifespan)


def get_pool() -> ConnectionPool:
    return app_state["pool"]


def build_chain(pairs):
    head = tail = None
    for ticker, prices in pairs:
        node = StockNode(ticker, prices)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


@app.get("/")
def root() -> dict:
    return {"message": "Sprint Day 18 is running.", "day": 18}


@app.post("/stocks/merge")
def merge_stocks(pool: ConnectionPool = Depends(get_pool)) -> dict:
    conn = pool.acquire()
    try:
        # Fresh chains each call — merge_two_lists rewires nodes in place,
        # so reusing the same nodes across requests would corrupt them.
        batch_a = build_chain([("ACME", [10]), ("MID", [7]), ("ZED", [5])])
        batch_b = build_chain([("BETA", [3]), ("NOVA", [9])])
        merged = merge_two_lists(batch_a, batch_b)
        order, node = [], merged
        while node:
            order.append(node.ticker)
            node = node.next
        return {"merged_order": order, "audit_connection": conn}
    finally:
        pool.release(conn)
