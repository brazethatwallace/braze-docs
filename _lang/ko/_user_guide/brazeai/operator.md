---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Braze 대시보드에 내장된 AI 기반 어시스턴트인 BrazeAI Operator<sup>TM</sup>의 기능과 모범 사례를 포함한 접근 및 사용 방법을 알아보세요."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup>는 대시보드에 내장된 AI 기반 어시스턴트입니다. Operator는 Campaigns, Canvases, Segments, 콘텐츠 초안 작성 등 구축 작업을 도와주며, 질문에 답변하고 문제를 해결하고 아이디어를 브레인스토밍하는 등 막히는 부분을 해결하는 데 도움을 줍니다.

## Operator에 접근하기 {#access-operator}

Braze 대시보드의 아무 페이지에서 Operator를 열 수 있습니다.

1. 사용자 프로필 옆에 있는 **BrazeAI Operator<sup>TM</sup>**를 선택합니다.
2. 사이드 패널에 Operator 채팅 패널이 열립니다.

![Operator 채팅 패널.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
패널을 최대화하면 더 편하게 읽을 수 있고, 최소화하면 작업하면서 Operator를 계속 사용할 수 있습니다.
{% endalert %}

## Operator 사용하기 {#use-operator}

자연어를 사용하여 달성하고자 하는 내용을 설명하세요. 명확하고 구체적인 프롬프트가 더 유용한 응답으로 이어집니다. 프롬프트는 간단한 질문부터 전체 빌드 요청까지 다양할 수 있습니다:

- **질문하기:** Liquid이 렌더링되지 않는 이유가 무엇인가요?
- **무언가 만들기:** 지난 7일 동안 장바구니를 이탈한 사용자의 Segment를 작성해 주세요.

Operator는 단계별 안내, Braze 설명서 링크, 쉬운 설명, 그리고 Campaigns, Canvases, Segments 및 콘텐츠 초안을 제공할 수 있으며, 이를 검토한 후 작업에 직접 삽입할 수 있습니다. Operator가 변경 사항을 제안하고 적용하는 방식에 대해서는 [Operator로 동작 수행하기](#take-action-with-operator)를 참조하세요.

Operator는 복잡한 다단계 작업에 적합한 [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra)를 사용합니다. Operator로 구축할 수 있는 전체 범위에 대해서는 [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)을 참조하세요. 바로 사용할 수 있는 예시는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)를 확인하세요.

아래 비디오에서 Operator가 할 수 있는 작업의 한 가지 예시를 확인하세요.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## 모범 사례 {#best-practices}

Operator를 검색 엔진이 아닌 대화로 활용하세요. 짧고 자연스러운 프롬프트가 가장 효과적입니다.

- **구체적으로 요청하세요:** "Canvas에 대해 알려줘" 대신 "Canvas에서 작업 경로를 어떻게 사용하나요?"라고 시도해 보세요.
- **후속 질문을 하세요:** 첫 번째 응답이 필요에 맞지 않으면 추가 설명이나 세부 정보를 요청하세요. Operator는 채팅 기록을 지울 때까지 대화의 이전 메시지를 기억합니다.
- **페이지 인식 컨텍스트를 활용하세요:** Operator는 Braze에서 현재 위치를 이해합니다. 가장 정확한 결과를 얻으려면 관련 페이지를 보면서 Operator를 열어 보세요.

## 사용 환경 맞춤 설정 {#customize-your-experience}

### 브랜드 가이드라인 적용 {#apply-brand-guidelines}

Operator 쿼리에 브랜드 가이드라인을 컨텍스트로 추가하면 응답이 브랜드의 목소리, 톤, 개성에 맞게 조정됩니다. Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하므로, 카피를 제안하거나 기능을 설명할 때 일관된 메시징을 보장합니다.

브랜드 가이드라인을 설정하려면 **콘텐츠** > **브랜드 가이드라인**으로 이동합니다. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)을 참조하세요.

![Operator 채팅 패널에서 브랜드 가이드라인을 선택하는 화면.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### 페이지 인식 컨텍스트 활용하기 {#leverage-page-aware-context}

Operator는 Braze 내 현재 위치를 자동으로 파악하고, 해당 컨텍스트를 기반으로 응답을 맞춤 조정합니다. 예를 들어 Canvas를 작성하는 동안 Operator를 열면, 워크플로에서 어디에 있는지 설명할 필요 없이 관련 단계를 제안하거나 Canvas 기능에 대한 안내를 제공합니다.

이러한 컨텍스트 인식 덕분에 "내 편집기 설정을 브랜드 가이드라인에 맞게 업데이트해 줘"처럼 짧고 자연스러운 프롬프트로 Operator와 상호작용할 수 있습니다. 요청에 대시보드의 다른 부분이 필요한 경우, Operator가 [해당 위치로 직접 이동]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)시켜 줍니다.


바로 사용할 수 있는 프롬프트 아이디어는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)를 참조하세요.

## Operator 응답으로 작업하기 {#work-with-operator-responses}

### 추천 프롬프트로 시작하기 {#get-started-with-suggested-prompts}

Operator와 대화를 열면, 일반적인 작업과 현재 페이지에 기반한 추천 프롬프트가 표시됩니다. 하나를 선택하면 빠르게 시작할 수 있고, 직접 커스텀 질문을 입력할 수도 있습니다.

### Operator의 사고 과정 이해하기 {#understand-how-operator-thinks}

