# Day 4 — FastAPI: PUT & DELETE, Completing CRUD
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 4", description="Dicts/Sets + Best Time to Buy/Sell + CRUD")


@app.get("/")
def root():
    return {"message": "Sprint Day 4 is running.", "day": 4}


# --- In-memory "database" ---
# Today's Python concept made real: a dict keyed by id is the simplest
# possible database. Real apps swap this for SQLAlchemy later (Day 31+),
# but the CRUD shape — read/write by key — never changes.
class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


@app.get("/stocks")
def list_stocks():
    return stock_db


@app.post("/stocks")
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


# --- Route: PUT — full replace of an existing resource by id ---
# PUT means "replace this resource entirely with what I'm sending."
# If the id doesn't exist yet, there's nothing to update.
@app.put("/stocks/{stock_id}")
def update_stock(stock_id: int, payload: StockIn):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}
    stock_db[stock_id] = payload.model_dump()
    return {"id": stock_id, **stock_db[stock_id]}


# --- Route: DELETE — remove a resource by id ---
@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int):
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}
    removed = stock_db.pop(stock_id)
    return {"deleted_id": stock_id, "ticker": removed["ticker"]}


# --- Route: Combined task — Best Time to Buy/Sell on a stored record ---
@app.get("/stocks/{stock_id}/max-profit")
def stock_max_profit(stock_id: int):
    """
    Runs today's DSA algorithm on a stock's stored price history.
    Same one-pass greedy from the DSA block, applied to real stored data
    instead of a hardcoded test list.
    """
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

# Note: real error handling (proper 404 status codes via HTTPException)
# lands on Day 6. For now, a dict with an "error" key keeps CRUD the
# only new concept in play.
