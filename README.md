# good_pi_filter

개인 문서를 검토하거나 공유하는 학생, 연구자, 소규모 조직을 위해 `.txt` 및 `.md` 문서 내 개인정보를 자동으로 탐지하고 비식별화하는 Python 패키지입니다.

## 1. What it does

이 Python 패키지는 지정된 문서 형식에서 이름, 이메일 주소, 전화번호, 주민등록번호, 계좌번호 등 지원하는 개인정보를 탐지하고, 사용자가 지정한 문자열로 마스킹하거나 삭제합니다. 개인정보 유형별 처리 건수를 요약하고, 입력 파일은 보존한 채 비식별화된 결과를 새 파일로 저장해 개인 문서를 공유하거나 공개하기 전 검토를 돕습니다.

## 2. Installation

pip install -i https://test.pypi.org/simple/ good-pi-filter

## 3. Quick start

```python
from good_pi_filter import anonymize_file

result = anonymize_file(
    "personal_data.txt",
    output_path="personal_data_anonymized.txt",
)
print(result.summary)
```

## 4. Dependencies

TODO: 구현에 사용할 외부 패키지와 각 패키지의 라이선스를 확인해 기재합니다.

## 5. Tests

TODO (later in this course)

## 6. Documentation

* [문서 사이트](https://kimhyunsung0406.github.io/9ood/proposal/)
* [API 문서](https://kimhyunsung0406.github.io/9ood/api/)

## 7. Release

TODO (later in this course)

## 8. Team

* 김현성 — [KimHyunSung0406](https://github.com/KimHyunSung0406)
* 곽운철 — [guoyunzhe156-coder](https://github.com/guoyunzhe156-coder)
* 배준웅 — [bjw2130](https://github.com/bjw2130)
* 이영재 — [hmmmhm](https://github.com/hmmmhm)
* 차수호 — [ChaSuHo0707](https://github.com/ChaSuHo0707)

### AI 사용

TODO: 프로젝트에서 AI를 어떻게 사용했는지 작성합니다.

팀 규칙은 [team_rules.md](https://github.com/KimHyunSung0406/9ood/blob/main/docs/team_rules.md)를 참고하세요.

## 9. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
