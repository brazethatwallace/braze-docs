---
nav_title: "트리거 등록정보 오브젝트"
article_title: API 트리거 등록정보 오브젝트
page_order: 11
page_type: reference
description: "이 참조 문서에서는 트리거 등록정보 오브젝트의 다양한 구성요소에 대해 설명합니다."
tool: Campaigns

---

# 트리거 등록정보 오브젝트 {#trigger-properties-object}

> API 트리거 전달로 Campaign을 발송하기 위해 엔드포인트 중 하나를 사용할 때, 메시지를 커스터마이즈하기 위한 키와 값의 맵을 제공할 수 있습니다.

`trigger_properties`에 오브젝트가 포함된 API 요청을 하면 해당 오브젝트의 값을 `api_trigger_properties` 네임스페이스 아래의 메시지 템플릿에서 참조할 수 있습니다. 예를 들어, 다음과 같은 요청은 {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}를 추가하여 메시지에 `"shoes"`라는 단어를 추가할 수 있습니다.

트리거 등록정보는 메시지에 템플릿으로 사용할 수 있지만, 기본적으로 고객 프로필에 자동으로 저장되지는 않습니다.

{% alert note %}
`trigger_properties` 오브젝트 및 {% raw %}`api_trigger_properties.${product_name}`{% endraw %} 구문은 Campaigns에서만 지원됩니다. Canvas의 API 트리거 요청에서 키와 값을 사용하여 메시지를 커스터마이즈하려면 [Canvas 진입 등록정보 오브젝트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 사용하세요. `trigger_properties` 오브젝트의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 오브젝트 본문 {#object-body}

`trigger_properties` 오브젝트는 문자열, 숫자, 불리언, 날짜, 오브젝트, 배열을 데이터 유형으로 지원합니다.

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"],
    "line_items": [
      {
        "sku": "WH-9000",
        "name": "Wireless Headphones",
        "quantity": 1,
        "pricing": {
          "amount": 79.99,
          "currency": "USD"
        }
      },
      {
        "sku": "RS-450",
        "name": "Running Shoes",
        "quantity": 2,
        "pricing": {
          "amount": 129.99,
          "currency": "USD"
        }
      }
    ]
  }
}
```

## Liquid 템플릿 예제 {#liquid-templating-examples}

`api_trigger_properties` 네임스페이스를 사용하여 메시지 템플릿에서 트리거 속성을 참조할 수 있습니다.

- 문자열: {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}는 `"shoes"`를 반환합니다
- 숫자: {% raw %}`{{api_trigger_properties.${product_price}}}`{% endraw %}는 `79.99`를 반환합니다
- 중첩 오브젝트: {% raw %}`{{api_trigger_properties.${details}.${color}}}`{% endraw %}는 `"red"`를 반환합니다
- 배열 요소: {% raw %}`{{api_trigger_properties.${related_skus}[0]}}`{% endraw %}는 `"123"`을 반환합니다
- 복합 오브젝트 배열: {% raw %}`{{api_trigger_properties.${line_items}[0]}}`{% endraw %}는 첫 번째 라인 아이템 오브젝트를 반환합니다