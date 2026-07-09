# Run: uvicorn main:app --reload

import time
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 8")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} -> {response.status_code} ({duration:.3f}s)")
    return response


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


def max_subarray(nums):
    best = nums[0]
    current = 0
    for n in nums:
        if current < 0:
            current = 0
        current += n
        best = max(best, current)
    return best


@app.get("/")
def root():
    return {"message": "Sprint Day 8 is running.", "day": 8}


@app.get("/stocks")
def list_stocks():
    return stock_db


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}/best-run")
def stock_best_run(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")

    prices = stock_db[stock_id]["prices"]
    if len(prices) < 2:
        return {"id": stock_id, "best_run_sum": 0}

    changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    return {"id": stock_id, "ticker": stock_db[stock_id]["ticker"], "best_run_sum": max_subarray(changes)}
