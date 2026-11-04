"""수학 유틸. 작성: 이나현"""


def clamp(value: float, low: float, high: float) -> float:
    """value 를 [low, high] 범위로 자른다.

    >>> clamp(15, 0, 10)
    10
    """
    return max(low, min(value, high))


def mean(values: list[float]) -> float:
    """산술 평균을 구한다.

    >>> mean([1, 2, 3, 4])
    2.5
    """
    return sum(values) / len(values)
