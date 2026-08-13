---
nav_title: "배너 생성"
article_title: "배너 생성"
page_order: 1
description: "이 참조 문서에서는 Braze Campaigns 및 Canvases를 사용하여 배너를 생성, 작성, 구성 및 발송하는 방법을 다룹니다."
tool:
  - Campaigns
channel:
  - banners
---

# 배너 생성 {#create-a-banner}

> Braze에서 Campaigns와 Canvases를 구축할 때 배너를 생성하는 방법을 알아보세요. 보다 일반적인 정보는 [배너 소개]({{site.baseurl}}/user_guide/channels/banners)를 참조하세요.

## 전제 조건 {#prerequisites}

배너를 시작하기 전에 개발팀에서 [앱 또는 웹사이트에 배치를 설정]({{site.baseurl}}/developer_guide/banners/placements)해야 합니다. 그동안 배너 Campaign 초안을 작성할 수는 있지만, 배치가 구성될 때까지 Campaign을 시작할 수는 없습니다.

## 배너 메시지 만들기 {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### 2단계: 메시지를 작성할 위치 선택 {#step-2-choose-where-to-build-your-message}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaign은 단일 타겟팅 메시징 캠페인에 적합하고, Canvas는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **Campaign 만들기**를 선택합니다.
2. **배너**를 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams)과 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다. 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, 보고서 빌더를 사용할 때 관련 태그로 필터링할 수 있습니다.
5. 이전에 만든 배치를 선택하여 Campaign에 연결합니다.
6. 필요에 따라 배리언트를 추가합니다. 각 배리언트에 대해 다른 메시지 유형과 레이아웃을 선택할 수 있습니다. 배리언트에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.
7. 배너 Campaign의 시작 날짜와 시간을 선택합니다. 기본적으로 배너는 무기한 지속됩니다. **종료 시간**을 선택하고 종료 날짜와 시간을 지정하여 이를 변경할 수 있습니다.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Canvas를 설정한 후 Canvas 빌더에서 메시지 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. 메시징 채널로 **배너**를 선택합니다.
4. 배너의 배치를 선택합니다.
5. 우선순위를 설정합니다. [배너 우선순위]({{site.baseurl}}/user_guide/channels/banners#priority)는 동일한 배치를 공유하는 배너가 표시되는 순서를 결정합니다.
6. 배너의 만료를 설정합니다. 단계가 사용 가능해진 후 일정 기간이 지나거나 특정 날짜와 시간에 만료되도록 설정할 수 있습니다. 최대 만료 기간은 단계가 사용자에게 제공된 후 31일입니다.

{% endtab %}
{% endtabs %}

### 3단계: 배너 작성 {#compose-a-banner}

다음으로, 작성을 시작할 방법을 선택합니다:

- **드래그 앤 드롭 편집기:** 빈 배너에서 시작하여 블록과 행을 사용해 시각적으로 구성합니다.
- **HTML 편집기:** 빈 배너에서 시작하여 HTML로 직접 작업합니다.
- **템플릿:** 템플릿 라이브러리를 열고 **Braze 템플릿** 또는 **내 템플릿**에서 디자인을 선택합니다. 템플릿은 커스터마이징을 위해 드래그 앤 드롭 편집기에서 열립니다.

![배너에 대해 드래그 앤 드롭 편집기, HTML 편집기 또는 템플릿을 선택하는 옵션.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### 3.1단계: 배너 스타일 지정 {#step-31-style-the-banner}

{% tabs %}
{% tab 드래그 앤 드롭 편집기 %}

블록과 행을 캔버스 영역으로 드래그 앤 드롭하여 메시지 작성을 시작할 수 있습니다. 배너 편집기 블록 및 공유 속성 세부 정보에 대한 참조는 [편집기 블록(배너)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners)을 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

메시지의 배경 속성, 테두리 설정 등을 커스터마이징하려면 **스타일**을 선택합니다. 특정 블록이나 행의 스타일만 커스터마이징하려면 해당 항목을 선택하여 변경합니다.

![배너 작성기의 스타일 패널.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab HTML 편집기 %}

HTML 편집기는 이미 자체 HTML 템플릿을 유지하고 있거나 마크업과 스타일링을 완전히 제어하고 싶은 팀에 가장 적합합니다. 커스텀 HTML을 편집기에 직접 작성하거나 붙여넣을 수 있습니다. Liquid 개인화 태그가 완전히 지원되므로 사용자 속성, 커스텀 속성, 카탈로그 항목 등을 참조할 수 있습니다.

{% alert tip %}
배너 HTML 작성에 도움이 필요하신가요? HTML 편집기에서 **Ask Operator**를 선택하고 원하는 배너를 설명하세요. [BrazeAI<sup>TM</sup> Operator]({{site.baseurl}}/user_guide/brazeai/operator)가 검토하고 편집기에 삽입할 수 있는 HTML을 생성합니다. 자세한 내용은 [메시지 생성]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages)을 참조하세요.
{% endalert %}

커스텀 HTML에서 클릭 및 닫기 추적을 위해서는 JavaScript 브릿지 메서드를 명시적으로 호출해야 합니다. 전체 참조는 [배너용 커스텀 코드 및 JavaScript 브릿지]({{site.baseurl}}/user_guide/channels/banners/custom_code)를 참조하세요.

{% endtab %}
{% endtabs %}

{% alert note %}
단일 배너 Campaign 내에서 다른 언어의 사용자를 타겟팅하려면 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.
{% endalert %}

#### 3.2단계: 클릭 시 동작 정의(선택 사항) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab 드래그 앤 드롭 편집기 %}

사용자가 배너의 링크를 클릭하면 앱 내부로 더 깊이 이동하거나 다른 웹페이지로 리디렉션할 수 있습니다. 또한 [커스텀 속성 또는 이벤트를 기록]({{site.baseurl}}/developer_guide/analytics)하도록 선택하여 사용자가 배너를 클릭할 때 커스텀 데이터로 사용자 프로필을 업데이트할 수 있습니다. 보다 세분화된 클릭 추적을 위해 속성 패널의 **보고용 식별자** 필드를 사용하여 각 인터랙티브 요소에 커스텀 식별자를 할당합니다.

{% alert important %}
{::nomarkdown}
특정 요소(예: 배너의 버튼, 링크 또는 이미지)에 자체 클릭 시 동작이 있는 경우 클릭 시 동작이 재정의될 수 있습니다. 예를 들어, 다음과 같은 클릭 시 동작이 있다고 가정합니다:<br><ul><li>배너에 웹사이트 홈페이지로 리디렉션하는 클릭 시 동작이 있습니다.</li><li>배너 내 이미지에 웹사이트 제품 페이지로 리디렉션하는 클릭 시 동작이 있습니다.</li></ul>사용자가 이미지를 클릭하면 제품 페이지로 리디렉션됩니다. 그러나 배너의 주변 영역을 클릭하면 홈페이지로 리디렉션됩니다.
{:/}
{% endalert %}

{% endtab %}
{% tab HTML 편집기 %}

HTML 편집기에서는 클릭 추적이 자동으로 이루어지지 않습니다. 추적하려는 각 클릭 가능한 요소에 대해 HTML 내에서 `brazeBridge.logClick()`을 호출해야 합니다. 예를 들어:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

전체 JavaScript 브릿지 참조는 [배너용 커스텀 코드 및 JavaScript 브릿지]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)를 참조하세요.

