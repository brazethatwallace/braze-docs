---
nav_title: エラーと応答
article_title: APIエラーと応答
description: "この参考記事では、Braze APIの使用中に発生する可能性のあるさまざまなエラーとサーバー応答、およびそれらのトラブルシューティング方法について説明します。"
page_type: reference
page_order: 2.3

---
# APIのエラーと応答 {#api-errors-and-responses}

> この参考記事では、Braze APIの使用中に発生する可能性のあるさまざまなエラーとサーバー応答、およびそれらのトラブルシューティング方法について説明します。

## サーバーの応答 {#server-responses}

POSTペイロードがサーバーで受理された場合、成功メッセージには以下の応答が返されます：

```json
{
  "message" : "success"
}
```

成功とは、RESTful APIのペイロードが正しく形成され、プッシュ通知やメール、その他のメッセージングサービスに渡されたことのみを意味します。メッセージが実際に配信されたことを意味するわけではありません。追加の要因によって配信が妨げられる可能性があるためです（例えば、デバイスがオフライン状態である場合、プッシュトークンがAppleのサーバーによって拒否される場合、あるいは不明なユーザーIDが提供された場合など）。

[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)のようなメッセージを送信しないエンドポイントの場合、成功メッセージは単にBrazeが処理リクエストを受信したことを意味します。処理後にエイリアスに一致するものが存在しない場合、リクエストは停止されます。

メッセージの送信が成功したが、致命的ではないエラーが発生した場合、以下の応答が返されます：

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

成功した場合、`errors`配列内のエラーの影響を受けなかったメッセージはすべて配信されます。メッセージに致命的なエラーがある場合、以下の応答を受け取ります：

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## 追跡された送信IDに対する応答 {#responses-for-tracked-send-ids}

分析は常にCampaignsで利用できます。さらに、Campaignがブロードキャストとして送信された場合、特定のCampaign送信インスタンスに対して分析が利用できます。特定のCampaign送信インスタンスに対してトラッキングが利用可能な場合、以下の応答を受け取ります：

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

指定された送信IDは、`/send/data_series`エンドポイントのパラメーターとして使用して、送信固有の分析を取得できます。

## エラー {#errors}

サーバー応答のステータスコード要素は3桁の数字であり、コードの最初の桁が応答のクラスを定義します。

- **2XXクラス**のステータスコード（致命的ではない）は、**リクエスト**が正常に受信され、理解され、受け入れられたことを示します。
- **4XXクラス**のステータスコード（致命的）は、**クライアントエラー**を示します。4XXエラーコードの全リストと説明については、致命的エラーチャートを参照してください。
- **5XXクラス**のステータスコード（致命的）は、**サーバーエラー**を示します。考えられる原因はいくつかあります。たとえば、アクセスしようとしているサーバーがリクエストを実行できない、サーバーがメンテナンス中でリクエストを実行できない、サーバーのトラフィックが高いレベルになっているなどです。このような場合、エクスポネンシャルバックオフでリクエストを再試行することを推奨します。インシデントまたは停止が発生した場合、Brazeはインシデント期間中に失敗したREST API呼び出しを再実行することはできません。インシデント期間中に失敗した呼び出しはすべて再試行する必要があります。
  - **502エラー**は、送信先サーバーに到達する前に発生した失敗です。
  - **503エラー**は、リクエストが送信先サーバーに到達したが、十分な容量がない、ネットワークに問題がある、または同様の理由でリクエストを完了できないことを意味します。
  - **504エラー**は、サーバーが上流の別のサーバーから応答を受信しなかったことを示します。

### 致命的なエラー {#fatal-errors}

リクエストが致命的なエラーに遭遇した場合、以下のステータスコードと関連するエラーメッセージが返されます。

{% alert warning %}
以下のエラーコードはすべて、メッセージが送信されないことを示しています。
{% endalert %}

