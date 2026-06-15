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

> WhatsApp 템플릿 빌더를 사용하면 Braze에서 직접 WhatsApp 메시지 템플릿을 생성하고 제출할 수 있으며, Braze와 Meta Business Manager 사이를 오갈 필요가 없습니다. Meta가 템플릿을 승인하면 원하는 만큼 많은 Campaigns과 Canvases에서 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## 템플릿 생성 {#create-a-template}

### 1단계: WhatsApp 템플릿으로 이동 {#step-1-go-to-whatsapp-templates}

**Content** > **WhatsApp**으로 이동한 다음 **Create new template**을 선택합니다.

![새 템플릿을 생성하는 버튼이 있는 WhatsApp 템플릿 페이지.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### 2단계: 템플릿 설정 구성 {#step-2-configure-template-settings}

다음 필드를 입력합니다:

| 필드 | 설명 |
| ----- | ----- |
| **계정** | 템플릿을 제출할 WhatsApp Business Account(WABA)입니다. WABA 내의 모든 구독 그룹과 전화번호가 템플릿 액세스를 공유합니다. |
| **언어** | 이 템플릿의 언어입니다. WhatsApp은 각 언어별로 별도의 템플릿을 요구합니다. |
| **템플릿 이름** | 템플릿의 고유한 이름입니다. 템플릿 이름에는 소문자, 숫자, 밑줄만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure template settings" }

### 3단계: 레이아웃 선택 {#step-3-choose-a-layout}

**Layout**에서 템플릿 유형을 선택합니다:

- **Default:** 표준 WhatsApp 메시지입니다. 이 문서에서 다루는 레이아웃입니다.
- **Carousel:** 가로로 스크롤할 수 있는 카드가 포함된 메시지입니다. 자세한 내용은 [캐러셀 템플릿]({{site.baseurl}}/whatsapp_carousel_templates/)을 참조하세요.

### 4단계: 템플릿 작성 {#step-4-build-your-template}

#### 헤더(선택 사항) {#header-optional}

메시지 본문 위에 표시할 헤더를 추가합니다. 다음 중 선택할 수 있습니다:

- **Text:** 짧은 텍스트 헤더입니다.
- **Media:** 이미지, 동영상 또는 문서(URL만 가능)입니다. Braze가 미디어 참조를 저장하고 승인을 위해 Meta에 샘플을 제출합니다.
- **None:** 헤더 없음

#### 본문 {#body}

메시지의 주요 콘텐츠를 입력하고 Liquid 또는 일반 변수를 사용하여 필요에 따라 본문을 개인화합니다:

{% raw %}
- Liquid 태그(예: `{{${first_name}}}`)를 사용합니다. Braze가 Liquid를 저장하고 Campaign 또는 Canvas 작성기에서 템플릿을 사용할 때 표시합니다.
- 메시지를 작성할 때 나중에 개인화를 추가하려면 번호가 매겨진 입력 안내(예: `{{1}}`)와 같은 일반 변수를 사용합니다.
{% endraw %}

**+** 플러스 버튼이 표시되는 곳이면 어디든 개인화를 추가할 수 있습니다. 모든 필드가 개인화를 지원하는 것은 아닙니다.

#### 푸터(선택 사항) {#footer-optional}

메시지 본문 아래에 표시할 짧은 푸터를 추가합니다.

#### 버튼(선택 사항) {#buttons-optional}

템플릿에 최대 10개의 버튼을 추가할 수 있습니다. 버튼 유형에 따라 카테고리와 사양이 다릅니다.

| 버튼 유형 | 카테고리 | 사양 |
| --- | --- | --- |
| 빠른 답장 | 빠른 답장 버튼 |{::nomarkdown}<ul><li><b>최대 개수:</b> 10</li><li><b>버튼 텍스트:</b> 최대 25자</li></ul> {:/}|
| 전화번호 | 행동 유도 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 1</li><li><b>버튼 텍스트:</b> 최대 25자</li><li><b>전화번호:</b> +를 제외한 국가 코드가 포함된 유효한 전화번호(예: "14155552671")</li></ul> {:/}|
| 웹사이트 방문 | 행동 유도 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 2</li><li><b>버튼 텍스트:</b> 최대 25자</li><li><b>웹사이트 URL:</b> 최대 2,000자</li></ul> {:/}|
| 오퍼 코드 복사 | 행동 유도 버튼 | {::nomarkdown}<ul><li><b>최대 개수:</b> 1</li><li><b>버튼 텍스트:</b> "Copy offer code"(편집 불가)</li><li><b>오퍼 코드:</b> 최대 15자</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

![빠른 답장 및 행동 유도 버튼이 있는 WhatsApp 템플릿 작성기.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### 5단계: 템플릿 미리보기 {#step-5-preview-your-template}

제출하기 전에 수신자에게 메시지가 어떻게 표시되는지 미리 확인합니다:

- **Preview as a user:** 메시지의 일반 미리보기를 확인합니다.
- **Preview as a specific user:** 해당 사용자의 데이터로 템플릿이 어떻게 렌더링되는지 확인할 고객 프로필을 선택합니다.

### 6단계: 검토를 위해 제출 {#step-6-submit-for-review}

**Submit**을 선택하여 Meta에 템플릿을 검토 요청합니다. 검토는 보통 몇 분 내에 완료되지만 최대 24시간이 걸릴 수 있습니다. 템플릿이 제출되면 **WhatsApp Templates** 페이지에 표시되며, **WhatsApp Templates** 페이지를 새로고침하면 상태가 업데이트됩니다.

## 지원되는 템플릿 카테고리 {#supported-template-categories}

현재 WhatsApp 템플릿 빌더에서는 마케팅 템플릿만 지원됩니다.

## 승인된 템플릿을 캠페인에서 사용하기 {#use-an-approved-template-in-a-campaign}

Meta가 템플릿을 승인하면 WhatsApp Campaign 또는 Canvas에서 사용할 수 있습니다.

1. **Campaigns**로 이동하여 **캠페인 생성** > **WhatsApp**을 선택합니다.
2. 메시지 작성기에서 승인된 템플릿을 선택합니다.
3. Braze가 템플릿 생성 시 입력한 미디어 및 Liquid를 포함하여 템플릿의 콘텐츠를 자동으로 채우므로 다시 입력할 필요가 없습니다.
4. 필요에 따라 변수 콘텐츠 또는 개인화를 업데이트합니다. Meta에 의해 잠긴 필드(회색으로 표시)는 편집할 수 없습니다. 잠긴 콘텐츠를 변경하려면 템플릿을 편집하고 승인을 위해 다시 제출해야 합니다.
5. **Test** 탭을 사용하여 메시지를 미리 보고, 본문 변수를 업데이트하고, 시작 전에 메시지가 예상대로 표시되는지 확인합니다.

WhatsApp Campaign 작성에 대한 자세한 내용은 [WhatsApp 메시지 생성]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### Meta 템플릿 검토는 얼마나 걸리나요? {#how-long-does-meta-template-review-take}

검토는 보통 5분 이내에 완료되지만 최대 24시간이 걸릴 수 있습니다.

### 승인된 후에 템플릿을 편집할 수 있나요? {#can-i-edit-a-template-after-its-been-approved}

잠긴 콘텐츠(본문 텍스트 또는 기타 Meta 제어 필드)를 변경하려면 템플릿을 승인을 위해 다시 제출해야 하며, 이는 WhatsApp Business Manager에서 수행해야 합니다. Campaign 또는 Canvas를 작성할 때 콘텐츠와 개인화를 업데이트할 수 있습니다.

### 템플릿 빌더가 제공되기 전에 제출한 템플릿은 어떻게 되나요? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Meta Business Manager에서 생성한 템플릿은 여전히 Braze에서 사용할 수 있습니다. 템플릿 빌더는 Braze 대시보드를 벗어나지 않고 템플릿을 생성하고 관리할 수 있는 추가적인 방법입니다.

### 모든 필드에 개인화를 추가할 수 없는 이유는 무엇인가요? {#why-cant-i-add-personalization-to-every-field}

Meta는 템플릿에서 개인화할 수 있는 부분을 제한합니다. **+** 플러스 버튼은 변수 콘텐츠를 지원하는 필드에서만 표시됩니다.