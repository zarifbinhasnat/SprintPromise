# Day 3 — FastAPI: Request Bodies with Pydantic Models
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sprint Day 3", description="Lists + Contains Duplicate + First POST")


@app.get("/")
def root():
    return {"message": "Sprint Day 3 is running.", "day": 3}


# --- Request body model ---
# Unlike path/query params (which are strings, ints, bools in the URL),
# a request body can carry a whole JSON object — here, a list of ints.
class NumberList(BaseModel):
    nums: List[int]


@app.post("/check-duplicates")
def check_duplicates(payload: NumberList):
    """
    POST /check-duplicates
    Body: { "nums": [1, 2, 3, 1] }
    -> { "nums": [1, 2, 3, 1], "has_duplicates": true }

    Same seen-set algorithm from the DSA block — the only new concept is
    that `nums` arrives as a validated JSON body instead of a plain list.
    """
    seen = set()
    has_duplicates = False
    for num in payload.nums:
        if num in seen:
            has_duplicates = True
            break
        seen.add(num)
    return {"nums": payload.nums, "has_duplicates": has_duplicates}
