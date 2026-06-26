---
nav_title: 드래그 앤 드롭 편집기
article_title: 드래그 앤 드롭 편집기로 인앱 메시지 만들기
alias: /iam_drag_and_drop/
page_order: 1
description: "이 참조 문서에서는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지를 만드는 방법, 필수 조건, 크리에이티브 세부 정보 등을 다룹니다."
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# 드래그 앤 드롭으로 인앱 메시지 만들기 {#create-an-in-app-message-with-drag-and-drop}

> 드래그 앤 드롭 편집기를 사용하면 Campaigns 또는 Canvas에서 드래그 앤 드롭 편집 환경을 통해 완전히 커스텀되고 개인화된 인앱 메시지를 만들 수 있습니다. 편집기에서 사용할 수 있는 빌딩 블록에 대한 자세한 내용은 [편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)을 참조하세요.


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

기존 커스텀 HTML 템플릿이나 서드파티에서 만든 템플릿을 사용하려면 드래그 앤 드롭 편집기에서 다시 만들어야 합니다.

인앱 메시지를 Campaign으로 보낼지 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)로 보낼지 확실하지 않으신가요? Campaigns는 단일 타겟 메시징에 적합하고, Canvases는 다단계 사용자 여정에 적합합니다. 메시지를 작성할 위치를 선택한 후, 드래그 앤 드롭 인앱 메시지를 만드는 단계를 살펴보겠습니다.

## 필수 조건 {#prerequisites}

### SDK 요구 사항 {#sdk-requirements}

| 최소 SDK 버전                                                          | 권장 SDK 버전                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK 요구 사항" }

{% details 최소 SDK에 대한 추가 정보 %}

드래그 앤 드롭 편집기를 사용하여 만든 메시지는 최소 SDK 버전(위 표 참조)을 사용하는 사용자에게만 전송할 수 있습니다. 사용자가 애플리케이션을 업데이트하지 않은 경우(즉, 이전 SDK 버전을 사용 중인 경우) 인앱 메시지를 수신하지 못합니다.

드래그 앤 드롭 편집기에서 사용 가능한 모든 기능을 활용하려면 SDK를 권장 SDK 버전으로 업데이트하세요. 이를 통해 다음과 같은 추가 기능을 활용할 수 있습니다:

- 메시지를 닫지 않는 텍스트 링크
- 푸시 프라이머 요청 버튼 동작

다음은 이러한 기능에 대한 개별 최소 SDK 요구 사항입니다:

| 텍스트 링크*                                                         | 푸시 프라이머 요청                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK 요구 사항" }

*인앱 메시지에 URL로 리디렉션하는 링크를 포함하고 최종 사용자가 지정된 최소 SDK 버전을 사용하지 않는 경우, 링크를 선택하면 메시지가 닫히고 사용자는 양식을 제출하기 위해 메시지로 돌아갈 수 없습니다.

{% enddetails %}

### 추가 필수 조건 {#additional-prerequisites}

- 웹 SDK의 경우 초기화 옵션 [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)를 `true`로 설정해야 합니다. `enableHtmlInAppMessages` 옵션도 이러한 메시지가 작동하도록 하지만, 더 이상 사용되지 않으므로 `allowUserSuppliedJavascript`로 업데이트해야 합니다.
- Google Tag Manager를 사용하는 경우 GTM 구성에서 "Allow HTML In-App Messages"를 활성화해야 합니다.

## 1단계: 인앱 메시지 만들기 {#step-1-create-an-in-app-message}

새 인앱 메시지 또는 캔버스 단계를 만든 다음 편집 환경으로 **드래그 앤 드롭 편집기**를 선택합니다.

## 2단계: 템플릿 선택 {#step-2-select-your-template}

드래그 앤 드롭 편집기를 편집 환경으로 선택한 후 다음을 선택할 수 있습니다:

- 빈 모달 템플릿으로 시작
- Braze 드래그 앤 드롭 인앱 메시지 템플릿 사용
- 저장된 드래그 앤 드롭 인앱 메시지 템플릿 선택

**메시지 작성**을 선택하여 드래그 앤 드롭 편집기에서 인앱 메시지 디자인을 시작합니다.

