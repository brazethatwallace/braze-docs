---
nav_title: 영구 진입 속성
article_title: 영구 진입 속성
alias: "/persistent_entry/"
page_type: reference
description: "이 참조 문서에서는 Canvas에서 영구 진입 속성을 사용하여 더 큐레이트된 메시지를 보내고, 고도로 세분화된 최종 사용자 경험을 만드는 방법을 설명합니다."
tool: Canvas
page_order: 5
---

# 영구 진입 속성 {#persistent-entry-properties}

> Canvas가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거되면, API 호출, 커스텀 이벤트 또는 구매 이벤트의 메타데이터를 Canvas 워크플로의 각 단계에서 개인화에 사용할 수 있습니다. 이러한 속성정보를 사용하여 더 큐레이트된 메시지를 보낼 수 있습니다.

{% alert important %}
영구 진입 속성은 원래 Canvas 편집기의 산물이므로, Canvas 진입 속성과 같은 용어에 대한 더 이상 사용되지 않는 참조가 역사적 참고를 위해 남아 있습니다. 현재 Canvas 편집기에 대해서는 [컨텍스트 및 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)를 참조하세요.<br><br>현재 Canvas 편집기에서 영구 진입 속성을 사용하려면 새 Canvas를 생성하거나 기존 Canvas를 현재 편집기로 [복제]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)해야 합니다.
{% endalert %}

## 진입 속성 사용 {#using-entry-properties}

진입 속성은 액션 기반 및 API 트리거 Canvases에서 사용할 수 있습니다. 이러한 진입 속성은 Canvas가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거될 때 정의됩니다. 자세한 내용은 다음 문서를 참조하세요:

- [Canvas 진입 속성정보 오브젝트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [이벤트 속성정보 오브젝트]({{site.baseurl}}/api/objects_filters/event_object)
- [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-product-id)

이러한 오브젝트에서 전달된 속성정보는 `canvas_entry_properties` Liquid 태그를 사용하여 참조할 수 있습니다. 예를 들어, `"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}`가 포함된 요청은 Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}를 추가하여 메시지에 "shoes"라는 단어를 추가할 수 있습니다.

Canvas에 `canvas_entry_properties` Liquid 태그가 포함된 메시지가 있으면, 해당 속성정보에 연결된 값은 사용자가 Canvas에서 여정을 진행하는 동안 저장되며, 사용자가 Canvas를 종료하면 삭제됩니다. Canvas 진입 속성은 Liquid에서의 참조에만 사용할 수 있습니다. Canvas 내에서 속성정보를 기준으로 필터링하려면 대신 [이벤트 속성정보 세분화]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 사용하세요.

{% alert note %}
Canvas 진입 속성정보 오브젝트의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 진입 속성을 사용하도록 Canvas 업데이트 {#updating-canvas-to-use-entry-properties}

이전에 `canvas_entry_properties`를 사용하는 메시지가 포함되지 않았던 활성 Canvas를 편집하여 `canvas_entry_properties`를 포함하도록 변경하면, `canvas_entry_properties`가 Canvas에 추가되기 전에 Canvas에 진입한 사용자에게는 해당 속성정보에 대응하는 값을 사용할 수 없습니다. 값은 변경이 이루어진 후 Canvas에 진입한 사용자에 대해서만 저장됩니다.

예를 들어, 11월 3일에 진입 속성을 사용하지 않는 Canvas를 처음 시작한 후 11월 11일에 Canvas에 새 속성정보 `product_name`을 추가한 경우, `product_name`의 값은 11월 11일 이후에 Canvas에 진입한 사용자에 대해서만 저장됩니다.

Canvas 진입 속성정보가 null이거나 비어 있는 경우, 조건문을 사용하여 메시지를 중단할 수 있습니다. 다음 코드 스니펫은 Liquid를 사용하여 메시지를 중단하는 방법의 예시입니다.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Liquid를 사용한 메시지 중단에 대해 자세히 알아보려면 [Liquid 설명서]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)를 확인하세요.

## 글로벌 Canvas 진입 속성 {#global-canvas-entry-properties}

`canvas_entry_properties`를 사용하면 모든 사용자에게 적용되는 글로벌 속성정보 또는 지정된 사용자에게만 적용되는 사용자별 속성정보를 설정할 수 있습니다. 사용자별 속성정보는 해당 사용자에 대해 글로벌 속성정보를 대체합니다.

### 요청 예시 {#example-request}

```bash
curl -X POST \
-H 'Content-Type: application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
      "canvas_entry_properties": {
        "food_allergies": "none"
      },
      "recipients": [
        {
          "external_user_id": "Customer_123",
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }'
```

이 요청에서 "food allergies"의 글로벌 값은 "none"입니다. Customer_123의 경우 값은 "dairy"입니다. 이 Canvas에서 Liquid 스니펫 {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%}이 포함된 메시지는 Customer_123에게는 "dairy"로, 다른 모든 사용자에게는 "none"으로 템플릿됩니다.

## 사용 사례 {#use-case}

사용자가 이커머스 사이트에서 상품을 탐색했지만 장바구니에 추가하지 않았을 때 트리거되는 Canvas가 있다면, Canvas의 첫 번째 단계는 해당 상품 구매에 관심이 있는지 묻는 푸시 알림일 수 있습니다. {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}를 사용하여 제품 이름을 참조할 수 있습니다.

![사용자가 이커머스 사이트에서 상품을 탐색했지만 장바구니에 추가하지 않았을 때 트리거되는 Canvas가 있는 경우, 첫 번째 단계는 해당 상품 구매에 관심이 있는지 묻는 푸시 알림일 수 있습니다. {% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}을 사용하여 제품 이름을 참조할 수 있습니다.]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

두 번째 단계에서는 사용자가 상품을 장바구니에 추가했지만 아직 구매하지 않은 경우 결제를 유도하는 또 다른 푸시 알림을 보낼 수 있습니다. {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}를 사용하여 `product_name` 진입 속성정보를 계속 참조할 수 있습니다.

![사용 사례와 관련된 스크린샷.]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}