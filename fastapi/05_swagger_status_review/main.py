# Day 5 — FastAPI: Swagger UI Deep Dive, Status Codes & Week 1 Review
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Sprint Day 5",
    description="Week 1 review: path/query params, request bodies, full CRUD — now with correct status codes.",
)


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


# --- In-memory "database" (same dict-by-id pattern since Day 4) ---
class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


# --- Week 1 review: GET, POST, PUT, DELETE all in one file ---
@app.get("/stocks")
def list_stocks():
    return stock_db


# status_code= tells FastAPI (and Swagger) what to document AND return —
# 201 Created is the correct code for "a new resource now exists",
# not the default 200 every route has used through Day 4.
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


# 204 No Content means "it worked, and there's nothing to send back" —
# the correct code for a successful DELETE.
@app.delete("/stocks/{stock_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stock(stock_id: int):
    stock_db.pop(stock_id, None)
    return None


# --- New today: a route that returns 200 for a valid palindrome check ---
# Proper 404s via HTTPException are Day 6's topic — today status_code=
# is only about naming the *success* code correctly. A missing/invalid
# input still falls back to the simple {"error": ...} dict for now.
@app.get("/palindrome-check")
def palindrome_check(text: str):
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return {"text": text, "is_palindrome": False}
        left += 1
        right -= 1
    return {"text": text, "is_palindrome": True}


# --- Combined task: run Day 5's DSA two-pointer check against a stored ticker ---
@app.get("/stocks/{stock_id}/ticker-palindrome")
def ticker_palindrome(stock_id: int):
    """
    Runs today's Valid Palindrome two-pointer check against a stored
    stock's ticker — Week 1's dict-by-id storage, wired to Week 1's
    newest DSA pattern.
    """
    if stock_id not in stock_db:
        return {"error": f"stock {stock_id} not found"}

    ticker = stock_db[stock_id]["ticker"]
    left, right = 0, len(ticker) - 1
    while left < right:
        while left < right and not ticker[left].isalnum():
            left += 1
        while left < right and not ticker[right].isalnum():
            right -= 1
        if ticker[left].lower() != ticker[right].lower():
            return {"id": stock_id, "ticker": ticker, "is_palindrome": False}
        left += 1
        right -= 1
    return {"id": stock_id, "ticker": ticker, "is_palindrome": True}
