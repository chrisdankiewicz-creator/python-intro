import re
from datetime import datetime

def walidacjaemail(email: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$", email or ""))

def area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("powinno być dodatne")
    return width * height

def filtrsort(nums, threshold=0):
    return sorted(n for n in nums if n > threshold)

def konwertacja(date_str: str, in_fmt: str = "%d-%m-%Y", out_fmt: str = "%Y/%m/%d") -> str:
    dt = datetime.strptime(date_str, in_fmt)
    return dt.strftime(out_fmt)

def palindrome(text: str) -> bool:
    s = "".join(ch.lower() for ch in (text or "") if ch.isalnum())
    return s == s[::-1]

