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
패널을 최대화하여 더 편하게 읽거나, 최소화하여 작업 중에도 Operator를 계속 사용할 수 있습니다.
{% endalert %}

## Operator 사용하기 {#use-operator}

자연어를 사용하여 달성하려는 내용을 설명하세요. 명확하고 구체적인 프롬프트가 더 유용한 응답으로 이어집니다. 프롬프트는 단순한 질문부터 전체 빌드 요청까지 다양할 수 있습니다:

- **질문하기:** Liquid가 왜 렌더링되지 않나요?
- **무언가 빌드하기:** 지난 7일 동안 장바구니를 포기한 사용자의 Segment 초안을 작성해 주세요.

Operator는 단계별 안내, Braze 설명서 링크, 쉬운 설명, 그리고 작업에 직접 검토하고 삽입할 수 있는 Campaigns, Canvases, Segments, 콘텐츠 초안을 제공할 수 있습니다. Operator가 변경 사항을 제안하고 적용하는 방법에 대해서는 [Operator로 동작 수행하기](#take-action-with-operator)를 참조하세요.

Operator는 복잡한 다단계 작업에 적합한 [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra)를 사용합니다. Operator가 빌드를 도울 수 있는 전체 범위에 대해서는 [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)을 참조하세요. 바로 사용할 수 있는 예시는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)를 참조하세요.

아래 비디오에서 Operator가 할 수 있는 것의 한 가지 예시를 확인하세요.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## 모범 사례 {#best-practices}

Operator를 검색 엔진이 아닌 대화처럼 활용하세요. 짧고 자연스러운 프롬프트가 가장 효과적입니다.

- **구체적으로 질문하세요:** "Canvas에 대해 알려줘" 대신 "Canvas에서 행동 경로를 어떻게 사용하나요?"라고 시도해 보세요.
- **후속 질문을 하세요:** 첫 번째 응답이 필요에 맞지 않으면 명확한 설명이나 추가 세부 사항을 요청하세요. Operator는 채팅 기록을 지울 때까지 대화의 이전 메시지를 기억합니다.
- **페이지 인식 컨텍스트를 활용하세요:** Operator는 Braze 내에서 현재 위치를 이해합니다. 가장 정확한 결과를 얻으려면 관련 페이지를 보면서 Operator를 열어보세요.

## 경험 커스터마이즈하기 {#customize-your-experience}

### 브랜드 가이드라인 적용하기 {#apply-brand-guidelines}

브랜드 가이드라인을 컨텍스트로 추가하면, Operator가 카피를 제안하거나 기능을 설명할 때 브랜드의 보이스, 톤, 개성에 맞출 수 있습니다.

1. 채팅 패널에서 <i class="fa-regular fa-plus"></i>&nbsp;**Operator에 컨텍스트 추가**를 선택합니다.
2. **브랜드 가이드라인** 아래에서 하나 이상의 가이드라인을 선택합니다.

Operator는 선택한 가이드라인만 적용합니다. 워크스페이스 기본값을 포함하여 기본적으로 선택되는 항목은 없습니다.

에이전트 콘솔에서 **Operator로 생성** 또는 **Operator로 다듬기**를 통해 Operator를 열면, 에이전트에 이미 설정된 가이드라인이 컨텍스트로 자동 첨부됩니다. 같은 메뉴에서 가이드라인을 추가하거나 제거할 수 있습니다.

브랜드 가이드라인을 설정하려면 **콘텐츠** > **브랜드 가이드라인**으로 이동하세요. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)을 참조하세요.

![Operator 채팅 패널에서 브랜드 가이드라인을 선택하는 화면.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### 페이지 인식 컨텍스트 활용하기 {#leverage-page-aware-context}

Operator는 Braze 내 현재 위치를 자동으로 파악하고, 해당 컨텍스트에 맞게 응답을 맞춤화합니다. 예를 들어, Canvas를 구성하는 동안 Operator를 열면 워크플로에서 어디에 있는지 설명할 필요 없이 관련 단계를 제안하거나 Canvas 기능에 대한 안내를 제공할 수 있습니다.

이러한 컨텍스트 인식 덕분에 "내 편집기 설정을 브랜드 가이드라인에 맞게 업데이트해 줘"와 같이 짧고 자연스러운 프롬프트로 Operator와 상호작용할 수 있습니다. 요청이 대시보드의 다른 부분을 필요로 하면, Operator가 [해당 위치로 직접 이동]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)시켜 줍니다.


바로 사용할 수 있는 프롬프트 아이디어는 [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library)를 참조하세요.

## Operator 응답 활용하기 {#work-with-operator-responses}

### 추천 프롬프트로 시작하기 {#get-started-with-suggested-prompts}

Operator와 대화를 시작하면 일반적인 작업 및 현재 페이지를 기반으로 추천 프롬프트가 표시됩니다. 하나를 선택하여 빠르게 시작하거나, 직접 커스텀 질문을 입력하세요.

### Operator의 사고 과정 이해하기 {#understand-how-operator-thinks}

Operator는 **Reasoned**라는 레이블이 있는 접을 수 있는 섹션에 추론 단계를 표시합니다. 드롭다운을 선택하여 이 섹션을 확장하면 Operator가 어떻게 답변을 도출했는지 확인할 수 있습니다. 이는 제안 이면의 로직을 이해하거나 접근 방식을 검증하고 싶을 때 유용합니다.

