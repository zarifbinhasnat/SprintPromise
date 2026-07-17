# fastapi/14_request_logging/main.py
# Run: uvicorn main:app --reload

import logging
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger("sprint")

app_state = {}


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_state["request_count"] = 0
    yield
    logger.info(f"shutdown: handled {app_state['request_count']} requests")
    app_state.clear()


app = FastAPI(title="Sprint Day 14", lifespan=lifespan)


class StockNotFoundError(Exception):
    def __init__(self, ticker: str):
        self.ticker = ticker


class StockIn(BaseModel):
    ticker: str
    prices: list[int]


tickers_sorted: list[str] = []


def get_stock_or_404(ticker: str) -> int:
    idx = binary_search(tickers_sorted, ticker)
    if idx == -1:
        raise StockNotFoundError(ticker)
    return idx


@app.exception_handler(StockNotFoundError)
def stock_not_found_handler(request: Request, exc: StockNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "stock_not_found", "detail": f"ticker {exc.ticker!r} not found"},
    )


@app.middleware("http")
async def log_requests(request: Request, call_next):
    app_state["request_count"] += 1
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({duration_ms:.2f}ms)")
    return response


@app.get("/")
def root() -> dict:
    return {"message": "Sprint Day 14 is running.", "day": 14, "requests_so_far": app_state["request_count"]}


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn) -> dict:
    if payload.ticker not in tickers_sorted:
        tickers_sorted.append(payload.ticker)
        tickers_sorted.sort()
    return {"ticker": payload.ticker, "prices": payload.prices}


@app.get("/stocks/{ticker}")
def get_stock(ticker: str, idx: int = Depends(get_stock_or_404)) -> dict:
    # binary_search found `ticker` at position `idx` in the sorted list —
    # O(log n) instead of scanning tickers_sorted linearly.
    return {"ticker": tickers_sorted[idx], "index": idx}
