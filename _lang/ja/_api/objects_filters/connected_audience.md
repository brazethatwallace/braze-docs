---
nav_title: "接続オーディエンスフィルターとオブジェクト"
article_title: API接続オーディエンスオブジェクト
page_order: 3
page_type: reference
description: "この記事では、接続オーディエンスオブジェクトについて、その仕組み、ユースケース、およびそれを構成するさまざまなフィルターを説明します。"

---

# 接続オーディエンスオブジェクト {#connected-audience-object}

> 接続オーディエンスは、APIリクエスト内でインラインに定義するダイナミックなオーディエンスフィルターです。Brazeダッシュボードでセグメントを作成・管理することなく、送信時に適切なユーザーをターゲットにできます。

あらゆるオーディエンスの組み合わせに対してセグメントを事前に構築する代わりに、APIコールにフィルター条件を直接渡します。エンドポイントに応じて、このオブジェクトは`audience`または`custom_audience`として渡されます。Brazeはリアルタイムで各ユーザーをその条件に照らして評価し、条件に一致するユーザーにのみメッセージを配信します。つまり、1つのキャンペーン、キャンバス、またはAPIのみのメッセージ定義で、ビジネスロジックに完全に基づいた無制限のオーディエンスバリエーションに対応できます。

## 仕組み {#how-it-works}

1. Brazeダッシュボードで API トリガーのキャンペーンまたはキャンバスを作成してメッセージを定義するか、API リクエスト内の[メッセージングオブジェクト]({{site.baseurl}}/api/objects_filters#messaging-objects)を使用してメッセージコンテンツを完全にインラインで定義します。ダイナミックなパーソナライゼーションには、[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)または[キャンバスコンテキスト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を使用します。
2. サポートされているエンドポイントを呼び出し、`audience` パラメーターにコネクテッドオーディエンスフィルターを含めます（`/messages/live_activity/start` の場合は `custom_audience` に含めます）。カスタム属性、プッシュ購読ステータス、メール購読ステータス、最終アプリ使用日時でフィルタリングできます。
3. Brazeは送信時にフィルターを評価し、条件に一致するユーザーにのみメッセージを配信します。

{% alert tip %}
`audience` パラメーターを使用する場合、`campaign_id` は必須ではありません。[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) および [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) エンドポイントでは、事前にキャンペーンを作成しなくてもメッセージコンテンツをインラインで定義できます。ただし、ダッシュボードでキャンペーンレベルの指標（送信数、クリック数、バウンス数など）を追跡したい場合は、`campaign_id` を含めてください。
{% endalert %}

オーディエンスはリクエストごとに定義されるため、バックエンドシステムは、ダッシュボードでの操作なしに、あらゆるビジネスイベント（価格変更、天気アラート、ライブスコア更新など）に応じて状況に即したメッセージをトリガーできます。

### 互換性のあるエンドポイント {#compatible-endpoints}

以下のエンドポイントでコネクテッドオーディエンスオブジェクトを使用できます。

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)（`custom_audience` を使用）

`audience` パラメーターはオブジェクトの配列をサポートしていません。

## ユースケース {#use-cases}

コネクテッドオーディエンスは、バックエンドシステムがイベントを検出し、動的に決定されたユーザーセットに通知する必要があるシナリオで使用します。

| カテゴリ | 例 |
| --- | --- |
| 天気アラート | 気象データプロバイダーが深刻な気象イベントを検出し、`preferred_city` 属性が影響を受ける地域と一致するユーザーにプッシュ通知を送信します。 |
| スポーツ・ライブイベント | スポーツアプリが、`favorite_team` 属性が試合中のチームのいずれかと一致するユーザーにリアルタイムのスコア更新や試合アラートを送信します。 |
| コンテンツ・エンターテイメント | ストリーミングサービスが、新しいエピソードがリリースされるたびに、`favorite_shows` 配列にそのシリーズタイトルが含まれるユーザーに通知します。 |
| Eコマース | オンライン小売店が、`wishlisted_products` 配列に該当する商品IDが含まれるユーザーに値下げや再入荷のアラートを送信します。 |
| 旅行 | 旅行アプリが、`booked_flight` 属性が影響を受けるフライト番号と一致するユーザーにフライト遅延通知を送信します。 |
| 金融サービス | 取引プラットフォームが、`watchlist` 配列に価格しきい値を超えた銘柄コードが含まれるユーザーにアラートを送信します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

いずれの場合も、単一のキャンペーンまたはAPIのみのメッセージ定義ですべてのバリエーションに対応できます。バックエンドがフィルター値を決定し、APIリクエストで渡すため、商品、番組、チーム、場所ごとに個別のセグメントやキャンペーンを作成する必要はありません。

## リクエスト例 {#example-request}

以下の例では、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) エンドポイントを使用して、特定の番組をお気に入りに登録し、プッシュ通知をオプトインしているユーザーをターゲットにしています。

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## オブジェクト本体 {#object-body}