![Operator 응답에서 접힌 상태의 Reasoned 드롭다운.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Operator로 동작 실행하기 {#take-action-with-operator}

Operator는 양식 필드 채우기, 설정 업데이트, 콘텐츠 생성, 또는 요청을 완료하기 위한 다른 페이지로의 이동 등 Braze 대시보드에서 직접 변경 사항을 제안하고 실행할 수 있습니다. 제안된 각 변경 사항은 적용되기 전에 검토하고 승인할 수 있도록 액션 카드로 제시됩니다. 작동 방식에 대한 자세한 내용은 [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)를 참조하세요.

### 다른 도구로 응답 복사하기 {#copy-responses-to-other-tools}

Operator 응답은 Markdown 형식으로 작성됩니다. 응답을 받으면 표시되는 도구 모음에서 **Copy**를 선택하여 전체 응답을 클립보드에 복사할 수 있습니다. 대부분의 도구는 Markdown을 기본적으로 렌더링하거나 약간의 조정으로 사용할 수 있습니다. 대상에 맞는 탭을 선택하세요:

{% tabs %}
{% tab Google Docs %}

먼저 **Tools** > **Preferences**로 이동하여 **Automatically detect Markdown**을 선택합니다. 그런 다음 Markdown을 붙여넣으려면 **Edit** > **Paste from Markdown**으로 이동합니다. 또한 마우스 오른쪽 버튼을 클릭하고 **Paste from Markdown**을 선택할 수도 있습니다.

{% endtab %}
{% tab Microsoft Word 및 Outlook %}

Word와 Outlook은 Markdown을 기본적으로 렌더링하지 않습니다. 응답을 웹 기반 Markdown 미리보기 도구에 붙여넣은 다음, 렌더링된 출력을 복사하여 **Keep Source Formatting**으로 Word 또는 Outlook에 붙여넣습니다. 또는 일반 텍스트로 붙여넣고 수동으로 서식을 지정할 수 있습니다.

{% endtab %}
{% tab Confluence 및 Notion %}

직접 붙여넣으세요. 두 플랫폼 모두 Markdown을 자동으로 렌더링합니다.

{% endtab %}
{% tab Slack %}

직접 붙여넣으세요. Slack은 굵게, 인라인 코드, 코드 블록, 인용문, 글머리 기호 목록을 렌더링하지만, Markdown 제목이나 링크 구문은 렌더링하지 않습니다.

{% endtab %}
{% tab 기타 도구 %}

파일에서 작업하거나 변환 도구를 사용하려면 다음 방법도 가능합니다:

- [VS Code](https://code.visualstudio.com/)와 같은 텍스트 편집기를 열고 새 텍스트 파일을 만든 다음, Markdown을 붙여넣고 미리보기로 서식을 확인한 후 다른 곳에 변환하거나 붙여넣습니다.
- [Pandoc](https://pandoc.org/)을 사용하여 Markdown을 Word 문서, HTML 또는 PDF로 변환하면 브라우저에서 붙여넣지 않고도 Word나 Outlook에서 예측 가능한 구조를 얻을 수 있습니다.

{% endtab %}
{% endtabs %}

## 세션 관리 {#manage-your-session}

### 응답 중지 {#stop-a-response}

Operator가 응답을 생성하는 동안 **전송** 버튼이 **중지** 버튼으로 변경됩니다. 질문을 다시 작성해야 하거나 응답이 잘못된 방향으로 진행되고 있는 경우 **중지**를 선택하여 응답을 조기에 종료할 수 있습니다.

### 기록 지우기 {#clear-your-history}

대화를 새로 시작하거나 대화에서 민감한 정보를 제거하려면 **채팅 기록 지우기**를 선택합니다. 이렇게 하면 현재의 모든 콘텐츠가 삭제되고 대화 컨텍스트가 초기화됩니다.

### 피드백 제공 {#provide-feedback}

각 응답 하단에 있는 엄지 위로 또는 엄지 아래로 버튼을 사용하여 간편하게 피드백을 제공할 수 있습니다. 여러분의 피드백은 Operator의 응답 품질을 지속적으로 개선하는 데 도움이 됩니다.

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합되며, OpenAI는 귀하와 Braze 간의 데이터 처리 부록(DPA) 조건에 따라 Braze 하위 처리자로 활동합니다. Braze를 통해 OpenAI로 전송되는 데이터는 OpenAI 모델을 학습하거나 개선하는 데 사용되지 않습니다. HIPAA(미국의료정보보호법) 준수, 데이터 유지, PII 처리 및 거버넌스에 대한 자세한 내용은 [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)을 참조하세요.

## 다음 단계 {#next-steps}

- [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): 대시보드 전반에서 Operator의 기능을 살펴보세요
- [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): 대시보드 페이지별로 정리된 예시 프롬프트를 확인하세요
- [동작 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Operator가 제안한 변경 사항을 검토하고 승인하는 방법을 알아보세요
- [지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Operator에서 직접 지원 티켓을 제출하세요
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): 일반적인 문제와 해결 방법을 확인하세요
- [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): HIPAA(미국의료정보보호법) 준수, 데이터 유지, PII 최소화 지침을 확인하세요