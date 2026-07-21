---
nav_title: "POST: メディアライブラリにアセットをアップロードする"
article_title: "POST: メディアライブラリにアセットをアップロードする"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、`POST /media_library/create` エンドポイントの詳細について説明します。"
---

{% api %}
# メディアライブラリにアセットをアップロードする {#upload-an-asset-to-the-media-library}
{% apimethod post %}
/media_library/create
{% endapimethod %}

> このエンドポイントを使用すると、外部でホストされているURL（`asset_url`）またはリクエスト本文で送信されたバイナリファイルデータ（`asset_file`）のいずれかを使用して、[Brazeメディアライブラリ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)にアセットを追加できます。このエンドポイントは画像と、画像を含むZIPファイルをサポートしています。

{% alert tip %}
このエンドポイントは、[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)から[`create_media_library_asset`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#media-library)関数を使用して呼び出すこともできます。これにより、ClaudeやCursorなどのAIツールが自然言語プロンプトを通じてメディアライブラリにアセットをアップロードできます。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`media_library.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## リクエスト本文 {#request-body}

`asset_url`を含めると、エンドポイントはURLからファイルをダウンロードします。`asset_file`を含めると、エンドポイントはリクエスト本文のバイナリデータを使用します。

`asset_url`のリクエスト本文の例：

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

`asset_file`のリクエスト本文の例：

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

リクエスト本文には以下のパラメーターが含まれます。

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `asset_url` | オプション | 文字列 | Brazeにアップロードするアセットの、一般にアクセス可能なURL。 |
| `asset_file` | オプション | バイナリ | バイナリファイルデータ。 |
| `name` | オプション | 文字列 | このアセットのメディアライブラリに表示される名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエスト本文" }

{% alert important %}
`asset_url`と`asset_file`は相互に排他的です。APIリクエストにはどちらか一方のみを含める必要があります。
{% endalert %}

### アップロードされたファイル名 {#uploaded-file-names}

このセクションでは、`name`パラメーターを含めるかどうかに基づいて、エンドポイントがアップロードされたファイルに名前を割り当てる方法について説明します。

#### 単一ファイルのアップロード {#single-file-uploads}

| シナリオ | 結果 |
| --- | --- |
| `name`を指定した場合 | `name`の値がメディアライブラリのアセット名として使用されます。 |
| `name`を省略した場合 | URLまたはアップロードされたファイルの元のファイル名が使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="単一ファイルのアップロード" }

#### ZIPファイルのアップロード {#zip-file-uploads}

| シナリオ | 結果 |
| --- | --- |
| `name`を指定した場合 | `name`の値がプレフィックスとして使用され、サフィックスとして連番が追加されます（例：「My File 1」、「My File 2」、「My File 3」）。 |
| `name`を省略した場合 | 各ファイルはZIPファイル内の元のファイル名を保持します。 |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="ZIPファイルのアップロード" }

## リクエスト例 {#example-request}

このセクションには2つの`curl`リクエスト例が含まれています。1つはURLを使用してアセットを追加する例、もう1つはバイナリファイルデータを使用する例です。

このリクエストは、`asset_url`を使用してメディアライブラリにアセットを追加する例を示しています。

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

このリクエストは、`asset_file`を使用してメディアライブラリにアセットを追加する例を示しています。

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### エラーレスポンス {#error-responses}

このセクションでは、発生する可能性のあるエラーとその対応するメッセージおよび説明を一覧にしています。

#### バリデーションエラー {#validation-errors}

バリデーションエラーは次のような構造を返します。

```json
{
  "message": (String) Human-readable error description
}
```

以下の表は、発生する可能性のあるバリデーションエラーの一覧です。

| HTTPステータス | メッセージ | 説明 |
| --- | --- | --- |
| 400 | "Either asset_url or asset_file must be provided." | リクエストにアセットパラメーターが指定されていません。 |
| 400 | "Both asset_url and asset_file cannot be provided. Please provide only one." | 両方のアセットパラメーターが指定されましたが、許可されているのは1つだけです。 |
| 403 | "Media Library Public APIs are not enabled for this company." | このワークスペースではメディアライブラリ機能が有効になっていません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バリデーションエラー" }

#### 処理エラー {#processing-errors}

処理エラーはエラーコード付きの異なるレスポンスを返します。

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

以下の表は、発生する可能性のある処理エラーの一覧です。

| エラーコード | HTTPステータス | 説明 |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | アップロードされたファイル形式はサポートされていません。`meta`オブジェクトには、拒否された`file_type`が含まれています。 |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | ファイルが最大許容サイズを超えています。画像には5 MBの制限があります。 |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | ワークスペースがアセットの最大数に達しました（無料トライアル企業ではデフォルトで200、それ以外は無制限）。`meta`オブジェクトには現在の`limit`が含まれています。 |
| `ASSET_UPLOAD_FAILED` | 400 | 処理の問題により、アセットのアップロードに失敗しました。 |
| `INVALID_ASSET_URL` | 400 | `asset_url`の値が有効なURIではありません。`meta`オブジェクトには`asset_url`が含まれています。 |
| `ZIP_UPLOAD_ERROR` | 400 | ZIPファイルが破損しているか、開くことができません。`meta`オブジェクトには`original_error`メッセージが含まれています。 |
| `ZIP_FILE_TOO_LARGE` | 400 | ZIPファイルの非圧縮時の合計サイズが5 MBの制限を超えています。`meta`オブジェクトには`zip_file_name`と`zip_file_size`が含まれています。 |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | ZIP内のファイルエントリに名前がありません。ZIPファイルが破損していないことを確認し、名前のないファイルエントリに名前を追加してください。 |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | ZIPファイルにネストされたディレクトリが含まれていますが、これはサポートされていません。すべてのファイルはZIPのルートレベルに配置する必要があります。 |
| `GENERIC_ERROR` | 500 | アップロード中に予期しないエラーが発生しました。`meta`オブジェクトにはデバッグ用の`original_error`メッセージが含まれています。再試行するか、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="処理エラー" }


## レスポンス {#response}

このエンドポイントには5つのステータスコードレスポンスがあります：`200`、`400`、`403`、`429`、および`500`。

以下のJSONは、レスポンスの想定される形式を示しています。

```json
{
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}