![기본, 배경 이미지, 전화번호 캡처 또는 빈 템플릿을 선택할 수 있는 Braze 템플릿 섹션.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

대시보드의 **템플릿** 섹션에서도 모든 템플릿에 액세스할 수 있습니다.

## 3단계: 추가 페이지 추가(선택 사항) {#multi-page}

인앱 메시지에 페이지를 추가하면 온보딩 플로우나 환영 여정과 같은 순차적 플로우를 통해 사용자를 안내할 수 있습니다. **빌드** 탭의 **페이지** 섹션에서 페이지를 관리할 수 있습니다.

![세 개의 페이지로 구성된 헬스케어 회사의 인앱 메시지.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab 페이지 추가 %}

인앱 메시지는 기본적으로 한 페이지로 시작합니다. 새 페이지를 추가하려면:

1. **+ 페이지 추가**를 선택합니다.
2. 커스텀 또는 Braze 제공 템플릿 목록에서 선택합니다.
3. 의미 있는 이름을 지정합니다. 이렇게 하면 페이지를 서로 연결할 때 도움이 됩니다.

{% alert tip %}
인앱 메시지당 최대 10개의 페이지를 추가할 수 있습니다.
{% endalert %}

기존 페이지를 복제하려면:

1. 목록에서 페이지 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> **추가 옵션**을 선택합니다.
2. **복제**를 선택합니다.
3. 의미 있는 이름을 지정합니다. 이렇게 하면 페이지를 서로 연결할 때 도움이 됩니다.

{% endtab %}
{% tab 페이지 삭제 또는 이름 변경 %}

페이지를 삭제하거나 이름을 변경하려면:

1. 목록에서 페이지 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> **추가 옵션**을 선택합니다.
2. **이름 변경** 또는 **삭제**를 선택합니다.

{% endtab %}
{% endtabs %}

### 3a단계: 페이지 연결 {#step-3a-connect-pages-together}

다중 페이지 인앱 메시지는 순차적이며, 사용자가 탭하거나 클릭하여 플로우의 다음 페이지로 이동하는 방식으로 메시지와 상호작용합니다.

페이지를 연결하려면:

1. 시작 페이지를 선택합니다.
2. 캔버스에서 버튼 또는 이미지 요소를 선택합니다.
3. **클릭 시 동작**을 **페이지로 이동**으로 설정합니다.
4. 시작 페이지에서 연결할 페이지를 선택합니다.
5. 모든 페이지가 연결될 때까지 계속합니다.

![사용자가 인앱 메시지의 2페이지로 이동하도록 기본 동작 버튼을 편집하고 있습니다.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

페이지가 다른 페이지에 연결되어 있지 않으면 메시지를 시작할 수 없습니다.

{% alert note %}
사용자는 언제든지 닫기 X 버튼을 선택하여 메시지를 종료할 수 있습니다. 이 버튼은 제거할 수 없습니다.
{% endalert %}

## 4단계: 인앱 메시지 작성 및 디자인 {#step-4-build-and-design-your-in-app-message}

여기서 메시지가 브랜드의 시그니처 스타일로 꾸며집니다. 편집기 블록과 스타일 설정의 조합을 사용하여 인앱 메시지를 커스텀하고 디자인할 수 있습니다.

- 사용 가능한 편집기 블록과 해당 속성 목록은 [편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)을 참조하세요.
- 메시지의 모양과 느낌을 커스텀하는 데 도움이 필요하면 [스타일 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/)을 확인하세요.
- 오른쪽에서 왼쪽으로 읽는 메시지를 만드는 모범 사례는 [오른쪽에서 왼쪽으로 읽는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)를 참조하세요.

## 5단계: 인앱 메시지 테스트 {#step-5-test-your-in-app-message}

**미리보기 및 테스트** 섹션에서 다양한 기기에서 인앱 메시지를 미리보고 기기로 테스트 메시지를 보낼 수 있습니다. 여기서 드래그 앤 드롭 인앱 메시지 Campaign의 모든 플랫폼에서 세부 정보가 올바르게 정렬되어 있는지 확인할 수 있습니다.

Campaigns를 보내기 전에 항상 인앱 메시지를 테스트하여 사용자 관점에서 최종 메시지가 어떻게 보이는지 시각화하는 것이 중요합니다.

### 사용자로서 메시지 미리보기 {#preview-message-as-a-user}

{% alert warning %}
콘텐츠 테스트 그룹이나 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 기기에서 푸시가 활성화되어 있어야 합니다.
{% endalert %}

**미리보기 및 테스트** 탭에서 사용자인 것처럼 메시지를 미리볼 수 있습니다. 특정 사용자, 랜덤 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다:

- **랜덤 사용자:** Braze가 데이터베이스에서 사용자를 무작위로 선택하고 해당 사용자의 속성 또는 이벤트 정보를 기반으로 인앱 메시지를 미리봅니다.
- **사용자 선택:** 이메일 주소 또는 `external_id`를 기반으로 특정 사용자를 선택할 수 있습니다. 해당 사용자의 속성 및 이벤트 정보를 기반으로 인앱 메시지가 미리보기됩니다.
- **커스텀 사용자:** 사용자를 커스텀할 수 있습니다. Braze가 사용 가능한 모든 속성 및 이벤트에 대한 입력 필드를 제공합니다. 미리보기 이메일에서 보고 싶은 정보를 입력하세요.

### 테스트 체크리스트 {#test-checklist}

인앱 메시지를 테스트할 때 다음 질문을 고려하세요:

- 다양한 기기에서 메시지를 테스트했나요?
- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우를 대비하여 기본 속성 값을 설정했나요?
- 문구가 명확하고 간결하며 정확한가요?
- 버튼이 사용자를 올바른 곳으로 안내하나요?

## 자주 묻는 질문 {#frequently-asked-questions}

### 분석 페이지에 본문 클릭이 표시되지 않는 이유는 무엇인가요? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

드래그 앤 드롭 편집기로 만든 인앱 메시지에서는 본문 클릭이 자동으로 수집되지 않습니다. 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100) SDK 체인지로그를 참조하세요.

### 버튼 클릭을 기반으로 세분화할 수 있나요? {#can-i-segment-based-on-button-clicks}

네, 메시지에서 최대 두 개의 버튼에 대한 버튼 클릭을 기반으로 세분화할 수 있습니다. 이를 위해 버튼의 **Identifier for Reporting**을 "0"과 "1"로 설정하면, 각각 "Clicked in-app message button 1" 및 "Clicked in-app message button 2" 세분화 필터에 해당합니다.

!["0" 값이 입력된 "Identifier for Reporting" 필드.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### 커스텀 HTML이나 JavaScript를 사용하여 인앱 메시지를 커스텀하거나 기존 HTML 메시지를 편집기로 전환할 수 있나요? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

기존 HTML 메시지를 편집기로 직접 전환할 수는 없지만, 커스텀 코드 블록에 원시 HTML, CSS 및 JavaScript를 삽입할 수 있습니다. 커스텀 코드 블록을 사용하여 서드파티 동영상과 연결된 콘텐츠 또는 조건문과 같은 고급 Liquid를 임베드할 수 있습니다.

### 슬라이드업 인앱 메시지를 만들려면 어떻게 해야 하나요? {#how-can-i-create-a-slideup-in-app-message}

현재 편집기는 모달 및 전체화면 메시지만 지원합니다. **메시지 스타일** 패널의 **메시지 컨테이너** 섹션에서 표시 유형을 전환할 수 있습니다.

### Campaign이나 Canvas에서 작성한 인앱 메시지를 템플릿으로 저장할 수 있나요? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

네. 향후 Campaign이나 캔버스 단계에서 재사용하려는 인앱 메시지의 경우, 편집기를 종료한 후 사용할 수 있는 **템플릿으로 저장** 버튼을 사용하여 커스텀 템플릿으로 저장할 수 있습니다. 템플릿으로 저장하려면 먼저 Campaign을 시작하거나 초안으로 저장해야 합니다.

![제품 투어를 위한 인앱 메시지 미리보기.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

**콘텐츠** > **인앱 메시지**로 이동하여 인앱 메시지 템플릿을 만들고 저장할 수도 있습니다.