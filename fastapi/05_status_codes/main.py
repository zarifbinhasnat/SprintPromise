# Run: uvicorn main:app --reload

from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 5")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


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


@app.put("/stocks/{stock_id}")
def update_stock(stock_id: int, payload: StockIn):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}
    stock_db[stock_id] = payload.model_dump()
    return {"id": stock_id, **stock_db[stock_id]}


@app.delete("/stocks/{stock_id}", status_code=status.HTTP_200_OK)
def delete_stock(stock_id: int):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}
    removed = stock_db.pop(stock_id)
    return {"deleted_id": stock_id, "ticker": removed["ticker"]}


@app.get("/stocks/{stock_id}/max-profit")
def stock_max_profit(stock_id: int):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}

    prices = stock_db[stock_id]["prices"]
    min_price = prices[0] if prices else 0
    best_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best_profit = max(best_profit, price - min_price)

    return {"id": stock_id, "ticker": stock_db[stock_id]["ticker"], "max_profit": best_profit}


@app.get("/stocks/{stock_id}/is-ticker-palindrome", status_code=status.HTTP_200_OK)
def is_ticker_palindrome(stock_id: int):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}

    ticker = stock_db[stock_id]["ticker"]
    result = is_palindrome(ticker)

    match result:
        case True:
            verdict = f"'{ticker}' reads the same forwards and backwards."
        case False:
            verdict = f"'{ticker}' is not a palindrome."

    return {"id": stock_id, "ticker": ticker, "is_palindrome": result, "verdict": verdict}
