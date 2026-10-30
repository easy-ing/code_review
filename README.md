# Code Review Archive

개인 알고리즘 학습 기록과 코드 리뷰 아카이브입니다.  
이 저장소는 문제 풀이 과정, 핵심 아이디어, 시간복잡도 분석, 개선 포인트를 정리해 두는 공간입니다.

## 목적

- 알고리즘 문제를 푸는 과정 기록
- 코드의 장단점과 개선 포인트 정리
- 풀이와 설명을 한 곳에 보관
- 테스트 기반으로 코드 신뢰성 확보

## 저장소 구성

```text
code_review/
├── README.md
├── IMPROVEMENT_PRIORITIES.md
├── graph_algorithms.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── 26_06_20_three_sum.py
│   ├── 26_07_01_hall_of_fame.py
│   └── ...
├── tests/
│   ├── test_26_06_20.py
│   ├── test_26_07_01.py
│   └── ...
├── Review/
│   ├── 26.03.23.md
│   ├── 26.06.20.md
│   └── ...
└── .github/
    └── ...
```

### 디렉터리 설명

- `src/`: 풀이 코드 저장
- `tests/`: pytest 기반 테스트 코드 저장
- `Review/`: 문제별 풀이 설명, 아이디어, 시간복잡도, 개선점 정리
- `IMPROVEMENT_PRIORITIES.md`: 개선 작업 우선순위와 로드맵 문서
- `graph_algorithms.md`: 그래프 알고리즘 정리 문서

## 현재 특징

- Python 기반 알고리즘 풀이 정리
- 문제별 리뷰 문서 보관
- 테스트 코드 병행 작성
- 개인 학습용 아카이브 구조

## 빠른 시작

1. 저장소 클론

```bash
git clone https://github.com/easy-ing/code_review.git
cd code_review
```

2. 가상환경 생성

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows의 경우:

```powershell
.venv\Scripts\activate
```

3. 의존성 설치

```bash
pip install -r requirements.txt
```

4. 테스트 실행

```bash
pytest
```

## 풀이 파일 작성 규칙

- `src/` 아래에 풀이 코드를 저장
- 파일명 예시:
  - `src/26_07_02_card_deck.py`
  - `src/26_06_20_three_sum.py`
- 함수는 가능하면 `solution()` 형태로 작성
- 입출력 예시와 문서화 주석을 포함하면 좋음

## 리뷰 문서 작성 규칙

- `Review/` 아래에 날짜 기반 markdown 파일 생성
- 포함 항목 예시:
  - 문제 설명
  - 핵심 아이디어
  - 구현 방법
  - 시간복잡도
  - 공간복잡도
  - 개선 포인트
  - 총평

## 테스트 규칙

- 관련 테스트는 `tests/` 디렉터리에 작성
- 파일명 예시:
  - `tests/test_26_06_20.py`
- 정상 케이스와 경계 케이스를 함께 포함하는 것을 권장

## 추천 커밋 규칙

Conventional Commits 스타일을 권장합니다.

```text
feat: add solution for 26_07_02 card deck
fix: fix logic bug in hall of fame solution
docs: update README and review notes
test: add unit tests for three sum solution
chore: clean repository metadata
```

## 로드맵

- 불필요 파일 정리
- README 정리 및 온보딩 개선
- 테스트 자동화 추가
- 핵심 알고리즘 최적화
- GitHub Actions 기반 CI 구성

자세한 계획은 `IMPROVEMENT_PRIORITIES.md`를 참고하세요.

## 라이선스

현재 저장소에는 별도 라이선스 파일이 없으며, 개인 학습용 아카이브로 운영되고 있습니다.

## 문의

이 저장소는 개인 학습 및 코드 리뷰 기록용으로 만들어졌습니다.  
문제 제안, 코드 개선 아이디어, 리뷰 의견은 GitHub에서 이슈 또는 PR로 남기시면 좋습니다.

---

This repository is a personal archive for algorithm problem-solving and code review notes. It is intended for learning, tracking thought process, and documenting improvements over time.