{% endtab %}
{% endtabs %}

#### 3.3단계: 닫기 동작 구성(선택 사항) {#dismiss-behavior}

{% alert important %}
배너 닫기에는 다음 최소 SDK 버전이 필요합니다. 이전 SDK 버전에서는 닫기가 활성화된 배너가 렌더링되지 않습니다.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab 드래그 앤 드롭 편집기 %}

**닫기 동작** 섹션에서 **배너를 닫을 수 있음** 체크박스를 선택하여 사용자가 배너를 닫을 수 있도록 합니다. 이 기능은 광범위한 오디언스에게 기간 한정 혜택을 홍보하면서도 관심 없는 사용자가 메시지를 숨길 수 있도록 하려는 경우에 유용합니다.

닫기가 활성화되면 **닫기 동작** 섹션에서 닫기 버튼을 커스터마이징할 수 있습니다:

| 설정 | 설명 |
|---------|-------------|
| **버튼 크기** | 배너에 표시되는 닫기 버튼의 크기입니다. |
| **버튼 색상** | 닫기 버튼의 색상입니다. |
| **ARIA 레이블** | 스크린 리더에서 사용하는 닫기 버튼의 접근성 레이블입니다. 비워두면 기본값은 "Close"입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="닫기 버튼 설정" }

