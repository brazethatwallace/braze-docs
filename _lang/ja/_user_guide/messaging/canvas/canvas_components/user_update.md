---
nav_title: ユーザーの更新
article_title: ユーザーの更新
alias: "/user_update/"
page_order: 12
page_type: reference
description: "このリファレンス記事では、ユーザーの更新コンポーネントと、キャンバスでの使用方法について説明します。"
tool: Canvas
---

# ユーザーの更新

> ユーザーの更新コンポーネントを使用すると、JSON エディターでユーザーの属性、イベント、購入を更新できるため、API キーなどの機密情報を含める必要がありません。

## このコンポーネントの仕組み

![属性「Is Premium Member」を「true」に更新する「Update loyalty」という名前のユーザーの更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

このコンポーネントをキャンバスで使用する場合、更新は `/users/track` の1分あたりのリクエスト数のレート制限にカウントされません。代わりに、これらの更新はバッチ処理されるため、Braze は Braze-to-Braze Webhook よりも効率的に処理できます。なお、このコンポーネントは、課金対象外のデータポイント（サブスクリプショングループなど）の更新に使用される場合、[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)を記録しません。

ユーザーがユーザーの更新ステップに入り、処理が完了すると、次のステップに進みます。つまり、これらのユーザー更新に依存する後続のメッセージングは、次のステップが実行される時点で最新の状態になっています。

## ユーザーの更新を作成する

サイドバーからコンポーネントをドラッグ＆ドロップするか、バリアントまたはステップの下部にある <i class="fas fa-plus-circle"></i> プラスボタンを選択して**ユーザーの更新**を選択します。

既存のユーザープロファイル情報の更新、新しい情報の追加、またはユーザープロファイル情報の削除を行う3つのオプションがあります。ワークスペース内のユーザーの更新ステップは、すべて合わせて1分あたり最大200,000のユーザープロファイルを更新できます。

{% alert tip %}
このコンポーネントで行った変更をテストすることもできます。ユーザーを検索して変更を適用すると、そのユーザーが更新されます。
{% endalert %}

## カスタム属性を更新する

カスタム属性を更新または削除するには、属性リストから属性名を選択し、値を入力します。

![2つの属性「Loyalty Member」と「Loyalty Program」を「true」に更新するユーザーの更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## カスタム属性を削除する

カスタム属性を削除するには、ドロップダウンを使用して属性名を選択します。[高度な JSON エディター](#advanced-json-editor)に切り替えて、さらに編集することもできます。

![属性「Loyalty Member」を削除するユーザーの更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### 値の増減

ユーザーの更新ステップでは、属性値を増加または減少させることができます。属性を選択し、**Increment By** または **Decrement By** を選択して、数値を入力します。

#### 週間の進捗をトラッキングする

イベントをトラッキングするカスタム属性をインクリメントすることで、ユーザーが1週間に受講したクラスの数をトラッキングできます。このコンポーネントを使用すると、クラスカウントを週の初めにリセットし、再びトラッキングを開始できます。

![属性「class_count」を1つインクリメントするユーザーの更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### オブジェクトの配列を更新する

[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/)は、ユーザーのプロファイルに保存されるデータリッチなカスタム属性です。ユーザーとブランドとのインタラクション履歴を作成したり、購入履歴や合計ライフタイムバリューなどの計算フィールドに基づいてセグメントを作成したりするために使用できます。

**Advanced JSON Editor** オプションを使用して、JSON を挿入し、このオブジェクトの配列にアイテムを追加したり、アイテムを削除したりできます。

#### ユースケース: ユーザーのウィッシュリストを更新する

ユーザーのウィッシュリストをトラッキングして、保存されたアイテムに基づいてセグメントやパーソナライゼーションを行います。

1. オブジェクトの配列であるカスタム属性を作成します（例: `wishlist`）。各オブジェクトには `product_id`、`product_name`、`added_at` などのフィールドを含めることができます。
2. ユーザーの更新ステップで、**Advanced JSON Editor** を選択します。次に、**作成**セクションで、`$add` オペレーションを使用してアイテムを追加するか、`$remove` オペレーションを使用して値でアイテムを削除します。

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

アイテムを削除するには、同じオブジェクト構造で `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` を使用して、Braze がマッチして削除できるようにします。

#### ユースケース: ショッピングカートの合計を計算する

ユーザーのショッピングカートにアイテムがある場合、新しいアイテムの追加やアイテムの削除、およびショッピングカートの合計金額をトラッキングします。

1. `shopping_cart` というカスタムオブジェクトの配列を作成します。以下の例は、この属性がどのように見えるかを示しています。各アイテムには固有の `product_id` があり、`price` を含む独自のネストされたオブジェクトの配列に追加データがあります。

{% raw %}
`````````javascript
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
2. ユーザーがカートにアイテムを追加したときに記録される `add_item_to_cart` という名前の[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)を作成します。
3. このカスタムイベントを実行したユーザーをターゲットとするキャンバスを作成します。これにより、ユーザーがカートにアイテムを追加すると、このキャンバスがトリガーされます。その後、特定の金額に達した場合のクーポンコードの提供、一定時間カートを放置した場合のリマインド、またはユースケースに合ったその他のメッセージングを、そのユーザーに直接ターゲティングできます。

`shopping_cart` 属性には、多くのカスタムイベントの合計が含まれます。すべてのアイテムの合計コスト、カート内のアイテムの合計数、ショッピングカートにギフトが含まれているかどうかなどです。これは以下のようになります。

{% raw %}
`````````javascript
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

## キャンバスエントリプロパティを属性として設定する

ユーザーの更新ステップを使用して、`canvas_entry_property` を永続化できます。例えば、アイテムがカートに追加されたときにトリガーされるイベントがあるとします。カートに最後に追加されたアイテムの ID を保存し、リマーケティングキャンペーンに使用できます。パーソナライゼーション機能を使用して、キャンバスエントリプロパティを取得し、属性に保存します。

![属性「most_recent_cart_item」をアイテム ID で更新するユーザーの更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### パーソナライゼーション

キャンバスのトリガーイベントのプロパティを属性として保存するには、パーソナライゼーションモーダルを使用してキャンバスエントリプロパティを抽出し、保存します。ユーザーの更新では、以下のパーソナライゼーション機能もサポートしています。

* [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
* [コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)
* [エントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/)
* Liquid ロジック（[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)を含む）
* オブジェクトごとの複数の属性またはイベントの更新

{% alert warning %}
ユーザーの更新ステップでのコネクテッドコンテンツ Liquid パーソナライゼーションの使用には注意が必要です。このステップタイプには1分あたり200,000リクエストのレート制限があります。このレート制限はキャンバスのレート制限を上書きします。
{% endalert %}

## 高度な JSON エディター

属性、イベント、または購入の JSON オブジェクトを最大65,536文字まで JSON エディターに追加できます。ユーザーの[グローバルサブスクリプション]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)および[サブスクリプショングループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)の状態も設定できます。

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

JSON エディターを使用すると、**プレビューとテスト**タブで、ユーザープロファイルが変更内容で更新されることをプレビューおよびテストすることもできます。ランダムなユーザーを選択するか、特定のユーザーを検索できます。その後、ユーザーにテストを送信した後、生成されたリンクを使用してユーザープロファイルを表示します。

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 注意事項

JSON エディターを使用する際に、API キーなどの機密データを含める必要はありません。これはプラットフォームによって自動的に提供されます。以下のフィールドは JSON エディターに含めないでください。
* 外部ユーザー ID
* API キー
* Braze クラスター URL
* プッシュトークンのインポートに関連するフィールド

{% alert important %}
キャンバスプロパティ（`canvas_id`、`canvas_name`、`canvas_variant_name` の Liquid タグなど）は、ユーザーの更新ステップではサポートされていません。
{% endalert %}

{% raw %}
### カスタムイベントを記録する

JSON エディターを使用して、カスタムイベントを記録することもできます。これには ISO 形式のタイムスタンプが必要なため、最初に Liquid で日時を割り当てる必要があります。時刻付きのイベントを記録する以下の例を参考にしてください。

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

次の例では、オプションのプロパティと `app_id` を持つカスタムイベントを使用して、イベントを特定のアプリにリンクしています。

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

### サブスクリプション状態を編集する

JSON エディター内で、ユーザーのサブスクリプション状態を編集することもできます。例えば、以下はユーザーのサブスクリプション状態を `opted_in` に更新する例です。

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### サブスクリプショングループを更新する

このキャンバスステップを使用して、サブスクリプショングループを更新することもできます。以下の例は、1つ以上のサブスクリプショングループを更新する方法を示しています。

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