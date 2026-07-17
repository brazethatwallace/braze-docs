---
nav_title: "POST: キャンバスの複製"
article_title: "POST: キャンバスの複製"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「キャンバスの複製」エンドポイントの詳細について説明します。"
---

{% api %}
# APIを使用したキャンバスの複製 {#duplicate-canvases-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> このエンドポイントを使用して、キャンバスを複製します。このAPIエンドポイントは、[Brazeダッシュボードでのキャンバスの複製]({{site.baseurl}}/user_guide/messaging/governance/duplicating)に似ています。

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
  "tag_names": (optional, array of strings) The tags of the resulting Canvas,
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [キャンバス識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `name` | 必須 | 文字列 | 作成されるキャンバスの名前。 |
| `description` | オプション | 文字列 | 作成されるキャンバスの説明フィールド。 |
| `tag_names` | オプション | 文字列の配列 | 作成されるキャンバスのタグ。これらは既存のタグである必要があります。リクエストに新しいタグを追加すると、元のキャンバスにあったすべてのタグが上書きされます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## レスポンス {#response}

このエンドポイントは `202` ステータスコードを返し、キャンバスの作成は非同期で行われます。[セキュリティイベントのダウンロード]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)を使用すると、キャンバスがいつ複製され、どのAPIキーによって行われたかの記録を確認できます。

{% endapi %}