---
page_order: 1.5
nav_title: 詳細ログの読み取り
article_title: 詳細ログの読み取り
description: "Braze SDKからの詳細ログ出力の読み方と解釈方法について説明します。プッシュ通知、アプリ内メッセージ、Content Cards、ディープリンクに関する主要なエントリが含まれます。"
---

# 詳細ログの読み取り {#reading-verbose-logs}

> このページでは、Braze SDKからの詳細ログ出力を解釈する方法について説明します。各メッセージングチャネルについて、確認すべき主要なログエントリ、その意味、および注意すべき一般的な問題を紹介します。

始める前に、[詳細ログの有効化]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)が完了していることと、お使いのプラットフォームでログを収集する方法を把握していることを確認してください。

## セッション {#sessions}

セッションはBrazeの分析とメッセージ配信の基盤です。アプリ内メッセージやContent Cardsを含む多くのメッセージング機能は、正常に動作するために有効なセッションが開始されている必要があります。セッションが正しく記録されていない場合は、まずこの問題を調査してください。セッショントラッキングの有効化に関する詳細については、[ステップ5: ユーザーセッショントラッキングを有効にする]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking)を参照してください。

### 主要なログエントリ {#key-log-entries}

{% tabs %}
{% tab Swift %}

**セッション開始：**

```
Started user session (id: <SESSION_ID>)
```

**セッション終了：**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**セッション開始：**

以下のエントリを確認してください：

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのネットワークリクエストをフィルターし、セッション開始（`ss`）イベントを確認します。

**セッション終了：**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### 確認すべき事項 {#what-to-check}

- アプリ起動時にセッション開始ログが表示されることを確認してください。
- セッション開始が表示されない場合は、SDKが正しく初期化されていること、および`openSession`（Android）が呼び出されていることを確認してください。
- Androidでは、Brazeエンドポイントへのネットワークリクエストが行われていることを確認してください。表示されない場合は、APIキーとエンドポイントの設定を確認してください。

## プッシュ通知 {#push-notifications}

プッシュ通知ログは、デバイストークンが登録されていること、通知が配信されていること、クリックイベントがトラッキングされていることを確認するのに役立ちます。

### トークン登録 {#token-registration}

セッションが開始されると、SDKはデバイスのプッシュトークンをBrazeに登録します。

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエスト本体の属性内で`push_token`を探してください：

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

また、デバイス情報に以下が含まれていることを確認してください：

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

FCM登録ログを探してください：

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

以下を確認してください：

- `com_braze_firebase_cloud_messaging_registration_enabled`が`true`であること。
- FCM送信者IDがFirebaseプロジェクトと一致していること。

よくあるエラーは`SENDER_ID_MISMATCH`で、設定された送信者IDがFirebaseプロジェクトと一致していないことを意味します。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- リクエスト本体に`push_token`がない場合、トークンが取得されていません。アプリの設定でプッシュ通知の設定を確認してください。
- `ios_push_auth`が`denied`または`provisional`と表示される場合、ユーザーは完全なプッシュ権限を許可していません。
- Androidで`SENDER_ID_MISMATCH`が表示される場合は、FCM送信者IDをFirebaseプロジェクトと一致するように更新してください。

### プッシュ配信とクリック {#push-delivery-and-click}

プッシュ通知がタップされると、SDKは処理イベントとクリックイベントを記録します。

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

続いてクリックイベント：

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

プッシュ通知にディープリンクが含まれている場合、以下も表示されます：

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

続いてプッシュペイロードと表示ログが出力されます。ディープリンクについては、ディープリンクデリゲートまたは`UriAction`エントリを探してください。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- プッシュペイロードに、期待される`title`、`body`、およびディープリンク（`ab_uri`）が含まれていることを確認してください。
- タップ後に`pushClick`イベントが記録されていることを確認してください。
- クリックイベントが記録されていない場合は、アプリデリゲートまたは通知ハンドラーがプッシュイベントをBraze SDKに正しく転送しているか確認してください。

## アプリ内メッセージ {#in-app-messages}

アプリ内メッセージのログは、サーバーからの配信、イベントに基づくトリガー、表示、インプレッションの記録、クリックのトラッキングという全ライフサイクルを示します。

### メッセージ配信 {#message-delivery}

ユーザーがセッションを開始し、アプリ内メッセージの受信対象である場合、SDKはサーバーからメッセージペイロードを受信します。

