---
nav_title: 커스텀 이벤트 속성정보
article_title: 커스텀 이벤트 속성정보
page_order: 0
page_type: reference
description: "이 문서에서는 커스텀 이벤트 속성정보, 예상 형식, 사용 방법, 커스텀 이벤트 속성정보 저장에 대해 설명합니다."
---

# 커스텀 이벤트 속성정보 {#custom-event-properties}

> 이 문서에서는 커스텀 이벤트 속성정보, 예상 형식, 메시징 및 세분화에 활용하는 방법, 커스텀 이벤트 속성정보 저장에 대해 설명합니다.

커스텀 이벤트 속성정보는 이벤트의 특정 발생을 설명하는 커스텀 이벤트 메타데이터 또는 속성입니다. 이러한 속성정보는 트리거 조건을 더 세밀하게 설정하고, 메시징에서 개인화를 강화하며, 전환을 추적하고, 원시 데이터 내보내기를 통해 더 정교한 분석을 생성하는 데 사용할 수 있습니다.

커스텀 이벤트 속성정보는 Braze 프로필에 저장되지 않으므로 데이터 포인트를 기록하지 않습니다(예외 사항은 [데이터 포인트](#data-points)를 참조하세요).

{% alert important %}
각 커스텀 이벤트 또는 구매에는 최대 256개의 고유한 커스텀 이벤트 속성정보를 포함할 수 있습니다. 커스텀 이벤트 또는 구매가 256개 이상의 속성정보와 함께 기록되면 처음 256개만 캡처되어 사용할 수 있습니다.
{% endalert %}

## 예상 형식 {#expected-format}

속성정보 값은 오브젝트여야 합니다. 키는 속성정보 이름(비어 있지 않은 문자열, 255자 이하, 선행 `$` 없음)이고, 값은 속성정보 값입니다. 지원되는 데이터 유형, 형식 요구 사항 및 페이로드 제한에 대해서는 [데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#event-property-data-types)을 참조하세요.

커스텀 이벤트 속성정보의 데이터 유형을 변경할 수 있지만, 데이터가 수집된 후 [데이터 유형을 변경]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#changing-custom-attribute-or-event-data-type)할 때의 영향에 유의하세요.

### 예약 키 {#reserved-keys}

예약 키를 이벤트 속성정보 이름으로 사용할 수 없습니다. `properties` 오브젝트에서 예약 키를 사용하면 "Invalid 'properties' field" 오류가 반환됩니다.

| 등록정보 | 예약 키 |
| --- | --- |
| 커스텀 이벤트 | `time` 및 `event_name` |
| 구매 이벤트 | `time`, `product_id`, `quantity`, `event_name`, `price`, `currency` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 커스텀 이벤트 속성정보 사용 {#using-custom-event-properties}

커스텀 이벤트 속성정보는 Campaign 트리거를 설정하고, 전환을 추적하며, 메시징을 개인화하는 데 사용할 수 있습니다.

### 메시지 트리거 {#trigger-messages}

커스텀 이벤트 속성정보를 사용하여 특정 Campaign 또는 Canvas의 오디언스를 더 세밀하게 좁힐 수 있습니다. 예를 들어, 이커머스 애플리케이션에서 사용자가 장바구니를 유기했을 때 메시지를 보내려면 `price`라는 커스텀 이벤트 속성정보를 추가하여 타겟 오디언스를 개선하고 Campaign 개인화를 강화할 수 있습니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 두 개의 필터가 AND 연산자로 결합되어 100달러에서 200달러 사이의 가격으로 장바구니를 유기한 사용자에게 이 Campaign을 전송합니다]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

중첩된 커스텀 이벤트 속성정보도 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)에서 지원됩니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 장바구니에 있는 항목 중 가격이 100달러 이상인 항목이 있으면 하나의 필터가 선택됩니다.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### 메시지 개인화 {#personalize-messages}

메시징 템플릿 내에서 개인화를 위해 커스텀 이벤트 속성정보를 사용할 수도 있습니다. 트리거 이벤트와 함께 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)을 사용하는 모든 Campaign은 해당 이벤트의 커스텀 이벤트 속성정보를 메시징 개인화에 활용할 수 있습니다.

예를 들어, 게임 앱에서 레벨을 완료한 사용자에게 메시지를 보내려면 해당 레벨을 완료하는 데 걸린 시간에 대한 속성정보로 메시지를 더욱 개인화할 수 있습니다. 이 예시에서는 [조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/)을 사용하여 세 가지 다른 세그먼트에 대해 메시지를 개인화합니다. `time_spent`라는 커스텀 이벤트 속성정보는 ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``를 호출하여 메시지에 포함할 수 있습니다.

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
사용자에게 인터넷 연결이 없는 경우, 템플릿화된 커스텀 이벤트 속성정보(예: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %})가 포함된 트리거된 인앱 메시지는 실패하여 표시되지 않습니다.
{% endalert %}

인앱 메시지를 템플릿화된 인앱 메시지로 전달하게 하는 Liquid 태그의 전체 목록은 [자주 묻는 질문]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages/)을 참조하세요.

#### 필터 관련 고려 사항 {#considerations-with-filters}