Operator는 **Reasoned** 라는 레이블이 붙은 접을 수 있는 섹션에 추론 단계를 표시합니다. 드롭다운을 선택하여 섹션을 확장하면 Operator가 어떻게 답변을 도출했는지 확인할 수 있습니다. 이는 제안 뒤의 논리를 이해하거나 접근 방식을 검증하고 싶을 때 유용합니다.

![Operator 응답에서 접힌 상태의 „Reasoned" 드롭다운.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operator로 동작 수행하기 {#take-action-with-operator}

Operator는 Braze 대시보드에서 양식 필드 채우기, 설정 업데이트, 콘텐츠 생성, 요청 완료를 위한 다른 페이지 이동 등의 변경 사항을 직접 제안하고 실행할 수 있습니다. 제안된 각 변경 사항은 적용되기 전에 검토하고 승인할 수 있는 액션 카드로 표시됩니다. 자세한 작동 방식은 [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)를 참조하세요.

### 응답을 다른 도구에 복사하기 {#copy-responses-to-other-tools}

Operator 응답은 Markdown 형식으로 제공됩니다. 응답을 받은 후, 표시되는 도구 모음에서 **Copy**를 선택하면 전체 응답을 클립보드에 복사할 수 있습니다. 대부분의 도구는 Markdown을 기본적으로 렌더링하거나 약간의 조정만으로 사용할 수 있습니다. 대상 도구에 맞는 탭을 선택하세요:

{% tabs %}
{% tab Google Docs %}

먼저 **도구** > **환경설정**으로 이동하여 **Markdown 자동 감지**를 선택합니다. 그런 다음 Markdown을 붙여넣으려면 **수정** > **Markdown에서 붙여넣기**를 선택합니다. 마우스 오른쪽 버튼을 클릭하고 **Markdown에서 붙여넣기**를 선택할 수도 있습니다.

{% endtab %}
{% tab Microsoft Word 및 Outlook %}

Word와 Outlook은 Markdown을 기본적으로 렌더링하지 않습니다. 응답을 웹 기반 Markdown 미리보기 도구에 붙여넣은 후, 렌더링된 결과를 복사하여 **원본 서식 유지**로 Word 또는 Outlook에 붙여넣으세요. 또는 일반 텍스트로 붙여넣고 수동으로 서식을 지정할 수도 있습니다.

{% endtab %}
{% tab Confluence 및 Notion %}

바로 붙여넣으세요. 두 플랫폼 모두 Markdown을 자동으로 렌더링합니다.

{% endtab %}
{% tab Slack %}

바로 붙여넣으세요. Slack은 굵은 글씨, 인라인 코드, 코드 블록, 인용 블록, 글머리 기호 목록을 렌더링하지만, Markdown 제목이나 링크 구문은 렌더링하지 않습니다.

{% endtab %}
{% tab 기타 도구 %}

파일로 작업하거나 변환 도구를 사용하고 싶다면 다음과 같은 방법도 있습니다:

- [VS Code](https://code.visualstudio.com/)와 같은 텍스트 편집기를 열고 새 텍스트 파일을 만든 다음, Markdown을 붙여넣고 미리보기로 서식을 확인한 후 변환하거나 다른 곳에 붙여넣으세요.
- [Pandoc](https://pandoc.org/)을 사용하여 Markdown을 Word 문서, HTML 또는 PDF로 변환하면 브라우저에서 붙여넣지 않고도 Word나 Outlook에서 예측 가능한 구조를 얻을 수 있습니다.

{% endtab %}
{% endtabs %}

## 세션 관리 {#manage-your-session}

### 응답 중지 {#stop-a-response}

Operator가 응답을 생성하는 동안 **전송** 버튼이 **중지** 버튼으로 바뀝니다. 질문을 다시 작성하거나 응답이 잘못된 방향으로 진행될 경우 **중지**를 선택하여 응답을 조기에 종료할 수 있습니다.

### 대화 기록 삭제 {#clear-your-history}

새로 시작하거나 대화에서 민감한 정보를 제거하려면 **대화 기록 삭제**를 선택합니다. 이렇게 하면 현재 콘텐츠가 모두 삭제되고 대화 컨텍스트가 초기화됩니다.

### 피드백 제공 {#provide-feedback}

각 응답 하단에 있는 좋아요 또는 싫어요 버튼을 사용하여 간편하게 피드백을 제공할 수 있습니다. 피드백은 시간이 지남에 따라 Operator의 답변 품질을 개선하는 데 도움이 됩니다.

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합되며, OpenAI는 귀하와 Braze 간의 데이터 처리 부록(DPA) 조건에 따라 Braze 하위 처리자로 활동합니다. Braze를 통해 OpenAI로 전송되는 데이터는 OpenAI 모델을 학습하거나 개선하는 데 사용되지 않습니다. HIPAA(미국의료정보보호법) 준수, 데이터 유지, PII 처리 및 거버넌스에 대한 자세한 내용은 [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)을 참조하세요.

## 다음 단계 {#next-steps}

- [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): 대시보드 전반에서 Operator의 기능을 살펴보세요
- [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): 대시보드 페이지별로 정리된 예시 프롬프트를 확인하세요
- [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Operator가 제안한 변경 사항을 검토하고 승인하는 방법을 알아보세요
- [지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Operator에서 직접 지원 티켓을 제출하세요
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): 일반적인 문제와 해결 방법을 확인하세요
- [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): HIPAA(미국의료정보보호법) 준수, 데이터 보존, PII 최소화 가이드를 확인하세요