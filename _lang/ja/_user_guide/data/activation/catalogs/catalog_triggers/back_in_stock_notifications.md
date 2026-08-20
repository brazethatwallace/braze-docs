---
nav_title: 再入荷通知
article_title: 再入荷通知を設定する
page_order: 2
description: "カタログとカスタムイベントを使用して再入荷通知を設定する方法を説明します。このように設定することで、商品が再入荷したときに通知を受け取るように、顧客を自動的に購読登録できます。"
---

# 再入荷通知 {#back-in-stock-notifications}

> カタログとカスタムイベントを使用して再入荷通知を設定する方法を説明します。このように設定することで、商品が再入荷したときに通知を受け取るように、顧客を自動的に購読登録できます。これは、すでに通知をオプトインしているユーザーにのみ適用されます。

## 仕組み {#how-it-works}

カスタムイベントを購読イベントとして設定できます（例：`product_clicked` イベント）。このイベントには、アイテムID（カタログアイテムID）のプロパティが含まれている必要があります。カタログ名を含めることをお勧めしますが、必須ではありません。また、在庫数量フィールドの名前も指定する必要があり、このフィールドは数値データ型である必要があります。

カタログアイテムの在庫がゼロである場合にのみ、ユーザーはそのアイテムを正常に購読できます。アイテムの在庫数量がゼロより大きくなると、Brazeはそのアイテムを購読しているすべてのユーザーを検索し、キャンペーンやキャンバスのトリガーに使用できるカスタムイベントを送信します。

イベントプロパティはユーザーとともに送信されるため、送信するキャンペーンやキャンバスにアイテムの詳細をテンプレートとして組み込むことができます。

## 在庫復活通知の設定 {#setting-up-back-in-stock-notifications}

特定のカタログで在庫復活通知を設定するには、以下のステップに従ってください。

1. カタログに移動し、**設定**タブを選択します。
2. **在庫復活**トグルを選択します。
3. グローバルな在庫復活設定がまだ構成されていない場合、在庫復活通知のトリガーに使用するカスタムイベントとプロパティの設定を求められます。
    <br> ![カタログ設定ドロワー。]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **フォールバックカタログ** カスタムイベントに `catalog_name` プロパティが存在しない場合に、在庫復活購読に使用されるカタログです。
    - **購読用カスタムイベント**は、ユーザーを在庫復活通知に購読させるために使用されるBrazeカスタムイベントです。このイベントが発生すると、イベントを実行したユーザーが購読されます。
    - **購読解除用カスタムイベント**は、ユーザーを在庫復活通知から購読解除するために使用されるBrazeカスタムイベントです。このイベントは任意です。ユーザーがこのイベントを実行しない場合、90日後または在庫復活イベントがトリガーされた時点のいずれか早い方で購読解除されます。
    - **アイテムIDイベントプロパティ**は、このセクションで前述したカスタムイベントのプロパティで、在庫復活の購読または購読解除の対象アイテムを決定するために使用されます。カスタムイベントのこのプロパティには、カタログに存在するアイテムID（`id`）が含まれている必要があります。アイテムIDは、対象カタログに保存されている `id` データ型と一致するように文字列として送信する必要があります。カスタムイベントには、このアイテムがどのカタログに属するかを指定する `catalog_name` プロパティも含める必要があります。

    - 以下の例は、REST APIを通じて送信されるサンプルカスタムイベントを示しています。

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

Braze SDKを使用して同じ購読イベントをトラッキングするには、以下のコードを使用してください。

{% tabs %}
{% tab Web SDK %}

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
在庫復活と価格低下のトリガーは、同じイベントを使用してユーザーを通知に購読させるため、`type` プロパティを使用して同じイベント内で価格低下と在庫復活の両方の通知を設定できます。`type` プロパティは配列である必要があることに注意してください。
{% endalert %}

{: start="4"}
4. **保存**を選択し、カタログの**設定**ページに進みます。
5. 通知ルールを設定します。2つのオプションがあります。
    - **購読中の全ユーザーに通知**は、アイテムが在庫復活した際に待機中のすべての顧客に通知します。
    - **通知制限を設定**は、10分ごとに指定された数の顧客に通知します。Brazeは、通知する顧客がいなくなるか、アイテムが在庫切れになるまで、指定された数の顧客に段階的に通知します。通知レートは1分あたり10,000ユーザーを超えることはできません。
6. **カタログ内の在庫フィールド**を設定します。このカタログフィールドは、アイテムが在庫切れかどうかを判断するために使用されます。フィールドは数値型である必要があります。
7. **設定を保存**を選択します。

![在庫復活機能がオンになっているカタログ設定。通知ルールは10分ごとに1,000ユーザーに通知する設定です。]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
これらの設定の通知ルールは、サイレント時間などのキャンバス通知設定を置き換えるものではありません。
{% endalert %}

## キャンバスで在庫復活通知を使用する {#using-back-in-stock-notifications-in-a-canvas}

カタログで在庫復活機能を設定した後、以下のステップに従ってキャンバスで使用します。

1. アクションベースのキャンバスを設定します。
2. トリガーとして**在庫復活**を選択します。
3. 在庫復活通知があるカタログの名前を選択します。
4. 通常どおりキャンバスの[設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を続けます。

これで、アイテムが在庫に戻ったときに顧客に通知できるようになります。

### Liquidの使用 {#using-liquid}

在庫に戻ったカタログアイテムの詳細をテンプレート化するには、`context` Liquidタグを使用して`item_id`にアクセスできます。

{%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%}を使用すると、在庫に戻ったアイテムのIDが返されます。{%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%}は更新前のアイテムの在庫値を返し、{%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%}は更新後の新しい在庫値を返します。

メッセージの先頭でLiquidタグ{%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%}を使用し、次に{%raw%}``{{ items[0].<field_name> }}``{%endraw%}を使用して、メッセージ全体でそのアイテムに関するデータにアクセスします。

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## 考慮事項 {#considerations}

- ユーザーの購読期間は90日間です。90日以内に商品が再入荷しない場合、ユーザーは購読解除されます。
- **購読中のすべてのユーザーに通知する**通知ルールを使用する場合、Brazeは10分間で100,000人のユーザーに通知します。
- Brazeは、再入荷通知のトリガー対象となるアイテムの更新を1日あたり最大50,000件サポートしています。アクティブな購読は一度に最大1億件まで保持でき、各購読はカタログアイテムの監視を購読しているユーザープロファイルを表します。