| エラーコード | 説明 |
|---|---|
| `5XX Internal Server Error` | エクスポネンシャルバックオフでリクエストを再試行してください。|
| `400 Bad Request` | 構文が正しくありません。|
| `400 No Recipients` | リクエストにexternal IDやSegment ID、プッシュトークンがありません。|
| `400 Invalid Campaign ID` | 入力されたCampaign IDに該当するメッセージングAPI Campaignが見つかりませんでした。|
| `400 Message Variant Unspecified` | Campaign IDは提供されていますが、メッセージバリエーションIDが提供されていません。|
| `400 Invalid Message Variant` | 有効なCampaign IDを入力しましたが、メッセージバリエーションIDがそのCampaignのどのメッセージとも一致しません。|
| `400 Mismatched Message Type` | 少なくとも1つのメッセージに、誤ったメッセージタイプのメッセージバリエーションを指定しました。|
| `400 Invalid Extra Push Payload` | `apple_push`または`android_push`のいずれかに`extra`キーを指定しましたが、それはディクショナリではありません。|
| `400 Max Input Length Exceeded` | `/users/track`の場合、このエラーは単一のリクエストで許可されるオブジェクトの最大数を超えたことが原因です。制限はレート制限モデルによって異なります。ほとんどのお客様の場合、各リクエストは`attributes`、`events`、`purchases`を合わせて最大75個のオブジェクトをサポートします。レガシーレート制限を使用しているお客様の場合、各配列は最大75個のオブジェクトを独立してサポートします。詳細については、[POST: ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を参照してください。|
| `400 The max number of external_ids and aliases per request was exceeded` | 50を超えるexternal IDを呼び出したことが原因です。|
| `400 The max number of ids per request was exceeded` | 50を超えるexternal IDを呼び出したことが原因です。|
| `400 No message to send` | メッセージにペイロードが指定されていません。|
| `400 Slideup Message Length Exceeded` | スライドアップメッセージが140文字を超えています。|
| `400 Apple Push Length Exceeded` | JSONペイロードが1,912バイトを超えています。|
| `400 Android Push Length Exceeded` | JSONペイロードが4,000バイトを超えています。|
| `400 Bad Request` | `send_at`の日時を解析できません。|
| `400 Bad Request` | リクエストで`in_local_time`がtrueですが、会社のタイムゾーンで`time`が既に経過しています。|
| `401 Unauthorized` | 無効なAPIキーです。一般的な原因は以下の通りです：<br><br>- **Authorizationヘッダーが欠落しているか、形式が正しくありません。** ヘッダーの値は`Bearer`の後にスペースとAPIキーを続ける必要があります：`Authorization: Bearer YOUR-API-KEY`。よくある間違いとして、`Bearer`の省略、`Bearer`の後のキーの省略、値を引用符で囲むことなどがあります。<br>- **RESTエンドポイントが間違っています。** リクエストを間違った[インスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)に送信しています。たとえば、アカウントがEUインスタンス（`https://dashboard-01.braze.eu`）にある場合、リクエストは`https://rest.fra-01.braze.eu`に送信する必要があります。<br>- **権限が不十分です。** 各APIキーは特定のワークスペースと権限のセットにスコープされています。ダッシュボードの**設定** > **APIキー**でキーの権限を確認してください。<br>- **APIキーが間違っています。** APIキーはワークスペース固有です。あるワークスペースのキーを別のワークスペースのリクエスト認証に使用することはできません。 |
| `403 Forbidden` | 料金プランが対応していない、またはアカウントが無効になっています。|
| `403 Access Denied` | 使用しているREST APIキーに十分な権限がありません。一般的な原因は以下の通りです：{::nomarkdown}<ul><li><strong>APIキーが機能より前に作成されています。</strong>APIキーが機能のリリース前に作成された場合（サブスクリプショングループやカタログなど）、そのキーはそれらの権限を自動的に継承しません。<strong>設定</strong> &gt; <strong>APIキー</strong>で必要な権限を持つ新しいAPIキーを作成してください。</li><li><strong>エンドポイント固有の権限がありません。</strong>各APIエンドポイントには特定の権限スコープが必要です（例：<code>users.track</code>や<code>email.status</code>）。キーの権限が呼び出しているエンドポイントと一致していることを確認してください。</li><li><strong>URLに末尾のスラッシュまたはタイプミスがあります。</strong>たとえば、<code>/users/track</code>の代わりに<code>/users/track/</code>（末尾にスラッシュあり）を使用すると、予期しないエラーが発生する可能性があります。</li></ul>{:/}|
| `404 Not Found` | 無効なURLです。 |
| `415 Unsupported Media Type` | `Content-Type`リクエストヘッダーが欠落しているか、正しくありません。**設定**ページで、`Content-Type`に`application/json`の値を追加してください。 |
| `429 Rate Limited` | レート制限を超えています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="致命的なエラー" }