## 인앱 메시지 편집기 블록 {#in-app-message-editor-blocks}

편집기 블록은 인앱 메시지의 **Build** 섹션에 있습니다. 블록을 열 안으로 드래그하면 열 너비에 맞게 자동으로 조정됩니다. 블록을 선택하면 오른쪽 패널에서 해당 설정을 편집할 수 있습니다.

**드래그 앤 드롭 편집기**에서 인앱 메시지를 만드는 방법에 대한 자세한 내용은 [드래그 앤 드롭으로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)를 참조하세요.

### 제목 및 단락 {#title-and-paragraph}

메시지에 제목 또는 단락 텍스트를 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### 버튼 {#button}

스타일, 링크, 분석을 설정할 수 있는 표준 버튼을 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### 클릭 시 동작 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### 라디오 버튼 {#radio-button}

사용자가 하나를 선택할 수 있는 옵션 목록을 추가합니다. 제출 시 고객 프로필에 관련 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)이 기록되며, 저장하려면 문자열이어야 합니다. 다른 데이터 유형의 커스텀 속성은 고객 프로필에 저장되지 않습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 이미지 {#image}

[미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에서 이미지를 삽입합니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

이미지 사양에 대한 내용은 [인앱 메시지 이미지 사양]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages)을 참조하세요.

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### 링크 {#link}

사용자가 클릭하여 지정된 URL로 이동할 수 있는 하이퍼링크를 삽입합니다. 텍스트 내에 포함하거나 독립적으로 사용할 수 있습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### 공백 {#spacer}

다른 블록 사이에 공간이나 패딩을 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 커스텀 코드 {#custom-code}

고급 커스터마이징을 위해 커스텀 HTML, CSS 또는 JavaScript를 삽입합니다.

| 속성정보 | 설명 |
| --- | --- |
| 커스텀 코드 | 인앱 메시지의 HTML, CSS 및 JavaScript를 추가, 편집 또는 삭제할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 코드" }

### 전화번호 캡처 {#phone-capture}

전화번호 입력 양식 필드를 삽입합니다. 제출 시 사용자는 [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) 또는 [WhatsApp 구독 그룹]({{site.baseurl}}/whatsapp_subscription_groups)에 가입됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### 이메일 캡처 {#email-capture}

이메일 주소 입력 양식 필드를 삽입합니다. 제출 시 이메일 주소가 Braze에서 해당 사용자의 프로필에 추가됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### 짧은 텍스트 {#short-text}

표준 속성(예: 이름 및 성) 또는 원하는 커스텀 속성 문자열을 지원하는 양식 필드를 삽입합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### 드롭다운 {#dropdown}

사용자가 하나를 선택할 수 있는 미리 정의된 항목 목록이 포함된 드롭다운을 삽입합니다. 목록에 커스텀 속성 문자열을 추가할 수 있습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### 체크박스 {#checkbox}

체크박스를 삽입합니다. 사용자가 체크박스를 선택하면 블록의 [부울 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)이 `true`로 설정됩니다. 선택하지 않으면 속성이 `false`로 설정됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### 체크박스 그룹 {#checkbox-group}

사용자는 여러 선택지 중에서 선택할 수 있습니다. 값은 정의된 [배열 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)에 설정되거나 추가됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### 긴 텍스트 {#long-text}

설문조사 스타일 플로우를 위한 여러 줄 텍스트 필드입니다. 이 블록이 보이지 않으면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support) 또는 Braze 고객 성공 매니저에게 문의하세요.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## 알아두어야 할 사항 {#things-to-know}

- **비디오:** 표준 작성기에는 전용 비디오 블록이 포함되어 있지 않습니다. 필요한 경우 **커스텀 코드**를 사용하여 플레이어를 삽입하세요. 자세한 내용은 [인앱 메시지: 자주 묻는 질문]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)을 참조하세요.