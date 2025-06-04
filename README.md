# med_agent

이 저장소는 간단한 건강검진 결과를 입력하면 의사 소견을 출력하는 파이썬 스크립트를 포함합니다.

## 사용법

1. 건강검진 결과를 JSON 형식으로 작성합니다. 예시는 `sample_results.json`을 참고하세요.
2. 아래 명령어로 소견을 생성합니다.

```bash
python3 doctor_note_agent.py sample_results.json
```

스크립트는 BMI, 혈압, 공복 혈당, LDL 콜레스테롤, 간효소(AST/ALT), 크레아티닌 수치를 이용해 간단한 의사 소견을 한국어로 출력합니다.
