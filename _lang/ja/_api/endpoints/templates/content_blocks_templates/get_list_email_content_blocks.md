---
nav_title: "GET: 利用可能なContent Blocksの一覧"
article_title: "GET: 利用可能なContent Blocksの一覧"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、利用可能なContent Blocksの一覧を取得するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 利用可能なContent Blocksの一覧 {#list-available-content-blocks}
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> このエンドポイントを使用して、既存の[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)情報を一覧表示します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`content_blocks.list` 権限を持つ[APIキー]({{site.baseurl}}/api/api_key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `modified_after` | オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列 | 指定した時刻以降に更新されたContent Blocksのみを取得します。 |
| `modified_before` | オプション | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列 | 指定した時刻以前に更新されたContent Blocksのみを取得します。 |
| `limit` | オプション | 正の数値 | 取得するContent Blocksの最大数。指定しない場合、デフォルトは100で、最大許容値は1000です。 |
| `offset` | オプション | 正の数値 | 検索条件に一致する残りのテンプレートを返す前にスキップするContent Blocksの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}

```json
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings
    }
  ]
}
```

## トラブルシューティング {#troubleshooting}

次の表に、返される可能性のあるエラーと、関連するトラブルシューティング手順を示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Modified after time is invalid` | 指定された日付は有効または解析可能な日付ではありません。この値をISO 8601形式（`yyyy-mm-ddThh:mm:ss.ffffff`）の文字列に再フォーマットしてください。 |
| `Modified before time is invalid` | 指定された日付は有効または解析可能な日付ではありません。この値をISO 8601形式（`yyyy-mm-ddThh:mm:ss.ffffff`）の文字列に再フォーマットしてください。 |
| `Modified after time must be earlier than or the same as modified before time.` | `modified_after` の値を `modified_before` の時刻より前の時刻に変更してください。 |
| `Content Block number limit is invalid` | `limit` パラメーターは0より大きい整数（正の数値）でなければなりません。 |
| `Content Block number limit must be greater than 0` | `limit` パラメーターを0より大きい整数に変更してください。 |
| `Content Block number limit exceeds maximum of 1000` | `limit` パラメーターを1000未満の整数に変更してください。 |
| `Offset is invalid` | `offset` パラメーターは0より大きい整数でなければなりません。 |
| `Offset must be greater than 0` | `offset` パラメーターを0より大きい整数に変更してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}