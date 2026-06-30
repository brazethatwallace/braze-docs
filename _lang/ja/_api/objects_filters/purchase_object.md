---
nav_title: "購入オブジェクト"
article_title: API購入オブジェクト
page_order: 8
page_type: reference
description: "このリファレンス記事では、購入オブジェクトのさまざまなコンポーネント、正しい使用方法、参考となる例について説明します。"

---

# 購入オブジェクト {#purchase-object}

> この記事では、購入オブジェクトのさまざまなコンポーネント、正しい使用方法、ベストプラクティス、参考となる例について説明します。

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## 購入オブジェクトとは {#what-is-a-purchase-object}

購入オブジェクトは、購入が行われたときにAPIを通じて渡されるオブジェクトです。各購入オブジェクトは購入配列内に配置され、各オブジェクトは特定のユーザーが特定の時間に行った単一の購入を表します。購入オブジェクトにはさまざまなフィールドがあり、Brazeのバックエンドはこの情報を保存して、カスタマイズ、データ収集、パーソナライゼーションに使用できます。

### オブジェクト本体 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [外部ユーザー ID]({{site.baseurl}}/api/basics#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types)
- [ISO 4217 通貨コード Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 時間コード Wiki](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
一部の識別子ペアは一緒に使用できません。また、両方が指定された場合は`email`が`phone`よりも優先されます。詳しくは、[識別子の解決]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)を参照してください。
{% endalert %}

## 購入製品 ID {#purchase-product-id}

購入オブジェクト内では、`product_id`は購入の識別子です（`Product Name`や`Product Category`など）。

- Brazeでは、ダッシュボードに最大5,000個の`product_id`を保存できます。
- `product_id`は最大255文字までです。

### 命名規則 {#naming-conventions}

Brazeでは、購入オブジェクトの`product_id`に関する一般的な命名規則を提供しています。`product_id`を選択する際、Brazeは記録されたすべてのアイテムをこの`product_id`でグループ化することを目的として、（SKUではなく）製品名や製品カテゴリなどのシンプルな名前を使用することを推奨しています。

これにより、セグメンテーションやトリガーの際に製品を識別しやすくなります。

### 注文レベルでの購入記録 {#log-purchases-at-the-order-level}

製品レベルではなく注文レベルで購入を記録したい場合は、注文名または注文カテゴリを`product_id`として使用できます（`Online Order`や`Completed Order`など）。

たとえば、Web SDKで注文レベルの購入を記録するには以下のようにします。

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## 購入プロパティオブジェクト {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

カスタム属性、イベントプロパティ、カタログにわたるデータタイプの統合リファレンスについては、[データタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#purchase-event-property-data-types)を参照してください。

### 購入プロパティ {#purchase-properties}

[購入プロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties)は、Liquidを使用したメッセージのトリガーやパーソナライゼーションに使用でき、これらのプロパティに基づいてセグメント化することもできます。

#### 命名規則

この機能は購入ごとではなく、**製品ごとに**有効であることに注意してください。たとえば、個別の製品が大量にあっても、それぞれのプロパティが同じである場合、セグメンテーションは不要になる可能性があります。

この場合、データ構造を設定する際に、トランザクションレベルの識別子ではなく「グループレベル」で製品名を使用することをお勧めします。たとえば、鉄道チケット会社では、「片道」、「往復」、「複数都市」といった製品を用意すべきであり、「取引123」や「取引046」などの特定の取引名にすべきではありません。別の例として、「食べ物」の購入イベントでは、プロパティは「ケーキ」や「サンドイッチ」に設定するのが最適です。

{% alert important %}
Braze REST APIを使用して製品を追加できます。たとえば、`/users/track`エンドポイントにコールを送信し、新しい購入IDを含めると、Brazeは自動的にダッシュボードの**データ設定** > **製品**セクションに製品を作成します。
{% endalert %}

### 購入オブジェクトの例 {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### 購入オブジェクト、イベントオブジェクト、およびWebhook {#purchase-objects-event-objects-and-webhooks}

提供された例を使用すると、誰かが色、モノグラム、チェックアウト時間、サイズ、ブランドのプロパティを持つバックパックを購入したことがわかります。次に、[購入イベントプロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties)を使用してこれらのプロパティでSegmentを作成したり、Liquidを使用してチャネル経由でカスタムメッセージを送信したりできます。たとえば、「こんにちは **Ann F.** さん、**赤のミディアムバックパック**を **$40.00** でご購入いただきありがとうございます！**Backpack Locker** でのお買い物ありがとうございました！」

プロパティを保存、保管、追跡してセグメント化に使用する場合は、それらをカスタム属性として設定する必要があります。これは[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用して行うことができ、カスタムイベントやそのユーザープロファイルの生涯にわたって保存される購入行動に基づいてユーザーをターゲットにすることができます。