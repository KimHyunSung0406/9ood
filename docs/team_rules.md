# Team Rules & Collaboration Guidelines

본 문서는 `docs/team-rules.md`, `README.md`, 그리고 규칙 제정용 GitHub Issue에 바로 복사하여 사용할 수 있도록 정리한 팀 협업 규칙입니다. `[...]`로 표시된 팀 고유 항목(소통 채널 등)만 팀 상황에 맞게 채워서 사용하세요.

## 1. Pull Request (PR) 규칙

* **PR 크기 제한 (200줄 이하)**: 리뷰어가 10분 이내에 전체 맥락을 파악할 수 있도록 PR 1개당 변경 코드(추가+삭제)는 **최대 200줄 이하**로 제한합니다.
* **단일 목적 원칙 (1 Issue = 1 Branch = 1 PR)**: 하나의 PR에서는 하나의 기능 추가, 버그 수정, 또는 문서 작업만 다룹니다. 버그 수정과 신규 기능 추가, 변수명 일괄 변경을 한 PR에 섞지 않습니다.
* **PR 제목 형식**: `<영역>: <변경 내용을 설명하는 한 문장>` 형식으로 작성하여 PR 목록만 보고도 목적을 알 수 있게 합니다.
  * 예시: `resize: Keep aspect ratio when only width is given`
* **이슈 연결 필수**: 모든 PR은 사전에 생성된 GitHub Issue와 연결되어야 하며, PR 본문 하단에 `Closes #<이슈번호>`를 명시합니다.
* **PR 템플릿 준수**: `.github/PULL_REQUEST_TEMPLATE.md`의 모든 항목(`What`, `Why`, `How I tested`, `AI use`, `Checklist`)을 빠짐없이 작성합니다.

## 2. 코드 리뷰 (Code Review) 규칙

* **리뷰 인원**: 모든 PR은 작성자를 제외한 **최소 2명 이상의 팀원 리뷰 및 승인(Approve)**을 받아야 병합할 수 있습니다. (`docs/proposal.md` 및 `docs/team-rules.md` 등 팀 전체 합의 문서는 **모든 팀원**이 리뷰 코멘트를 남깁니다.)
* **리뷰 기한**: PR이 올라온 시점부터 **48시간 이내**에 리뷰를 완료합니다. 기한 내 리뷰가 어려운 경우 팀 소통 채널에 미리 공유합니다.
* **리뷰 중점 확인 사항**:
  1. 연결된 Issue의 요구사항을 정확히 충족하는가?
  2. 테스트 실행 결과 등 검증 가능한 근거(`How I tested`)가 있는가?
  3. 다른 팀원이 코드와 Docstring만 읽고도 동작을 이해하고 유지보수할 수 있는가?
* **리뷰 코멘트 접두사(Prefix) 규칙**: 리뷰 의도를 명확히 전달하기 위해 모든 코멘트 앞에 아래 4가지 접두사 중 하나를 붙입니다.

| 접두사 | 의미 및 병합 차단 여부 | 작성 예시 |
| :--- | :--- | :--- |
| **`blocking:`** | **병합 차단 (필수 수정)**: 버그, 요구사항 불일치, 타입 누락, 규칙 위반 등 병합 전 반드시 해결해야 하는 문제 | `blocking: width가 0 이하일 때 ValueError가 발생하지 않습니다.` |
| **`suggestion:`** | **개선 제안**: 더 나은 설계, 가독성 개선, 대안적인 구현 방식 제안 | `suggestion: 색상 값은 상수로 분리하는 것이 유지보수에 좋습니다.` |
| **`question:`** | **질문 및 설명 요청**: 코드의 의도나 예외 처리 방식에 대한 질문 (작성자 답변 필수) | `question: 홀수 높이 계산 시 반올림 대신 버림을 선택한 이유가 있나요?` |
| **`nit:`** | **사소한 다듬기 (선택 반영)**: 공백, 오탈자, 사소한 스타일 수정 (병합을 막지 않음) | `nit: 함수 사이에 빈 줄 2개를 유지해 주세요.` |

## 3. 병합 (Merge) 규칙

