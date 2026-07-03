# fastapi/05_status_codes_swagger/main.py
# Run: uvicorn main:app --reload
# Then open http://localhost:8000/docs

from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Sprint Day 5")


@app.get("/")
def root():
    return {"message": "Sprint Day 5 is running.", "day": 5}


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


@app.get(
    "/palindrome-check/{text}",
    status_code=status.HTTP_200_OK,
    tags=["palindrome"],
    summary="Check whether a string is a palindrome",
)
def palindrome_check(text: str):
    if not text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="text must not be empty or whitespace-only",
        )

    result = is_palindrome(text)
    verdict = "palindrome" if result else "not a palindrome"
    return {"text": text, "is_palindrome": result, "verdict": verdict}
