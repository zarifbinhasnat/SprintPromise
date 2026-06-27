# Day 1 — FastAPI: Project Setup + First Routes
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 1", description="Variables + Two Sum + First API")


# --- Route 1: Root ---
@app.get("/")
def root():
    return {"message": "Hello from Sprint Day 1!", "status": "running"}


# --- Route 2: Greet by name (path parameter) ---
@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}


# --- Route 3: Two Sum endpoint (combined task) ---
class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int


@app.post("/two-sum")
def solve_two_sum(request: TwoSumRequest):
    """
    Accepts a list of integers and a target.
    Returns the indices of the two numbers that sum to the target.
    Uses O(n) hash map approach from today's DSA block.
    """
    seen = {}  # value -> index
    for i, num in enumerate(request.nums):
        complement = request.target - num
        if complement in seen:
            return {
                "indices": [seen[complement], i],
                "values": [request.nums[seen[complement]], num],
                "found": True,
            }
        seen[num] = i
    return {"indices": [], "values": [], "found": False}
