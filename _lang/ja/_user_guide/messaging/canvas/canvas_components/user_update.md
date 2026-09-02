---
nav_title: ユーザーの更新
article_title: ユーザーの更新
alias: "/user_update/"
page_order: 12
page_type: reference
description: "このリファレンス記事では、ユーザーの更新コンポーネントと、キャンバスでの使用方法について説明します。"
tool: Canvas
---

# ユーザーの更新 {#user-update}

> ユーザーの更新コンポーネントを使用すると、JSON エディターでユーザーの属性、イベント、購入を更新できるため、API キーなどの機密情報を含める必要がありません。

## このコンポーネントの仕組み {#how-this-component-works}

![「ロイヤルティ更新」という名前のユーザー更新ステップ。属性「Is Premium Member」を「true」に更新しています。]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

このコンポーネントをキャンバスで使用すると、更新は `/users/track` リクエストの1分あたりのレート制限にカウントされません。代わりに、これらの更新はバッチ処理されるため、BrazeはBraze-to-Braze Webhookよりも効率的に処理できます。このコンポーネントは、課金対象外のデータポイント（購読グループなど）の更新に使用される場合、[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)を記録しません。

ユーザーがユーザー更新ステップに入り、処理が完了すると、次のステップに進みます。つまり、これらのユーザー更新に依存する後続のメッセージングは、次のステップが実行される時点で最新の状態になっています。

## ユーザー更新の作成 {#creating-a-user-update}

サイドバーからコンポーネントをドラッグ＆ドロップするか、バリアントまたはステップの下部にある<i class="fas fa-plus-circle"></i>プラスボタンを選択して、**ユーザー更新**を選択します。

既存のユーザープロファイル情報の更新、新しい情報の追加、またはユーザープロファイル情報の削除を行う3つのオプションがあります。すべて合わせると、ワークスペース内のユーザー更新ステップは1分あたり最大200,000のユーザープロファイルを更新できます。

{% alert tip %}
このコンポーネントで行った変更は、ユーザーを検索して変更を適用することでテストすることもできます。これによりユーザーが更新されます。
{% endalert %}

## カスタム属性の更新 {#updating-custom-attributes}

カスタム属性を更新または削除するには、属性リストから属性名を選択し、値を入力します。

