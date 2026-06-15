---
nav_title: "GET: ジョブ同期ステータスの一覧"
article_title: "GET: ジョブ同期ステータスの一覧"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "この記事では、ジョブ同期ステータスの一覧を取得するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# ジョブ同期ステータスの一覧 {#list-job-sync-status}
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> このエンドポイントを使用して、指定された統合の過去の同期ステータスの一覧を返します。

{% alert note %}
このエンドポイントを使用するには、`cdi.integration_job_status` 権限を持つAPIキーを生成する必要があります。
{% endalert %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `integration_id` | 必須 | 文字列 | 統合 ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## クエリパラメーター {#query-parameters}

このエンドポイントへの各呼び出しでは、10件のアイテムが返されます。10件を超える同期がある統合については、以下の応答例に示すように、`Link` ヘッダーを使用して次のページのデータを取得してください。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | 同期ステータスのページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Query parameters" }

## リクエスト例 {#example-request}

### カーソルなし {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、以下の応答本文を返す可能性があります。

{% alert note %}
`Link` ヘッダーは、同期の合計が10件以下の場合には存在しません。カーソルなしの呼び出しでは、`prev` は表示されません。アイテムの最後のページを表示している場合、`next` は表示されません。
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors
    }
  ],
  "message": "success"
}
```

| job_status | 説明 |
| --- | --- |
| `running` | ジョブは現在実行中です。 |
| `success` | すべての行が正常に同期されました。 |
| `partial` | 一部の行はエラーのため同期に失敗しました。 |
| `error` | 行は同期されませんでした。 |
| `config_error` | 統合設定にエラーがありました。統合のセットアップを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example success response" }

## トラブルシューティング {#troubleshooting}

以下のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid cursor` | `cursor` が有効であることを確認してください。 |
| `400 Invalid integration ID` | `integration_id` が有効であることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

その他のステータスコードと関連するエラーメッセージについては、[致命的なエラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% endapi %}