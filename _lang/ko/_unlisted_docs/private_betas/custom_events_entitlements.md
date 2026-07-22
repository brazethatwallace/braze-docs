---
article_title: 커스텀 이벤트
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Braze 학습 과정]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 이벤트 {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> 이 문서에서는 커스텀 이벤트와 속성정보, 관련 세분화 필터, Canvas 진입 속성정보, 관련 분석 등에 대해 설명합니다. Braze 이벤트에 대한 일반적인 내용은 [이벤트]({{site.baseurl}}/user_guide/data/custom_data/events)를 참조하세요.

커스텀 이벤트는 사용자가 수행한 행동이나 사용자에 대한 업데이트입니다. 커스텀 이벤트가 기록되면 다양한 수와 유형의 후속 Campaign을 트리거할 수 있습니다. 그런 다음 [세분화 필터](#segmentation-filters)를 사용하여 해당 커스텀 이벤트가 발생한 빈도와 최근 시점을 기준으로 사용자를 세분화할 수 있습니다. 이러한 특성 덕분에 커스텀 이벤트는 애플리케이션 내에서 높은 가치를 지닌 사용자 상호작용을 추적하는 데 가장 적합합니다.

## 사용 사례 {#use-cases}

일반적인 커스텀 이벤트 사용 사례는 다음과 같습니다:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## 권한 {#entitlements}

권한은 커스텀 이벤트 용량을 결정하며, 정의한 서로 다른 이벤트 이름의 수를 추적합니다. 워크스페이스당 최대 2,000개의 커스텀 이벤트를 사용할 수 있습니다. 용량을 늘려야 하는 경우 Braze 계정 매니저에게 문의하여 자세한 정보를 확인하세요.

워크스페이스가 최대 커스텀 이벤트 수에 가까워지면 대시보드와 이메일을 통해 알림을 받아 상황을 파악할 수 있습니다.

용량에 도달한 후에도 기존 커스텀 이벤트는 계속 수신할 수 있습니다. 그러나 새로운 커스텀 이벤트를 생성할 수는 없습니다. 이미 존재하지 않는 커스텀 이벤트에 대해 수신된 데이터는 처리되지 않습니다.

## 커스텀 이벤트 관리 {#managing-custom-events}

대시보드에서 **데이터 설정** > **커스텀 이벤트**로 이동하여 커스텀 이벤트를 관리, 생성 또는 차단 목록에 추가할 수 있습니다.

커스텀 이벤트 옆의 메뉴를 선택하면 다음 작업을 수행할 수 있습니다:

### 차단 목록 추가 {#blocklisting}

작업 메뉴를 통해 개별 커스텀 이벤트를 차단 목록에 추가하거나, 최대 100개의 이벤트를 선택하여 일괄 차단할 수 있습니다.

커스텀 이벤트를 차단하면:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

또한 차단된 커스텀 이벤트가 현재 Braze의 다른 영역에서 필터나 트리거에 의해 참조되고 있는 경우, 해당 이벤트를 참조하는 모든 필터 또는 트리거 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

### 설명 추가 {#adding-descriptions}

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)이 있는 경우 커스텀 이벤트가 생성된 후 설명을 추가할 수 있습니다. 커스텀 이벤트에 대해 **설명 편집**을 선택하고 팀을 위한 메모 등 원하는 내용을 입력하세요.

## 태그 추가 {#adding-tags}

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)이 있는 경우 커스텀 이벤트가 생성된 후 태그를 추가할 수 있습니다. 태그를 사용하여 이벤트 목록을 필터링할 수 있습니다.

### 사용 보고서 보기 {#viewing-usage-reports}

사용 보고서에는 특정 커스텀 이벤트를 사용하는 모든 Canvases, Campaigns 및 Segments가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

여러 커스텀 이벤트의 체크박스를 선택한 다음 **사용 보고서 보기**를 선택하면 한 번에 최대 100개의 사용 보고서를 볼 수 있습니다.

## 데이터 내보내기 {#exporting-data}

커스텀 이벤트 목록을 CSV 파일로 내보내려면 페이지 상단의 **모두 내보내기** 버튼을 선택하세요. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

## 커스텀 이벤트 기록 {#logging-custom-events}

커스텀 이벤트에는 추가 설정이 필요합니다. 커스텀 이벤트를 기록하고 속성정보 및 수량을 추가하는 데 사용되는 메서드를 확인하려면 아래 플랫폼별 설명서 링크를 참조하세요.

