---
nav_title: 재입고 알림
article_title: 재입고 알림 설정하기
page_order: 2
description: "카탈로그와 커스텀 이벤트를 사용하여 재입고 알림을 설정하는 방법을 알아보세요. 상품이 재입고되면 고객이 자동으로 알림을 받도록 구독할 수 있습니다."
---

# 재입고 알림 {#back-in-stock-notifications}

> 카탈로그와 커스텀 이벤트를 사용하여 재입고 알림을 설정하는 방법을 알아보세요. 상품이 재입고되면 고객이 자동으로 알림을 받도록 구독할 수 있습니다. 이 기능은 이미 알림 수신에 동의한 사용자에게만 적용됩니다.

## 작동 방식 {#how-it-works}

`product_clicked` 이벤트와 같은 커스텀 이벤트를 구독 이벤트로 설정할 수 있습니다. 이 이벤트에는 항목 ID(카탈로그 항목 ID)의 속성정보가 포함되어야 합니다. 카탈로그 이름을 포함하는 것을 권장하지만 필수는 아닙니다. 또한 재고 수량 필드의 이름을 제공해야 하며, 이 필드는 숫자 데이터 유형이어야 합니다.

사용자가 항목을 성공적으로 구독하려면 카탈로그 항목의 재고가 0이어야 합니다. 항목의 재고 수량이 0보다 클 경우, Braze는 해당 항목을 구독한 모든 사용자를 조회하고 Campaign 또는 Canvas를 트리거하는 데 사용할 수 있는 커스텀 이벤트를 전송합니다.

이벤트 속성정보는 사용자와 함께 전송되므로, 전송하는 Campaign 또는 Canvas에 항목 세부 정보를 템플릿으로 삽입할 수 있습니다.

## 재입고 알림 설정하기 {#setting-up-back-in-stock-notifications}

특정 카탈로그에서 재입고 알림을 설정하려면 다음 단계를 따르세요.