사용자가 배너를 닫으면 Campaign의 타겟팅 기준에 여전히 해당하더라도 해당 사용자에게 다시 표시되지 않습니다.

{% endtab %}
{% tab HTML 편집기 %}

HTML 편집기에서 닫기는 `brazeBridge.closeMessage()`를 사용하여 HTML에서 처리됩니다. 닫기 동작을 클릭 이벤트로도 추적하려면 `brazeBridge.logClick()`과 함께 사용합니다. 예를 들어:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

사용자가 이 방법으로 배너를 닫으면 Campaign의 타겟팅 기준에 여전히 해당하더라도 해당 사용자에게 다시 표시되지 않습니다.

전체 JavaScript 브릿지 참조는 [배너용 커스텀 코드 및 JavaScript 브릿지]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)를 참조하세요.

{% endtab %}
{% endtabs %}

#### 3.4단계: 커스텀 속성정보 추가(선택 사항) {#custom-properties}

배너에 커스텀 속성정보를 추가하여 문자열이나 JSON 객체와 같은 구조화된 메타데이터를 첨부할 수 있습니다. 이러한 속성정보는 배너 표시 방식에 영향을 미치지 않지만 [Braze SDK를 통해 액세스]({{site.baseurl}}/developer_guide/banners/placements)하여 앱의 동작이나 외관을 수정할 수 있습니다. 예를 들어 다음과 같은 작업이 가능합니다:

{% multi_lang_include banners/metadata_use_cases.md %}

커스텀 속성정보는 드래그 앤 드롭 편집기와 HTML 편집기 모두에서 동일하게 작동합니다. 커스텀 속성정보를 추가하려면 **설정** > **속성정보** > **속성정보 추가**를 선택합니다.

![배너 Campaign에 첫 번째 커스텀 속성정보를 추가하는 옵션이 표시된 속성정보 페이지.]({% image_buster /assets/img/banners/add_property.png %})

추가하려는 각 속성정보에 대해 다음을 입력합니다:

| 필드 | 설명 | 예시 |
|-------|-------------|---------|
| 속성정보 유형 | 속성정보의 데이터 유형입니다. 지원되는 유형에는 문자열, 불리언, 숫자, 타임스탬프, 이미지 URL 및 JSON 객체가 포함됩니다. | 문자열 |
| 속성정보 키 | 속성정보의 고유 식별자입니다. 이 키는 SDK에서 속성정보에 액세스하는 데 사용됩니다. | `color` |
| 값 | 속성정보에 할당된 값입니다. 선택한 속성정보 유형과 일치해야 합니다. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="3.4단계: 커스텀 속성정보 추가(선택 사항) #custom-properties" }

완료되면 **완료**를 선택합니다.

