---
nav_title: "GET: キャンバスデータサマリー分析のエクスポート"
article_title: "GET: キャンバスデータサマリー分析のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、キャンバスデータサマリー分析のエクスポートBrazeエンドポイントについて説明します。"

---
{% api %}
# キャンバスデータサマリー分析のエクスポート {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの時系列データのロールアップをエクスポートし、キャンバス結果の簡潔なサマリーを提供します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.data_summary` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバスAPI識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `ending_at` | 必須 | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートの終了日。デフォルトはリクエスト時刻です。 |
| `starting_at` | オプション* | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートの開始日。<br><br>* `length` または `starting_at` のいずれかが必須です。 |
| `length` | オプション* | 文字列 | 返されるシリーズに含まれる `ending_at` より前の最大日数。1以上14以下（両端を含む）でなければなりません。<br><br>* `length` または `starting_at` のいずれかが必須です。 |
| `include_variant_breakdown` | オプション | ブール値 | バリアント統計を含めるかどうか（デフォルトは `false`）。  |
| `include_step_breakdown` | オプション | ブール値 | ステップ統計を含めるかどうか（デフォルトは `false`）。 |
| `include_deleted_step_data` | オプション | ブール値 | 削除されたステップの統計を含めるかどうか（デフォルトは `false`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert important %}
キャンバスの分析は、Brazeで設定された会社のタイムゾーン（ダッシュボードが使用するタイムゾーンと同じ）に基づいて日次で集計されます。APIは `starting_at` と `ending_at` をそのタイムゾーンの午前0時に正規化します。統計がダッシュボードと一致するように、タイムスタンプが会社のタイムゾーンに合っていることを確認してください。たとえば、会社のタイムゾーンがUTC+2の場合、タイムスタンプはUTC+2の午前0時にする必要があります。
{% endalert %}

## リクエスト例 {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## レスポンス {#response}

### コンバージョンイベントフィールド {#conversion-event-fields}

レスポンスには、キャンバスに設定された各コンバージョンイベントに対して1組のコンバージョンフィールドが含まれます。1次コンバージョンイベントは `conversions` と `conversions_by_entry_time` を使用します。追加の各イベントは、2番目のイベントに対して `1` から始まり、追加のイベントごとに1ずつ増加する数値サフィックスを持つ同じベース名を使用します。

| キャンバス上のコンバージョンイベントの順序 | コンバージョンフィールド | エントリ時刻別フィールド |
| --- | --- | --- |
| 1次 | `conversions` | `conversions_by_entry_time` |
| 2番目 | `conversions1` | `conversions1_by_entry_time` |
| 3番目 | `conversions2` | `conversions2_by_entry_time` |
| 4番目 | `conversions3` | `conversions3_by_entry_time` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="コンバージョンの順序" }

5番目以降のイベントも同じパターンに従います（例: `conversions4` と `conversions4_by_entry_time`）。これらのフィールドは `total_stats` に表示され、ブレークダウンをリクエストした場合は `variant_stats` と `step_stats` にも同じ名前で表示されます。

{% alert note %}
`total_stats`、`variant_stats`、`step_stats`において、`conversions`はキャンバスの[1次コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)のカウントです。追加のコンバージョンイベントを設定すると、ペイロードには2番目、3番目、およびそれ以降のイベントに対応する `conversions1`、`conversions2`、およびより大きなインデックスのフィールドも含まれる場合があります。これは `/campaigns/data_series` エンドポイントの[多変量レスポンス]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics#multivariate-response)と同様です。存在する場合、`_by_entry_time` で終わるフィールドは、キャンバスのエントリ時刻によるコンバージョンを示します。
{% endalert %}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "entries": (int) the number of entries,
      "conversions": (int) the number of conversions for the primary conversion event,
      "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
      "conversions1": (optional, int) the number of conversions for the second conversion event,
      "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
      "conversions2": (optional, int) the number of conversions for the third conversion event,
      "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
      "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (optional, int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert important %}
APIレスポンスでは、`influenced_opens` フィールドは開封の総数（直接開封と間接開封の両方を合わせたもの）を表します。Brazeダッシュボードでは、「間接開封」は直接開封を除いた間接開封のみを指します。これはAPIのレガシー命名規則によるものです。
{% endalert %}

## 関連記事 {#related-articles}

- [エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)


{% endapi %}