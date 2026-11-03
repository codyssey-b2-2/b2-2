# <팀명> — Git 협업 실습 저장소

> [B2-2] 친구 3~5명과 함께 프로그램 만드는 법 연습하기 (Python과 Git 심화)

3~5인 팀이 GitHub Flow, Issue/PR, 코드 리뷰, 충돌 해결, Git 트러블슈팅을 실제로 해 보고 그 과정을 기록하는 저장소입니다.
결과물의 완성도보다 **협업 과정이 기록으로 남는 것**을 목표로 합니다.

## 팀원

| 이름 | GitHub | 역할 | 담당 유틸 함수 | 소개 |
| --- | --- | --- | --- | --- |
| <name1> | [@id1](https://github.com/id1) | <역할> | `src/utils/<file>.py` | [team/<name1>.md](team/<name1>.md) |
| <name2> | [@id2](https://github.com/id2) | <역할> | `src/utils/<file>.py` | [team/<name2>.md](team/<name2>.md) |
| <name3> | [@id3](https://github.com/id3) | <역할> | `src/utils/<file>.py` | [team/<name3>.md](team/<name3>.md) |

## 폴더 구조

```txt
.
├── README.md                  # 프로젝트 소개 (이 문서)
├── SUBMISSION.md              # 제출물 인덱스 (팀원별 Issue/PR/문서/증빙 링크)
├── .gitignore
├── .github/
│   └── pull_request_template.md   # PR 본문 템플릿 (Closes # / What / Why / How)
├── docs/
│   ├── CONTRIBUTING.md        # 협업 규칙 (브랜치, 커밋, PR, 리뷰, 충돌 대응)
│   ├── conflict-resolution.md # 충돌 해결 기록 (최소 2회, 비자명 충돌 1회 포함)
│   ├── troubleshooting-log.md # amend / reset --soft / revert / stash 기록
│   └── git-history.md         # git log --oneline --graph --all 결과
├── src/
│   └── utils/                 # 간단한 결과물: 팀원별 유틸 함수 모음 (Python 3.10+)
│       └── __init__.py
└── team/                      # 팀원별 소개 문서 (선택)
```

## 브랜치 전략: GitHub Flow

- `main`: 항상 깨지지 않는 상태를 유지합니다. 직접 push는 막혀 있고 PR로만 병합합니다(승인 1명 이상).
- `feature/<name>-<topic>`: 작업 단위 브랜치입니다. Issue 하나당 브랜치 하나를 만듭니다.

**GitHub Flow를 선택한 이유**
1. 브랜치가 `main`과 `feature/*` 두 종류뿐이라 3~5인 소규모 팀이 처음 배우기에 단순하다.
2. 모든 변경이 PR을 거치므로 코드 리뷰와 Issue 추적이 자연스럽게 기록된다.
3. 작업 단위를 작게 나눠 자주 병합하므로 충돌 범위가 줄어든다.

자세한 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 참고하세요.

## 작업 흐름

```bash
# 1. Issue 생성 (GitHub 웹) → 이슈 번호 확인 (예: #3)

# 2. 최신 main에서 브랜치 생성
git switch main
git pull origin main
git switch -c feature/<name>-<topic>

# 3. 작업 후 컨벤션에 맞게 커밋
git add <files>
git commit -m "feat: add <function> to <module>"

# 4. 원격에 push 후 PR 생성 (본문에 Closes #3)
git push -u origin feature/<name>-<topic>

# 5. 리뷰 반영 → 승인 1명 이상 → main에 병합 → 브랜치 삭제
```

## 간단한 결과물: 유틸 함수 모음

팀원마다 `src/utils/`에 함수를 1개 이상 추가하고 docstring에 사용 예시를 적습니다.

| 모듈 | 함수 | 작성자 | 설명 |
| --- | --- | --- | --- |
| `src/utils/<file>.py` | `<function>()` | <name1> | <설명> |
| `src/utils/<file>.py` | `<function>()` | <name2> | <설명> |
| `src/utils/<file>.py` | `<function>()` | <name3> | <설명> |

사용 예시:

```python
from src.utils.<file> import <function>

print(<function>(...))
```

## 문서

- [SUBMISSION.md](SUBMISSION.md): 제출물 인덱스
- [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md): 협업 가이드
- [docs/conflict-resolution.md](docs/conflict-resolution.md): 충돌 해결 기록
- [docs/troubleshooting-log.md](docs/troubleshooting-log.md): Git 트러블슈팅 기록
- [docs/git-history.md](docs/git-history.md): Git 히스토리 증빙

## 운영 규칙

- `main` 등 공유 브랜치에서는 히스토리를 재작성하지 않습니다.
- 팀 합의 없이 `git push --force`나 공유 브랜치 rebase를 하지 않습니다.
- 충돌과 트러블슈팅은 상황/절차/결과/주의점을 포함해 재현할 수 있게 기록합니다.

## 개발 환경

- Python 3.10 이상
- Git, GitHub