![「Loyalty Member」と「Loyalty Program」の2つの属性を「true」に更新するユーザー更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## カスタム属性の削除 {#removing-custom-attributes}

カスタム属性を削除するには、ドロップダウンを使用して属性名を選択します。[高度なJSONエディター](#advanced-json-editor)に切り替えて、さらに編集することもできます。

![属性「Loyalty Member」を削除するユーザー更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### 値の増減 {#increasing-and-decreasing-values}

ユーザー更新ステップでは、属性値を増減できます。属性を選択し、**Increment By** または **Decrement By** を選択して、数値を入力します。

#### 週ごとの進捗をトラッキングする {#track-weekly-progress}

イベントをトラッキングするカスタム属性をインクリメントすることで、ユーザーが1週間に受講したクラスの回数をトラッキングできます。このコンポーネントを使用すると、週の始まりにクラスカウントをリセットし、再びトラッキングを開始できます。

![属性「class_count」を1ずつインクリメントするユーザー更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### オブジェクト配列の更新 {#updating-an-array-of-objects}

[オブジェクト配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)は、ユーザーのプロファイルに保存されるデータが豊富なカスタム属性です。ユーザーとブランドとのインタラクション履歴を作成したり、購入履歴やLTVの合計などの計算フィールドに基づいてセグメントを作成したりできます。

**Advanced JSON Editor** オプションを使用すると、JSONを挿入してこのオブジェクト配列にアイテムを追加したり、アイテムを削除したりできます。

#### ユースケース: ユーザーのウィッシュリストを更新する {#use-case-updating-a-users-wishlist}

ユーザーのウィッシュリストをトラッキングして、保存されたアイテムに基づいてセグメントやパーソナライゼーションを行います。

1. オブジェクト配列であるカスタム属性（例: `wishlist`）を作成します。各オブジェクトには、`product_id`、`product_name`、`added_at` などのフィールドを含めることができます。
2. ユーザー更新ステップで、**Advanced JSON Editor** を選択します。次に、**Compose** セクションで、`$add` オペレーションを使用してアイテムを追加するか、`$remove` オペレーションを使用して値でアイテムを削除します。

以下は、ウィッシュリストにアイテムを追加する例です。

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

アイテムを削除するには、同じオブジェクト構造で `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` を使用して、Brazeがマッチして削除できるようにします。

#### ユースケース: ショッピングカートの合計を計算する {#use-case-calculating-the-shopping-cart-total}

ユーザーのショッピングカートにアイテムがあるとき、新しいアイテムの追加や削除のタイミング、およびショッピングカートの合計金額をトラッキングします。

1. `shopping_cart` というカスタムオブジェクト配列を作成します。以下の例は、この属性がどのようになるかを示しています。各アイテムには固有の `product_id` があり、`price` を含む独自のネストされたオブジェクト配列に追加データが含まれています。

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
2. ユーザーがバスケットにアイテムを追加したときに記録される `add_item_to_cart` という[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を作成します。
3. このカスタムイベントを実行するユーザーをターゲットとするキャンバスを作成します。ユーザーがカートにアイテムを追加すると、このキャンバスがトリガーされます。そのユーザーに直接メッセージングをターゲットして、一定の金額に達したときにクーポンコードを提供したり、一定時間カートを放棄した場合にメッセージを送信したり、ユースケースに合ったその他のアクションを行うことができます。

`shopping_cart` 属性には、多くのカスタムイベントの合計が含まれます。すべてのアイテムの合計金額、カート内のアイテムの合計数、ショッピングカートにギフトが含まれているかどうかなどです。これは次のようになります。

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

## キャンバスエントリプロパティを属性として設定する {#setting-canvas-entry-property-as-an-attribute}

ユーザー更新ステップを使用して、`canvas_entry_property` を永続化できます。たとえば、アイテムがカートに追加されたときにトリガーされるイベントがあるとします。カートに最後に追加されたアイテムのIDを保存し、リマーケティングキャンペーンに使用できます。パーソナライゼーション機能を使用して、キャンバスエントリプロパティを取得し、属性に保存します。

![属性「most_recent_cart_item」をアイテムIDで更新するユーザー更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### パーソナライゼーション {#personalization}

キャンバスのトリガーイベントのプロパティを属性として保存するには、パーソナライゼーションモーダルを使用してキャンバスエントリプロパティを抽出し、保存します。ユーザー更新では、以下のパーソナライゼーション機能もサポートされています。

* [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [エントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Liquidロジック（[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)を含む）
* オブジェクトごとの複数の属性またはイベントの更新

{% alert warning %}
ユーザー更新ステップでのConnected Content Liquidパーソナライゼーションの使用は慎重に行うことをお勧めします。このステップタイプには毎分200,000リクエストのレート制限があります。このレート制限はキャンバスのレート制限を上書きします。
{% endalert %}

## 高度なJSONエディター {#advanced-json-editor}

属性、イベント、または購入のJSONオブジェクト（最大65,536文字）をJSONエディターに追加します。ユーザーの[グローバル購読]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)および[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)の状態も設定できます。

![属性、イベント、または購入のJSONオブジェクト（最大65,536文字）をJSONエディターに追加します。ユーザーのグローバル購読および購読グループの状態も設定できます。]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

JSONエディターを使用すると、**プレビューとテスト**タブで、変更によりユーザープロファイルが更新されることをプレビューおよびテストすることもできます。ランダムなユーザーを選択するか、特定のユーザーを検索できます。その後、ユーザーにテストを送信した後、生成されたリンクを使用してユーザープロファイルを確認します。

![JSONエディターを使用すると、プレビューとテストタブで、変更によりユーザープロファイルが更新されることをプレビューおよびテストすることもできます。ランダムなユーザーを選択するか、特定のユーザーを検索できます。その後、ユーザーにテストを送信した後、生成されたリンクを使用してユーザープロファイルを確認します。]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 考慮事項 {#considerations}

JSONエディターの使用時に、APIキーなどの機密データを含める必要はありません。これはプラットフォームによって自動的に提供されます。以下のフィールドはJSONエディターに含めないでください:
* 外部ユーザー ID
* APIキー
* Brazeクラスター URL
* プッシュトークンのインポートに関連するフィールド

{% alert important %}
キャンバスプロパティ（`canvas_id`、`canvas_name`、`canvas_variant_name` Liquidタグなど）は、ユーザー更新ステップではサポートされていません。
{% endalert %}

{% raw %}
### カスタムイベントを記録する {#log-custom-events}

JSONエディターを使用して、カスタムイベントを記録することもできます。これにはISO形式のタイムスタンプが必要なため、最初にLiquidで日時を割り当てる必要があります。時間を含むイベントを記録する次の例を考えてみてください。

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

次の例では、オプションのプロパティと `app_id` を持つカスタムイベントを使用して、イベントを特定のアプリにリンクします。

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

### 購読状態を編集する {#edit-subscription-state}

JSONエディター内で、ユーザーの購読状態を編集することもできます。たとえば、以下はユーザーの購読状態が `opted_in` に更新された例です。

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### 購読グループを更新する {#update-subscription-groups}

このキャンバスステップを使用して、購読グループを更新することもできます。以下の例では、1つ以上の購読グループを更新する方法を示しています。

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