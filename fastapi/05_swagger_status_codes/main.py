# fastapi/05_swagger_status_codes/main.py
# Run: uvicorn main:app --reload

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Sprint Day 5")


class PalindromeIn(BaseModel):
    text: str


class PalindromeOut(BaseModel):
    text: str
    is_palindrome: bool
    verdict: str


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


@app.get("/", tags=["Meta"])
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


@app.post(
    "/palindrome-check",
    response_model=PalindromeOut,
    status_code=status.HTTP_200_OK,
    tags=["DSA Demos"],
    summary="Check whether a string is a valid palindrome",
)
def palindrome_check(payload: PalindromeIn):
    result = is_palindrome(payload.text)
    verdict = "palindrome" if result else "not a palindrome"
    return PalindromeOut(text=payload.text, is_palindrome=result, verdict=verdict)
