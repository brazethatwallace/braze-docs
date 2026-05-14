---
nav_title: 캔버스 진입 등록정보
article_title: 캔버스 진입 등록정보
page_order: 4
description: "메시지에서 캔버스 진입 등록정보를 개인화 소스로 사용하는 방법을 알아보세요."
---

# 캔버스 진입 등록정보

> 캔버스가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거되면, 해당 트리거의 메타데이터를 사용하여 캔버스 워크플로 전체에서 메시지를 개인화할 수 있습니다. 이러한 값을 진입 등록정보라고 하며, 캔버스의 모든 단계에서 유지됩니다.

## 작동 방식

{% raw %}
진입 등록정보는 `{{context.${property_name}}}` Liquid 태그를 통해 사용할 수 있습니다. 사용자가 캔버스에 진입하면 Braze가 트리거 이벤트 또는 API 호출의 등록정보를 캡처하며, 이후 모든 캔버스 단계에서 해당 등록정보를 참조할 수 있습니다.

예를 들어, `product_name` 등록정보가 포함된 `completed_order` 이벤트에 의해 캔버스가 트리거된 경우:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

진입 등록정보는 액션 기반 및 API 트리거 캔버스에서 사용할 수 있습니다.

## 영구 진입 등록정보

영구 진입 등록정보를 사용하면 지연 후에 발생하는 단계를 포함하여 캔버스의 모든 단계에서 원래 진입 데이터를 참조할 수 있습니다. 영구 등록정보가 없으면 진입 등록정보는 첫 번째 단계에서만 사용할 수 있습니다.

{% alert important %}
영구 진입 등록정보는 기존 캔버스 진입 등록정보 워크플로의 일부입니다. 현재 업데이트된 캔버스 편집기에 대해서는 [컨텍스트 및 이벤트 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)를 참조하세요.
{% endalert %}

영구 진입 등록정보에 대한 전체 참조는 [영구 진입 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/)를 확인하세요.