# fastapi/10_week2_review/main.py
# Run: uvicorn main:app --reload

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Sprint Day 10")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]
    notes: Optional[str] = None


stock_db = {}
next_id = 1


def is_valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        elif ch in pairs.values():
            stack.append(ch)
    return not stack


def validate_notes(payload: StockIn):
    if payload.notes and not is_valid_parentheses(payload.notes):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="notes has unbalanced brackets")
    return payload


def get_stock_or_404(stock_id: int):
    if stock_id not in stock_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock {stock_id} not found")
    return stock_db[stock_id]


@app.get("/")
def root():
    return {"message": "Sprint Day 10 is running.", "day": 10}


@app.get("/stocks")
def list_stocks():
    return stock_db


# Static path registered BEFORE /stocks/{stock_id} — otherwise "sorted" would
# be routed to the dynamic path first and fail int conversion with a 422.
@app.get("/stocks/sorted")
def sorted_stocks(by: str = "price"):
    def avg_price(item):
        return sum(item[1]["prices"]) / len(item[1]["prices"])

    key_fn = avg_price if by == "price" else (lambda item: item[1]["ticker"])
    ordered = sorted(stock_db.items(), key=key_fn)
    return [{"id": sid, **data} for sid, data in ordered]


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn = Depends(validate_notes)):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    return stock


@app.put("/stocks/{stock_id}")
def update_stock(stock_id: int, payload: StockIn, stock: dict = Depends(get_stock_or_404)):
    stock_db[stock_id] = payload.model_dump()
    return {"id": stock_id, **stock_db[stock_id]}


@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    del stock_db[stock_id]
    return {"deleted_id": stock_id, "ticker": stock["ticker"]}
