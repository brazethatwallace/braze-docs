---
nav_title: "POST: メールテンプレートの更新"
article_title: "POST: メールテンプレートの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートの更新」Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# 既存のメールテンプレートを更新する {#update-existing-email-templates}
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボードのメールテンプレートを更新します。

メールテンプレートの`email_template_id`には、**テンプレートとメディア**ページからアクセスできます。[メールテンプレートの作成エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)も`email_template_id`の参照を返します。

`email_template_id`以外のフィールドはすべてオプションですが、更新するフィールドを少なくとも1つ指定する必要があります。

{% alert tip %}
このエンドポイントは、[`update_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates)関数を使用して、[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)経由で呼び出すこともできます。これにより、ClaudeやCursorなどのAIツールが自然言語プロンプトを通じてメールテンプレートを更新できます。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## 前提条件 {#prerequisites}
このエンドポイントを使用するには、`templates.email.update`権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `email_template_id` | 必須 | 文字列 | [メールテンプレートのAPI識別子]({{site.baseurl}}/api/identifier_types)。|
| `template_name` | オプション | 文字列 | メールテンプレートの名前。|
| `subject` | オプション | 文字列 | メールテンプレートの件名。|
| `body` | オプション | 文字列 | HTMLを含む可能性のあるメールテンプレート本文。|
| `plaintext_body` | オプション | 文字列 | メールテンプレート本文のプレーンテキストバージョン。|
| `preheader` | オプション | 文字列 | 一部のクライアントでプレビューを生成するために使用されるメールプリヘッダー。|
| `tags` | オプション | 文字列 | [タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)はすでに存在している必要があります。|
| `should_inline_css` | オプション | ブール値 | テンプレートごとに`inline_css`機能を有効または無効にします。指定されない場合、BrazeはAppGroupのデフォルト設定を使用します。`true`または`false`のいずれかを指定します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## トラブルシューティング {#troubleshooting}

以下の表は、返される可能性のあるエラーと、該当する場合の関連するトラブルシューティングステップを示しています。

| エラー | トラブルシューティング |
| --- | --- |
| テンプレート名は必須です | テンプレート名を入力してください。 |
| タグは配列でなければなりません | タグは文字列の配列としてフォーマットする必要があります（例: `["marketing", "promotional", "transactional"]`）。 |
| すべてのタグは文字列でなければなりません | タグが引用符（`""`）で囲まれていることを確認してください。 |
| 一部のタグが見つかりませんでした | メールテンプレート作成時にタグを追加するには、そのタグがすでにBrazeに存在している必要があります。 |
| `should_inline_css`の値が無効です。`true`または`false`のいずれかが必要です | このパラメーターはブール値（trueまたはfalse）のみを受け付けます。`should_inline_css`の値が引用符（`""`）で囲まれていないことを確認してください。囲まれている場合、値は文字列として送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}