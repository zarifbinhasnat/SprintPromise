# fastapi/05_response_models/main.py
# Run: uvicorn main:app --reload
# Then open http://localhost:8000/docs

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Sprint Day 5")


class StockIn(BaseModel):
    ticker: str
    prices: list[int]


class StockOut(BaseModel):
    id: int
    ticker: str
    max_profit: int


stock_db = {}
next_id = 1


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()
    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}/max-profit", response_model=StockOut)
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

    return {
        "id": stock_id,
        "ticker": stock_db[stock_id]["ticker"],
        "max_profit": best_profit,
    }


# --- Combined task: two-pointer Valid Palindrome, wired into an endpoint ---


class PalindromeIn(BaseModel):
    text: str


class PalindromeOut(BaseModel):
    text: str
    is_palindrome: bool


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


@app.post(
    "/palindrome-check",
    response_model=PalindromeOut,
    status_code=status.HTTP_200_OK,
)
def palindrome_check(payload: PalindromeIn):
    # truthy/falsy guard from today's Python block — no need for "== ''"
    if not payload.text.strip():
        return {"text": payload.text, "is_palindrome": False}
    return {"text": payload.text, "is_palindrome": is_palindrome(payload.text)}
