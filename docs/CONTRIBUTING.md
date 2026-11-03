# Contributing Guide

> 팀원이 섹션을 나눠 작성합니다. 각 섹션 끝에 작성자를 적어 주세요.

## 브랜치 전략 (GitHub Flow)

- `main`: 항상 깨지지 않는 상태. 직접 push 금지, PR로만 병합, 승인 1명 이상 필요.
- `feature/*`: Issue 하나당 작업 브랜치 하나. 병합 후 삭제.

우리 팀이 GitHub Flow를 선택한 이유:
1. 브랜치가 두 종류뿐이라 소규모 팀이 익히기 쉽다.
2. 모든 변경이 PR을 거쳐 리뷰와 Issue 추적이 남는다.
3. 작은 단위로 자주 병합해 충돌 범위를 줄인다.

작성자: <name>

## 브랜치 네이밍 규칙

- 형식: `feature/<name>-<topic>` (영문 소문자, 단어는 `-`로 연결)
- 예: `feature/kim-math-utils`, `feature/lee-contributing-pr-rule`

작성자: <name>

## 커밋 메시지 컨벤션

- 형식: `<type>: <subject>` (subject에 무엇을 바꿨는지 구체적으로)
- type: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- 좋은 예: `feat: add clamp() to math utils`, `docs: add stash scenario to troubleshooting log`
- 금지 예:
  - 대상을 알 수 없는 단어만 있는 경우: `update`, `fix`, `temp`, `wip`, `final`
  - 무엇을/왜 바꿨는지 없는 경우: `bug fix`, `edit file`

작성자: <name>

## PR 규칙

- 제목: 커밋 컨벤션과 같은 형식 (`feat: ...`)
- 본문 필수 항목 ([.github/pull_request_template.md](../.github/pull_request_template.md) 사용)
  - 연결 이슈: `Closes #<번호>`
  - 변경 사항 (What)
  - 변경 이유 (Why)
  - 테스트/검증 방법 (How)
- 병합 조건: 승인 1명 이상, 충돌 해결 완료

작성자: <name>

## 코드 리뷰 규칙

- "LGTM", "좋아요"만 남기는 리뷰는 금지. PR마다 실질 코멘트를 1개 이상 남깁니다.
  - 특정 라인/파일을 근거로 한 질문
  - 대안 제안, 리스크 지적, 개선 제안
- 작성자는 코멘트에 답글을 달거나 수정 커밋으로 반영합니다. 리뷰어와 작성자 사이에 최소 1회 상호작용이 남아야 합니다.
- 코멘트 예시: "`src/utils/math_utils.py` 12번째 줄: `min > max`일 때 처리가 없는데 `ValueError`를 던지면 어떨까요?"

작성자: <name>

## 충돌 대응 흐름

1. 발견: PR 또는 로컬 merge에서 충돌이 나면 해당 PR 작성자가 팀 채널에 공유합니다.
2. 협의: 충돌한 상대 작업자와 어떤 쪽을 남길지(keep both / choose one / refactor) 정합니다.
3. 해결: PR 작성자가 자기 브랜치에서 `main`을 merge해 충돌을 해결하고 push합니다. 공유 브랜치에 force push는 하지 않습니다.
4. 기록: 해결한 사람이 [conflict-resolution.md](conflict-resolution.md)에 템플릿대로 기록합니다.

작성자: <name>
