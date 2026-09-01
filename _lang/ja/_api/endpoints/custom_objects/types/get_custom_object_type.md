---
nav_title: "GET: カスタムオブジェクトタイプの取得"
article_title: "GET: カスタムオブジェクトタイプの取得"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトタイプの取得エンドポイントについて説明します。"
---
{% api %}
# カスタムオブジェクトタイプの取得 {#get-custom-object-type}
{% apimethod get %}
/custom_objects/types/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、1つのカスタムオブジェクトタイプとそのスキーマ定義を返します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトAPIキーの権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト読み取りバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

次の表は、`/custom_objects/types/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトタイプの取得パスパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのパスパラメーターペイロードとサンプルのcURLリクエストが含まれます。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのパスパラメーターの参考として、次のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`account` カスタムオブジェクトタイプの定義を取得します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれます。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、次のレスポンスボディを返す可能性があります。

```json
{
  "custom_object_type": {
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
| `custom_object_type` | 必須 | Object | 返されるカスタムオブジェクトタイプレコード |
| `custom_object_type.type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `custom_object_type.metadata` | 必須 | Object | タイプメタデータオブジェクト |
| `custom_object_type.schema_def` | 必須 | Object | オブジェクト属性のJSONスキーマ定義 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトタイプの取得レスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つかりません (`custom-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と正確に一致していることを確認してください。 |
| `401` | REST APIキーが欠落しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.read` 権限があり、設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクトタイプの取得エラー" }
{% endapi %}