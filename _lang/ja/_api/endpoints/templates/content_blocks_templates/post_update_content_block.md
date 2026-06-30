---
nav_title: "POST:コンテンツブロックを更新する"
article_title: "POST:コンテンツブロックを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「コンテンツブロックを更新する」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# コンテンツブロックを更新する {#update-content-block}
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> このエンドポイントを使用して、[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)を更新します。

{% alert tip %}
このエンドポイントは、[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)から[`update_content_block`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#content-blocks)関数を使用して呼び出すこともできます。これにより、ClaudeやCursorなどのAIツールが自然言語プロンプトを通じてコンテンツブロックを更新できます。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## 前提条件 {#prerequisites}
このエンドポイントを使用するには、`content_blocks.update` 権限を持つ[APIキー]({{site.baseurl}}/api/api_key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `content_block_id` | 必須 | 文字列 | コンテンツブロックのAPI識別子。|
| `name` | オプション | 文字列 | コンテンツブロックの名前。100文字未満でなければなりません。 |
| `description` | オプション | 文字列 | コンテンツブロックの説明。250文字未満でなければなりません。 |
| `content` | オプション | 文字列 | Content Blocks内のHTMLまたはテキストコンテンツ。 |
| `state` | オプション | 文字列 | `active` または `draft` を選択します。指定がない場合のデフォルトは `active` です。 |
| `tags` | オプション | 文字列の配列 | [タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)はすでに存在している必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```bash
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## 応答 {#response}

```json
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

次の表に、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Content cannot be blank` | |
| `Content must be a string` | コンテンツが引用符（`""`）で囲まれていることを確認してください。 |
| `Content must be smaller than 50kb` | コンテンツブロックのコンテンツは合計50KB未満である必要があります。 |
| `Content contains malformed liquid` | 指定されたLiquidは有効でないか、解析できません。有効なLiquidで再試行するか、サポートにお問い合わせください。 |
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | コンテンツブロックの説明が引用符（`""`）で囲まれていることを確認してください。 |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
| `Content Block name can only contain alphanumeric characters` | コンテンツブロック名には、文字（大文字または小文字）`A` ～ `Z`、数字 `0` ～ `9`、ダッシュ `-`、アンダースコア `_` のいずれかを含めることができます。絵文字、`!`、`@`、`~`、`&`、その他の「特殊」文字など、英数字以外の文字を含めることはできません。 |
| `Content Block with this name already exists` | 別の名前をお試しください。 |
| `Content Block name cannot be updated for active Content Blocks` | |
| `Content Block state must be either active or draft` | |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` | |
| `Tags must be an array` | タグは文字列の配列としてフォーマットする必要があります（例: `["marketing", "promotional", "transactional"]`）。 |
| `All tags must be strings` | タグが引用符（`""`）で囲まれていることを確認してください。 |
| `Some tags could not be found` | コンテンツブロックの作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }


{% endapi %}