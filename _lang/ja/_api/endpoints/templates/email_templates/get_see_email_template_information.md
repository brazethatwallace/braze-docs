---
nav_title: "GET: メールテンプレート情報の表示"
article_title: "GET: メールテンプレート情報の表示"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、メールテンプレートの表示Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# メールテンプレート情報の表示 {#see-email-template-information}
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> このエンドポイントを使用して、メールテンプレートに関する情報を取得します。

{% alert important %}
メール用のドラッグ＆ドロップエディターを使用して作成されたテンプレートは受け付けられません。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## 前提条件 {#prerequisites}
このエンドポイントを使用するには、`templates.email.info` 権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `email_template_id` | 必須 | 文字列 | [メールテンプレートAPI識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## レスポンス {#response}

```json
{
  "email_template_id": (string) Your email template's API Identifier,
  "template_name": (string) The name of your email template,
  "description": (string) The email template description,
  "subject": (string) The email template subject line,
  "preheader": (optional, string) The email preheader used to generate previews in some clients),
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) Tag names,
  "created_at": (string) The time the email was created at in ISO 8601,
  "updated_at": (string) The time the email was updated in ISO 8601
}
```

このレスポンスの画像は、HTMLとして `body` 変数に表示されます。

{% endapi %}