{% details 플랫폼별 설명서 펼치기 %}

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [웹]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## 커스텀 이벤트 저장 {#custom-event-storage}

커스텀 이벤트 메타데이터(첫 번째 또는 마지막 발생, 총 횟수, 30일 동안의 X in Y)를 포함하여 **고객 프로필**에 저장된 모든 데이터는 각 프로필이 [활성]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users) 상태인 한 무기한 보존됩니다.

## 세분화 필터 {#segmentation-filters}

다음 표는 커스텀 이벤트를 기준으로 사용자를 세분화하는 데 사용할 수 있는 필터를 보여줍니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 커스텀 이벤트가 **X회 이상** 발생했는지 확인 | **MORE THAN** | **NUMBER** |
| 커스텀 이벤트가 **X회 미만** 발생했는지 확인 | **LESS THAN** | **NUMBER** |
| 커스텀 이벤트가 **정확히 X회** 발생했는지 확인 | **EXACTLY** | **NUMBER** |
| 커스텀 이벤트가 마지막으로 **X 날짜 이후에** 발생했는지 확인 | **AFTER** | **TIME** |
| 커스텀 이벤트가 마지막으로 **X 날짜 이전에** 발생했는지 확인 | **BEFORE** | **TIME** |
| 커스텀 이벤트가 마지막으로 **X일 이상 전에** 발생했는지 확인 | **MORE THAN** | **NUMBER OF DAYS AGO** (양수) |
| 커스텀 이벤트가 마지막으로 **X일 미만 전에** 발생했는지 확인 | **LESS THAN** | **NUMBER OF DAYS AGO** (양수) |
| 커스텀 이벤트가 **X회(최대 = 50) 이상** 발생했는지 확인 | **MORE THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
| 커스텀 이벤트가 **X회(최대 = 50) 미만** 발생했는지 확인 | **LESS THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
| 커스텀 이벤트가 **정확히 X회(최대 = 50)** 발생했는지 확인 | **EXACTLY** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 분석 {#analytics}

Braze는 커스텀 이벤트가 발생한 횟수와 각 사용자가 마지막으로 수행한 시점을 기록하여 세분화에 활용합니다. **Analytics** > **커스텀 이벤트 보고서**로 이동하여 이러한 분석을 확인하세요.

대시보드의 **커스텀 이벤트 보고서** 페이지에서 각 커스텀 이벤트가 발생한 빈도를 집계하여 볼 수 있습니다. 시계열 위에 겹쳐진 회색 선은 마지막으로 Campaign이 전송된 시점을 나타내며, Campaign이 커스텀 이벤트 활동에 어떤 영향을 미쳤는지 확인하는 데 유용합니다.

![대시보드의 커스텀 이벤트 페이지에서 커스텀 이벤트의 추세를 보여주는 커스텀 이벤트 횟수 그래프][8]

**필터**를 사용하여 시간별, 월간 활성 사용자(MAU), Segments 또는 핵심 성과 지표(KPI) 공식별로 커스텀 이벤트를 세분화할 수도 있습니다.

{% alert tip %}
커스텀 이벤트와 유사한 사용자 행동에 대한 카운터를 유지하려면 [커스텀 속성 증가]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers)를 사용하세요. 그러나 커스텀 속성 데이터는 시계열로 볼 수 없습니다. 시계열로 분석할 필요가 없는 사용자 행동은 이 메서드를 사용하여 기록해야 합니다.
{% endalert %}

### 커스텀 이벤트 분석이 표시되지 않는 이유 {#why-custom-events-analytics-arent-showing}

커스텀 이벤트 데이터로 생성된 Segments는 생성 이전의 과거 데이터를 표시할 수 없습니다.

## 커스텀 이벤트 속성정보 {#custom-event-properties}

커스텀 이벤트 속성정보는 이벤트의 특정 발생을 설명하는 커스텀 이벤트 메타데이터 또는 속성입니다. 이러한 속성정보는 트리거 조건을 더 세밀하게 설정하고, 메시징의 개인화를 높이며, 전환을 추적하고, 원시 데이터 내보내기를 통해 더 정교한 분석을 생성하는 데 사용할 수 있습니다.

