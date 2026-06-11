---
nav_title: "接続オーディエンスフィルターとオブジェクト"
article_title: API接続オーディエンスオブジェクト
page_order: 3
page_type: reference
description: "この記事では、接続オーディエンスオブジェクトについて、その仕組み、ユースケース、およびそれを構成するさまざまなフィルターを説明します。"

---

# 接続オーディエンスオブジェクト {#connected-audience-object}

> 接続オーディエンスは、APIリクエスト内でインラインに定義するダイナミックなオーディエンスフィルターです。Brazeダッシュボードでセグメントを作成・管理することなく、送信時に適切なユーザーをターゲットにできます。

あらゆるオーディエンスの組み合わせに対してSegmentを事前に構築する代わりに、APIコールにフィルター条件を直接渡します。エンドポイントに応じて、このオブジェクトは`audience`または`custom_audience`として渡されます。Brazeはリアルタイムで各ユーザーをその条件に照らして評価し、条件に一致するユーザーにのみメッセージを配信します。つまり、1つのCampaign、Canvas、またはAPIのみのメッセージ定義で、ビジネスロジックに完全に基づいた無制限のオーディエンスバリエーションに対応できます。

## 仕組み {#how-it-works}

1. BrazeダッシュボードでAPIトリガーのCampaignまたはCanvasを作成してメッセージを定義するか、APIリクエストの[メッセージングオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)を使用してメッセージコンテンツを完全にインラインで定義します。ダイナミックなパーソナライゼーションには[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)または[Canvasコンテキスト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)を使用します。
2. 対応するエンドポイントを呼び出し、接続オーディエンスフィルターを`audience`パラメーターに含めます。`/messages/live_activity/start`の場合は`custom_audience`に含めます。カスタム属性、プッシュ通知のサブスクリプションステータス、メールのサブスクリプションステータス、最後にアプリを使用した時間でフィルターできます。
3. Brazeは送信時にフィルターを評価し、条件に一致するユーザーにのみメッセージを配信します。

