# Day 5 — FastAPI: Swagger UI Deep Dive & Status Codes (Week 1 Review)
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 5", description="Control Flow + Valid Palindrome + Status Codes")


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


# --- Carried over from Day 4, now with honest status codes ---
class StockIn(BaseModel):
    ticker: str
    prices: List[int]


stock_db = {}
next_id = 1


@app.get("/stocks")
def list_stocks():
    return stock_db


# status_code=201 — a new resource now exists, which is not the same as 200
@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int, response: Response):
    if stock_id not in stock_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"stock {stock_id} not found"}
    return {"id": stock_id, **stock_db[stock_id]}


@app.put("/stocks/{stock_id}")
def update_stock(stock_id: int, payload: StockIn, response: Response):
    if stock_id not in stock_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"stock {stock_id} not found"}
    stock_db[stock_id] = payload.model_dump()
    return {"id": stock_id, **stock_db[stock_id]}


@app.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int, response: Response):
    if stock_id not in stock_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"stock {stock_id} not found"}
    removed = stock_db.pop(stock_id)
    return {"deleted_id": stock_id, "ticker": removed["ticker"]}


# --- Route: Combined task — Valid Palindrome via two pointers ---
class TextIn(BaseModel):
    text: str


def is_palindrome(s: str) -> bool:
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


@app.post("/strings/palindrome-check")
def palindrome_check(payload: TextIn, response: Response):
    text = payload.text

    # truthy/falsy check — an empty/whitespace-only string is a client
    # error, not a valid check, so it earns its own status code.
    if not text.strip():
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "text must not be empty"}

    result = is_palindrome(text)

    match (result, len(text)):
        case (True, n) if n <= 1:
            reason = "trivially a palindrome (0 or 1 character)"
        case (True, _):
            reason = "reads the same forwards and backwards"
        case (False, _):
            reason = "does not read the same forwards and backwards"

    return {"text": text, "is_palindrome": result, "reason": reason}
