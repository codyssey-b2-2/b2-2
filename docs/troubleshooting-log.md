# Troubleshooting Log

> 4개 시나리오를 모두 수행합니다. 팀원마다 최소 1개 시나리오의 기록에 참여하고, 이름과 역할을 남깁니다.

## 시나리오 1: git commit --amend (최근 커밋 메시지 수정)

### 참여자
- <name> (<역할: 실행/기록/검토>)

### 상황
- 문제가 무엇이었는지 (재현 가능한 설명)

### 시도한 명령/절차
```bash
git commit --amend -m "<수정한 메시지>"
```

### 결과
- 무엇이 어떻게 해결됐는지
- 주의할 점 (이미 push한 커밋이면 히스토리가 바뀜)

### 왜 이 방법을 선택했는가 (Why)
-

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
- <name> (<역할>)

### 상황
-

### 시도한 명령/절차
```bash
git stash
git switch <other-branch>
# ... 다른 작업 ...
git switch <original-branch>
git stash pop
```

### 결과
-

### 왜 이 방법을 선택했는가 (Why)
-
