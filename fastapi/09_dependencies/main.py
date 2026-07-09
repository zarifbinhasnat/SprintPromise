# Run: uvicorn main:app --reload

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 9")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


def get_stock_or_404(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    return stock_db[stock_id]


def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums


@app.get("/")
def root():
    return {"message": "Sprint Day 9 is running.", "day": 9}


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
def get_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    return stock


@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    del stock_db[stock_id]
    return {"deleted_id": stock_id, "ticker": stock["ticker"]}


@app.get("/stocks/{stock_id}/compact-prices")
def compact_prices(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    prices = list(stock["prices"])
    move_zeroes(prices)
    return {"id": stock_id, "ticker": stock["ticker"], "compacted_prices": prices}
