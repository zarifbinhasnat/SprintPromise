# Run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 7")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]
    internal_notes: str = ""


class StockOut(BaseModel):
    id: int
    ticker: str
    prices: List[int]


class TickerReverseOut(BaseModel):
    id: int
    original: str
    reversed: str


stock_db = {}
next_id = 1


def reverse_string(chars):
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


@app.get("/")
def root():
    return {"message": "Sprint Day 7 is running.", "day": 7}


@app.get("/stocks")
def list_stocks():
    return stock_db


@app.post("/stocks", response_model=StockOut, status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}", response_model=StockOut)
def get_stock(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}/reverse-ticker", response_model=TickerReverseOut)
def reverse_ticker(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")

    ticker = stock_db[stock_id]["ticker"]
    chars = list(ticker)
    reverse_string(chars)

    return {"id": stock_id, "original": ticker, "reversed": "".join(chars)}
