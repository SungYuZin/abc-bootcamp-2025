
# 데이터 부트캠프 AI 실습 프로젝트

이 프로젝트는 데이터 부트캠프 실습용으로 제작되었습니다. Python 3.13 (Anaconda 환경)에서 동작하며, 다양한 AI 및 데이터 분석 예제를 포함하고 있습니다.

## 주요 파일 및 역할

- `melon_api.py` : 멜론 차트 데이터를 수집하거나 분석하는 기능을 제공합니다.
- `openai_example.py` : OpenAI API를 활용한 텍스트 생성 또는 AI 예제 코드가 포함되어 있습니다.
- `streamlit_app.py` : Streamlit을 이용한 웹 대시보드/인터페이스를 구현합니다.
- `data_preprocessing.py` : 데이터 전처리 및 정제 관련 함수들을 포함합니다.
- `utils.py` : 프로젝트 전반에서 사용하는 유틸리티 함수들을 모아둔 파일입니다.
- `requirements.txt` : 프로젝트 실행에 필요한 주요 패키지 목록입니다.

> **참고:** 실제 파일명이 다르거나, 추가로 설명이 필요한 파일이 있다면 알려주세요.

## 설치 방법

1. Anaconda 환경에서 Python 3.13 버전으로 가상환경을 생성합니다.
2. 필요한 패키지를 설치합니다.

```bash
conda create -n abcbootcamp_ai python=3.13
conda activate abcbootcamp_ai
pip install -r requirements.txt
```

## 실행 방법

예시) Streamlit 앱 실행

```bash
streamlit run streamlit_app.py
```

## 필요 환경

- Python 3.13 (Anaconda 권장)
- 주요 패키지: streamlit, openai 등 (`requirements.txt` 참고)

## 라이선스

별도의 라이선스가 명시되지 않은 경우, 개인/교육용으로만 사용해 주세요.

---

추가로 포함할 내용이나 수정할 부분이 있다면 말씀해 주세요!