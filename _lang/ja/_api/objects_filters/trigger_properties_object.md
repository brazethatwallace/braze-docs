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

`trigger_properties`のオブジェクトを含むAPIリクエストを行った場合、そのオブジェクトの値は、`api_trigger_properties` 名前空間の下のメッセージテンプレートで参照できます。例えば、以下を使ったリクエストの場合、{% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} を追加することで、メッセージに `"shoes"` という単語を追加できます。

トリガープロパティはメッセージにテンプレート化できますが、デフォルトではユーザープロファイルに自動的には保存されないことに注意してください。

{% alert note %}
`trigger_properties` オブジェクトと{% raw %}`api_trigger_properties.${product_name}`{% endraw %} 構文はキャンペーンでのみサポートされます。キャンバスのAPIトリガーリクエストからのキーと値でメッセージをカスタマイズするには、[キャンバスエントリプロパティオブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)を使用してください。`trigger_properties` オブジェクトの最大サイズ制限は50 KBです。
{% endalert %}

## オブジェクト本体 {#object-body}

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
    "related_skus": ["123", "456", "789"]
  }
}
```


