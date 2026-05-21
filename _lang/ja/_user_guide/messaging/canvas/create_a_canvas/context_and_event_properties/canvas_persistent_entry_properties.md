---
nav_title: 永続的なエントリプロパティ
article_title: 永続的なエントリプロパティ
alias: "/persistent_entry/"
page_type: reference
description: "このリファレンス記事では、キャンバスで永続的なエントリプロパティを使用して、よりキュレートされたメッセージを送信し、高度に洗練されたエンドユーザー体験を作成する方法について説明します。"
tool: Canvas
page_order: 5
---

# 永続的なエントリプロパティ {#persistent-entry-properties}

> キャンバスがカスタムイベント、購入、またはAPI呼び出しによってトリガーされた場合、API呼び出し、カスタムイベント、または購入イベントのメタデータを使用して、キャンバスワークフローの各ステップでパーソナライゼーションを行うことができます。これらのプロパティを使用して、よりキュレートされたメッセージを送信できます。

{% alert important %}
永続的なエントリプロパティは、元のキャンバスエディターのアーティファクトであるため、キャンバスエントリプロパティなどの用語への非推奨の参照が歴史的な参考として残っています。現在のキャンバスエディターについては、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)を参照してください。<br><br>現在のキャンバスエディターで永続的なエントリプロパティを使用するには、新しいキャンバスを作成するか、既存のキャンバスを現在のエディターに[複製]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)する必要があります。
{% endalert %}

## エントリプロパティの使用 {#using-entry-properties}

エントリプロパティは、アクションベースおよびAPIトリガーのキャンバスで使用できます。これらのエントリプロパティは、キャンバスがカスタムイベント、購入、またはAPI呼び出しによってトリガーされたときに定義されます。詳細については、以下の記事を参照してください。

- [キャンバスエントリプロパティオブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)
- [イベントプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)
- [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

これらのオブジェクトから渡されたプロパティは、`canvas_entry_properties` Liquidタグを使用して参照できます。例えば、`"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}` というリクエストでは、Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}を追加することで、メッセージに「shoes」という単語を追加できます。

キャンバスに`canvas_entry_properties` Liquidタグを含むメッセージがある場合、それらのプロパティに関連付けられた値は、ユーザーのキャンバス内のジャーニーの間保存され、ユーザーがキャンバスを退出すると削除されます。キャンバスエントリプロパティは、Liquidでの参照にのみ使用できます。キャンバス内でプロパティによるフィルタリングを行うには、代わりに[イベントプロパティセグメンテーション]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/)を使用してください。

{% alert note %}
キャンバスエントリプロパティオブジェクトの最大サイズは50 KBです。
{% endalert %}

## エントリプロパティを使用するためのキャンバスの更新 {#updating-canvas-to-use-entry-properties}

以前`canvas_entry_properties`を使用するメッセージを含んでいなかったアクティブなキャンバスを編集して`canvas_entry_properties`を含めるようにした場合、そのプロパティに対応する値は、`canvas_entry_properties`がキャンバスに追加される前にキャンバスに入ったユーザーには利用できません。値は、変更が行われた後にキャンバスに入ったユーザーに対してのみ保存されます。

例えば、11月3日にエントリプロパティを使用しないキャンバスを最初に起動し、11月11日にキャンバスに新しいプロパティ`product_name`を追加した場合、`product_name`の値は11月11日以降にキャンバスに入ったユーザーに対してのみ保存されます。

キャンバスエントリプロパティがnullまたは空白の場合、条件文を使用してメッセージを中止できます。以下のコードスニペットは、Liquidを使用してメッセージを中止する方法の例です。
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Liquidを使用したメッセージの中止について詳しくは、[Liquidドキュメント]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages)をご覧ください。

## グローバルキャンバスエントリプロパティ {#global-canvas-entry-properties}

`canvas_entry_properties`を使用すると、すべてのユーザーに適用されるグローバルプロパティ、または指定されたユーザーにのみ適用されるユーザー固有のプロパティを設定できます。ユーザー固有のプロパティは、そのユーザーのグローバルプロパティを上書きします。

### リクエスト例 {#example-request}

`````````bash
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

このリクエストでは、「food allergies」のグローバル値は「none」です。Customer_123の場合、値は「dairy」です。このキャンバス内のLiquidスニペット{%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%}を含むメッセージは、Customer_123には「dairy」、その他のユーザーには「none」としてテンプレート化されます。

## ユースケース {#use-case}

ユーザーがeコマースサイトでアイテムを閲覧したがカートに追加しなかった場合にトリガーされるキャンバスがある場合、キャンバスの最初のステップは、そのアイテムの購入に興味があるかどうかを尋ねるプッシュ通知にすることができます。{% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}を使用して製品名を参照できます。

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

2番目のステップでは、ユーザーがアイテムをカートに追加したがまだ購入していない場合に、チェックアウトを促す別のプッシュ通知を送信できます。{% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}を使用して、引き続き`product_name`エントリプロパティを参照できます。

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}