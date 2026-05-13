## 환경설정 센터 편집기 블록 {#preference-center-editor-blocks}

**구축** 섹션에서 블록을 드래그하여 드래그 앤 드롭 환경설정 센터 편집기의 행에 놓습니다. 각 블록에는 고유한 설정이 있으며, 오른쪽 패널은 선택한 요소의 등록정보 또는 스타일링으로 전환됩니다.

블록을 편집하기 전에 구독 그룹을 추가하고 구독 **스마트 블록**을 구성하세요(아래 참조). 전체 설정 흐름은 [드래그 앤 드롭으로 이메일 환경설정 센터 만들기]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/)를 참조하세요.

### 제목 및 단락 {#title-and-paragraph}

서식 있는 텍스트 옵션을 사용하여 제목 또는 본문 텍스트를 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### 버튼 {#button}

클릭 가능한 버튼을 추가합니다(예: **저장** 또는 내비게이션).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### 이미지 {#image}

[미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) 또는 URL에서 이미지를 표시합니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### 스페이서 {#spacer}

블록 사이에 세로 간격을 추가합니다.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 구독 그룹(스마트 블록) {#subscription-groups-smart-block}

구독 그룹, 선택 사항인 **모두 구독** / **모두 구독 취소** 제어, 설명을 나열하는 템플릿 블록을 추가합니다. 환경설정 센터 워크플로에서 그룹을 추가한 후 구성하세요.

[구독 그룹을 추가]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-3-add-subscription-groups-to-the-preference-center)한 후, 캔버스에서 스마트 블록을 선택하여 다음을 수행할 수 있습니다:

- 구독 그룹 순서 변경
- 그룹 추가 또는 제거
- 설명 추가 또는 제거
- 해당 블록의 그룹에 대해 **모두 구독** 및 **모두 구독 취소** 토글

기본 템플릿 하단의 **모두 구독 취소** 제어는 필수이며, 이메일에서 [글로벌 탈퇴]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states)를 수행합니다.

## 알아두어야 할 사항 {#things-to-know}

- **공통 스타일:** 개별 블록을 조정하기 전에 **Common Styles**에서 페이지 전체 기본값을 설정할 수 있습니다. 자세한 내용은 [드래그 앤 드롭 편집기를 사용하여 환경설정 센터 커스터마이즈하기]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-4-customize-the-preference-center-using-the-drag-and-drop-editor)를 참조하세요.
- **확인 페이지:** 편집기 상단에서 **확인 페이지**로 전환하면 동일한 블록 유형을 사용하여 저장 후 경험을 스타일링할 수 있습니다.