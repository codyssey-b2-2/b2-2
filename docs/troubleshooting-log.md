# Troubleshooting Log

> 4개 시나리오를 모두 수행합니다. 팀원마다 최소 1개 시나리오의 기록에 참여하고, 이름과 역할을 남깁니다.

## 시나리오 1: git commit --amend (최근 커밋 메시지 수정)

### 참여자
- 경내 / @datecoco (실행, 기록)

### 상황
- 이슈 #6 작업 중 `src/utils/string_utils.py`를 커밋하면서 메시지에 함수 이름 오타를 냈다: `feat: add slugfy() to string utils` (`89289f3`).
- 아직 push 전이라 원격에는 올라가지 않은 상태였다.

### 시도한 명령/절차
```bash
git log --oneline -1
# 89289f3 feat: add slugfy() to string utils
git commit --amend -m "feat: add slugify() to string utils"
git log --oneline -1
# 263d55b feat: add slugify() to string utils
```

### 결과
- 커밋 메시지가 올바른 함수 이름으로 고쳐졌고, 커밋 해시가 `89289f3`에서 `263d55b`로 바뀌었다.
- 주의할 점: amend는 커밋을 새로 만드는 것이라 이미 push한 커밋에 쓰면 원격과 히스토리가 달라진다. 그래서 push 전에만 쓴다.

### 왜 이 방법을 선택했는가 (Why)
- push 전의 가장 최근 커밋 하나만 고치면 되는 상황이라, 새 커밋을 추가하는 것보다 amend로 고치는 게 히스토리가 깔끔하다.

## 시나리오 2: git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지)

### 참여자
- <name> (<역할>)

### 상황
-

### 시도한 명령/절차
```bash
git reset --soft HEAD~1
```

### 결과
-

### 왜 이 방법을 선택했는가 (Why)
-

## 시나리오 3: git revert (원격에 push된 커밋 취소)

### 참여자
- <name> (<역할>)

### 상황
-

### 시도한 명령/절차
```bash
git revert <commit_hash>
```

### 결과
-

### 왜 이 방법을 선택했는가 (Why)
- reset 대신 revert를 선택한 이유

## 시나리오 4: git stash / git stash pop (작업 보관 후 전환)

### 참여자
- 경내 / @datecoco (실행, 기록)

### 상황
- `feature/datecoco-string-utils` 브랜치에서 `slugify()`를 반쯤 작성하던 중, `main`의 최신 커밋을 확인해야 했다.
- 작성 중인 파일(`src/utils/string_utils.py`, 아직 untracked)은 커밋하기엔 미완성이었다.

### 시도한 명령/절차
```bash
git stash push -u -m "wip: slugify 작성 중"   # -u: untracked 파일도 보관
git stash list
# stash@{0}: On feature/datecoco-string-utils: wip: slugify 작성 중
git switch main
git log --oneline -1
# 3fdc8c4 docs: add mission details, checklist and submission notes
git switch feature/datecoco-string-utils
git stash pop
# Dropped refs/stash@{0} (27089c3...)
```

### 결과
- 미완성 파일을 커밋하지 않고 잠시 치워 둔 뒤, `main` 확인 후 그대로 되살렸다.
- 주의할 점: 새로 만든 파일(untracked)은 `git stash`만으로는 보관되지 않아 `-u` 옵션이 필요하다.

### 왜 이 방법을 선택했는가 (Why)
- 의미 없는 "wip" 커밋을 남기면 커밋 컨벤션에 어긋나므로, 커밋 대신 stash로 작업을 임시 보관했다.
