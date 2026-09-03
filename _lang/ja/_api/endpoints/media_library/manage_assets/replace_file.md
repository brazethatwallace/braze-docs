---
nav_title: "PUT: メディアライブラリのアセットを置換する"
article_title: "PUT: メディアライブラリのアセットを置換する"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、`PUT /media_library/replace_file` エンドポイントについて詳しく説明します。"
---

{% api %}
# メディアライブラリのアセットを置換する {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> このエンドポイントを使用して、[Brazeメディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications)内の既存アセットのファイルを、アセットIDとURLを保持したまま置換できます。置換ファイルは、外部ホストURL（`asset_url`）またはリクエストボディで送信するバイナリファイルデータ（`asset_file`）のいずれかで指定できます。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`media_library.replace` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## リクエストボディ {#request-body}

`asset_url` を含めると、エンドポイントはそのURLからファイルをダウンロードします。`asset_file` を含めると、エンドポイントはリクエストボディのバイナリデータを使用します。

`asset_url` のリクエストボディの例:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

`asset_file` のリクエストボディの例:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

リクエストボディには以下のパラメーターが含まれます:

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `asset_id` | 必須 | 文字列 | 置換するアセットのID。 |
| `asset_url` | オプション | 文字列 | 置換ファイルの公開アクセス可能なURL。 |
| `asset_file` | オプション | バイナリ | 置換ファイルのバイナリファイルデータ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストボディ" }

{% alert important %}
`asset_url` と `asset_file` は相互に排他的です。APIリクエストにはどちらか一方のみを含める必要があります。
{% endalert %}

### 置換ファイルの要件 {#replacement-file-requirements}

- 置換ファイルの拡張子は、既存アセットの拡張子と完全に一致する必要があります。たとえば、`.png` アセットを `.jpg` ファイルで置換することはできません。
- ファイルの置換は、画像、SVG、文書、フォント、連絡先カード、コードファイルでサポートされています。動画アセットは置換できません。

## リクエスト例 {#example-request}

このセクションには、URLを使用してアセットを置換する例と、バイナリファイルデータを使用する例の2つの `curl` リクエスト例が含まれています。

このリクエストは、`asset_url` を使用してメディアライブラリのアセットを置換する例です。

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

このリクエストは、`asset_file` を使用してメディアライブラリのアセットを置換する例です。

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### エラーレスポンス {#error-responses}

このセクションでは、発生する可能性のあるエラーとそれに対応するメッセージおよび説明を一覧にしています。

#### バリデーションエラー {#validation-errors}

バリデーションエラーは次のような構造を返します:

```json
{
  "message": (String) Human-readable error description
}
```

次の表は、発生する可能性のあるバリデーションエラーの一覧です。

| HTTPステータス | メッセージ | 説明 |
| --- | --- | --- |
| 400 | "asset_id is required." | リクエストにアセットIDが指定されていません。 |
| 400 | "Either file or asset_url is required." | `asset_file` も `asset_url` も指定されていません。いずれか一方が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バリデーションエラー" }

#### 処理エラー {#processing-errors}

処理エラーは、エラーコードを含む異なるレスポンスを返します:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

次の表は、発生する可能性のある処理エラーの一覧です。

| エラーコード | HTTPステータス | 説明 |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | 指定された `asset_id` のアセットがこのワークスペースに存在しません。`meta` オブジェクトには `asset_id` が含まれます。 |
| `INVALID_ASSET_URL` | 400 | `asset_url` の値が有効なURIではありません。`meta` オブジェクトには `asset_url` が含まれます。 |
| `EXTENSION_MISMATCH` | 400 | 置換ファイルの拡張子が既存アセットの拡張子と一致しません。`meta` オブジェクトには `expected_extension` と `received_extension` が含まれます。 |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | このアセットタイプ（動画など）ではファイルの置換がサポートされていません。`meta` オブジェクトには `asset_type` が含まれます。 |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | ファイルが許可される最大サイズを超えています。`meta` オブジェクトには `size_limit_bytes` と `file_size_bytes` が含まれます。 |
| `CORRUPT_FILE` | 400 | 画像ファイルが破損しているか読み取れません。`meta` オブジェクトには `file_name` が含まれます。 |
| `GENERIC_ERROR` | 500 | ファイルの置換中に予期しないエラーが発生しました。`meta` オブジェクトにはデバッグ用の `original_error` が含まれます。再試行するか、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="処理エラー" }

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`404`、`429`、`500` の5つのステータスコードレスポンスがあります。

以下のJSONは、レスポンスの想定される形式を示しています。

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}