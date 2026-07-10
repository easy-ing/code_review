# Code Review Archive

개요
- 개인 알고리즘 풀이 및 코드 리뷰 아카이브입니다. 각 문제에 대해 풀이 코드, 핵심 아이디어, 시간복잡도·공간복잡도 분석, 개선 포인트를 정리합니다.

링크
- 개선 로드맵: IMPROVEMENT_PRIORITIES.md

---

폴더 구조(권장)
- Review/ : 일별 풀이와 해설 마크다운 파일(.md)
- src/ : 풀이 소스 코드(.py)
- tests/ : pytest 기반 단위 테스트
- docs/ : 추가 문서(선택)

예시
```
/README.md
/IMPROVEMENT_PRIORITIES.md
/.gitignore
/Review/26.07.02.md
/src/26_07_02.py
/tests/test_26_07_02.py
```

---

빠른 시작 (로컬)
1. 저장소 클론
   - git clone https://github.com/easy-ing/code_review.git
   - cd code_review
2. 가상환경 생성 및 활성화
   - python -m venv venv
   - source venv/bin/activate  (macOS/Linux)
   - venv\Scripts\activate     (Windows)
3. 개발 의존성 설치 (향후 requirements.txt 추가 예정)
   - pip install pytest
4. 테스트 실행
   - pytest

---

문제 추가 규칙(권장)
1. 풀이 코드
   - src/에 파일 생성: src/YY_MM_DD_problemname.py 또는 src/26_07_02_card_deck.py
   - 함수는 `solution()` 이름으로 노출
   - 간단한 docstring(입력·출력 설명, 시간복잡도)을 추가
2. 리뷰 문서
   - Review/에 풀이 설명 마크다운(.md) 유지
   - 문서 내에 코드 블록(완전한 코드)와 핵심 아이디어/시간복잡도/총평 포함
3. 테스트
   - tests/에 해당 문제의 pytest 테스트 추가: tests/test_26_07_02.py
   - 예제 입력과 경계 케이스 포함

---

커밋 메시지 규칙(권장)
- Conventional Commits 스타일 권장
  - feat: 새로운 풀이 추가
  - fix: 버그 수정
  - docs: 문서 변경
  - chore: 리포트/설정 변경
  - test: 테스트 추가

예: `feat: add solution for 26_07_02 card deck` 또는 `docs: update README with testing guide`

---

정리 및 향후 작업
- 우선적으로 아래 작업을 권장합니다(상세: IMPROVEMENT_PRIORITIES.md 참고)
  1. .DS_Store 등 불필요 파일 제거 및 .gitignore 적용
  2. pytest 기반 테스트 추가 및 GitHub Actions로 자동화
  3. 일부 문제 최적화(명예의전당, 삼총사 등)

문의/기여
- 개인 학습용 저장소입니다. PR이나 개선 제안은 환영합니다. PR을 보낼 때는 변경 목적과 추가한 테스트에 대해 간단히 설명해주세요.
