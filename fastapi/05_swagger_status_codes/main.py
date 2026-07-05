# Day 5 — Swagger UI Deep Dive, Response Status Codes & Week 1 Review
# Run: uvicorn main:app --reload
#
# Interactive docs to open once the server is running:
#   http://localhost:8000/docs       Swagger UI — try requests from the browser
#   http://localhost:8000/redoc      ReDoc — read-only, cleaner for sharing
#   http://localhost:8000/openapi.json  the raw schema both UIs render

from fastapi import FastAPI, status

app = FastAPI(
    title="Sprint Day 5",
    description="Week 1 review — Swagger UI, status codes, and a palindrome check.",
)


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


# --- Success status codes via the `status_code` parameter ---
# Default for a plain return is 200. Naming the code that actually
# describes the response (201 for "I created something") is what
# makes the Swagger UI docs honest about what each route does.
# Proper *error* codes (404, etc.) via HTTPException are Day 6's topic.
@app.post("/echo", status_code=status.HTTP_201_CREATED)
def echo(payload: dict):
    return {"received": payload}


# --- Combined task: two-pointer palindrome check + control flow ---
# Reuses the two-pointer walk from today's DSA block, then a `match`
# statement (today's Python block) turns the boolean into a verdict.
@app.get("/check-ticker-palindrome/{ticker}")
def check_ticker_palindrome(ticker: str):
    left, right = 0, len(ticker) - 1
    is_palindrome = True
    while left < right:
        while left < right and not ticker[left].isalnum():
            left += 1
        while left < right and not ticker[right].isalnum():
            right -= 1
        if ticker[left].lower() != ticker[right].lower():
            is_palindrome = False
            break
        left += 1
        right -= 1

    match is_palindrome:
        case True:
            verdict = "palindrome"
        case False:
            verdict = "not a palindrome"

    return {"ticker": ticker, "is_palindrome": is_palindrome, "verdict": verdict}


# --- Week 1 mini-review ---
# Day 1: GET routes, path params           -> root()
# Day 2: query params                       -> fastapi/02_path_query_params
# Day 3: POST + Pydantic request bodies     -> fastapi/03_request_body
# Day 4: PUT/DELETE, dict-by-id "database"  -> fastapi/04_put_delete
# Day 5: status codes + docs                -> echo(), this file