커스텀 이벤트 속성정보는 Braze 프로필에 저장되지 않으므로 데이터 포인트를 소비하지 않습니다(예외 사항은 [데이터 포인트](#data-points) 참조).

{% alert important %}
각 커스텀 이벤트 또는 구매에는 최대 256개의 고유한 커스텀 이벤트 속성정보를 포함할 수 있습니다. 커스텀 이벤트 또는 구매가 256개 이상의 속성정보와 함께 기록되면 처음 256개만 캡처되어 사용할 수 있습니다.
{% endalert %}

### 예상 형식 {#expected-format}

속성정보 값은 키가 속성정보 이름이고 값이 속성정보 값인 오브젝트여야 합니다. 속성정보 이름은 255자 이하의 비어 있지 않은 문자열이어야 하며, 앞에 달러 기호(`$`)가 올 수 없습니다.

속성정보 값은 다음 데이터 유형 중 하나일 수 있습니다:

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | [정수](https://en.wikipedia.org/wiki/Integer) 또는 [플로트](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| 부울 | `true` 또는 `false` 값 |
| 날짜/시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열로 포맷됩니다. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하 |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 오브젝트 | 오브젝트는 문자열로 수집됩니다. |
| 중첩 오브젝트 | 다른 오브젝트 내부에 있는 오브젝트입니다. 자세한 내용은 이 문서의 [중첩 오브젝트](#nested-objects) 섹션을 참조하세요.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

배열 또는 오브젝트 값을 포함하는 이벤트 속성정보 오브젝트는 최대 100&nbsp;KB의 이벤트 속성정보 페이로드를 가질 수 있습니다.

커스텀 이벤트 속성정보의 데이터 유형을 변경할 수 있지만, 데이터가 수집된 후 [데이터 유형을 변경]({{site.baseurl}}/help/help_articles/data/change_custom_data_type)하면 미치는 영향에 유의하세요.

### 커스텀 이벤트 속성정보 사용 {#using-custom-event-properties}

커스텀 이벤트 속성정보는 Campaign 트리거 조건 설정, 전환 추적 및 메시징 개인화에 사용할 수 있습니다.

#### 메시지 트리거 {#trigger-messages}

커스텀 이벤트 속성정보를 사용하여 특정 Campaign 또는 Canvas의 오디언스를 더 세밀하게 좁힐 수 있습니다. 예를 들어, 이커머스 애플리케이션이 있고 사용자가 장바구니를 유기했을 때 메시지를 보내려면 `cart value`의 커스텀 이벤트 속성정보를 추가하여 타겟 오디언스를 개선하고 Campaign 개인화를 강화할 수 있습니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 두 개의 필터가 AND 연산자로 결합되어 장바구니 값이 100달러에서 200달러 사이인 장바구니를 유기한 사용자에게 이 Campaign을 전송합니다][16]

중첩된 커스텀 이벤트 속성정보도 [실행 기반 전달][19]에서 지원됩니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 장바구니의 항목 중 가격이 100달러 이상인 항목이 있는 경우 하나의 필터가 선택됩니다.][20]

#### 메시지 개인화 {#personalize-messages}

메시징 템플릿 내에서 개인화를 위해 커스텀 이벤트 속성정보를 사용할 수도 있습니다. 트리거 이벤트가 있는 [실행 기반 전달][19]을 사용하는 모든 Campaign은 해당 이벤트의 커스텀 이벤트 속성정보를 메시징 개인화에 사용할 수 있습니다.

예를 들어, 게임 앱이 있고 레벨을 완료한 사용자에게 메시지를 보내려는 경우, 사용자가 해당 레벨을 완료하는 데 걸린 시간에 대한 속성정보로 메시지를 더욱 개인화할 수 있습니다. 이 예에서는 [조건 로직][18]을 사용하여 세 가지 다른 Segments에 대해 메시지를 개인화합니다. `time_spent`라는 커스텀 이벤트 속성정보는 ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``를 호출하여 메시지에 포함할 수 있습니다.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
사용자에게 인터넷 연결이 없는 경우, 템플릿화된 커스텀 이벤트 속성정보(예: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %})가 포함된 트리거 인앱 메시지는 실패하여 표시되지 않습니다.
{% endalert %}

인앱 메시지를 템플릿화된 인앱 메시지로 전달하게 하는 Liquid 태그의 전체 목록은 [자주 묻는 질문]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)을 참조하세요.

##### 필터 관련 고려 사항 {#considerations-with-filters}

- **API 호출:** API 호출을 하고 "is blank" 필터를 사용할 때, 커스텀 이벤트 속성정보가 호출에서 제외되면 "blank"로 간주됩니다. 예를 들어, `"event_property": ""`를 포함하면 사용자는 "not blank"로 간주됩니다.
- **정수:** 숫자 커스텀 이벤트 속성정보로 필터링할 때 숫자가 매우 큰 경우 "exactly" 필터를 사용하지 마세요. 숫자가 너무 크면 특정 길이에서 반올림될 수 있으므로 필터가 예상대로 작동하지 않을 수 있습니다.

