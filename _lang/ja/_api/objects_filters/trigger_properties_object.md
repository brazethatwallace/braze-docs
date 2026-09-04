---
nav_title: "トリガープロパティオブジェクト"
article_title: APIトリガープロパティオブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、トリガープロパティオブジェクトのさまざまなコンポーネントについて説明します。"
tool: Campaigns

---

# トリガープロパティオブジェクト {#trigger-properties-object}

> APIトリガー配信でキャンペーンを送信するためにエンドポイントの1つを使用する場合、メッセージをカスタマイズするためにキーと値のマップを提供できます。

`trigger_properties`のオブジェクトを含むAPIリクエストを行った場合、そのオブジェクトの値は、`api_trigger_properties`名前空間の下のメッセージテンプレートで参照できます。例えば、以下のようなリクエストでは、{% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}を追加することで、メッセージに`"shoes"`という単語を追加できます。

トリガープロパティはメッセージにテンプレート化できますが、デフォルトではユーザープロファイルに自動的には保存されないことに注意してください。

{% alert note %}
`trigger_properties`オブジェクトと{% raw %}`api_trigger_properties.${product_name}`{% endraw %}構文はキャンペーンでのみサポートされます。キャンバスのAPIトリガーリクエストからのキーと値でメッセージをカスタマイズするには、[キャンバスエントリプロパティオブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を使用してください。`trigger_properties`オブジェクトの最大サイズ制限は50 KBです。
{% endalert %}

## オブジェクト本文 {#object-body}

`trigger_properties` オブジェクトは、データ型として文字列、数値、ブール値、日付、オブジェクト、および配列をサポートしています。

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

## Liquidテンプレートの例 {#liquid-templating-examples}

`api_trigger_properties`名前空間を使用して、メッセージテンプレート内でトリガープロパティを参照できます。

- 文字列: {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} は`"shoes"`を返します
- 数値: {% raw %}`{{api_trigger_properties.${product_price}}}`{% endraw %} は`79.99`を返します
- ネストされたオブジェクト: {% raw %}`{{api_trigger_properties.${details}.${color}}}`{% endraw %} は`"red"`を返します
- 配列要素: {% raw %}`{{api_trigger_properties.${related_skus}[0]}}`{% endraw %} は`"123"`を返します
- 複合オブジェクト配列: {% raw %}`{{api_trigger_properties.${line_items}[0]}}`{% endraw %} は最初のラインアイテムオブジェクトを返します