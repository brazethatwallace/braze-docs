---
nav_title: "POST:同期をトリガー"
article_title: "POST:同期をトリガー"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "この記事では、「同期をトリガー」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 同期をトリガー {#trigger-a-sync}
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> このエンドポイントを使用して、特定の統合の同期をトリガーします。

{% alert note %}
このエンドポイントを使用するには、`cdi.integration_sync` 権限を持つAPIキーを生成する必要があります。
{% endalert %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `integration_id` | 必須 | 文字列 | 統合ID。これは、Brazeダッシュボードで統合を表示した際のURLに含まれています。URLの形式は `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

### 成功応答の例 {#example-success-response}

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid integration ID` | `integration_id` が有効であることを確認してください。 |
| `404 Integration not found` | 指定された統合IDに対応する統合が存在しません。統合IDが有効であることを確認してください。 |
| `429 Another job is in progress` | この統合に対して現在同期が実行中です。同期が完了してから再度お試しください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

その他のステータスコードと関連するエラーメッセージについては、[致命的なエラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% endapi %}