---
nav_title: "GET: Content Blocksの情報を見る"
article_title: "GET: Content Blocksの情報を見る"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Content Blocksの情報を見るBrazeエンドポイントの詳細について概説します。"
---

{% api %}
# Content Blocksの情報を見る {#see-content-block-information}
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> このエンドポイントを使用して、既存の[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)の情報を呼び出します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## 前提条件 {#prerequisites}
このエンドポイントを使用するには、`content_blocks.info` 権限を持つ[APIキー]({{site.baseurl}}/api/api_key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `content_block_id`  | 必須 | 文字列 | コンテンツブロックの識別子。<br><br>これは、APIコールでコンテンツブロックの情報をリストアップするか、[APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページに移動し、一番下までスクロールしてコンテンツブロックのAPI識別子を検索することで見つけることができます。|
| `include_inclusion_data`  | オプション | ブール値 | `true` に設定された場合、APIはこのコンテンツブロックが含まれるキャンペーンおよびキャンバスのメッセージバリエーションAPI識別子を返し、以降の呼び出しで使用できるようにします。結果には、アーカイブまたは削除されたキャンペーンやキャンバスは含まれません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答 {#response}

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Content Block ID cannot be blank` | コンテンツブロックがリクエストにリストされ、引用符（`""`）で囲まれていることを確認してください。 |
| `Content Block ID is invalid for this workspace` | このコンテンツブロックは存在しないか、別の会社アカウントまたはワークスペースにあります。 |
| `Content Block has been deleted—content not available` | このコンテンツブロックは、以前は存在していた可能性がありますが、削除されています。 |
| `Include Inclusion Data—error` | このパラメーターはブール値（true または false）のみを受け付けます。`include_inclusion_data` の値が引用符（`""`）で囲まれていないことを確認してください。囲まれている場合、値は文字列として送信されます。詳細については、[リクエストパラメーター](#request-parameters)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }


{% endapi %}