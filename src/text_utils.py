"""문자열 유틸. 작성: 임유현"""
import re


def slugify(text: str) -> str:
    """제목을 URL 에 쓸 수 있는 소문자-하이픈 문자열로 바꾼다.

    >>> slugify("Hello Git Flow")
    'hello-git-flow'
    """
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate(text: str, limit: int) -> str:
    """limit 글자를 넘으면 잘라 끝에 … 을 붙인다.

    >>> truncate("collaboration", 5)
    'colla…'
    >>> truncate("abc", 0)
    Traceback (most recent call last):
    ...
    ValueError: limit must be 1 or greater
    """
    if limit < 1:
        raise ValueError("limit must be 1 or greater")
    return text if len(text) <= limit else text[:limit] + "…"
