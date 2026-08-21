---
nav_title: エラーと応答
article_title: APIエラーと応答
description: "この参考記事では、Braze APIの使用中に発生する可能性のあるさまざまなエラーとサーバー応答、およびそれらのトラブルシューティング方法について説明します。"
page_type: reference
page_order: 2.3

---
# APIのエラーと応答 {#api-errors-and-responses}

> この参考記事では、Braze APIの使用中に発生する可能性のあるさまざまなエラーとサーバー応答、およびそれらのトラブルシューティング方法について説明します。

## サーバーレスポンス {#server-responses}

POST ペイロードがサーバーに受け入れられた場合、成功したメッセージには以下のレスポンスが返されます。

```json
{
  "message" : "success"
}
```

成功は、RESTful API ペイロードが正しく構成され、プッシュ通知やメールなどのメッセージングサービスに渡されたことのみを意味します。メッセージが実際に配信されたことを意味するものではありません。メッセージの配信を妨げる追加の要因が存在する可能性があるためです（例えば、デバイスがオフラインである、プッシュトークンが Apple のサーバーによって拒否された、不明なユーザー ID を指定したなど）。

### リクエストが成功を返すのにメッセージが配信されないのはなぜですか？ {#why-does-my-request-return-success-when-no-message-was-delivered}

