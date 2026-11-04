"""문자열 유틸 함수 모음 (작성자: datecoco)."""

import re


def slugify(text: str) -> str:
    """문자열을 URL에 쓰기 좋은 형태로 바꾼다.

    영문은 소문자로 바꾸고, 공백과 기호는 하이픈(-) 하나로 합친다.
    한글과 숫자는 그대로 둔다. 앞뒤 하이픈은 지운다.

    사용 예시:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("  B2-2  Git 협업  ")
        'b2-2-git-협업'
        >>> slugify("!!!")
        ''
    """
    if not isinstance(text, str):
        raise TypeError("text는 문자열이어야 합니다.")
    lowered = text.strip().lower()
    slug = re.sub(r"[^0-9a-z가-힣]+", "-", lowered)
    return slug.strip("-")
