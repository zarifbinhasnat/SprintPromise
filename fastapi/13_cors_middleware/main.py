# fastapi/13_cors_middleware/main.py
# Run: uvicorn main:app --reload

from contextlib import asynccontextmanager
from functools import lru_cache
from fastapi import FastAPI, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app_state = {}


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_state["request_count"] = 0
    yield
    app_state.clear()


app = FastAPI(title="Sprint Day 13", lifespan=lifespan)

# CORS — without this, a browser-based frontend running on a different
# origin (e.g. http://localhost:3000 calling this API on :8000) gets its
# request BLOCKED by the browser itself before a response body is ever read,
# even though the server responded fine. This middleware tells the browser
# which origins are allowed to read the response.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],   # exact origins only — no "*" with credentials
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return {"message": "Sprint Day 13 is running.", "day": 13, "requests_so_far": app_state["request_count"]}


@app.get("/fib/{n}")
def fibonacci(n: int):
    return {"n": n, "value": fib(n)}


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