`message: success` または `2XX` レスポンスは、Braze が関連するエンドポイントのリクエストを受け入れてキューに入れたことを意味します。すべての受信者がメッセージを受け取ったことを意味するものではありません。メッセージングの場合、配信はチャネルの適格性、トークン、プロバイダーエラー、およびコンテンツのバリデーションに依存します。送信をブロックする HTTP エラーについては[致命的なエラー]({{site.baseurl}}/api/errors#fatal-errors)テーブルを参照し、ダウンストリームの配信指標についてはキャンペーンまたはキャンバスの分析を確認してください。

メッセージを送信しない[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)のようなエンドポイントの場合、成功メッセージは Braze がリクエストを処理のために受信したことのみを意味します。処理後にエイリアスに一致するものがない場合、リクエストは停止されます。

メッセージが成功したが致命的でないエラーがある場合、以下のレスポンスが返されます。

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

成功の場合、`errors` 配列のエラーの影響を受けなかったメッセージは引き続き配信されます。メッセージに致命的なエラーがある場合、以下のレスポンスが返されます。

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## トラッキング対象の送信IDに対するレスポンス {#responses-for-tracked-send-ids}

分析はキャンペーンに対して常に利用できます。さらに、キャンペーンがブロードキャストとして送信された場合、特定のキャンペーン送信インスタンスに対しても分析を利用できます。特定のキャンペーン送信インスタンスに対してトラッキングが利用可能な場合、以下のレスポンスが返されます。

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

提供された送信IDは、`/send/data_series`エンドポイントのパラメーターとして使用して、送信固有の分析を取得できます。

## エラー {#errors}

サーバーレスポンスのステータスコード要素は3桁の数字で、コードの最初の桁がレスポンスのクラスを定義します。

- **2XXクラス**のステータスコード（致命的でない）は、**リクエスト**が正常に受信、理解、受理されたことを示します。
- **4XXクラス**のステータスコード（致命的）は、**クライアントエラー**を示します。4XXエラーコードと説明の完全な一覧については、致命的エラーの表を参照してください。
- **5XXクラス**のステータスコード（致命的）は、**サーバーエラー**を示します。考えられる原因はいくつかあります。たとえば、アクセスしようとしているサーバーがリクエストを実行できない、サーバーがメンテナンス中でリクエストを実行できない、サーバーが高レベルのトラフィックを経験しているなどです。この場合は、指数バックオフを使用してリクエストを再試行することをお勧めします。インシデントまたは障害が発生した場合、Brazeはインシデント期間中に失敗したREST API呼び出しを再実行することはできません。インシデント期間中に失敗した呼び出しは再試行する必要があります。
  - **502エラー**は、宛先サーバーに到達する前に発生した障害です。
  - **503エラー**は、リクエストが宛先サーバーに到達したものの、容量不足やネットワークの問題などにより、リクエストを完了できないことを意味します。
  - **504エラー**は、サーバーが上流の別のサーバーからレスポンスを受信しなかったことを示します。

### 致命的エラー {#fatal-errors}

リクエストで致命的エラーが発生した場合、以下のステータスコードと関連するエラーメッセージが返されます。

{% alert warning %}
以下のエラーコードはすべて、メッセージが送信されないことを示しています。
{% endalert %}

| エラーコード | 説明 |
|---|---|
| `5XX Internal Server Error` | 指数バックオフを使用してリクエストを再試行してください。|
| `400 Bad Request` | 構文不正。無効なJSONはHTTP 400を返します。`error`フィールドには、リクエストボディに有効な`application/json`を渡す必要があるというメッセージ、または`Error while parsing request body. Please check your syntax.`が含まれる場合があります。[リクエストボディの解析エラー](#error-while-parsing-request-body)を参照してください。|
| `400 No Recipients` | リクエストにexternal ID、セグメントID、またはプッシュトークンがありません。|
| `400 Invalid キャンペーン ID` | 指定されたキャンペーンIDに対応するメッセージングAPIキャンペーンが見つかりません。|
| `400 Message Variant Unspecified` | キャンペーンIDは指定されていますが、メッセージバリアントIDが指定されていません。|
| `400 Invalid Message Variant` | 有効なキャンペーンIDが指定されていますが、メッセージバリアントIDがそのキャンペーンのメッセージのいずれとも一致しません。|
| `400 Mismatched Message Type` | 少なくとも1つのメッセージに対して、誤ったメッセージタイプのメッセージバリアントが指定されています。|
| `400 Invalid Extra Push Payload` | `apple_push`または`android_push`に`extra`キーが指定されていますが、ディクショナリではありません。|
| `400 Max Input Length Exceeded` | `/users/track`の場合、このエラーは単一のリクエストで許可されるオブジェクトの最大数を超えたことが原因です。制限はレートリミットモデルによって異なります。ほとんどのお客様の場合、各リクエストは`attributes`、`events`、`purchases`を合わせて最大75個のオブジェクトをサポートします。レガシーレートリミットを使用しているお客様の場合、各配列は最大75個のオブジェクトを独立してサポートします。詳細については、[POST：ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を参照してください。|
| `400 The max number of external_ids and aliases per request was exceeded` | 50個を超えるexternal IDを呼び出したことが原因です。|
| `400 The max number of ids per request was exceeded` | 50個を超えるexternal IDを呼び出したことが原因です。|
| `400 No message to send` | メッセージのペイロードが指定されていません。|
| `400 Slideup Message Length Exceeded` | スライドアップメッセージが140文字を超えています。|
| `400 Apple Push Length Exceeded` | JSONペイロードが1,912バイトを超えています。|
| `400 Android Push Length Exceeded` | JSONペイロードが4,000バイトを超えています。|
| `400 Bad Request` | `send_at`の日時を解析できません。|
| `400 Bad Request` | リクエストで`in_local_time`がtrueに設定されていますが、会社のタイムゾーンでは`time`がすでに過ぎています。|
| `401 Unauthorized` | 無効なAPIキーです。一般的な原因は次のとおりです。<br><br>- **Authorizationヘッダーの欠落または不正な形式。**ヘッダーの値は`Bearer`の後にスペース、続いてAPIキーの形式にする必要があります：`Authorization: Bearer YOUR-API-KEY`。よくある間違いには、`Bearer`の省略、`Bearer`の後のキーの省略、値を引用符で囲むことなどがあります。<br>- **RESTエンドポイントの誤り。**リクエストを間違った[インスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)に送信しています。たとえば、アカウントがEUインスタンス（`https://dashboard-01.braze.eu`）にある場合、リクエストは`https://rest.fra-01.braze.eu`に送信する必要があります。<br>- **権限の不足。**各APIキーは特定のワークスペースと権限のセットにスコープされています。ダッシュボードの**設定** > **APIキー**でキーの権限を確認してください。<br>- **APIキーの誤り。**APIキーはワークスペース固有です。あるワークスペースのキーを別のワークスペースのリクエストの認証に使用することはできません。 |
| `403 Forbidden` | 料金プランがサポートしていないか、アカウントが無効化されています。|
| `403 Access Denied` | 使用しているREST APIキーに十分な権限がありません。一般的な原因は次のとおりです。{::nomarkdown}<ul><li><strong>APIキーが機能より前に作成された。</strong>APIキーが機能のリリース前（購読グループやカタログなど）に作成された場合、キーはそれらの権限を自動的に継承しません。<strong>設定</strong> &gt; <strong>APIキー</strong>で必要な権限を持つ新しいAPIキーを作成してください。</li><li><strong>エンドポイント固有の権限の欠落。</strong>各APIエンドポイントには特定の権限スコープが必要です（たとえば、<code>users.track</code>や<code>email.status</code>）。キーの権限が呼び出しているエンドポイントと一致していることを確認してください。</li><li><strong>URLの末尾のスラッシュまたはタイプミス。</strong>たとえば、<code>/users/track</code>の代わりに<code>/users/track/</code>（末尾にスラッシュあり）を使用すると、予期しないエラーが発生する可能性があります。</li></ul>{:/}|
| `404 Not Found` | 無効なURLです。 |
| `415 Unsupported Media Type` | `Content-Type`リクエストヘッダーが欠落しているか、正しくありません。**設定**ページで、`Content-Type`を値`application/json`で追加してください。 |
| `429 Rate Limited` | レートリミットを超えています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="致命的エラー" }

### リクエストボディの解析エラー {#error-while-parsing-request-body}

リクエストボディが有効なJSONでない場合、BrazeはHTTP 400を返します。これは、POST、PUT、PATCHなど、JSONボディを受け付けるRESTエンドポイントに適用されます。

`error`フィールドには、リクエストボディに有効な`application/json`を渡す必要があるというメッセージが含まれます。`Error while parsing request body. Please check your syntax.`と表示される場合もあります。

一般的な原因には、末尾のカンマ、JSON内のコメント、シングルクォートの文字列、ペイロードの前の余分な開き`{`、またはJSONエンコードされたオブジェクトの代わりに連結された文字列の送信などがあります。

再試行する前に：

1. JSONリンターでペイロードを検証してください。
2. `Content-Type: application/json`を設定し、UTF-8エンコードのJSONを送信してください。
3. HTTPクライアントが生の文字列を連結するのではなく、オブジェクトをJSONエンコードしていることを確認してください。

`/users/track`のペイロードサイズとリクエストごとのオブジェクト制限については、[構文不正または解析エラーで`400 Bad Request`が返されるのはなぜですか？]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error)を参照してください。