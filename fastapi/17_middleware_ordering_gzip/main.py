# fastapi/17_middleware_ordering_gzip/main.py
# Run: uvicorn main:app --reload

import logging
import time
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
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

    @classmethod
    def from_pydantic(cls, payload) -> "StockNode":
        return cls(payload.ticker, payload.prices)

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


app = FastAPI(title="Sprint Day 17")
app.add_middleware(TimingLoggerMiddleware, logger=logger)  # inner: registered first
app.add_middleware(GZipMiddleware, minimum_size=1)           # outer: registered second

_head = None
_tail = None


class StockIn(BaseModel):
    ticker: str
    prices: list[int]


@app.get("/")
def root() -> dict:
    return {"message": "Sprint Day 17 is running.", "day": 17}


@app.post("/stocks", status_code=201)
def create_stock(payload: StockIn) -> dict:
    global _head, _tail
    node = StockNode.from_pydantic(payload)
    if _head is None:
        _head = _tail = node
    else:
        _tail.next = node
        _tail = node
    return {"ticker": payload.ticker, "prices": payload.prices}


@app.post("/stocks/reverse")
def reverse_stocks() -> dict:
    global _head
    _head = reverse_list(_head)
    result, node = [], _head
    while node:
        result.append(repr(node))
        node = node.next
    return {"order": result}
