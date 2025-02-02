# -*- coding: utf-8 -*-
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1) Configure CORS (allowing all domains here for demonstration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_prime(n: int) -> bool:
    """
    Returns True if 'n' is a prime number, otherwise False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_perfect(n: int) -> bool:
    """
    Returns True if 'n' is a perfect number, otherwise False.
    A perfect number is equal to the sum of its proper divisors.
    """
    if n <= 1:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != (n // i):
                total += n // i
        i += 1
    return total == n


def is_armstrong(n: int) -> bool:
    """
    Returns True if 'n' is an Armstrong (Narcissistic) number, otherwise False.
    An Armstrong number is the sum of its own digits raised to
    the power of the number of digits.
    e.g. 371 -> 3^3 + 7^3 + 1^3 = 371
    """
    s = str(abs(n))
    power = len(s)
    total = sum(int(digit)**power for digit in s)
    return total == abs(n)


def sum_of_digits(n: int) -> int:
    """
    Returns the sum of the digits of 'n'.
    """
    return sum(int(digit) for digit in str(abs(n)))


def get_numbers_api_fact(n: int) -> str:
    """
    Fetches a 'math' type fact for the absolute value of 'n' from the Numbers API.
    Returns the 'text' field from the API response.
    """
    url = f"http://numbersapi.com/{abs(n)}/math?json=true"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data.get("text", f"No fact found for {n}.")
    except Exception:
        # Fallback if request fails or times out
        return f"No fact could be retrieved for the number {n}."


@app.get("/api/classify-number")
def classify_number(number: str):
    """
    Example:
      GET /api/classify-number?number=371

    Returns a JSON response with:
      {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "class_sum": 11,          # sum of its digits
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
      }

    Or if invalid:
      {
        "number": "alphabet",
        "error": true
      }
    """

    #  Validate the Input.
    try:
        num = int(number)
    except ValueError:
        # Return 400 Bad Request for non-numeric input
        return JSONResponse(
            status_code=400,
            content={
                "number": number,
                "error": True
            }
        )

    # Determine Basic Properties (Armstrong, Even/Odd)
    armstrong_check = is_armstrong(num)
    even_odd = "even" if (num % 2 == 0) else "odd"

    # The "properties" array can only have one or two items:
    # - "armstrong" + "odd"
    # - "armstrong" + "even"
    # - "odd"
    # - "even"
    properties = []
    if armstrong_check:
        properties.append("armstrong")
    properties.append(even_odd)

    #  Check for Prime and Perfect numbers.
    prime_check = is_prime(num)
    perfect_check = is_perfect(num)

    # Compute class_sum (sum of digits)
    class_sum_val = sum_of_digits(num)  # must be numeric

    # Build the Fun Fact
    # If Armstrong => custom message; otherwise => Numbers API
    if armstrong_check:
        digits_str = str(abs(num))
        power = len(digits_str)
        expression_parts = " + ".join(f"{d}^{power}" for d in digits_str)
        fun_fact = f"{num} is an Armstrong number because {expression_parts} = {num}"
    else:
        fun_fact = get_numbers_api_fact(num)

    # Return the 200 OK Response.
    return {
        "number": num,
        "is_prime": prime_check,
        "is_perfect": perfect_check,
        "properties": properties,
        "class_sum": class_sum_val,  # numeric
        "fun_fact": fun_fact
    }