- **API 호출:** API 호출을 하고 "is blank" 필터를 사용할 때, 커스텀 이벤트 속성정보가 호출에서 제외되면 "blank"로 간주됩니다. 예를 들어, `"event_property": ""`를 포함하면 사용자는 "not blank"로 간주됩니다.
- **정수:** 숫자 커스텀 이벤트 속성정보로 필터링할 때 숫자가 매우 큰 경우 "exactly" 필터를 사용하지 마세요. 숫자가 너무 크면 특정 길이에서 반올림될 수 있어 필터가 예상대로 작동하지 않을 수 있습니다.

### 세분화 {#segmentation}

이벤트 속성정보 세분화를 사용하여 수행된 커스텀 이벤트와 해당 이벤트에 연결된 속성정보를 기반으로 사용자를 타겟팅할 수 있습니다. 이를 통해 구매 및 커스텀 이벤트별 세분화 시 필터링 옵션이 확장됩니다.

커스텀 이벤트의 이벤트 속성정보는 이를 사용하는 모든 Segment에 대해 실시간으로 업데이트됩니다. **데이터 설정** > **커스텀 이벤트**로 이동하여 관련 커스텀 이벤트에 대해 **속성정보 관리**를 선택하면 속성정보를 관리할 수 있습니다. 특정 Segment 필터에서 사용되는 커스텀 이벤트 속성정보는 최대 30일의 조회 기록을 가집니다.

#### 세분화를 위한 이벤트 속성정보 추가 {#adding-event-properties-for-segmentation}

이벤트 속성정보 빈도 및 최근성을 기반으로 Segment를 생성하려면 "Edit Custom Event Property Segmentation" [사용자 권한]({{site.baseurl}}/user_guide/data/infrastructure/data_points/#viewing-data-point-usage)이 필요합니다.

기본적으로 워크스페이스당 20개의 세분화 가능한 이벤트 속성정보를 사용할 수 있습니다. 이 제한을 늘리려면 Braze 계정 매니저에게 문의하세요.

세분화를 위한 이벤트 속성정보를 추가하려면 다음을 수행하세요:

1. 커스텀 이벤트로 이동하여 **속성정보 관리**를 선택합니다.
2. **세분화 활성화** 토글을 선택하여 세분화를 위한 이벤트 속성정보를 추가합니다. 세분화 시 추가 필터링 옵션에 접근할 수 있습니다.

이벤트 속성정보 세분화 필터에는 다음이 포함됩니다:

- 지난 Y일 동안 속성정보 A의 값이 B인 커스텀 이벤트를 X회 수행한 경우.
- 지난 Y일 동안 속성정보 A의 값이 B인 구매를 X회 한 경우.
- 1일에서 30일 범위 내에서 세분화하는 기능을 추가합니다.

![속성정보 'number of items'가 2이고 값이 지난 30 캘린더 일 동안 1회 이상인 'Abandoned Cart' 필터 그룹.]({% image_buster /assets/img/nested_object3.png %})

데이터는 해당 이벤트 속성정보를 활성화한 후에만 기록되며, 이벤트 속성정보는 해당 날짜 이후부터만 사용할 수 있습니다.

#### 데이터 포인트 {#data-points}

구독 사용량과 관련하여, 다음 필터로 세분화가 활성화된 커스텀 이벤트 속성정보는 커스텀 이벤트 자체에서 계산되는 데이터 포인트 외에 별도의 데이터 포인트로 각각 계산됩니다:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas 진입 속성정보 및 이벤트 속성정보 {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### 중첩 오브젝트 {#nested-objects}

중첩 오브젝트(다른 오브젝트 내부의 오브젝트)를 사용하여 커스텀 이벤트 및 구매의 속성정보로 중첩된 JSON 데이터를 전송할 수 있습니다. 이 중첩 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하며, 사용자를 세분화하는 데 사용할 수 있습니다.

자세한 내용은 [중첩 오브젝트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/) 전용 페이지를 참조하세요.

## 커스텀 이벤트 속성정보 저장 {#custom-event-property-storage}

커스텀 이벤트 속성정보는 타겟팅 정밀도를 높이고 메시지를 더욱 개인화된 느낌으로 만들 수 있도록 설계되었습니다. 커스텀 이벤트 속성정보는 Braze 내에서 단기 및 장기 모두 저장할 수 있습니다.

이벤트 속성정보 값을 기반으로 세분화하는 방법은 두 가지가 있습니다:

1. **30일 이내:** Braze Segments 내에서 특정 이벤트 속성정보 값의 빈도 및 최근성을 기반으로 이벤트 속성정보 세분화를 사용할 수 있습니다. 이 옵션은 데이터 사용량에 영향을 미칩니다.<br><br>
2. **30일 이내 및 이후:** 단기 및 장기 이벤트 속성정보 세분화를 모두 다루려면 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)을 사용할 수 있습니다. 이 기능은 지난 2년 동안 추적된 커스텀 이벤트 및 이벤트 속성정보를 기반으로 사용자를 세분화합니다. 이 옵션은 데이터 사용량에 영향을 미치지 않습니다.

특정 요구 사항에 따른 최적의 접근 방식에 대한 권장 사항은 Braze 고객 성공 매니저에게 문의하세요.