# Run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 6")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


@app.get("/")
def root():
    return {"message": "Sprint Day 6 is running.", "day": 6}


@app.get("/stocks")
def list_stocks():
    return stock_db


@app.get("/stocks/common-prefix")
def stocks_common_prefix():
    tickers = [record["ticker"] for record in stock_db.values()]
    if not tickers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no stocks yet")

    prefix = tickers[0]
    for i, char in enumerate(prefix):
        for ticker in tickers[1:]:
            if i >= len(ticker) or ticker[i] != char:
                return {"tickers": tickers, "common_prefix": prefix[:i]}
    return {"tickers": tickers, "common_prefix": prefix}


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


@app.put("/stocks/{stock_id}")
def update_stock(stock_id: int, payload: StockIn):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    stock_db[stock_id] = payload.model_dump()
    return {"id": stock_id, **stock_db[stock_id]}


@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    removed = stock_db.pop(stock_id)
    return {"deleted_id": stock_id, "ticker": removed["ticker"]}
