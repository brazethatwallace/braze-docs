---
nav_title: "POST: Canvasの複製"
article_title: "POST: Canvasの複製"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「Canvasの複製」エンドポイントの詳細について説明します。"
---

{% api %}
# APIを使用したCanvasの複製 {#duplicate-canvases-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> このエンドポイントを使用して、Canvasを複製します。このAPIエンドポイントは、[BrazeダッシュボードでのCanvasの複製][1]に似ています。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.duplicate` 権限を持つAPIキーを生成する必要があります。

## レート制限 {#rate-limit}

このエンドポイントは、1分あたり100回のAPIコールに制限されます。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [Canvas識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `name` | 必須 | 文字列 | 作成されるCanvasの名前。 |
| `description` | オプション | 文字列 | 作成されるCanvasの説明フィールド。 |
| `tag_names` | オプション | 文字列 | 作成されるCanvasのタグ。これらは既存のタグである必要があります。リクエストに新しいタグを追加すると、元のCanvasにあったすべてのタグが上書きされます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## 応答 {#response}

このエンドポイントは `202` ステータスコードを返し、Canvasの作成は非同期で行われます。[セキュリティイベントのダウンロード][2]を使用すると、Canvasがいつ複製され、どのAPIキーによって行われたかの記録を確認できます。

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}