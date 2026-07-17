# fastapi/11_custom_exception_handlers/main.py
# Run: uvicorn main:app --reload

from fastapi import FastAPI, Depends, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 11")


class StockIn(BaseModel):
    ticker: str
    prices: List[int]


class StockNotFoundError(Exception):
    def __init__(self, stock_id: int):
        self.stock_id = stock_id


class EmptyPricesError(Exception):
    def __init__(self, ticker: str):
        self.ticker = ticker


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def get_min(self):
        return self.min_stack[-1]


stock_db = {}
min_stacks = {}
next_id = 1


def get_stock_or_404(stock_id: int):
    if stock_id not in stock_db:
        raise StockNotFoundError(stock_id)
    return stock_db[stock_id]


def validate_prices(payload: StockIn):
    if not payload.prices:
        raise EmptyPricesError(payload.ticker)
    return payload


@app.exception_handler(StockNotFoundError)
def stock_not_found_handler(request: Request, exc: StockNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "stock_not_found", "detail": f"stock {exc.stock_id} not found"},
    )


@app.exception_handler(EmptyPricesError)
def empty_prices_handler(request: Request, exc: EmptyPricesError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": "empty_prices", "detail": f"{exc.ticker} needs at least one price"},
    )


@app.exception_handler(RequestValidationError)
def validation_handler(request: Request, exc: RequestValidationError):
    # Overrides FastAPI's default 422 body shape with the same
    # {"error", "detail"} envelope every handler above uses.
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": "validation_error", "detail": exc.errors()},
    )


@app.get("/")
def root():
    return {"message": "Sprint Day 11 is running.", "day": 11}


@app.get("/stocks")
def list_stocks():
    return stock_db


@app.get("/stocks/ranked")
def ranked_stocks():
    def avg_price(item):
        return sum(item[1]["prices"]) / len(item[1]["prices"])

    # Multi-key tuple sort — average price DESC, ticker ASC as the tiebreaker.
    # Negating only the price keeps the ticker tiebreak ascending; a plain
    # reverse=True would flip the ticker order too (Day 11 Python insight).
    ordered = sorted(stock_db.items(), key=lambda item: (-avg_price(item), item[1]["ticker"]))
    return [{"id": sid, **data, "avg_price": avg_price((sid, data))} for sid, data in ordered]


@app.post("/stocks", status_code=status.HTTP_201_CREATED)
def create_stock(payload: StockIn = Depends(validate_prices)):
    global next_id
    stock_id = next_id
    stock_db[stock_id] = payload.model_dump()

    ms = MinStack()
    for price in payload.prices:
        ms.push(price)
    min_stacks[stock_id] = ms

    next_id += 1
    return {"id": stock_id, **stock_db[stock_id]}


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int, stock: dict = Depends(get_stock_or_404)):
    return stock


@app.post("/stocks/{stock_id}/prices")
def add_price(stock_id: int, price: int, stock: dict = Depends(get_stock_or_404)):
    stock_db[stock_id]["prices"].append(price)
    min_stacks[stock_id].push(price)
    return {"id": stock_id, "price_added": price, "running_min": min_stacks[stock_id].get_min()}
