## 랜딩 페이지 편집기 블록 {#landing-page-editor-blocks}

랜딩 페이지의 편집기 블록은 **드래그 앤 드롭 편집기**의 **구축** 섹션에서 **행** 및 블록 카테고리 아래에 있습니다. 블록을 행 열로 드래그하면 열 너비에 맞게 자동 조정됩니다. 블록을 선택하면 오른쪽 속성 패널에서 설정을 편집할 수 있습니다.

랜딩 페이지 생성 및 게시에 대한 자세한 내용은 [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)를 참조하세요.

### 제목 및 단락 {#title-and-paragraph}

제목 또는 본문 텍스트를 추가합니다. 섹션을 구조화하고 가독성을 높이는 데 유용합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### 버튼 {#button}

링크 열기 또는 양식 제출과 같은 동작을 위한 클릭 가능한 요소를 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### 클릭 시 동작 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
**Submit form when button is clicked**로 버튼을 구성하고 새 탭에서 웹 URL을 열도록 설정하면, iOS Safari에서 내비게이션을 차단할 수 있습니다. 양식을 제출할 때는 제출 후 URL을 같은 탭에서 여세요. 자세한 내용은 [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)를 참조하세요.
{% endalert %}

### 라디오 버튼 {#radio-button}

사용자가 하나를 선택할 수 있는 옵션 목록을 추가합니다. 속성 패널을 사용하여 사용 가능한 옵션과 선택된 값을 수신할 커스텀 속성을 구성하세요. 양식이 제출되면 고객 프로필에 선택된 값이 [문자열 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)으로 기록됩니다. 다른 데이터 유형의 커스텀 속성은 고객 프로필에 저장되지 않습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 이미지 {#image}

업로드 또는 외부 URL에서 이미지를 표시합니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### 링크 {#link}

사용자가 선택하여 URL로 이동할 수 있는 하이퍼링크를 추가합니다. 텍스트 안에 배치하거나 독립적으로 사용할 수 있습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### 클릭 시 동작

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### 스페이서 {#spacer}

요소 사이에 수직 간격을 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 커스텀 코드 {#custom-code}

[Google Tag 매니저]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page)와 같은 고급 커스터마이징을 위해 커스텀 HTML, CSS 또는 JavaScript를 삽입합니다.

| 속성정보 | 설명 |
| --- | --- |
| 커스텀 코드 | HTML, CSS, JavaScript를 추가, 편집 또는 삭제할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 코드" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success 매니저.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### 이메일 캡처 {#email-capture}

이메일 주소를 위한 양식 필드를 추가합니다. 제출 시 해당 주소가 사용자의 Braze 프로필에 저장됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### 전화번호 캡처 {#phone-capture}

전화번호를 위한 양식 필드를 추가합니다. 제출 시 사용자가 선택한 [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) 또는 [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) 구독 그룹에 가입됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### 입력 필드 {#input-field}

표준 속성(예: 이름 또는 성) 또는 커스텀 속성 문자열을 위한 양식 필드를 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### 드롭다운 {#dropdown}

미리 정의된 항목 목록으로, 사용자가 하나를 선택합니다. 값을 커스텀 속성 문자열에 매핑할 수 있습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### 체크박스 {#checkbox}

체크하면 블록의 [부울 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)이 `true`로 설정되고, 체크 해제하면 `false`로 설정됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### 체크박스 그룹 {#checkbox-group}

사용자가 여러 옵션을 선택할 수 있으며, 값이 정의된 [배열 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)에 설정되거나 추가됩니다.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### 긴 텍스트 {#long-text}

설문조사 스타일 플로우를 위한 여러 줄 텍스트 필드입니다. 이 블록이 보이지 않으면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support) 또는 Braze 고객 성공 매니저에게 문의하세요. 이 블록은 표준 랜딩 페이지에서는 사용할 수 없습니다.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success 매니저.
-->

## 알아두어야 할 사항 {#things-to-know}

- **비디오:** 표준 작성기에는 전용 비디오 블록이 포함되어 있지 않습니다. 필요한 경우 **커스텀 코드**를 사용하여 플레이어를 삽입하세요. 자세한 내용은 [랜딩 페이지]({{site.baseurl}}/user_guide/messaging/landing_pages)를 참조하세요.