コネクテッドオーディエンスオブジェクトは、単一のコネクテッドオーディエンスフィルター、または `AND` と `OR` 演算子で組み合わされた複数のコネクテッドオーディエンスフィルターで構成されます。

**複数フィルターの例:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## コネクテッドオーディエンスフィルター {#connected-audience-filters}

複数のフィルターを `AND` および `OR` 演算子で組み合わせて、コネクテッドオーディエンスフィルターを作成します。

### 考慮事項 {#considerations}

コネクテッドオーディエンスでは、以下の条件でユーザーをフィルタリングすることはできません。

 - デフォルト属性
 - カスタムイベント
 - セグメント
 - メッセージエンゲージメントイベント
 - 階層化カスタム属性

これらのフィルターを使用するには、オーディエンスセグメントに組み込み、[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)の `segment_id` パラメーターでそのセグメントを指定することをお勧めします。他のエンドポイントを使用する場合は、まずBrazeダッシュボードでAPIトリガーのキャンペーンまたはキャンバスにセグメントを追加する必要があります。階層化属性でフィルタリングする必要がある場合は、代わりに[標準セグメント]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)を使用してください。


### カスタム属性フィルター {#custom-attribute-filter}

このフィルターを使用すると、ユーザーのカスタム属性に基づいてセグメント化できます。これらのフィルターには最大3つのフィールドが含まれます。

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### データ型別の許可される比較 {#allowed-comparisons-by-data-type}

カスタム属性のデータ型によって、特定のフィルターで有効な比較が決まります。

| カスタム属性の型 | 許可される比較 |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データ型別の許可される比較" }

#### 属性比較に関する注意事項 {#attribute-comparison-caveats}

| 比較 | 追加の考慮事項 |
| --- | --- |
| `value` | `exists` または `does_not_exist` の比較を使用する場合、`value` は不要です。`before` および `after` の比較を使用する場合、`value` はISO 8601日時文字列である必要があります。 |
| `matches_regex` | `matches_regex` の比較を使用する場合、渡される値は文字列である必要があります。Brazeでの正規表現の使用について詳しくは、[正規表現]({{site.baseurl}}/user_guide/engagement_tools/segments/regex#regex-with-braze)および[カスタム属性のデータ型]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-data-types)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="属性比較に関する注意事項" }

#### 複数値の比較 {#multi-value-comparisons}

`is_any_of` と `is_none_of` は、1回の比較で複数の値に対するマッチングをサポートしています。これらの比較は、文字列型と配列型の両方のカスタム属性で使用できます。

- `is_any_of`: 属性値が指定された値のいずれかと一致するユーザーにマッチします。`value` は単一の文字列または文字列の配列にすることができます。
- `is_none_of`: 属性値が指定された値のいずれとも一致しないユーザーにマッチします。`value` は単一の文字列または文字列の配列にすることができます。プロファイルにその属性を持たないユーザーは、常にこの比較の対象となることに注意してください。

配列属性の場合:

- `includes_value` は、ユーザーの配列に指定された値のいずれかが含まれているかどうかを確認するために、値の配列を受け入れることもできます。
- 配列属性で `is_any_of` または `is_none_of` を使用する場合、それぞれ `includes_value` および `does_not_include_value` と同じように機能します。

{% alert tip %}
複数値のマッチングには、`includes_value` ではなく `is_any_of` を使用してください。
{% endalert %}

#### カスタム属性の例 {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### 複数値の比較例 {#multi-value-comparison-examples}

##### 文字列の配列を使用した `is_any_of` {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### 文字列の配列を使用した `is_none_of` {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### 配列を使用した `includes_value`（配列属性） {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

これは、`subscribed_products` 配列に `"1001"`、`"1002"`、または `"1003"` のいずれかの値が含まれるユーザーにマッチします。

### プッシュ購読フィルター {#push-subscription-filter}

このフィルターを使用すると、ユーザーのプッシュ購読ステータスに基づいてセグメント化できます。

#### フィルター本文 {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **許可される比較:** `is`, `is_not`
- **許可される値:** `opted_in`, `subscribed`, `unsubscribed`

### メール購読フィルター {#email-subscription-filter}

このフィルターを使用すると、ユーザーのメール購読ステータスに基づいてセグメント化できます。

#### フィルター本文

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **許可される比較:** `is`, `is_not`
- **許可される値:** `opted_in`, `subscribed`, `unsubscribed`

### 最終アプリ使用フィルター {#last-used-app-filter}

このフィルターを使用すると、ユーザーが最後にアプリを使用した日時に基づいてセグメント化できます。これらのフィルターには2つのフィールドが含まれます。

#### フィルター本文

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **許可される比較:** `after`, `before`
- **許可される値:** datetime（ISO 8601文字列）