* **병합 주체**: PR 작성자 본인이 직접 병합하지 않고, **`blocking:` 코멘트가 모두 해결된 것을 확인한 마지막 승인 리뷰어(또는 팀장)**가 Merge 버튼을 누릅니다.
* **병합 방식**: 커밋 히스토리와 PR 단위의 맥락을 보존하기 위해 **`Create a merge commit`** 옵션을 기본으로 사용합니다.
* **브랜치 정리**: `main` 브랜치로 병합이 완료된 작업 브랜치는 즉시 삭제(`Delete branch`)합니다.
* **보호 브랜치 주의사항**:
  * `main` 브랜치에는 직접 푸시(Direct Push)하지 않으며, 모든 변경 사항은 PR을 통해서만 반영합니다.
  * `gh-pages` 브랜치는 GitHub Actions가 문서를 빌드하여 자동 배포하는 브랜치이므로 사람이 직접 수정하거나 건드리지 않습니다.

## 4. 브랜치 및 커밋 메시지 규칙

* **브랜치 명명 규칙**: 작업 목적에 따라 아래 접두사를 사용하며, 소문자와 하이픈(`-`)으로 작성합니다.
  * `feat/<name>`: 새로운 기능 구현 또는 함수 Docstring 작성 (예: `feat/docstrings`, `feat/blur-face`)
  * `fix/<name>`: 버그 및 오류 수정 (예: `fix/resize-aspect`)
  * `docs/<name>`: 제안서, 팀 규칙, README, MkDocs 설정 등 문서 작업 (예: `docs/proposal`, `docs/site`)
  * `chore/<name>`: 라이선스 추가, 패키지 의존성, 환경 설정 작업 (예: `chore/license`)
* **커밋 메시지 형식**: `<영역>: <동사로 시작하는 구체적인 변경 요약>` 형식으로 작성합니다.
  * 좋은 예시: `resize: Add _fit_height() helper with tests.`
  * 금지 예시: `wip`, `fix`, `fix again`, `asdf`, `final`, `update code` 등 변경 내용을 알 수 없는 메시지 금지

## 5. AI 도구 사용 및 명시 규칙 (필수 준수)

* **AI 활용 원칙**: 코딩 및 문서화에 AI 도구 활용은 허용되지만, **작성자는 자신이 올린 코드의 모든 줄을 직접 읽고 동작 원리를 완벽히 설명할 수 있어야 합니다.** 검증 및 최종 병합 결정의 책임은 사람에게 있습니다.
* **`## AI use` 작성 4대 필수 요소**: 모든 PR의 `## AI use` 섹션에 아래 4가지 사실을 2~3줄로 구체적으로 명시합니다.
  1. **Tool**: 사용한 AI 서비스/모델명 (예: Claude Code, GitHub Copilot, ChatGPT 등)
  2. **Where**: AI가 적용된 파일 경로, 함수명 또는 코드 라인 범위
  3. **How**: 활용 방식 (`generated` 초안 생성 / `completed` 자동완성 / `refactored` 리팩토링 / `explained` 개념 설명 / `reviewed` 코드 리뷰)
  4. **After**: AI 결과물에서 본인이 직접 수정, 삭제하거나 테스트·검증한 내용
* **올바른 작성 예시**:
  * 코드 생성에 활용한 경우:
    > `Claude Code generated the first draft of resize() and test_resize_width() in ossimg/proc.py and tests/test_proc.py. I rewrote the height calculation (it ignored aspect ratio) and added the height assertion. Copilot completed the docstrings; I checked each one.`
  * AI로 코드를 생성하지 않은 경우 (`none` 명시):
    > `none. I wrote this by hand. ChatGPT explained what Image.resize's filter argument does; no code was generated.`
* **페널티 주의**: `## AI use` 항목을 비워두거나 단순히 `used ChatGPT`, `AI helped a bit`처럼 어디에 어떻게 썼는지 알 수 없게 작성할 경우 **해당 PR 작성자 기여도 0점 및 팀 문서화 점수 -1점**이 부여됩니다.

