# fastapi/16_class_based_middleware/main.py
# Run: uvicorn main:app --reload

import logging
import time
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger("sprint")


class StockNode:
    def __init__(self, ticker: str, prices: list, next=None):
        self.ticker = ticker
        self.prices = prices
        self.next = next

    def total_value(self) -> int:
        return sum(self.prices)


def has_cycle(head) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


class TimingLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        self.logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({duration_ms:.2f}ms)")
        return response


app = FastAPI(title="Sprint Day 16")
app.add_middleware(TimingLoggerMiddleware, logger=logger)

_head = None
_tail = None


class StockIn(BaseModel):
    ticker: str
    prices: list[int]


@app.get("/")
def root() -> dict:
    return {"message": "Sprint Day 16 is running.", "day": 16}


@app.post("/stocks", status_code=201)
def create_stock(payload: StockIn) -> dict:
    global _head, _tail
    node = StockNode(payload.ticker, payload.prices)
    if _head is None:
        _head = _tail = node
    else:
        _tail.next = node
        _tail = node
    return {"ticker": payload.ticker, "prices": payload.prices}


@app.get("/stocks")
def list_stocks() -> dict:
    if has_cycle(_head):
        raise RuntimeError("corrupted stock list: cycle detected")
    result, node = [], _head
    while node:
        result.append({"ticker": node.ticker, "total_value": node.total_value()})
        node = node.next
    return {"stocks": result}