1. 카탈로그로 이동하여 **설정** 탭을 선택합니다.
2. **재입고** 토글을 선택합니다.
3. 글로벌 재입고 설정이 구성되지 않은 경우, 재입고 알림을 트리거하는 데 사용할 커스텀 이벤트와 속성정보를 설정하라는 메시지가 표시됩니다:
    <br> ![카탈로그 설정 서랍.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **대체 카탈로그** 커스텀 이벤트에 `catalog_name` 속성정보가 없는 경우 재입고 가입에 사용될 카탈로그입니다.
    - **가입용 커스텀 이벤트**는 사용자를 재입고 알림에 가입시키는 데 사용되는 Braze 커스텀 이벤트입니다. 이 이벤트가 발생하면 해당 이벤트를 수행한 사용자가 가입됩니다.
    - **탈퇴용 커스텀 이벤트**는 사용자를 재입고 알림에서 탈퇴시키는 데 사용되는 Braze 커스텀 이벤트입니다. 이 이벤트는 선택 사항입니다. 사용자가 이 이벤트를 수행하지 않으면 90일 후 또는 재입고 이벤트가 트리거될 때 중 먼저 발생하는 시점에 탈퇴됩니다.
    - **항목 ID 이벤트 속성정보**는 이 섹션 앞부분의 커스텀 이벤트에 있는 속성정보로, 재입고 가입 또는 탈퇴 대상 항목을 결정하는 데 사용됩니다. 커스텀 이벤트의 이 속성정보에는 카탈로그에 존재하는 항목 ID(`id`)가 포함되어야 합니다. 항목 ID는 대상 카탈로그에 저장된 `id` 데이터 유형과 일치하도록 문자열로 전송해야 합니다. 커스텀 이벤트에는 이 항목이 속한 카탈로그를 지정하는 `catalog_name` 속성정보도 포함되어야 합니다.

    - 다음 예시는 REST API를 통해 전송되는 샘플 커스텀 이벤트를 보여줍니다:

```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

Braze SDK를 사용하여 동일한 가입 이벤트를 추적하려면 다음 코드를 사용하세요:

{% tabs %}
{% tab 웹 SDK %}

```javascript
import { logCustomEvent } from "@braze/web-sdk";

logCustomEvent("subscription", {
  id: "shirt-xl",
  catalog_name: "on_sale_products",
  type: ["back_in_stock"]
});
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.logCustomEvent(
  name: "subscription",
  properties: [
    "id": "shirt-xl",
    "catalog_name": "on_sale_products",
    "type": ["back_in_stock"]
  ]
)
```

{% endtab %}
{% tab Android %}

```kotlin
Braze.getInstance(context).logCustomEvent(
  "subscription",
  BrazeProperties(
    JSONObject()
      .put("id", "shirt-xl")
      .put("catalog_name", "on_sale_products")
      .put("type", JSONArray().put("back_in_stock")),
  ),
)
```

{% endtab %}
{% endtabs %}

{% alert note %}
재입고 및 가격 인하 트리거는 동일한 이벤트를 사용하여 사용자를 알림에 가입시키므로, `type` 속성정보를 사용하여 동일한 이벤트에서 가격 인하와 재입고 알림을 모두 설정할 수 있습니다. `type` 속성정보는 반드시 배열이어야 합니다.
{% endalert %}

{: start="4"}
4. **저장**을 선택하고 카탈로그의 **설정** 페이지로 계속 진행합니다.
5. 알림 규칙을 설정합니다. 두 가지 옵션이 있습니다:
    - **가입한 모든 사용자에게 알림**은 항목이 재입고되었을 때 대기 중인 모든 고객에게 알림을 보냅니다.
    - **알림 제한 설정**은 10분마다 지정된 수의 고객에게 알림을 보냅니다. Braze는 알림을 보낼 고객이 더 이상 없거나 항목이 품절될 때까지 지정된 수의 고객에게 점진적으로 알림을 보냅니다. 알림 속도는 분당 10,000명의 사용자를 초과할 수 없습니다.
6. **카탈로그의 재고 필드**를 설정합니다. 이 카탈로그 필드는 항목이 품절인지 여부를 판단하는 데 사용됩니다. 이 필드는 숫자 유형이어야 합니다.
7. **설정 저장**을 선택합니다.

![재입고 기능이 켜진 카탈로그 설정. 알림 규칙은 10분마다 1,000명의 사용자에게 알림을 보내도록 설정되어 있습니다.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
이 설정의 알림 규칙은 방해금지 시간과 같은 Canvas 알림 설정을 대체하지 않습니다.
{% endalert %}

## Canvas에서 재입고 알림 사용하기 {#using-back-in-stock-notifications-in-a-canvas}

카탈로그에서 재입고 기능을 설정한 후, 다음 단계에 따라 Canvas에서 사용하세요.

1. 액션 기반 Canvas를 설정합니다.
2. 트리거로 **재입고**를 선택합니다.
3. 재입고 알림이 있는 카탈로그의 이름을 선택합니다.
4. 평소처럼 Canvas [설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)을 계속 진행합니다.

이제 아이템이 재입고되면 고객에게 알림을 보낼 수 있습니다.

### Liquid 사용하기 {#using-liquid}

재입고된 카탈로그 아이템에 대한 세부 정보를 템플릿으로 작성하려면 `context` Liquid 태그를 사용하여 `item_id`에 접근할 수 있습니다.

{%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%}를 사용하면 재입고된 아이템의 ID를 반환합니다. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%}는 업데이트 이전의 아이템 재고 값을 반환하고, {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%}는 업데이트 이후의 새로운 재고 값을 반환합니다.

메시지 상단에 Liquid 태그 {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%}를 사용한 다음, {%raw%}``{{ items[0].<field_name> }}``{%endraw%}를 사용하여 메시지 전체에서 해당 아이템에 대한 데이터에 접근하세요.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## 고려 사항 {#considerations}

- 사용자는 90일 동안만 가입 상태가 유지됩니다. 90일 이내에 해당 항목이 재입고되지 않으면 사용자의 가입이 해제됩니다.
- **모든 가입 사용자에게 알림** 알림 규칙을 사용하면, Braze는 10분 동안 100,000명의 사용자에게 알림을 보냅니다.
- Braze는 재입고 알림 트리거 대상으로 매일 최대 50,000개의 업데이트된 항목을 지원합니다. 주어진 시점에 최대 1억 개의 활성 가입을 보유할 수 있으며, 각 가입은 카탈로그 항목을 모니터링하도록 등록된 고객 프로필을 나타냅니다.