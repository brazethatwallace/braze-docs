---
nav_title: "GET: 統合一覧の取得"
article_title: "GET: 統合一覧の取得"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "この記事では、「統合一覧の取得」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 統合一覧の取得 {#list-integrations}
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> このエンドポイントを使用して、既存の統合の一覧を返します。


{% alert note %}
このエンドポイントを使用するには、`cdi.integration_list` 権限を持つAPIキーを生成する必要があります。
{% endalert %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## クエリパラメーター {#query-parameters}

このエンドポイントへの各呼び出しでは、10件のアイテムが返されます。10件を超える統合があるリストについては、応答例に示すように、`Link` ヘッダーを使用して次のページのデータを取得してください。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | 統合リストのページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエスト例 {#example-request}

### カーソルなし {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答本文を返す可能性があります。

{% alert note %}
統合の合計が10件以下の場合、`Link` ヘッダーは存在しません。カーソルなしの呼び出しでは、`prev` は表示されません。アイテムの最後のページを表示している場合、`next` は表示されません。
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601
    }
  ],
  "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

次の表に、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid cursor` | `cursor` が有効であることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

その他のステータスコードと関連するエラーメッセージについては、[致命的なエラーと応答]({{site.baseurl}}/api/errors#fatal-errors)を参照してください。

{% endapi %}