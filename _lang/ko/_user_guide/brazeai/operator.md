---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Braze 대시보드에 내장된 AI 기반 어시스턴트인 BrazeAI Operator<sup>TM</sup>의 기능과 모범 사례를 포함한 접근 및 사용 방법을 알아보세요."
---

# BrazeAI Operator {#brazeai-operator}

> BrazeAI Operator<sup>TM</sup>는 대시보드에 내장된 AI 기반 어시스턴트입니다. Operator는 질문에 답변하고, 설정을 안내하며, 문제를 해결하고, 아이디어를 함께 고민하는 등 다양한 업무를 도와줍니다.

## Operator 접근하기 {#access-operator}

Braze 대시보드의 모든 페이지에서 Operator를 열 수 있습니다.

1. 고객 프로필 옆에 있는 **BrazeAI Operator<sup>TM</sup>**를 선택하세요.

![고객 프로필 옆의 BrazeAI Operator 아이콘.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Operator 채팅 패널이 화면 오른쪽에 열립니다.

![Operator 채팅 패널.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
패널을 최대화하여 읽기 편하게 확장하거나, 작업 중에도 Operator를 사용할 수 있도록 최소화하세요.
{% endalert %}

아래 동영상에서 Operator가 할 수 있는 작업의 한 가지 예시를 확인하세요.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Operator 사용하기 {#use-operator}

자연어로 달성하려는 목표를 설명하세요. 프롬프트는 간단한 질문부터 복잡한 요청까지 다양할 수 있습니다:

- **간단한 질문:** 왜 내 Liquid가 렌더링되지 않나요?
- **복잡한 요청:** 내 메시지의 `abort_message` 태그에 중단을 유발한 사용자 속성을 포함시키려면 어떻게 해야 하나요?

Operator는 단계별 지침, Braze 설명서 링크 및 쉬운 설명을 제공할 수 있습니다. 명확하고 구체적인 질문은 더 유용한 답변을 이끌어냅니다. Operator는 강력한 추론 능력을 제공하며 복잡한 다단계 작업에 적합한 [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2)를 사용합니다. 바로 사용할 수 있는 예시는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library/)를 참조하세요.

## 모범 사례 {#best-practices}

Operator를 검색 엔진이 아닌 대화 상대처럼 대하세요. 짧고 자연스러운 프롬프트가 가장 효과적입니다.

- **구체적으로 질문하세요:** "Canvas에 대해 알려주세요" 대신 "Canvas에서 행동 경로를 어떻게 사용하나요?"라고 물어보세요.
- **추가 질문을 하세요:** 첫 번째 답변이 필요한 내용을 충족하지 못할 경우, 명확한 설명이나 추가 세부 정보를 요청하세요.
- **페이지 인식 컨텍스트를 활용하세요:** Operator는 Braze 내에서 사용자의 위치를 파악합니다. 가장 정확한 결과를 얻으려면 관련 페이지를 보면서 Operator를 열어주세요.

## 경험 커스터마이즈하기 {#customize-your-experience}

### 브랜드 가이드라인 적용 {#apply-brand-guidelines}

Operator 쿼리에 브랜드 가이드라인을 컨텍스트로 추가하여 응답이 브랜드의 목소리, 어조 및 개성을 반영하도록 하세요. Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하므로, 문구를 제안하거나 기능을 설명할 때 일관된 메시징을 보장하는 데 도움이 됩니다.

브랜드 가이드라인을 설정하려면 **설정** > **브랜드 가이드라인**으로 이동하세요. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)을 참조하세요.

![Operator 채팅 패널에서 브랜드 가이드라인 선택하기.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### 페이지 인식 컨텍스트 활용 {#leverage-page-aware-context}

Operator는 Braze 내에서 사용자의 위치를 자동으로 파악하고 해당 컨텍스트에 맞춰 응답을 조정합니다. 예를 들어, Canvas를 구축하는 동안 Operator를 열면, 사용자가 워크플로에서 현재 위치를 설명하지 않아도 관련 단계를 제안하거나 Canvas 기능에 대한 안내를 제공할 수 있습니다.

이러한 컨텍스트 인식 기능 덕분에 "Canvas 워크플로에서 지연 단계를 추가하는 방법은 무엇인가요?" 대신 "지연을 추가하려면 어떻게 해야 하나요?"와 같이 더 짧고 자연스러운 질문을 할 수 있습니다. 대시보드 페이지별로 정리된 바로 사용할 수 있는 프롬프트는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library/)를 참조하세요.

## Operator 응답 활용하기 {#work-with-operator-responses}

### 추천 프롬프트로 시작하기 {#get-started-with-suggested-prompts}

Operator와 대화를 시작하면 일반적인 작업과 현재 페이지에 기반한 추천 프롬프트가 표시됩니다. 빠르게 시작하려면 하나를 선택하거나, 직접 커스텀 질문을 입력하세요.

### Operator의 사고 과정 이해하기 {#understand-how-operator-thinks}

Operator는 **Reasoned**라고 표시된 접을 수 있는 섹션에 추론 단계를 보여줍니다. 드롭다운을 선택하여 해당 섹션을 확장하고 Operator가 답변을 어떻게 도출했는지 확인하세요. 이는 제안의 배경 논리를 이해하거나 접근 방식을 검증하고자 할 때 유용합니다.

![Operator 응답에서 접힌 "Reasoned" 드롭다운.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operator와 함께 동작 실행하기 {#take-action-with-operator}

Operator는 Braze 대시보드에서 직접 변경 사항을 제안하고 실행할 수 있습니다. 예를 들어, 양식 필드 입력, 설정 업데이트 또는 콘텐츠 생성이 가능합니다. 제안된 각 변경 사항은 액션 카드로 제시되며, 적용되기 전에 검토하고 승인해야 합니다. 이 기능의 작동 방식에 대한 자세한 내용은 [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)를 참조하세요.

### 다른 도구로 응답 복사하기 {#copy-responses-to-other-tools}

Operator 응답은 Markdown 형식으로 제공됩니다. 응답을 받은 후, 표시되는 도구 모음에서 **Copy**를 선택하면 전체 응답이 클립보드에 복사됩니다. 대부분의 도구는 Markdown을 기본적으로 렌더링하거나 약간의 조정만으로 사용할 수 있습니다. 대상 도구에 맞는 탭을 선택하세요:

{% tabs %}
{% tab Google Docs %}

먼저 **Tools** > **Preferences**로 이동하여 **Automatically detect Markdown**을 선택하세요. 그런 다음 Markdown을 붙여넣으려면 **Edit** > **Paste from Markdown**을 선택하세요. 마우스 오른쪽 버튼을 클릭하고 **Paste from Markdown**을 선택할 수도 있습니다.

{% endtab %}
{% tab Microsoft Word 및 Outlook %}

Word와 Outlook은 Markdown을 기본적으로 렌더링하지 않습니다. 응답을 웹 기반 Markdown 미리보기 도구에 붙여넣은 다음, 렌더링된 출력을 복사하여 Word 또는 Outlook에 **Keep Source Formatting**으로 붙여넣으세요. 또는 일반 텍스트로 붙여넣고 수동으로 서식을 지정할 수도 있습니다.

{% endtab %}
{% tab Confluence 및 Notion %}

직접 붙여넣으세요. 두 플랫폼 모두 Markdown을 자동으로 렌더링합니다.

{% endtab %}
{% tab Slack %}

직접 붙여넣으세요. Slack은 굵은 글씨, 인라인 코드, 코드 블록, 인용문 및 글머리 기호 목록을 렌더링하지만, Markdown 제목이나 링크 구문은 렌더링하지 않습니다.

{% endtab %}
{% tab 기타 도구 %}

파일에서 작업하거나 변환 도구를 사용하려면 다음과 같은 방법도 있습니다:

- [VS Code](https://code.visualstudio.com/)와 같은 텍스트 편집기를 열고 새 텍스트 파일을 만든 다음, Markdown을 붙여넣고 미리보기로 서식을 확인한 후 다른 곳에 변환하거나 붙여넣으세요.
- [Pandoc](https://pandoc.org/)을 사용하여 Markdown을 Word 문서, HTML 또는 PDF로 변환하면 브라우저에서 붙여넣지 않고도 Word나 Outlook에서 예측 가능한 구조를 얻을 수 있습니다.

{% endtab %}
{% endtabs %}

## 세션 관리 {#manage-your-session}

### 응답 중지 {#stop-a-response}

Operator가 응답을 생성하는 동안, **Send** 버튼이 **Stop** 버튼으로 바뀝니다. 질문을 다시 표현해야 하거나 응답이 잘못된 방향으로 흘러갈 경우, **Stop**을 선택하여 응답을 조기에 종료하세요.

### 기록 지우기 {#clear-your-history}

대화를 새로 시작하거나 민감한 정보를 삭제하려면 **Clear chat history**를 선택하세요. 이렇게 하면 현재 모든 내용이 제거되고 대화 컨텍스트가 초기화됩니다.

### 피드백 제공 {#provide-feedback}

각 응답 하단에 있는 좋아요 또는 싫어요 버튼을 사용하여 빠른 피드백을 제공하세요. 피드백은 시간이 지남에 따라 Operator의 답변을 개선하는 데 도움이 됩니다.

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

### 모델 제공자를 하위 처리자 또는 제3자 제공자로 지정 {#model-providers-as-sub-processors-or-third-party-providers}

Braze 서비스를 통해 Braze가 제공하는 LLM 제공자와의 통합("Braze 제공 LLM")을 사용할 경우, 해당 Braze 제공 LLM의 제공자는 귀하와 Braze 간의 데이터 처리 부속서(DPA) 조건에 따라 Braze의 하위 처리자로서 역할을 수행합니다. BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합됩니다.

### OpenAI에서 데이터가 사용되는 방식 {#how-data-is-used-with-openai}

OpenAI를 활용하는 BrazeAI 기능을 통해 AI 출력("출력")을 생성하기 위해, Braze는 특정 정보("입력")를 OpenAI로 전송합니다. 입력은 사용자의 프롬프트, 대시보드에 표시되는 콘텐츠, 그리고 사용자의 쿼리와 관련된 워크스페이스 데이터로 구성됩니다. [OpenAI의 API 플랫폼 약관](https://openai.com/enterprise-privacy/)에 따라, Braze를 통해 OpenAI API로 전송된 데이터는 OpenAI 모델의 훈련 또는 개선에 사용되지 않습니다. 귀하와 Braze 사이에서, 출력은 귀하의 지적 재산입니다. Braze는 해당 출력에 대해 저작권 소유권을 주장하지 않습니다. Braze는 출력을 포함한 모든 AI 생성 콘텐츠에 대해 어떠한 종류의 보증도 하지 않습니다.

## 다음 단계 {#next-steps}

- [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library/): 대시보드 페이지별로 정리된 예시 프롬프트를 찾아보세요
- [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Operator가 제안한 변경 사항을 검토하고 승인하는 방법을 알아보세요
- [고객지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/): Operator에서 직접 고객지원 티켓을 제출하세요
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): 일반적인 문제 및 해결 방법을 참조하세요