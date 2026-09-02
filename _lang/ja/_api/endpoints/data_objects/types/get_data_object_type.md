---
nav_title: "GET: データオブジェクトタイプの取得"
article_title: "GET: データオブジェクトタイプの取得"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトタイプの取得エンドポイントの詳細について説明します。"
---
{% api %}
# データオブジェクトタイプの取得 {#get-data-object-type}
{% apimethod get %}
/data_objects/types/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、1つのデータオブジェクトタイプとそのスキーマ定義を返します。

{% alert important %}
データオブジェクトは現在、早期アクセス中です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントは、データオブジェクト読み取りバケットに属し、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

次の表は、`/data_objects/types/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトタイプの取得パスパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのパスパラメーターペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのパスパラメーターの参照として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`account` データオブジェクトタイプの定義を取得します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功時のサンプルレスポンスとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "data_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def` は許可されたオブジェクトフィールドを記述します。このレスポンススキーマは説明的なものですが、書き込み時には宣言されていないフィールドは拒否されます。

### レスポンスパラメーター {#response-parameters}

次の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `data_object_type` | 必須 | Object | 返されるデータオブジェクトタイプのレコード |
| `data_object_type.type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `data_object_type.metadata` | 必須 | Object | タイプメタデータオブジェクト |
| `data_object_type.schema_def` | 必須 | Object | オブジェクト属性のJSONスキーマ定義 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトタイプの取得レスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つかりません (`data-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と完全に一致することを確認してください。 |
| `401` | REST APIキーが未設定または無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `data_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超えました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクトタイプの取得エラー" }
{% endapi %}