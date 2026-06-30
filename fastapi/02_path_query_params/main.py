# Day 2 — FastAPI: Path & Query Parameters
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI
from typing import Optional

app = FastAPI(title="Sprint Day 2", description="Strings + Valid Anagram + Query Params")


# --- Route 1: Path parameter (same as Day 1) ---
@app.get("/")
def root():
    return {"message": "Sprint Day 2 is running.", "day": 2}


# --- Route 2: Query parameters with defaults ---
# Anything NOT in the path that has a type hint becomes a query param.
# ?limit=5&q=hello -> limit=5, q="hello"
@app.get("/search")
def search(q: str = "", limit: int = 10):
    return {"query": q, "limit": limit, "results": [f"{q}-{i}" for i in range(limit)]}


# --- Route 3: Optional query parameter ---
@app.get("/greet/{name}")
def greet(name: str, loud: Optional[bool] = False):
    greeting = f"Assalamu Alaikum, {name}!"
    return {"greeting": greeting.upper() if loud else greeting}


# --- Route 4: Valid Anagram endpoint (combined task) ---
# Two strings arrive as query params: /check-anagram?s=anagram&t=nagaram
@app.get("/check-anagram")
def check_anagram(s: str, t: str):
    """
    Uses the same frequency-count algorithm from today's DSA block.
    """
    if len(s) != len(t):
        return {"s": s, "t": t, "is_anagram": False}

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts:
            return {"s": s, "t": t, "is_anagram": False}
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]

    return {"s": s, "t": t, "is_anagram": len(counts) == 0}
