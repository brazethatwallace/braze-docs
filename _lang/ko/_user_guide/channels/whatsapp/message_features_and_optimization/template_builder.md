---
nav_title: WhatsApp 템플릿 빌더
article_title: WhatsApp 템플릿 빌더
description: "WhatsApp 템플릿 빌더를 사용하여 Braze에서 직접 WhatsApp 메시지 템플릿을 생성, 구성 및 제출하는 방법을 알아보세요."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 템플릿 빌더 {#whatsapp-template-builder}

> WhatsApp 템플릿 빌더를 사용하면 Braze에서 직접 WhatsApp 메시지 템플릿을 생성하고 제출할 수 있으며, Braze와 Meta Business 매니저 사이를 오갈 필요가 없습니다. Meta가 템플릿을 승인하면 원하는 만큼 많은 Campaign과 Canvas에서 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## 템플릿 만들기 {#create-a-template}

### 1단계: WhatsApp 템플릿으로 이동하기 {#step-1-go-to-whatsapp-templates}

**콘텐츠** > **템플릿** > **WhatsApp**으로 이동한 다음 **새 템플릿 만들기**를 선택합니다.

![새 템플릿을 만드는 버튼이 있는 WhatsApp 템플릿 페이지.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

WhatsApp Campaign 또는 Canvas를 작성하는 도중에도 템플릿을 만들 수 있습니다. 자세한 내용은 [Campaign 또는 Canvas에서 템플릿 만들기](#create-a-template-from-a-campaign-or-canvas)를 참조하세요.

### 2단계: 카테고리 및 유형 선택하기 {#step-2-choose-a-category-and-type}

템플릿 카테고리와 템플릿 유형을 선택한 다음, 준비가 되면 **템플릿으로 계속**을 선택합니다.

{% alert note %}
Meta는 [카테고리 가이드라인](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization)과 콘텐츠를 기준으로 템플릿을 검토합니다.
{% endalert %}

#### 마케팅 {#marketing}

마케팅 템플릿은 프로모션 및 인게이지먼트 메시지(예: 환영 메시지, 프로모션, 오퍼, 쿠폰, 뉴스레터, 공지)에 사용됩니다.

| 유형 | 설명 |
| --- | --- |
| **커스텀** | 처음부터 직접 작성하는 표준 WhatsApp 메시지입니다. 이 레이아웃은 [템플릿 작성하기](#step-4-build-your-template)에서 다룹니다. |
| **캐러셀** | 가로로 스크롤할 수 있는 카드가 포함된 메시지입니다. 자세한 내용은 [캐러셀 템플릿]({{site.baseurl}}/whatsapp_carousel_templates)을 참조하세요. |
| **한정 기간 오퍼** | 시간 제한이 있는 프로모션 오퍼입니다. 자세한 내용은 [한정 기간 오퍼 템플릿]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates)을 참조하세요. |
| **Flow** | WhatsApp Flow를 여는 템플릿입니다(예: 설문조사 또는 예약). Meta의 WhatsApp 매니저에서 Flow를 만들고 관리한 다음, 템플릿을 작성할 때 선택합니다. 자세한 내용은 [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마케팅 템플릿 유형" }

#### 유틸리티 {#utility}

유틸리티 템플릿은 비프로모션 메시지(예: 주문 확인, 계정 업데이트, 영수증, 예약 리마인더, 청구서)에 사용됩니다. Meta는 프로모션 콘텐츠를 마케팅으로 재분류합니다.

| 유형 | 설명 |
| --- | --- |
| **커스텀** | 처음부터 직접 작성하는 표준 유틸리티 메시지입니다. [템플릿 작성하기](#step-4-build-your-template)와 동일한 구성 단계를 따릅니다. |
| **Flow** | 유틸리티 Flow 템플릿입니다(예: 리마인더, 피드백, 주문 관리). Meta의 WhatsApp 매니저에서 Flow를 만들고 관리한 다음, 템플릿을 작성할 때 선택합니다. 자세한 내용은 [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="유틸리티 템플릿 유형" }

{% alert note %}
캐러셀 및 한정 기간 오퍼 레이아웃은 마케팅 템플릿에서만 사용할 수 있습니다.
{% endalert %}

### 3단계: 템플릿 설정 구성하기 {#step-3-configure-template-settings}

다음 필드를 입력합니다:

| 필드 | 설명 |
| ----- | ----- |
| **계정** | 템플릿을 제출할 WhatsApp 비즈니스 계정(WABA)입니다. WABA 내의 모든 구독 그룹과 전화번호가 템플릿 액세스를 공유합니다. |
| **언어** | 이 템플릿의 언어입니다. WhatsApp은 각 언어마다 별도의 템플릿을 요구합니다. |
| **템플릿 이름** | 템플릿의 고유 이름입니다. 템플릿 이름에는 소문자, 숫자, 밑줄만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 템플릿 설정 구성하기" }

### 4단계: 템플릿 작성하기 {#step-4-build-your-template}

#### 헤더 (선택 사항) {#header-optional}

메시지 본문 앞에 표시할 헤더를 추가합니다. 다음 중 하나를 선택할 수 있습니다:

- **텍스트:** 짧은 텍스트 헤더.
- **미디어:** 이미지, 비디오 또는 문서(URL만 지원). Braze가 미디어 참조를 저장하고 승인을 위해 Meta에 샘플을 제출합니다.
- **없음:** 헤더 없음

#### 본문 {#body}

메시지의 주요 콘텐츠를 입력하고 Liquid 또는 일반 변수를 사용하여 필요에 따라 본문을 개인화합니다:

{% raw %}
- Liquid 태그(예: `{{${first_name}}}`)를 사용합니다. Braze가 Liquid를 저장하며, Campaign 또는 Canvas 작성기에서 템플릿을 사용할 때 표시합니다.
- 나중에 메시지를 작성할 때 개인화를 추가하려면 번호가 매겨진 입력 안내(예: `{{1}}`)와 같은 일반 변수를 사용합니다.
{% endraw %}

**+** 플러스 버튼이 표시되는 곳이면 어디서든 개인화를 추가할 수 있습니다. 모든 필드가 개인화를 지원하는 것은 아닙니다.

#### Liquid 글자 수 제한 {#liquid-character-limits}

Meta는 승인을 위해 제출하는 템플릿 구조에 글자 수 제한을 적용합니다(예: 본문은 1,024자, 텍스트 헤더는 60자). 템플릿 빌더에서 이러한 제한은 발송 시 최종 렌더링되는 메시지가 아닌, Meta에 전송되는 템플릿에 적용됩니다.

- **{% raw %}`{{ }}`{% endraw %} 변수:** Braze는 길이를 확인하기 전에 Liquid 변수를 번호가 매겨진 입력 안내({% raw %}`{{1}}`, `{{2}}`{% endraw %})로 변환합니다. {% raw %}`{{${first_name}}}`{% endraw %}와 같은 긴 표현식은 전체 Liquid 구문이 아닌 짧은 입력 안내로 계산됩니다.
- **{% raw %}`{% %}`{% endraw %} 태그:** Liquid 로직 태그는 전체 길이의 리터럴 텍스트로 계산되며 템플릿 메시지에서 편집할 수 없는 텍스트로 표시됩니다.

복잡한 개인화의 경우 [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)를 사용하여 값을 계산한 다음 템플릿에서 더 짧은 변수를 참조하세요. 메시지 추가 정보 및 조건 로직 제약에 대해서는 [WhatsApp 템플릿 빌더의 Liquid]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid)를 참조하세요.

#### 푸터 (선택 사항) {#footer-optional}

메시지 본문 뒤에 표시할 짧은 푸터를 추가합니다.

#### 버튼 (선택 사항) {#buttons-optional}

템플릿에 최대 10개의 버튼을 추가할 수 있습니다. 버튼 유형은 카테고리와 사양이 다르며, 메시지 본문 뒤에 카테고리별로 그룹화됩니다. 기본적으로 빠른 답장 버튼이 먼저 표시됩니다. 표시 순서를 변경하려면(예: 빠른 답장 버튼을 실행 버튼 뒤로 이동) **그룹 순서 변경**을 선택합니다.

| 버튼 유형 | 카테고리 | 사양 |
| --- | --- | --- |
| 빠른 답장 | 빠른 답장 버튼 |{::nomarkdown}<ul><li><b>최대 개수:</b> 10</li><li><b>버튼 텍스트:</b> 최대 25자</li></ul> {:/}|
| 전화번호 | 실행 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 1</li><li><b>버튼 텍스트:</b> 최대 25자</li><li><b>전화번호:</b> +를 제외한 국가 코드가 포함된 유효한 전화번호(예: "14155552671")</li></ul> {:/}|
| 웹사이트 방문 | 실행 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 2</li><li><b>버튼 텍스트:</b> 최대 25자</li><li><b>웹사이트 URL:</b> 최대 2,000자</li></ul> {:/}|
| 오퍼 코드 복사 | 실행 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 1</li><li><b>버튼 텍스트:</b> "Copy offer code" (편집 불가)</li><li><b>오퍼 코드:</b> 최대 15자</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="버튼 (선택 사항)" }

Flow 템플릿의 경우, 표준 실행 버튼을 추가하는 대신 Flow 버튼을 구성하고 Meta에서 기존 Flow를 선택합니다.

### 5단계: 템플릿 미리보기 {#step-5-preview-your-template}

제출하기 전에 수신자에게 메시지가 어떻게 표시되는지 미리 봅니다:

- **사용자로 미리보기:** 메시지의 일반 미리보기를 확인합니다.
- **특정 사용자로 미리보기:** 고객 프로필을 선택하여 해당 사용자의 데이터로 템플릿이 어떻게 렌더링되는지 미리 봅니다.

### 6단계: 검토 제출하기 {#step-6-submit-for-review}

**제출**을 선택하여 Meta에 템플릿 검토를 요청합니다. 검토는 보통 몇 분 이내에 완료되지만 최대 24시간이 걸릴 수 있습니다. 템플릿이 제출되면 **WhatsApp 템플릿** 페이지에 표시되며, **WhatsApp 템플릿** 페이지를 새로고침하면 상태가 업데이트됩니다.

## Campaign 또는 Canvas에서 템플릿 만들기 {#create-a-template-from-a-campaign-or-canvas}

Campaign 또는 Canvas 메시지 단계를 떠나지 않고도 WhatsApp 템플릿을 만들고 제출할 수 있습니다.

1. WhatsApp [Campaign]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) 또는 Canvas 메시지 단계에서 **WhatsApp Template Message** 메시지 유형을 선택합니다.
2. **Create new template**을 선택합니다.
3. 카테고리와 유형을 선택한 다음, WhatsApp Templates 페이지에서와 동일한 방식으로 템플릿을 작성하고 제출합니다.
4. 제출 후 Braze가 대기 중인 템플릿을 메시지에 바인딩합니다. 템플릿이 대기 중인 동안 개인화 작성을 계속하고, Meta가 승인한 후 발송합니다.

빌더를 나가고 기존 템플릿을 선택하려면 **Choose template from library**를 선택합니다.

{% alert note %}
Campaign 또는 Canvas에서 템플릿을 만들 때 Braze는 작업 내용을 초안으로 저장할 수 있으므로 메시지 단계를 떠나더라도 작업이 유지됩니다.
{% endalert %}

## 승인된 템플릿을 Campaign에서 사용하기 {#use-an-approved-template-in-a-campaign}

Meta가 템플릿을 승인한 후, WhatsApp Campaign 또는 Canvas에서 사용할 수 있습니다.

1. **Campaigns**로 이동하여 **Create Campaign** > **WhatsApp**을 선택합니다.
2. 메시지 작성기에서 승인된 템플릿을 선택합니다.
3. Braze는 템플릿 생성 시 입력한 미디어와 Liquid를 포함하여 템플릿의 콘텐츠를 자동으로 채우므로 다시 입력할 필요가 없습니다.
4. 필요에 따라 변수 콘텐츠 또는 개인화를 업데이트합니다. Meta에 의해 잠긴 필드(회색으로 표시)는 편집할 수 없습니다. 잠긴 콘텐츠를 변경하려면 템플릿을 수정한 후 승인을 위해 다시 제출해야 합니다.
5. **Test** 탭을 사용하여 메시지를 미리 보고, 본문 변수를 업데이트하고, 발송 전에 메시지가 예상대로 표시되는지 확인합니다.

WhatsApp Campaign 작성에 대한 자세한 내용은 [WhatsApp 메시지 만들기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### Meta 템플릿 검토는 얼마나 걸리나요? {#how-long-does-meta-template-review-take}

검토는 보통 5분 이내에 완료되지만, 최대 24시간이 걸릴 수 있습니다.

### 승인된 후 템플릿을 수정할 수 있나요? {#can-i-edit-a-template-after-its-been-approved}

Campaign 또는 Canvas를 작성할 때 변수 콘텐츠와 개인화를 업데이트할 수 있습니다. 잠긴 콘텐츠(본문 텍스트, 버튼 레이아웃 또는 기타 Meta가 제어하는 필드)를 변경하려면 템플릿 빌더에서 새 템플릿을 만들거나 Meta의 WhatsApp 매니저에서 템플릿을 수정한 후 Meta의 재승인을 기다려야 합니다. [클릭 추적]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking)을 사용하는 경우, Meta의 WhatsApp 매니저에서 Braze가 생성한 템플릿을 수정하기 전에 해당 문서를 참고하세요.

### 템플릿 빌더가 제공되기 전에 제출한 템플릿은 어떻게 되나요? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Meta Business 매니저에서 만든 템플릿은 Braze에서 계속 사용할 수 있습니다. 템플릿 빌더는 Braze 대시보드를 벗어나지 않고 템플릿을 만들고 관리할 수 있는 추가적인 방법입니다.

### 모든 필드에 개인화를 추가할 수 없는 이유는 무엇인가요? {#why-cant-i-add-personalization-to-every-field}

Meta는 템플릿에서 개인화할 수 있는 부분을 제한합니다. **+** 플러스 버튼은 변수 콘텐츠를 지원하는 필드에서만 표시됩니다.