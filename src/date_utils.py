"""날짜 유틸. 작성: 박경내"""
from datetime import date


def days_between(start: str, end: str) -> int:
    """두 ISO 날짜(YYYY-MM-DD) 사이의 일수를 구한다.

    >>> days_between("2026-09-01", "2026-09-15")
    14
    >>> days_between("2026-09-15", "2026-09-01")
    14
    """
    return abs((date.fromisoformat(end) - date.fromisoformat(start)).days)


def is_weekend(day: str) -> bool:
    """토요일·일요일이면 True.

    >>> is_weekend("2026-09-19")
    True
    """
    return date.fromisoformat(day).weekday() >= 5
