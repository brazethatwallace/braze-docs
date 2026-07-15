---
nav_title: 사용자 업데이트
article_title: 사용자 업데이트
alias: "/user_update/"
page_order: 12
page_type: reference
description: "이 참조 문서에서는 사용자 업데이트 구성요소와 Canvases에서 이를 사용하는 방법을 다룹니다."
tool: Canvas
---

# 사용자 업데이트 {#user-update}

> 사용자 업데이트 구성요소를 사용하면 JSON 편집기에서 사용자의 속성, 이벤트, 구매를 업데이트할 수 있으므로 API 키와 같은 민감한 정보를 포함할 필요가 없습니다.

## 이 구성요소의 작동 방식 {#how-this-component-works}

!["로열티 업데이트"라는 이름의 사용자 업데이트 단계로, "Is Premium Member" 속성을 "true"로 업데이트합니다.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Canvas에서 이 구성요소를 사용하면 업데이트가 분당 `/users/track` 요청 사용량 제한에 포함되지 않습니다. 대신 이러한 업데이트는 일괄 처리되어 Braze가 Braze-to-Braze 웹훅보다 더 효율적으로 처리할 수 있습니다. 이 구성요소는 비과금 데이터 포인트(예: 구독 그룹)를 업데이트하는 데 사용될 때 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)를 기록하지 않습니다.

사용자가 사용자 업데이트 단계에 진입하고 처리가 완료되면 다음 단계로 진행합니다. 즉, 이러한 사용자 업데이트에 의존하는 후속 메시징은 다음 단계가 실행될 때 최신 상태입니다.

## 사용자 업데이트 생성 {#creating-a-user-update}

사이드바에서 구성요소를 드래그 앤 드롭하거나, 배리언트 또는 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 다음 **사용자 업데이트**를 선택합니다.

기존 고객 프로필 정보를 업데이트하거나, 새 정보를 추가하거나, 고객 프로필 정보를 제거할 수 있는 세 가지 옵션이 있습니다. 워크스페이스의 모든 사용자 업데이트 단계를 합산하면 분당 최대 200,000개의 고객 프로필을 업데이트할 수 있습니다.

{% alert tip %}
사용자를 검색하고 변경 사항을 적용하여 이 구성요소로 수행한 변경 사항을 테스트할 수도 있습니다. 이렇게 하면 해당 사용자가 업데이트됩니다.
{% endalert %}

## 커스텀 속성 업데이트 {#updating-custom-attributes}

커스텀 속성을 업데이트하거나 제거하려면 속성 목록에서 속성 이름을 선택하고 값을 입력합니다.