## 6. 문서화 (Docstring & MkDocs) 및 라이선스 규칙

* **Docstring 선행 작성 및 동기화**:
  * 모든 공개(Public) 함수는 Google 스타일 Docstring을 작성합니다.
  * 각 Docstring에는 **한 줄 요약(Summary line)**, **`Args:` (인자명, 타입, 의미, 제약조건)**, **`Returns:` (반환 타입 및 설명)**, **`Raises:` (예외 타입 및 발생 조건)**, **`Examples:` (복사·실행 가능한 `>>>` 예제 및 출력)** 5가지 요소를 모두 포함합니다.
  * 함수 동작이나 인자가 변경되면 같은 PR 안에서 Docstring과 `README.md`도 함께 업데이트합니다.
* **오픈소스 라이선스 및 외부 라이브러리 규칙**:
  * 팀 프로젝트의 기본 라이선스는 **MIT License**를 사용합니다.
  * 외부 파이썬 패키지를 새로 `import`하기 전에 해당 라이브러리의 라이선스가 허용적 라이선스(**MIT, BSD, Apache 2.0**)인지 반드시 확인합니다.
  * **GPL, AGPL 등 강한 카피레프트(Copyleft) 라이선스** 라이브러리는 프로젝트 전체 라이선스에 영향을 주므로 임의로 병합하지 않으며, 대체재가 없어 반드시 써야 할 경우 병합 전 팀원 및 교수님과 사전 논의합니다.

## 7. 팀 소통 및 이슈 관리 규칙

* **공식 소통 채널**: `[카카오톡 단톡방 / Discord / Slack 등 팀 채널 기입]`
* **응답 시간**: 팀 채널 메시지 및 GitHub 멘션(`@username`)은 가능한 한 **24시간 이내**에 확인하고 응답합니다.
* **이슈 기반 작업 기록**:
  * 브레인스토밍, 기능 제안, 버그 리포트 등 모든 주요 논의는 GitHub Issue에 기록합니다.
  * 팀 전체 논의 이슈에는 **모든 팀원이 최소 1줄 이상 직접 코멘트**를 남겨 히스토리에 기록을 남깁니다.
  * 회의나 논의가 끝난 뒤에는 다음 할 일(Next actions)과 담당자 이름을 Issue에 명시합니다.

## 8. `docs/team-rules.md` 제출용 영문 요약본 (선택 활용)

강의 레퍼런스 저장소([sujinj-hyu/ossimg](https://www.google.com/search?q=https://github.com/sujinj-hyu/ossimg)) 스타일에 맞춰 영문으로 `docs/team-rules.md`를 구성할 경우 아래 내용을 사용할 수 있습니다.

* **Pull request size**: One function, one bug fix, or one document update per PR, **200 changed lines or fewer**. Never mix bug fixes, new features, and renames in a single PR.
* **Pull request format**: Use `<area>: <one full sentence>` for the PR title, link the target issue with `Closes #<issue_number>`, and fill out every section of `.github/PULL_REQUEST_TEMPLATE.md`.
* **Review**: At least **two reviewers** must review and approve within **48 hours**. Use review prefixes (`blocking:`, `suggestion:`, `question:`, `nit:`). Any unresolved `blocking:` comment stops the merge.
* **Merge**: The approving reviewer (or team leader), not the PR author, presses the merge button using **"Create a merge commit"**, then deletes the working branch immediately. Never edit `gh-pages` manually.
* **Branch names**: `feat/<name>`, `fix/<name>`, `docs/<name>`, `chore/<name>`
* **Commit messages**: `<area>: <imperative summary of what changed>` (no vague messages like `wip`, `fix`, or `asdf`).
* **AI use**: Always disclosed in the `## AI use` section of every pull request with four specific facts (**Tool**, **Where**, **How**, and **After / what was changed or verified by hand**). Write `none` if no AI tool was used.
* **Documentation & License**: Every public function requires a Google-style docstring (`Args` with types, `Returns`, `Raises`, `Examples`). All dependencies must be permissive (`MIT`, `BSD`, `Apache 2.0`) to stay compatible with our **MIT License**.
