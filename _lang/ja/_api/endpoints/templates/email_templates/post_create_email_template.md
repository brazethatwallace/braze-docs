---
nav_title: "POST: メールテンプレートを作成する"
article_title: "POST: メールテンプレートを作成する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Brazeのメールテンプレート作成エンドポイントの詳細について説明します。"
---
{% api %}
# メールテンプレートを作成する {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボードでメールテンプレートを作成します。

これらのテンプレートは**テンプレートとメディア**ページで利用できます。このエンドポイントからのレスポンスには`email_template_id`フィールドが含まれており、後続のAPI呼び出しでテンプレートを更新するために使用できます。

{% alert tip %}
このエンドポイントは、[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)を通じて[`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates)関数を使用して呼び出すこともできます。これにより、ClaudeやCursorなどのAIツールが自然言語プロンプトを通じてメールテンプレートを作成できます。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## 前提条件 {#prerequisites}
このエンドポイントを使用するには、`templates.email.create`権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `template_name` | 必須 | 文字列 | メールテンプレートの名前。 |
| `subject` | 必須 | 文字列 | メールテンプレートの件名。 |
| `body` | 必須 | 文字列 | HTMLを含むことができるメールテンプレート本文。最大400&nbsp;KB。 |
| `plaintext_body` | オプション | 文字列 | メールテンプレート本文のプレーンテキストバージョン。 |
| `preheader` | オプション | 文字列 | 一部のクライアントでプレビューを生成するために使用されるメールプリヘッダー。 |
| `tags` | オプション | 文字列 | [タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)はすでに存在している必要があります。 |
| `should_inline_css` | オプション | ブール値 | テンプレートごとに`inline_css`機能を有効または無効にします。指定されない場合、Brazeはアプリグループのデフォルト設定を使用します。`true`または`false`のいずれかが期待されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## レスポンス例 {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

以下の表は、返される可能性のあるエラーと、該当する場合の関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
| テンプレート名は必須です | テンプレート名を入力してください。 |
| タグは配列でなければなりません | タグは文字列の配列としてフォーマットする必要があります。例: `["marketing", "promotional", "transactional"]`。 |
| すべてのタグは文字列でなければなりません | タグが引用符（`""`）で囲まれていることを確認してください。 |
| 一部のタグが見つかりませんでした | メールテンプレート作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要があります。 |
| メールには有効なContent Blocks名が必要です | メールにこの環境に存在しないContent Blocksが含まれている可能性があります。 |
| `should_inline_css`の値が無効です。`true`または`false`のいずれかが期待されます | このパラメーターはブール値（trueまたはfalse）のみを受け付けます。`should_inline_css`の値が引用符（`""`）で囲まれていないことを確認してください。囲まれている場合、値は文字列として送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}