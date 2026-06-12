---
nav_title: "GET: ワークスペースアプリの一覧"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "この記事では、ワークスペースアプリの一覧を取得するBrazeエンドポイントについて詳しく説明します。"
---
{% api %}
# ワークスペースアプリの一覧 {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のアプリの名前とユニーク識別子（`api_key`）を一覧表示します。

このエンドポイントにリクエストを送信すると、`apps` というオブジェクト配列が返されます。`apps` 内の各オブジェクトには、アプリの名前とユニーク識別子が含まれています。

{% apiref postman %}  {% endapiref %}

## レート制限 {#rate-limit}

このエンドポイントには、1日（24時間）あたり100リクエストのレート制限があります。

## リクエストパラメーター {#request-parameters}

このリクエストにはパラメーターはありません。

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### トラブルシューティング {#troubleshooting}

以下の表は、返される可能性のあるエラーと、関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
| `401: Unauthorized` | APIキーに必要な権限がありません。APIキーに `apps.get` 権限があることを確認してください。 |
| `403: Forbidden` | この会社ではフィーチャーフリッパーが有効になっていません。カスタマーサクセスマネージャーにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}