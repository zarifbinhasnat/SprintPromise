# fastapi/12_lifespan_events/main.py
# Run: uvicorn main:app --reload

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app_state = {}


def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP — runs once, before the app accepts any requests.
    # This is where you'd open a DB pool or load a model; here it precomputes
    # a small cache instead of recalculating climb_stairs() on every request.
    app_state["stair_cache"] = {n: climb_stairs(n) for n in range(1, 31)}
    app_state["request_count"] = 0
    print("startup: stair_cache warmed for n=1..30")

    yield  # <- the app runs here, handling requests, until shutdown

    # SHUTDOWN — runs once, after the last request finishes.
    # This is where you'd close a DB pool or flush a queue.
    print(f"shutdown: handled {app_state['request_count']} requests")
    app_state.clear()


app = FastAPI(title="Sprint Day 12", lifespan=lifespan)


class StockNotFoundError(Exception):
    def __init__(self, stock_id: int):
        self.stock_id = stock_id


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


def get_stock_or_404(stock_id: int):
    if stock_id not in stock_db:
        raise StockNotFoundError(stock_id)
    return stock_db[stock_id]


@app.exception_handler(StockNotFoundError)
def stock_not_found_handler(request: Request, exc: StockNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "stock_not_found", "detail": f"stock {exc.stock_id} not found"},
    )


@app.middleware("http")
async def count_requests(request: Request, call_next):
    app_state["request_count"] += 1
    return await call_next(request)


@app.get("/")
def root():
    return {"message": "Sprint Day 12 is running.", "day": 12, "requests_so_far": app_state["request_count"]}


@app.get("/stairs/{n}")
def stairs(n: int):
    # Served from the cache the lifespan startup hook built — no recomputation.
    if n not in app_state["stair_cache"]:
        return {"n": n, "ways": climb_stairs(n), "cached": False}
    return {"n": n, "ways": app_state["stair_cache"][n], "cached": True}


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    return stock