#### 세분화 {#segmentation}

이벤트 속성정보 세분화를 사용하여 수행된 커스텀 이벤트와 해당 이벤트에 연결된 속성정보를 기반으로 사용자를 타겟팅할 수 있습니다. 이를 통해 구매 및 커스텀 이벤트별 세분화 시 필터링 옵션이 확장됩니다.

커스텀 이벤트의 이벤트 속성정보는 이를 사용하는 모든 Segment에 대해 실시간으로 업데이트됩니다. **데이터 설정** > **커스텀 이벤트**로 이동하고 관련 커스텀 이벤트에 대해 **속성정보 관리**를 선택하여 속성정보를 관리할 수 있습니다. 특정 Segment 필터에서 사용되는 커스텀 이벤트 속성정보는 최대 30일의 조회 기록을 가집니다.

##### 세분화를 위한 이벤트 속성정보 추가 {#adding-event-properties-for-segmentation}

이벤트 속성정보의 최근성 및 빈도를 기반으로 Segments를 생성하려면 "Manage Custom Event Property Segmentation" [사용자 권한]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage)이 필요합니다.

기본적으로 워크스페이스당 20개의 세분화 가능한 이벤트 속성정보를 사용할 수 있습니다. 이 한도를 늘리려면 Braze 계정 매니저에게 문의하세요.

세분화를 위한 이벤트 속성정보를 추가하려면 다음을 수행하세요:

1. 커스텀 이벤트로 이동하여 **속성정보 관리**를 선택합니다.
2. **세분화 활성화** 토글을 선택하여 세분화를 위한 이벤트 속성정보를 추가합니다. 세분화 시 추가 필터링 옵션에 접근할 수 있습니다.

이벤트 속성정보 세분화 필터에는 다음이 포함됩니다:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![속성정보 'number of items'의 값이 '2'인 'Abandoned Cart'를 지난 '30' 캘린더 일 동안 '1'회 '이상' 수행한 필터 그룹.][3]

데이터는 고객 성공 매니저가 활성화한 후에만 해당 이벤트 속성정보에 대해 기록되며, 이벤트 속성정보는 해당 날짜 이후부터만 사용할 수 있습니다.

##### 데이터 포인트 {#data-points}

구독 사용량과 관련하여, 다음 필터로 세분화가 활성화된 커스텀 이벤트 속성정보는 커스텀 이벤트 자체에 의해 계산되는 데이터 포인트에 추가로 별도의 데이터 포인트로 계산됩니다:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas 진입 속성정보 및 이벤트 속성정보 {#canvas-entry-properties-and-event-properties}

Canvas 사용자 여정에서 `canvas_entry_properties`와 `event_properties`를 사용할 수 있습니다. 자세한 정보와 예시는 [Canvas 진입 속성정보 및 이벤트 속성정보]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)를 참조하세요.

{% tabs local %}
{% tab Canvas 진입 속성정보 %}

[Canvas 진입 속성정보]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object)는 실행 기반 또는 API 트리거 Canvases에 매핑하는 속성정보입니다. `canvas_entry_properties` 오브젝트의 최대 크기 제한은 50KB입니다.

{% alert note %}
인앱 메시지 채널의 경우, `canvas_entry_properties`는 Canvas Flow 및 원래 Canvas 편집기에서만 참조할 수 있으며, 원래 편집기에서는 이전 얼리 액세스의 일부로 영구 진입 속성정보가 활성화된 경우에만 가능합니다.
{% endalert %}

Canvas Flow 메시징의 경우, `canvas_entry_properties`는 다음 Liquid 형식으로 모든 메시지 단계에서 사용할 수 있습니다: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. 이 방식으로 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

#### 사용 사례 {#use-case}

