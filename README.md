# Code Review Archive

이 리포지토리는 알고리즘 및 문제 해결 과정을 기록하고 코드 리뷰를 정리하는 개인 아카이브입니다. 각 문제에 대해 시간 복잡도와 공간 복잡도를 분석하고 개선 포인트를 정리합니다.

## 리뷰 계획

- 스케줄: 월요일부터 토요일까지 매일 최소 1개의 코드를 리뷰하고 업로드합니다.
- 초점: 시간 복잡도(Time Complexity)와 공간 복잡도(Space Complexity)에 중점을 둡니다.
- 목적: 지속적인 학습과 코드 최적화 능력 향상을 위해 매일 코드 리뷰를 실시합니다.

## 폴더 구조 (권장)

- Review/ : 일별 문제 풀이와 해설 마크다운 파일(.md)
- src/ : 문제별 파이썬 풀이(.py) — 추후 테스트 자동화를 위해 권장
- tests/ : pytest 기반 단위 테스트
- docs/ : 추가 문서(선택)

예:
```
/README.md
/IMPROVEMENT_PRIORITIES.md
/.gitignore
/Review/26.07.02.md
/src/26_07_02.py
/tests/test_26_07_02.py
```

## 테스트 실행 방법 (초기 가이드)

1. Python 설치(권장: 3.8+)
2. 가상환경 생성 및 활성화
   - python -m venv venv
   - source venv/bin/activate (macOS/Linux) 또는 venv\Scripts\activate (Windows)
3. pytest 설치
   - pip install pytest
4. 테스트 실행
   - pytest

(향후 requirements.txt와 GitHub Actions 워크플로를 추가하여 자동화 예정)

## 기여

이 저장소는 개인 학습용입니다. 개선 제안이나 PR은 환영합니다. PR을 보낼 때는 변경 목적과 테스트 추가 여부를 간단히 설명해주세요.
