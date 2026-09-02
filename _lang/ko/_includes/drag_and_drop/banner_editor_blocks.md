## 배너 편집기 블록 {#banner-editor-blocks}

배너 작성기에서 **구축** 섹션의 행과 블록을 캔버스로 드래그하여 메시지를 레이아웃합니다. **스타일**을 선택하여 페이지 수준 스타일을 조정하거나, 블록 또는 행을 선택하여 사이드 패널에서 속성을 편집합니다.

전체 배너 생성 흐름은 [배너 만들기]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner)를 참조하세요.

배너 작성기는 다른 드래그 앤 드롭 화면과 동일한 종류의 레이아웃 블록을 제공하지만, 전체 양식 블록 세트를 지원하지는 않습니다(예: 라디오 버튼, 짧은 텍스트, 드롭다운 또는 체크박스 블록 없음). **전화번호 수집** 및 **이메일 수집** 블록을 추가할 수 있으며, 메시지당 전화번호 수집 블록과 이메일 수집 블록은 각각 **하나**만 허용됩니다.

### 제목 및 단락 {#title-and-paragraph}

서식 있는 텍스트 옵션과 함께 제목 또는 본문 텍스트를 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### 버튼 {#button}

클릭 가능한 버튼을 추가합니다. 속성 패널에서 링크 및 분석 옵션을 설정할 수 있습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### 클릭 시 동작 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

자세한 내용은 배너 문서의 [클릭 시 동작 정의]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional)를 참조하세요.

### 이미지 {#image}

호스팅된 URL의 이미지를 표시합니다. 속성 패널에서 표시 옵션을 구성합니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### 링크 {#link}

사용자가 선택할 수 있는 하이퍼링크를 삽입합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### 스페이서 {#spacer}

블록 사이에 세로 간격을 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 커스텀 코드 {#custom-code}

고급 레이아웃 또는 임베디드 콘텐츠(예: 동영상)를 위한 커스텀 HTML을 삽입합니다. 커스텀 HTML 내부의 클릭은 `brazeBridge.logClick()`을 호출하지 않는 한 추적되지 않습니다. 자세한 내용은 [배너용 커스텀 코드 및 JavaScript 브리지]({{site.baseurl}}/user_guide/channels/banners/custom_code/)를 참조하세요.

| 등록정보 | 설명 |
| --- | --- |
| 커스텀 코드 | 배너용 HTML(및 관련 자산)을 추가하거나 편집합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### 전화번호 수집 {#phone-capture}

전화번호를 수집합니다. 제출 시 사용자를 선택한 [단문 메시지 서비스]({{site.baseurl}}/sms_rcs_subscription_groups/) 또는 [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) 구독 그룹에 가입시킵니다. 배너당 하나만 허용됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### 이메일 수집 {#email-capture}

이메일 주소를 수집하고 제출 시 사용자의 Braze 프로필에 추가합니다. 배너당 하나만 허용됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### 긴 텍스트 {#long-text}

설문조사 스타일 흐름을 위한 여러 줄 텍스트 필드입니다. 이 블록이 보이지 않으면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support/) 또는 Braze 고객 성공 매니저에게 문의하세요.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### 저장된 행 {#saved-row}

이전에 드래그 앤 드롭 Content Block으로 저장한 재사용 가능한 행을 삽입합니다. 저장된 행은 원본 Content Block에 **연결되지 않습니다**. 원본이 업데이트되면 최신 버전을 가져오려면 편집기에 다시 드래그해야 합니다. 자세한 내용은 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)를 참조하세요. **행** 아래에 **저장된 행**이 보이지 않으면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support/) 또는 Braze 고객 성공 매니저에게 문의하세요.
-->

## 알아두어야 할 사항 {#things-to-know}

- **동영상:** 표준 작성기에는 전용 동영상 블록이 포함되어 있지 않습니다. 필요한 경우 **커스텀 코드**를 사용하여 플레이어를 임베드하세요. 자세한 내용은 [배너: 자주 묻는 질문]({{site.baseurl}}/user_guide/channels/banners/faq/)을 참조하세요.
- **Liquid:** 대부분의 Liquid가 지원되지만, 카탈로그 리렌더 태그 등 일부 예외가 있습니다. 자세한 내용은 [배너: 자주 묻는 질문]({{site.baseurl}}/user_guide/channels/banners/faq/)을 참조하세요.