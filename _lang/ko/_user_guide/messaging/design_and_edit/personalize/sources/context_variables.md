---
nav_title: 컨텍스트 변수
article_title: 컨텍스트 변수
page_type: reference
description: "이 참조 문서에서는 BRAZE 캔버스의 컨텍스트 변수에 대해 유형, 사용법, 모범 사례를 포함하여 설명합니다."
---

# 컨텍스트 변수 {#context-variables}

> 컨텍스트 변수는 특정 Canvas를 통한 사용자 여정 내에서 생성하고 사용할 수 있는 임시 데이터입니다. 컨텍스트 변수를 사용하면 사용자의 프로필 정보를 영구적으로 변경하지 않고도 지연을 개인화하고, 사용자를 동적으로 세그먼트하며, 메시징을 풍부하게 만들 수 있습니다. 컨텍스트 변수는 Canvas 세션 내에서만 존재하며, 다른 Canvas나 세션 외부에서는 유지되지 않습니다.

## 컨텍스트 변수의 작동 방식 {#how-context-variables-work}

컨텍스트 변수는 두 가지 방법으로 설정할 수 있습니다:

- **Canvas 진입 시:** 사용자가 Canvas에 진입하면 이벤트 또는 API 트리거의 데이터가 자동으로 컨텍스트 변수를 채울 수 있습니다.
- **컨텍스트 단계에서:** [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 추가하여 Canvas 내에서 컨텍스트 변수를 수동으로 정의하거나 업데이트할 수 있습니다.

각 컨텍스트 변수에는 다음이 포함됩니다:

- 이름(예: `flight_time` 또는 `subscription_renewal_date`)
- 데이터 유형(예: 숫자, 문자열, 시간 또는 배열)
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 또는 **개인화 추가** 도구를 통해 할당하는 값

정의된 후에는 다음 형식으로 참조하여 Canvas 전체에서 컨텍스트 변수를 사용할 수 있습니다: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

예를 들어, {% raw %}`{{context.${flight_time}}}`{% endraw %}은 사용자의 예정된 비행 시간을 반환할 수 있습니다.

사용자가 Canvas에 진입할 때마다(이전에 진입한 적이 있더라도) 컨텍스트 변수는 최신 진입 데이터와 Canvas 설정에 따라 재정의됩니다. 이 상태 기반 접근 방식을 통해 각 Canvas 진입은 자체적인 독립 컨텍스트를 유지할 수 있으며, 사용자가 동일한 여정 내에서 여러 활성 상태를 가지면서도 각 상태에 대한 특정 컨텍스트를 유지할 수 있습니다.

예를 들어, 고객에게 예정된 항공편이 두 개 있는 경우 두 개의 별도 여정 상태가 동시에 실행되며, 각각 출발 시간과 목적지와 같은 고유한 항공편별 컨텍스트 변수를 갖습니다. 이를 통해 뉴욕행 오후 2시 항공편에 대한 개인화된 알림을 보내는 동시에 내일 로스앤젤레스행 오전 8시 항공편에 대한 다른 업데이트를 보낼 수 있어, 각 메시지가 특정 예약과 관련성을 유지합니다.

## 고려 사항 {#considerations}

[컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)당 최대 10개의 컨텍스트 변수를 정의할 수 있습니다. 각 변수 이름은 최대 100자이며 문자, 숫자 또는 밑줄만 사용해야 합니다.

컨텍스트 변수 정의는 최대 10,240자까지 가능합니다. API 트리거 Canvas에 컨텍스트 변수를 전달하는 경우, 컨텍스트 단계에서 생성된 변수와 동일한 네임스페이스를 공유합니다. 예를 들어, [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) 컨텍스트 오브젝트에서 `purchased_item` 변수를 보내면 {% raw %}`{{context.${purchased_item}}}`{% endraw %}으로 참조할 수 있습니다. 컨텍스트 단계에서 해당 변수를 재정의하면 새 값이 해당 사용자 여정의 API 값을 덮어씁니다.

컨텍스트 단계당 최대 50KB를 저장할 수 있으며, 최대 10개의 변수에 분산됩니다. 단계의 모든 변수 총 크기가 50KB를 초과하면 한도를 초과하는 변수는 평가되거나 저장되지 않습니다. 예를 들어, 컨텍스트 단계에 세 개의 변수가 있는 경우:

- 변수 1: 30KB
- 변수 2: 19KB
- 변수 3: 2KB

변수 3은 이전 변수의 합계가 50KB를 초과하므로 평가되거나 저장되지 않습니다.

## 데이터 유형 {#data-types}

단계에서 생성되거나 업데이트되는 컨텍스트 변수에는 다음 데이터 유형을 할당할 수 있습니다.

{% alert note %}
컨텍스트 변수는 [이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format)와 동일한 데이터 유형 예상 형식을 갖습니다. <br><br>배열 유형을 사용할 때 Braze는 값을 JSON으로 구문 분석하려고 시도하며, 이를 통해 오브젝트 배열을 성공적으로 생성할 수 있습니다. 배열 내의 오브젝트가 유효한 JSON이 아닌 경우 결과는 단순 문자열 배열이 됩니다. <br><br>중첩 오브젝트 및 오브젝트 배열의 경우 [`as_json_string` Liquid 필터](#converting-connected-content-strings-to-json)를 사용하세요. 컨텍스트 단계에서 동일한 오브젝트를 생성하는 경우 `as_json_string`을 사용하여 오브젝트를 렌더링해야 합니다. 예: {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| 데이터 유형 | 예시 변수 이름 | 예시 값 |
|---|---|---|
| 부울 | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| 숫자 | credit_score |{% raw %}<code>740</code>{% endraw %}|
| 문자열 | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| 배열 | favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| 배열(오브젝트) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| 시간(UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| 오브젝트(평탄화) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 유형" }

기본적으로 시간 데이터 유형은 UTC입니다. 문자열 데이터 유형을 사용하여 시간 값을 저장하면 PST와 같은 다른 시간대로 시간을 정의할 수 있습니다.

예를 들어, 사용자의 생일 전날에 메시지를 보내는 경우 전날 발송과 관련된 Liquid 로직이 있으므로 컨텍스트 변수를 시간 데이터 유형으로 저장합니다. 그러나 크리스마스(12월 25일)에 휴일 메시지를 보내는 경우 시간을 동적 변수로 참조할 필요가 없으므로 문자열 데이터 유형을 사용하는 것이 좋습니다.

오브젝트 데이터 유형의 경우 점 표기법을 사용하여 데이터 경로를 지정할 수 있습니다. 예를 들어, 컨텍스트 단계에서 다음 구조의 컨텍스트 변수 `order_summary`를 정의하는 경우:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

[오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 또는 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 필터에서 점 표기법을 사용하여 컨텍스트 변수 이름으로 경로를 입력합니다(예: `order_summary.shipping.carrier`). 필터가 평가되면 Braze는 해당 경로를 `overnight` 값으로 확인합니다.

Liquid에서([메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) 단계 등) 대신 {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}를 사용합니다.

## 컨텍스트 변수 사용 {#using-context-variables}

Canvas에서 Liquid를 사용하는 모든 곳에서 컨텍스트 변수를 사용할 수 있습니다. 예를 들어 [메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) 및 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계에서 **개인화 추가**를 선택하여 사용할 수 있습니다. 메시지 단계의 인앱 메시지 및 배너의 경우 컨텍스트 변수를 선택하여 메시지 만료 시점을 결정할 수 있습니다.

예를 들어, 승객에게 다가오는 항공편 전에 VIP 라운지 이용 권한에 대해 알리고 싶다고 가정해 보겠습니다. 이 메시지는 퍼스트 클래스 티켓을 구매한 승객에게만 발송되어야 합니다. 컨텍스트 변수는 이 정보를 추적하는 유연한 방법입니다.

사용자는 비행기 티켓을 구매할 때 Canvas에 진입합니다. 라운지 이용 자격을 결정하기 위해 컨텍스트 단계에서 `lounge_access_granted`라는 컨텍스트 변수를 생성한 다음, 사용자 여정의 후속 단계에서 해당 컨텍스트 변수를 참조합니다.

![승객이 VIP 라운지 이용 자격이 있는지 추적하도록 설정된 컨텍스트 변수.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

이 컨텍스트 단계에서는 {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}를 사용하여 구매한 항공편 유형이 `first_class`인지 확인합니다.

다음으로, {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %}가 `true`인 사용자를 타겟으로 하는 메시지 단계를 생성합니다. 이 메시지는 개인화된 라운지 정보가 포함된 푸시 알림입니다. 이 컨텍스트 변수를 기반으로 자격이 있는 승객은 항공편 전에 관련 메시지를 받게 됩니다.

- 퍼스트 클래스 티켓 승객은 다음을 받습니다: "독점 VIP 라운지 이용을 즐기세요!"
- 비즈니스 및 이코노미 티켓 승객은 다음을 받습니다: "독점 VIP 라운지 이용을 위해 항공편을 업그레이드하세요."

![구매한 비행기 티켓 유형에 따라 다른 메시지를 보내는 메시지 단계.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
컨텍스트 단계의 정보를 사용하여 [개인화된 지연 옵션]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays)을 추가할 수 있습니다. 즉, 사용자를 지연시키는 변수를 선택할 수 있습니다.
{% endalert %}

### 작업 경로 및 종료 기준 {#for-action-paths-and-exit-criteria}

다음 트리거 동작에서 속성정보 필터를 컨텍스트 변수 또는 커스텀 속성과 비교할 수 있습니다: **커스텀 이벤트 수행** 및 **구매하기**. 이러한 동작 트리거는 기본 및 중첩 속성정보 모두에 대한 속성정보 필터도 지원합니다.

- 기본 속성정보와 비교할 때 사용 가능한 비교는 커스텀 이벤트에서 정의한 속성정보 유형과 일치합니다. 예를 들어, 문자열 속성정보는 정확히 일치, 정규식 일치가 있습니다. 부울 속성정보는 참 또는 거짓입니다.
- 중첩 속성정보와 비교할 때 유형은 사전 정의되지 않으므로 중첩 커스텀 속성의 비교와 유사하게 부울, 숫자, 문자열, 시간 및 연중 일자에 대해 여러 데이터 유형에 걸쳐 비교를 선택할 수 있습니다. 비교 시점에 중첩 속성정보의 실제 데이터 유형과 일치하지 않는 데이터 유형을 선택하면 사용자가 작업 경로 또는 종료 기준과 일치하지 않습니다.

#### 작업 경로 예시 {#action-path-examples}

{% alert important %}
커스텀 속성 비교의 경우 동작이 수행되는 시점의 커스텀 속성 값을 사용합니다. 즉, 비교 시점에 사용자에게 이 커스텀 속성이 채워져 있지 않거나 커스텀 속성 값이 정의된 속성정보 비교와 일치하지 않으면 사용자는 작업 경로 그룹과 일치하지 않습니다. 사용자가 작업 경로 단계에 진입했을 때 일치했더라도 마찬가지입니다.
{% endalert %}

{% tabs %}
{% tab 커스텀 이벤트 수행 %}

다음 작업 경로는 기본 속성정보 `source`가 컨텍스트 변수 `app_source_variable`과 일치하는 커스텀 이벤트 `Account_Created`를 수행한 사용자를 분류하도록 설정되어 있습니다.

![커스텀 이벤트 수행 시 컨텍스트 변수를 참조하는 작업 경로 예시.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab 구매하기 %}

다음 작업 경로는 특정 제품 이름 `shoes`에 대한 기본 속성정보 `brand`를 컨텍스트 변수 `promoted_shoe_brand`와 일치시키도록 설정되어 있습니다.

![구매 시 컨텍스트 변수를 참조하는 작업 경로 예시.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 종료 기준 예시 {#exit-criteria-examples}

{% tabs %}
{% tab 커스텀 이벤트 수행 %}

종료 기준은 Canvas에서 사용자 여정의 어느 시점에서든 다음 조건을 충족하면 Canvas를 종료한다고 명시합니다:

- 커스텀 이벤트 **장바구니 포기**를 수행하고,
- 기본 속성정보 **장바구니 내 항목**이 컨텍스트 변수 `cart_item_threshold`의 문자열 값과 일치하는 경우.

![컨텍스트 변수를 기반으로 커스텀 이벤트를 수행하면 사용자를 종료시키도록 설정된 종료 기준.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab 구매하기 %}

종료 기준은 Canvas에서 사용자 여정의 어느 시점에서든 다음 조건을 충족하면 Canvas를 종료한다고 명시합니다:

- "book" 제품 이름에 대한 특정 구매를 하고,
- 해당 구매의 중첩 속성정보 "loyalty_program"이 사용자의 커스텀 속성 "VIP"와 같은 경우.

![구매 시 사용자를 종료시키도록 설정된 종료 기준.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### 만료 설정 {#set-an-expiration}

Canvas [메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) 단계의 [배너]({{site.baseurl}}/user_guide/channels/banners) 및 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)의 경우, 만료에 대해 **단계가 사용 가능한 후 기간**을 선택한 다음 **기간 개인화**를 켜서 컨텍스트 변수에서 가용성 기간을 설정합니다. 예를 들어, 컨텍스트 단계의 프로모션 또는 예약 기간과 일치시킬 수 있습니다.

**기간 개인화**는 해당 기간 기반 만료 옵션에 적용됩니다. 대신 **특정 날짜 및 시간에**를 선택하는 경우 날짜 및 시간 컨트롤을 사용하여 만료를 설정합니다.

### 작업 경로 지연 {#action-path-delays}

[작업 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) 단계에서 **평가 기간** 아래의 **지연 개인화**를 켜서 컨텍스트 변수에서 사용자가 단계에 머무는 시간을 설정합니다. 등급이나 지역과 같은 세부 정보에 따라 사용자별로 대기 기간이 달라야 할 때 사용합니다.

### 컨텍스트 변수 필터 {#context-variable-filters}

[오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 단계에서 이전에 선언된 컨텍스트 변수를 사용하는 필터를 생성할 수 있습니다.

{% alert note %}
컨텍스트 변수 필터는 오디언스 경로 및 결정 분할 단계에서만 사용할 수 있습니다.
{% endalert %}

컨텍스트 변수는 Canvas 범위 내에서만 선언되고 접근할 수 있으므로 Segments에서 참조할 수 없습니다. 컨텍스트 변수 필터는 오디언스 경로와 결정 분할 단계에서 유사하게 작동합니다. 오디언스 경로 단계는 여러 그룹을 나타내고, 결정 분할 단계는 이진 결정을 나타냅니다.

![컨텍스트 변수로 필터를 생성하는 옵션이 있는 결정 분할 단계 예시.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Canvas 컨텍스트 변수에 사전 정의된 유형이 있는 것과 마찬가지로, 컨텍스트 변수와 정적 값 간의 비교는 [일치하는 데이터 유형]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)이어야 합니다. 컨텍스트 변수 필터는 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)의 비교와 유사하게 부울, 숫자, 문자열, 시간 및 연중 일자에 대해 여러 데이터 유형에 걸쳐 비교를 허용합니다.

다음은 컨텍스트 변수 `product_name`을 정규식 `/braze/`와 비교하는 컨텍스트 변수 필터의 예시입니다.

![컨텍스트 변수 "product_name"이 정규식 "/braze/"와 일치하도록 설정된 필터.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### 날짜 컨텍스트 변수에 대한 연중 일자 및 시간 필터 {#day-of-year-and-time-filters-for-date-context-variables}

컨텍스트 변수에 **연중 일자** 또는 **시간** 비교 필터를 사용하려면:

1. 컨텍스트 변수를 캘린더 날짜(예: 2025년 10월 23일)로 설정하는 [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 추가합니다.
2. 컨텍스트 단계 뒤에 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계를 추가합니다.
3. 오디언스 경로 단계에서 해당 컨텍스트 변수를 기반으로 사용자를 분할하는 필터를 추가합니다.
4. **연중 일자** 또는 **시간** 카테고리에서 비교를 선택합니다.

컨텍스트 변수에 선언된 유형이 없는 경우 Braze는 **연중 일자** 및 **시간**을 포함한 사용 가능한 모든 비교 유형을 드롭다운에 표시합니다. 변수가 컨텍스트 단계에서 **시간** 유형으로 선언된 경우 **연중 일자** 및 **시간** 비교만 표시됩니다. 알려진 유형이 있는 다른 데이터 유형(예: 시간 유형의 중첩 커스텀 속성)의 경우 해당 유형에 적용되는 비교만 표시됩니다.

{% alert note %}
컨텍스트 변수와 비교에 동일한 데이터 유형을 사용하세요. 예를 들어, 컨텍스트 변수가 시간 데이터 유형인 경우 시간 비교("이전" 또는 "이후" 등)를 사용하세요. 일치하지 않는 데이터 유형(예: 시간 컨텍스트 변수에 문자열 비교)을 사용하면 예기치 않은 동작이 발생할 수 있습니다.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

#### 컨텍스트 변수 또는 커스텀 속성과 비교 {#comparing-to-context-variables-or-custom-attributes}

**컨텍스트 변수 또는 커스텀 속성과 비교** 토글을 선택하면 이전에 정의된 컨텍스트 변수 또는 사용자 커스텀 속성과 비교하는 컨텍스트 변수 필터를 구성할 수 있습니다. 이는 API 트리거 `context`와 같이 사용자별로 동적인 비교를 수행하거나 컨텍스트 변수에 걸쳐 정의된 복잡한 비교 로직을 압축하는 데 유용할 수 있습니다.

{% tabs %}
{% tab 예시 1 %}

동적 비활성 기간 후에 사용자에게 개인화된 리마인더를 보내고 싶다고 가정해 보겠습니다. 지난 3일 동안 앱에 로그인하지 않은 모든 사용자가 메시지를 받아야 합니다.

{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}로 정의된 컨텍스트 변수 `re_engagement_date`가 있습니다. `3 days`는 사용자의 커스텀 속성으로도 저장되는 가변적인 값일 수 있습니다. 따라서 `re_engagement_date`가 `last_login_date`(고객 프로필에 커스텀 속성으로 저장됨) 이후인 경우 메시지가 발송됩니다.

![컨텍스트 변수 "re_engagement_date"가 커스텀 속성 "last_login_date" 이후인 경우에 대한 개인화 유형으로 커스텀 속성이 설정된 필터.]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab 예시 2 %}

다음 필터는 컨텍스트 변수 `reminder_date`를 컨텍스트 변수 `appointment_deadline` 이전으로 비교합니다. 이를 통해 오디언스 경로 단계에서 사용자를 그룹화하여 예약 마감일 전에 추가 리마인더를 받아야 하는지 여부를 결정할 수 있습니다.

![컨텍스트 변수 "reminder_date"가 컨텍스트 변수 "appointment_deadline"에 대해 설정된 개인화 유형으로 컨텍스트 변수가 설정된 필터.]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## 시간대 일관성 표준화 {#time-zone-consistency-standardization}

타임스탬프 유형을 사용하는 대부분의 이벤트 속성정보는 Canvas에서 이미 UTC로 되어 있지만 일부 예외가 있습니다. Canvas 컨텍스트의 추가로 인해 동작 기반 Canvases의 모든 기본 타임스탬프 이벤트 속성정보가 일관되게 UTC로 표시됩니다. 이 변경은 캔버스 단계와 메시지를 편집할 때 보다 예측 가능하고 일관된 경험을 보장하기 위한 광범위한 노력의 일환입니다. 이 변경은 특정 Canvas가 컨텍스트 단계를 사용하는지 여부에 관계없이 모든 동작 기반 Canvases에 영향을 미칩니다.

{% alert important %}
모든 상황에서 타임스탬프가 원하는 시간대로 표시되도록 [Liquid time_zone 필터]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know)를 사용하는 것을 강력히 권장합니다. 예시는 [컨텍스트 단계 문서의 자주 묻는 질문]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example)을 참조하세요.
{% endalert %}

## 관련 문서 {#related-articles}

- [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Liquid를 사용한 개인화 및 동적 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)