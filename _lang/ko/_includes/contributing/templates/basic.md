이 템플릿을 사용하여 Braze Docs의 페이지 또는 섹션을 생성할 수 있습니다. 환경 설정, 미리보기, 콘텐츠 유형에 대해서는 리포지토리 접근 권한이 있는 기여자는 `docs/contributing/` 아래의 핸드북(예: `generating_a_preview.md` 및 `content_types.md`)을 참고하세요. 다른 모든 사용자는 [설명서 피드백]({{site.baseurl}}/feedback/)을 통해 문서 팀에 연락할 수 있습니다.

{% details 템플릿 보기 %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- 페이지 제목으로, 페이지 내 제목을 렌더링하는 데 사용됩니다. -->
# ARTICLE_TITLE

<!-- 개요는 '>' 문자로 시작하며 다룰 내용을 설명합니다. 선택 사항인 다음 단락에서는 주제를 높은 수준에서 소개합니다. -->
> DESCRIPTION.

INTRODUCTION.

<!-- 이 작업의 필수 조건입니다. 필수 조건이 없는 경우 이 섹션을 제거할 수 있습니다. -->
## 필수 조건

시작하기 전에 다음을 완료해야 합니다:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- 기능 워크플로에 대한 선택적 간략 설명입니다. -->
## 작동 방식

CONTENT.

<!-- 사용자에게 기능 통합 및 활성화 방법을 안내합니다. -->
 ## 통합
CONTENT.

<!-- 중첩 단계가 포함된 사용 가이드입니다. -->
## TASK_TO_COMPLETE

<!-- 작업에 대한 선택적 개요입니다. -->
CONTENT.

<!-- 단계의 목표를 설명하는 동작 지향적 헤더입니다. -->
### 1단계: ACTION_TO_COMPLETE

<!-- 이 동작을 완료하는 방법을 번호 목록 또는 단락으로 설명합니다. -->
CONTENT.

### 2단계: ACTION_TO_COMPLETE

CONTENT.
<!-- 지원되는 데이터 유형, 필드, 정의 등과 같은 선택적 참조입니다. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- 선택적 단계의 경우 헤더 끝에 "(선택 사항)"을 추가합니다. -->
### 3단계: OPTIONAL_ACTION_TO_COMPLETE (선택 사항)

CONTENT.
<!-- 지원되는 항목에 대한 선택적 섹션입니다. 더 구체적으로 하려면 중첩 헤더를 추가합니다. -->
## 지원되는 데이터 유형 / 지원되는 속성 / 지원되는 이벤트 / 지원되는 기타
CONTENT.
<!-- 기능을 사용하기 전에 사용자가 검토해야 할 중요한 고려 사항에 대한 선택적 섹션입니다. -->
## 고려 사항

CONTENT.

<!-- 일반적인 문제 해결을 안내하는 선택적 섹션입니다. -->
## 문제 해결

### ISSUE_TO_TROUBLESHOOT
CONTENT.

`````
{% endraw %}
{% enddetails %}