![키가 color이고 값이 #FF0000인 문자열 속성정보가 있는 속성정보 페이지.]({% image_buster /assets/img/banners/example_property.png %})

#### 3.5단계: 연결된 콘텐츠로 개인화(선택 사항) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

배너는 세션 새로고침 중에 인라인으로 렌더링되므로 이 채널의 연결된 콘텐츠는 다른 채널과 다르게 작동합니다:

- GET 요청만 지원됩니다.
- 단일 새로고침의 모든 배치(최대 10개)는 약 2초의 렌더링 예산을 공유합니다. 호출이 느리거나 시간 초과되거나 예산이 초과되면 해당 배치의 연결된 콘텐츠 결과는 null로 처리됩니다. 배너는 재시도하지 않습니다.

최상의 결과를 위해:

- 엔드포인트를 빠르게 유지하고 가능하면 [응답을 캐시]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)하세요.
- 함께 렌더링되는 배치 전체에서 고유한 연결된 콘텐츠 URL 수를 제한하세요.
- 하나의 연결된 콘텐츠 응답이 다음 URL을 결정하는 체인 호출을 피하세요. 추가 호출마다 공유 예산이 소모됩니다.
- Liquid 가드 구문 또는 [`default` 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)를 사용하여 null 결과를 처리하고 빈 배너를 방지하세요.

### 4단계: Campaign 또는 Canvas의 나머지 부분 구성 {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### 배너 우선순위 설정(선택 사항) {#set-banner-priority-optional}

[배너 우선순위]({{site.baseurl}}/user_guide/channels/banners#priority)는 동일한 배치를 공유하는 배너가 표시되는 순서를 결정합니다. 우선순위를 수동으로 설정하려면:

1. **정확한 우선순위 설정**을 선택합니다.
2. Campaign을 드래그 앤 드롭하여 올바른 우선순위로 정렬합니다.
3. **정렬 적용**을 선택합니다.

{% alert tip %}
동일한 배치 ID를 사용하는 여러 배너 Campaign이 있는 경우, 드래그 앤 드롭 우선순위 정렬기를 사용하여 정확한 우선순위를 정의하는 것을 권장합니다.
{% endalert %}

#### 재자격 구성(선택 사항) {#re-eligibility}

기본적으로 배너를 닫은 사용자는 해당 Campaign에 대해 다시 자격을 얻지 못합니다. 닫은 사용자가 배너를 다시 볼 수 있도록 하려면 **전달 제어** 단계로 이동하여 **사용자가 Campaign을 다시 받을 수 있도록 허용**을 선택합니다. 활성화되면 분, 시간, 일 또는 주 단위로 쿨다운 기간을 설정합니다.

카운트다운은 사용자가 배너를 닫은 시점부터 시작됩니다. 기간이 만료되면 사용자는 자동으로 재자격을 얻으며, Campaign을 다시 시작할 필요가 없습니다. 재자격은 사용자별, Campaign별로 추적됩니다.

#### 오디언스 선택 {#choose-your-audience}

1. **타겟 오디언스**에서 Segment 또는 필터를 선택하여 오디언스를 좁힙니다. 대략적인 Segment 인구의 미리보기가 자동으로 제공됩니다. 정확한 Segment 멤버십은 메시지가 전송되기 전에 계산됩니다.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. **전환 할당**에서 전환 이벤트를 정의하여 Campaign을 받은 후 사용자가 특정 작업을 수행하는 빈도를 추적합니다. 작업을 전환으로 카운트하기 위한 최대 30일 기간을 설정할 수 있습니다.

#### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 Campaign을 받은 후 사용자가 특정 작업을 수행하는 빈도인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환으로 카운트되는 최대 30일 기간을 허용할 수 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 Canvas 구성 요소의 나머지 섹션을 완료합니다. Canvas의 나머지 부분을 구성하고, [다변량 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing) 및 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) 단계를 참조하세요.

Canvas 배너 단계의 재자격을 제어하려면 Canvas 재진입 설정을 사용합니다. 자세한 내용은 [Campaign 및 Canvas의 재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 참조하세요.

{% endtab %}
{% endtabs %}

### 5단계: 메시지 테스트(선택 사항) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas 구성을 완료한 후 세부 사항을 검토하고, [테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)한 다음 준비가 되면 전송합니다.