{% raw %}
소매점 RetailApp이 다음과 같은 요청을 보낸다고 가정합니다: `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. RetailApp은 Liquid `{{canvas_entry_properties.${product_name}}}`를 사용하여 제품 이름(shoes)을 메시지에 포함할 수 있습니다.
{% endraw %}

RetailApp은 또한 사용자가 구매 이벤트를 트리거한 후 해당 사용자를 타겟팅하는 Canvas에서 다양한 `product_name` 속성정보에 대해 특정 메시지를 전송하도록 트리거할 수 있습니다. 예를 들어, 신발을 구매한 사용자와 다른 것을 구매한 사용자에게 다른 메시지를 보내려면 메시지 단계에 다음 Liquid를 추가할 수 있습니다.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details 원래 Canvas 편집기에 대해 펼치기 %}

2023년 2월 28일부터 원래 편집기를 사용하여 Canvases를 생성하거나 복제할 수 없습니다. 이 섹션은 참조용으로만 제공됩니다.

원래 편집기로 구축된 Canvases의 경우, `canvas_entry_properties`는 Canvas의 첫 번째 전체 단계에서만 참조할 수 있습니다.

{% enddetails %}
{% endtab %}

{% tab 이벤트 속성정보 %}

{% alert important %}
리드 메시지 단계에서는 `event_properties`를 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.
{% endalert %}

이벤트 속성정보는 커스텀 이벤트 및 구매에 대해 설정한 속성정보를 의미합니다. 이러한 `event_properties`는 실행 기반 전달을 사용하는 Campaigns 및 Canvases에서 사용할 수 있습니다.

Canvas Flow에서 커스텀 이벤트 및 구매 이벤트 속성정보는 작업 경로 단계 뒤에 오는 모든 메시지 단계에서 Liquid로 사용할 수 있습니다. 이러한 `event_properties`를 참조할 때는 {% raw %} ``{{event_properties.${property_name}}}``{% endraw %}를 사용해야 합니다. 이 방식으로 메시지 구성요소에서 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

작업 경로 뒤의 첫 번째 메시지 단계에서는 해당 작업 경로에서 참조된 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이러한 `event_properties`는 사용자가 실제로 행동을 수행한 경우에만 사용할 수 있습니다(다른 모든 사용자 그룹으로 이동하지 않은 경우). 이 작업 경로와 메시지 단계 사이에 다른 단계(다른 작업 경로 또는 메시지 단계가 아닌)를 둘 수 있습니다.

{% details 원래 Canvas 편집기에 대해 펼치기 %}

2023년 2월 28일부터 원래 편집기를 사용하여 Canvases를 생성하거나 복제할 수 없습니다. 이 섹션은 참조용으로만 제공됩니다.

원래 Canvas 편집기의 경우, `event_properties`는 예약된 전체 단계에서 사용할 수 없습니다. 그러나 실행 기반 Canvas의 첫 번째 전체 단계에서는 해당 전체 단계가 예약된 경우에도 `event_properties`를 사용할 수 있습니다.

{% enddetails %}

{% endtab %}
{% endtabs %}

### 중첩 오브젝트 {#nested-objects}

중첩 오브젝트(다른 오브젝트 내부의 오브젝트)를 사용하여 중첩된 JSON 데이터를 커스텀 이벤트 및 구매의 속성정보로 전송할 수 있습니다. 이 중첩 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하며, 사용자를 세분화하는 데 사용할 수 있습니다.

자세한 내용은 [중첩 오브젝트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects) 전용 페이지를 참조하세요.

## 커스텀 이벤트 속성정보 저장 {#custom-event-property-storage}

커스텀 이벤트 속성정보는 타겟팅 정밀도를 높이고 메시지를 더욱 개인화된 느낌으로 만들 수 있도록 설계되었습니다. 커스텀 이벤트 속성정보는 Braze 내에서 단기 및 장기 모두 저장할 수 있습니다.

이벤트 속성정보의 값을 기반으로 두 가지 방법으로 세분화할 수 있습니다:

1. **30일 이내:** Braze 지원 담당자가 Braze Segments 내에서 특정 이벤트 속성정보 값의 빈도와 최근성을 기반으로 이벤트 속성정보 세분화를 활성화할 수 있습니다. Segments 내에서 이벤트 속성정보를 활용하려면 Braze 계정 담당자 또는 고객 성공 매니저에게 문의하세요. 이 옵션은 데이터 사용량에 영향을 미칩니다.<br><br>
2. **30일 이내 및 이후:** 단기 및 장기 이벤트 속성정보 세분화를 모두 다루려면 [세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension)을 사용할 수 있습니다. 이 기능은 지난 2년 동안 추적된 커스텀 이벤트 및 이벤트 속성정보를 기반으로 사용자를 세분화합니다. 이 옵션은 데이터 사용량에 영향을 미치지 않습니다.

특정 요구 사항에 따른 최적의 접근 방식에 대한 권장 사항은 Braze 고객 성공 매니저에게 문의하세요.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"