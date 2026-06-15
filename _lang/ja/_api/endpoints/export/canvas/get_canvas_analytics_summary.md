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

このエンドポイントを使用するには、`canvas.data_summary` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [Canvas API識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `ending_at` | 必須 | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートの終了日。デフォルトはリクエスト時刻です。 |
| `starting_at` | オプション* | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートの開始日。<br><br>* `length` または `starting_at` のいずれかが必要です。 |
| `length` | オプション* | 文字列 | 返されるシリーズに含まれる `ending_at` より前の最大日数。1以上14以下（両端を含む）でなければなりません。<br><br>* `length` または `starting_at` のいずれかが必要です。 |
| `include_variant_breakdown` | オプション | ブール値 | バリアント統計を含めるかどうか（デフォルトは `false`）。  |
| `include_step_breakdown` | オプション | ブール値 | ステップ統計を含めるかどうか（デフォルトは `false`）。 |
| `include_deleted_step_data` | オプション | ブール値 | 削除されたステップの統計を含めるかどうか（デフォルトは `false`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert important %}
**タイムゾーンの整合:** Brazeダッシュボードの分析は、ダッシュボードで設定された会社のタイムゾーンに基づいて日次で集計されます。統計がダッシュボードと一致するように、タイムスタンプが会社のタイムゾーンと揃っていることを確認してください。たとえば、会社の時刻がUTC+2の場合、タイムスタンプは12AM UTC+2にする必要があります。
{% endalert %}

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答 {#response}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "conversions": (int) the number of conversions,
      "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
      "entries": (int) the number of entries
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
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
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**`influenced_opens` フィールド:** APIレスポンスでは、`influenced_opens` フィールドは開封の総数（直接開封と間接開封の両方を合わせたもの）を表します。Brazeダッシュボードでは、「間接開封」は直接開封を除いた間接開封のみを指します。これはAPIのレガシー命名規則によるものです。
{% endalert %}

{% alert tip %}
CSVおよびAPIエクスポートに関するヘルプについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)を参照してください。
{% endalert %}

{% endapi %}