{% alert tip %}
`audience`パラメーターを使用する場合、`campaign_id`は必須ではありません。[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)および[`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)エンドポイントでは、事前に作成したCampaignなしでメッセージコンテンツをインラインで定義できます。ただし、ダッシュボードでCampaignレベルの指標（送信数、クリック数、バウンスなど）を追跡したい場合は、`campaign_id`を含めてください。
{% endalert %}

オーディエンスはリクエストごとに定義されるため、バックエンドシステムは任意のビジネスイベント（価格変更、気象警報、ライブスコア更新など）に応じて、ダッシュボードの操作なしに状況に即した関連メッセージをトリガーできます。

### 対応エンドポイント {#compatible-endpoints}

接続オーディエンスオブジェクトは、以下のエンドポイントで使用できます。

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/)（`custom_audience`を使用）

## ユースケース {#use-cases}

バックエンドシステムがイベントを検出し、動的に決定されたユーザーセットに通知する必要があるシナリオで接続オーディエンスを使用します。

| カテゴリ | 例 |
| --- | --- |
| 気象警報 | 気象データプロバイダーが深刻な気象イベントを検出し、`preferred_city`属性が影響を受ける地域に一致するユーザーにプッシュ通知を送信します。 |
| スポーツ・ライブイベント | スポーツアプリが、`favorite_team`属性が試合中のチームに一致するユーザーにリアルタイムのスコア更新や試合アラートを送信します。 |
| コンテンツ・エンターテイメント | ストリーミングサービスが、新しいエピソードがリリースされるたびに、`favorite_shows`配列にそのシリーズタイトルを含むユーザーに通知します。 |
| Eコマース | オンライン小売業者が、`wishlisted_products`配列に該当する商品IDを含むユーザーに値下げや再入荷のアラートを送信します。 |
| 旅行 | 旅行アプリが、`booked_flight`属性が影響を受けるフライト番号に一致するユーザーにフライト遅延通知を送信します。 |
| 金融サービス | 取引プラットフォームが、`watchlist`配列に価格閾値を超えた銘柄コードを含むユーザーにアラートを送信します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

いずれの場合も、1つのCampaignまたはAPIのみのメッセージ定義ですべてのバリエーションに対応します。バックエンドがフィルター値を決定してAPIリクエストに渡すため、商品、番組、チーム、ロケーションごとに個別のSegmentやCampaignを作成する必要はありません。

## リクエスト例 {#example-request}

以下の例では、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)エンドポイントを使用して、特定の番組をお気に入りに登録し、プッシュ通知をオプトインしているユーザーをターゲットにしています。

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

## オブジェクト本文 {#object-body}

接続オーディエンスオブジェクトは、1つの接続オーディエンスフィルター、または`AND`と`OR`演算子で組み合わせた複数の接続オーディエンスフィルターで構成されます。

**複数フィルターの例：**

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

## 接続オーディエンスフィルター {#connected-audience-filters}

複数のフィルターを`AND`および`OR`演算子と組み合わせて、接続オーディエンスフィルターを作成します。

### カスタム属性フィルター {#custom-attribute-filter}

このフィルターでは、ユーザーのカスタム属性に基づいてセグメント化できます。これらのフィルターには最大3つのフィールドが含まれます。

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

#### データタイプ別の許容される比較 {#allowed-comparisons-by-data-type}

カスタム属性のデータタイプによって、指定されたフィルターで有効な比較が決まります。

| カスタム属性タイプ | 許容される比較 |
| ---------------------| --------------- |
| 文字列 | `equals`、`not_equal`、`matches_regex`、`does_not_match_regex`、`exists`、`does_not_exist` |
| 配列 | `includes_value`、`does_not_include_value`、`exists`、`does_not_exist` |
| 数値 | `equals`、`not_equal`、`greater_than`、`greater_than_or_equal_to`、`less_than`、`less_than_or_equal_to`、`exists`、`does_not_exist` |
| ブール値 | `equals`、`not_equal`、`exists`、`does_not_exist` |
| 時刻 | `less_than_x_days_ago`、`greater_than_x_days_ago`、`less_than_x_days_in_the_future`、`greater_than_x_days_in_the_future`、`after`、`before`、`exists`、`does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Allowed comparisons by data type" }

#### 属性比較の注意点 {#attribute-comparison-caveats}

| 比較 | その他の考慮事項 |
| --- | --- |
| `value` | `exists`または`does_not_exist`の比較を使用する場合、`value`は必要ありません。`before`および`after`の比較を使用する場合、`value`はISO 8601日時文字列である必要があります。 |
| `matches_regex` | `matches_regex`比較を使用する場合、渡される値は文字列である必要があります。Brazeでの正規表現の使用については、[正規表現]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze)と[カスタム属性のデータタイプ]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attribute comparison caveats" }

#### カスタム属性の例 {#custom-attribute-example}

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
### プッシュ通知のサブスクリプションフィルター {#push-subscription-filter}

このフィルターでは、ユーザーのプッシュ通知のサブスクリプションステータスに基づいてセグメント化できます。

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

- **許容される比較：** `is`、`is_not`
- **許容される値：** `opted_in`、`subscribed`、`unsubscribed`

### メールのサブスクリプションフィルター {#email-subscription-filter}

このフィルターでは、ユーザーのメールのサブスクリプションステータスに基づいてセグメント化できます。

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

- **許容される比較：** `is`、`is_not`
- **許容される値：** `opted_in`、`subscribed`、`unsubscribed`

### 最後に使用したアプリフィルター {#last-used-app-filter}

このフィルターでは、ユーザーが最後にアプリを使用した時間に基づいてセグメント化できます。これらのフィルターには2つのフィールドが含まれます。

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

- **許容される比較：** `after`、`before`
- **許容される値：** datetime（ISO 8601文字列）

### 考慮事項 {#considerations}

接続オーディエンスでは、デフォルト属性、カスタムイベント、Segments、またはメッセージエンゲージメントイベントによるユーザーのフィルタリングはできません。これらのフィルターを使用するには、オーディエンスSegmentに組み込んだうえで、[`/messages/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)の`segment_id`パラメーターでそのSegmentを指定することをお勧めします。他のエンドポイントを使用する場合は、まずBrazeダッシュボードでAPIトリガーのCampaignまたはCanvasにSegmentを追加する必要があります。