!["Loyalty Member"와 "Loyalty Program" 두 속성을 "true"로 업데이트하는 사용자 업데이트 단계.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## 커스텀 속성 제거 {#removing-custom-attributes}

커스텀 속성을 제거하려면 드롭다운을 사용하여 속성 이름을 선택합니다. [고급 JSON 편집기](#advanced-json-editor)로 전환하여 추가 편집할 수 있습니다.

!["Loyalty Member" 속성을 제거하는 사용자 업데이트 단계.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### 값 증가 및 감소 {#increasing-and-decreasing-values}

사용자 업데이트 단계에서 속성 값을 증가시키거나 감소시킬 수 있습니다. 속성을 선택하고 **Increment By** 또는 **Decrement By**를 선택한 다음 숫자를 입력합니다.

#### 주간 진행 상황 추적 {#track-weekly-progress}

이벤트를 추적하는 커스텀 속성을 증가시키면 사용자가 일주일 동안 수강한 수업 수를 추적할 수 있습니다. 이 구성요소를 사용하면 주 시작 시 수업 횟수를 초기화하고 다시 추적을 시작할 수 있습니다.

!["class_count" 속성을 1만큼 증가시키는 사용자 업데이트 단계.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### 오브젝트 배열 업데이트 {#updating-an-array-of-objects}

[오브젝트 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)은 고객 프로필에 저장되는 데이터가 풍부한 커스텀 속성입니다. 이를 사용하여 사용자와 브랜드 간의 상호작용 기록을 생성하고, 구매 내역이나 총 생애주기 가치와 같은 계산된 필드를 기반으로 세그먼트를 만들 수 있습니다.

**Advanced JSON Editor** 옵션을 사용하면 JSON을 삽입하여 이 오브젝트 배열에 항목을 추가하거나 제거할 수 있습니다.

#### 사용 사례: 사용자의 위시리스트 업데이트 {#use-case-updating-a-users-wishlist}

사용자의 위시리스트를 추적하여 저장된 항목을 기반으로 세그먼트를 만들거나 개인화할 수 있습니다.

1. 오브젝트 배열인 커스텀 속성을 생성합니다(예: `wishlist`). 각 오브젝트에는 `product_id`, `product_name`, `added_at`과 같은 필드가 포함될 수 있습니다.
2. 사용자 업데이트 단계에서 **Advanced JSON Editor**를 선택합니다. 그런 다음 **작성** 섹션에서 `$add` 연산을 사용하여 항목을 추가하거나 `$remove` 연산을 사용하여 값으로 항목을 제거합니다.

다음은 위시리스트에 항목을 추가하는 예시입니다:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

항목을 제거하려면 동일한 오브젝트 구조로 `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }`를 사용하여 Braze가 일치하는 항목을 찾아 제거할 수 있도록 합니다.

#### 사용 사례: 장바구니 합계 계산 {#use-case-calculating-the-shopping-cart-total}

사용자의 장바구니에 항목이 있을 때, 새 항목을 추가하거나 제거할 때, 그리고 총 장바구니 금액이 얼마인지 추적합니다.

1. `shopping_cart`라는 커스텀 오브젝트 배열을 생성합니다. 다음 예시는 이 속성이 어떻게 보일 수 있는지 보여줍니다. 각 항목에는 `price`를 포함한 자체 중첩 오브젝트 배열에 추가 데이터가 있는 고유한 `product_id`가 있습니다.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. 사용자가 장바구니에 항목을 추가할 때 기록되는 `add_item_to_cart`라는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 생성합니다.
3. 이 커스텀 이벤트를 수행하는 사용자를 타겟으로 하는 Canvas를 생성합니다. 이제 사용자가 장바구니에 항목을 추가하면 이 Canvas가 트리거됩니다. 그런 다음 해당 사용자에게 직접 메시지를 보내 특정 금액에 도달했을 때 쿠폰 코드를 제공하거나, 일정 시간 동안 장바구니를 방치했을 때, 또는 사용 사례에 맞는 다른 상황에서 메시지를 보낼 수 있습니다.

`shopping_cart` 속성은 모든 항목의 총 비용, 장바구니의 총 항목 수, 장바구니에 선물이 포함되어 있는지 여부 등 여러 커스텀 이벤트의 합계를 담고 있습니다. 이는 다음과 같이 보일 수 있습니다:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Canvas 진입 등록정보를 속성으로 설정 {#setting-canvas-entry-property-as-an-attribute}

사용자 업데이트 단계를 사용하여 `canvas_entry_property`를 유지할 수 있습니다. 장바구니에 항목이 추가될 때 트리거되는 이벤트가 있다고 가정해 보겠습니다. 장바구니에 가장 최근에 추가된 항목의 ID를 저장하고 리마케팅 Campaign에 사용할 수 있습니다. 개인화 기능을 사용하여 Canvas 진입 등록정보를 검색하고 속성에 저장합니다.

![항목 ID로 "most_recent_cart_item" 속성을 업데이트하는 사용자 업데이트 단계.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### 개인화 {#personalization}

Canvas의 트리거 이벤트 등록정보를 속성으로 저장하려면 개인화 모달을 사용하여 Canvas 진입 등록정보를 추출하고 저장합니다. 사용자 업데이트는 다음 개인화 기능도 지원합니다:

* [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [진입 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Liquid 로직([메시지 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) 포함)
* 오브젝트당 다중 속성 또는 이벤트 업데이트

{% alert warning %}
사용자 업데이트 단계에서 연결된 콘텐츠 Liquid 개인화를 사용할 때는 주의하는 것이 좋습니다. 이 단계 유형은 분당 200,000건의 요청 사용량 제한이 있습니다. 이 사용량 제한은 Canvas 사용량 제한보다 우선 적용됩니다.
{% endalert %}

## 고급 JSON 편집기 {#advanced-json-editor}

JSON 편집기에 최대 65,536자의 속성, 이벤트 또는 구매 JSON 오브젝트를 추가할 수 있습니다. 사용자의 [글로벌 구독]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) 및 [구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) 상태도 설정할 수 있습니다.

![JSON 편집기에 최대 65,536자의 속성, 이벤트 또는 구매 JSON 오브젝트를 추가합니다. 사용자의 글로벌 구독 및 구독 그룹 상태도 설정할 수 있습니다.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

JSON 편집기를 사용하면 **미리보기 및 테스트** 탭에서 고객 프로필이 변경 사항으로 업데이트되는지 미리보기하고 테스트할 수도 있습니다. 랜덤 사용자를 선택하거나 특정 사용자를 검색할 수 있습니다. 그런 다음 사용자에게 테스트를 보낸 후 생성된 링크를 사용하여 고객 프로필을 확인합니다.

![JSON 편집기를 사용하여 미리보기 및 테스트 탭에서 고객 프로필이 변경 사항으로 업데이트되는지 미리보기하고 테스트할 수 있습니다. 랜덤 사용자를 선택하거나 특정 사용자를 검색할 수 있습니다. 그런 다음 사용자에게 테스트를 보낸 후 생성된 링크를 사용하여 고객 프로필을 확인합니다.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 고려 사항 {#considerations}

JSON 편집기를 사용할 때 API 키와 같은 민감한 데이터를 포함할 필요가 없습니다. 이는 플랫폼에서 자동으로 제공됩니다. 다음 필드는 JSON 편집기에 포함하지 않아야 합니다:
* 외부 사용자 ID
* API 키
* Braze 클러스터 URL
* 푸시 토큰 가져오기 관련 필드

{% alert important %}
Canvas 등록정보(예: `canvas_id`, `canvas_name`, `canvas_variant_name` Liquid 태그)는 사용자 업데이트 단계에서 지원되지 않습니다.
{% endalert %}

{% raw %}
### 커스텀 이벤트 기록 {#log-custom-events}

JSON 편집기를 사용하여 커스텀 이벤트를 기록할 수도 있습니다. 이를 위해서는 ISO 형식의 타임스탬프가 필요하므로 시작 부분에서 Liquid로 시간과 날짜를 할당해야 합니다. 다음은 시간과 함께 이벤트를 기록하는 예시입니다.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

다음 예시는 선택적 등록정보와 `app_id`를 포함한 커스텀 이벤트를 사용하여 이벤트를 특정 앱에 연결합니다.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### 구독 상태 편집 {#edit-subscription-state}

JSON 편집기 내에서 사용자의 구독 상태를 편집할 수도 있습니다. 예를 들어, 다음은 사용자의 구독 상태를 `opted_in`으로 업데이트하는 예시입니다.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### 구독 그룹 업데이트 {#update-subscription-groups}

이 캔버스 단계를 사용하여 구독 그룹을 업데이트할 수도 있습니다. 다음 예시는 하나 이상의 구독 그룹을 업데이트하는 방법을 보여줍니다.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}