{% tabs %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）からの応答で、アプリ内メッセージデータを含むものをフィルターしてください。

レスポンス本体にはメッセージペイロードが含まれており、以下の内容が含まれます：

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

トリガーイベントに一致するログを探してください：

```
Triggering action: <CAMPAIGN_BSON_ID>
```

これは、アプリ内メッセージがトリガーイベントに一致したことを確認するものです。

{% endtab %}
{% endtabs %}

### メッセージ表示とインプレッション {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

続いてインプレッションログ：

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### クリックとボタンイベント {#click-and-button-events}

ユーザーがボタンをタップするか、メッセージを閉じた場合：

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

これ以上一致するトリガーメッセージがない場合、以下も表示されます：

```
No matching trigger for event.
```

このイベントに対して追加のアプリ内メッセージが設定されていない場合、これは想定される動作です。

{% endtab %}
{% tab Android %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエスト本体内でイベント名`sbc`（ボタンクリック）または`si`（インプレッション）を探してください。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- アプリ内メッセージが表示されない場合は、まずセッション開始が記録されているか確認してください。
- 設定済みのBrazeエンドポイントからの応答をフィルターし、メッセージペイロードが配信されたことを確認してください。
- インプレッションが記録されていない場合は、ログ記録を抑制するカスタム`inAppMessageDisplay`デリゲートを実装していないか確認してください。
- 「No matching trigger for event」と表示される場合、これは正常であり、そのイベントに対して追加のアプリ内メッセージが設定されていないことを示しています。

## Content Cards

Content Cardsのログは、カードがデバイスに同期され、ユーザーに表示され、インタラクション（インプレッション、クリック、非表示操作）がトラッキングされていることを確認するのに役立ちます。

### カード同期 {#card-sync}

Content Cardsはセッション開始時と手動更新が要求された時に同期されます。セッションが記録されていない場合、Content Cardsは表示されません。

{% tabs %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）からの応答で、カードデータを含むものをフィルターしてください。

レスポンス本体にはカードデータが含まれており、以下のような内容です：

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

主要なフィールド：
- `v`（閲覧済み）：`0` = 未閲覧、`1` = 閲覧済み
- `cl`（クリック済み）：`0` = 未クリック、`1` = クリック済み
- `p`（固定済み）：`0` = 固定されていない、`1` = 固定されている
- `tp`（タイプ）：`short_news`、`captioned_image`、`classic`など

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

続いて、設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのPOSTリクエストが送信されます。このリクエストにはユーザー情報とデバイス情報が含まれます。

{% endtab %}
{% endtabs %}

### インプレッション、クリック、非表示 {#impressions-clicks-and-dismissals}

{% tabs %}
{% tab Swift %}

**インプレッション：**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**クリック：**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

カードにURLがある場合、以下も表示されます：

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**非表示：**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエスト本体内のイベント名を確認してください：
- `cci` — Content Cardsのインプレッション
- `ccc` — Content Cardsのクリック
- `ccd` — Content Cardsの非表示

{% endtab %}
{% endtabs %}

### 確認すべき事項

- **カードが表示されない**：セッション開始が記録されていることを確認してください。Content Cardsは同期するためにアクティブなセッションが必要です。
- **新規ユーザーにカードが表示されない**：新規ユーザーは初回セッションではContent Cardsが表示されない場合があります。次のセッションまでお待ちください。これは想定される動作です。
- **カードがサイズ制限を超えている**：2KBを超えるContent Cardsは表示されず、メッセージは中断されます。
- **キャンペーンを停止した後もカードが残る**：キャンペーンを停止した後に同期が完了したことを確認してください。同期が成功すると、Content Cardsはデバイスから削除されます。キャンペーンを停止する際は、ユーザーフィードからアクティブなカードを削除するオプションが選択されていることを確認してください。

## ディープリンク {#deep-links}

ディープリンクのログは、プッシュ通知、アプリ内メッセージ、Content Cardsに表示されます。ログ構造はソースチャネルに関係なく一貫しています。

{% tabs %}
{% tab Swift %}

SDKがディープリンクを処理する場合：

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

`<SOURCE_CHANNEL>`は`notification`、`inAppMessage`、または`contentCard`のいずれかです。

{% endtab %}
{% tab Android %}

ディープリンクについては、Logcat内の**Deep Link Delegate**または**UriAction**エントリを探してください。ディープリンクの解決を独立してテストするには、以下のコマンドを実行してください：

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

これにより、Braze SDKの外部でディープリンクが正しく解決されるかどうかを確認できます。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- ディープリンクURLがキャンペーンで設定した内容と一致していることを確認してください。
- あるチャネル（例：プッシュ通知）ではディープリンクが機能するが、別のチャネル（例：Content Cards）では機能しない場合は、ディープリンク処理の実装がすべてのチャネルに対応しているか確認してください。
- iOSでは、ユニバーサルリンクには追加の処理が必要です。Brazeチャネルからユニバーサルリンクが機能しない場合は、アプリがURL処理用の`BrazeDelegate`プロトコルを実装しているか確認してください。
- Androidでは、カスタムハンドラーを使用する場合、自動ディープリンク処理が無効になっていることを確認してください。そうでなければ、デフォルトのハンドラーが実装と競合する可能性があります。

## ユーザー識別 {#user-identification}

ユーザーが`external_id`で識別されると、SDKはユーザー変更イベントを記録します。

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

知っておくべき重要な点：
- ユーザーがログインしたら、できるだけ早く`changeUser`を呼び出してください。
- ユーザーがログアウトした場合、`changeUser`を呼び出して匿名ユーザーに戻す方法はありません。
- 匿名ユーザーを許可したくない場合は、セッション開始時またはアプリ起動時に`changeUser`を呼び出してください。

{% endtab %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエスト本体内でユーザー識別情報を探してください：

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## ネットワークリクエスト {#network-requests}

詳細ログには、SDKがBrazeサーバーと通信する際の完全なHTTPリクエストとレスポンスの詳細が含まれます。これらは接続の問題を診断するのに役立ちます。

### リクエスト構造 {#request-structure}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターしてください。リクエスト構造には以下が含まれます：

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### 確認すべき事項

- **APIキー**：`X-Braze-Api-Key`がワークスペースのAPIキーと一致していることを確認してください。
- **エンドポイント**：リクエストURLが設定済みのSDKエンドポイントと一致していることを確認してください。
- **再試行回数**：`X-Braze-Req-Attempt`が1より大きい場合、SDKが失敗したリクエストを再試行していることを示しており、接続の問題がある可能性があります。
- **レート制限**：`X-Braze-Req-Tokens-Remaining`は残りのリクエストトークン数を示します。カウントが低い場合、SDKがレート制限に近づいている可能性があります。
- **リクエストが見つからない**：Androidでは、セッション開始後にBrazeエンドポイントへのリクエストが表示されない場合は、APIキーとエンドポイントの設定を確認してください。

## 一般的なイベントの略称 {#common-event-abbreviations}

詳細ログのペイロードにおいて、Brazeは省略形のイベント名を使用します。以下は参照用の一覧です：

| 略称 | イベント |
|---|---|
| `ss` | セッション開始 |
| `se` | セッション終了 |
| `si` | アプリ内メッセージのインプレッション |
| `sbc` | アプリ内メッセージのボタンクリック |
| `cci` | Content Cardsのインプレッション |
| `ccc` | Content Cardsのクリック |
| `ccd` | Content Cardsの非表示 |
| `lr` | 位置情報の記録 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="一般的なイベントの略称" }

## トラブルシューティング {#troubleshooting}

### ユーザープロファイルのセッション数が0と記録されるのはどのような場合ですか？ {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

ユーザープロファイルのセッション数が0と表示されるのは、REST API（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)）またはCSVインポートで**初回セッション**や**最終セッション**のフィールドを含めずにユーザーをインポートした場合です。セッションは、ユーザーがSDKを通じてアプリを操作した際に記録されます。詳細については、[ユーザープロファイルのセッション数が0]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions)を参照してください。

### SDKとREST APIを同時に使用した場合のユーザーデータの不一致 {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

SDKとREST APIを同時に使用すると、競合によりデータの不一致が発生する可能性があります。`changeUser()`を呼び出した後は、重要なREST API呼び出しを行う前にSDKが保留中のデータをフラッシュするのを待ち、時間的に重要な更新のバッチ処理を避け、SDKとAPIリクエストの間に短い遅延を入れることを検討してください。`changeUser()`の動作については、[changeUser()の仕組み]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works)を参照してください。

### データがBrazeに到達しない {#data-not-reaching-braze}

データがBrazeに到達しない場合は、ファイアウォールがBraze APIエンドポイントおよびCDNプロバイダーへの送信トラフィックを許可していることを確認してください。問題が発生している間にMTRテストを実行し、[Fastly Debug](https://www.fastly-debug.com/)を使用してください。許可リストへの登録と接続のトラブルシューティングについては、[APIネットワーク接続の問題]({{site.baseurl}}/api/network_connectivity_issues)を参照してください。