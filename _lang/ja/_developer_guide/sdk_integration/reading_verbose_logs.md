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

セッションはBrazeの分析とメッセージ配信の基盤です。アプリ内メッセージやContent Cardsなど、多くのメッセージング機能は、有効なセッションが開始されてから動作します。セッションが正しく記録されていない場合は、まずこの問題を調査してください。セッショントラッキングの有効化について詳しくは、[ステップ5：ユーザーセッショントラッキングを有効にする]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking)を参照してください。

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

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのネットワークリクエストをフィルタリングして、セッション開始（`ss`）イベントを確認します。

**セッション終了：**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### 確認すべきポイント {#what-to-check}

- アプリ起動時にセッション開始ログが表示されることを確認します。
- セッション開始が表示されない場合は、SDKが正しく初期化されていること、および `openSession`（Android）が呼び出されていることを確認してください。
- Androidでは、Brazeエンドポイントへのネットワークリクエストが送信されていることを確認します。表示されない場合は、APIキーとエンドポイントの設定を確認してください。

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

設定済みのBrazeエンドポイント（例: sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエストボディの属性で `push_token` を確認します。

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

デバイス情報に以下が含まれていることも確認します。

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

FCM登録ログを確認します。

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

以下を確認します。

- `com_braze_firebase_cloud_messaging_registration_enabled` が `true` であること。
- FCMの送信者IDがFirebaseプロジェクトと一致していること。

よくあるエラーは `SENDER_ID_MISMATCH` で、設定された送信者IDがFirebaseプロジェクトと一致していないことを意味します。

{% endtab %}
{% endtabs %}

### 確認事項

- リクエストボディに `push_token` がない場合、トークンが取得されていません。アプリ設定でプッシュの設定を確認してください。
- `ios_push_auth` が `denied` または `provisional` と表示される場合、ユーザーがプッシュのフル権限を許可していません。
- Androidで `SENDER_ID_MISMATCH` が表示される場合は、FCMの送信者IDをFirebaseプロジェクトに合わせて更新してください。

### プッシュの配信とクリック {#push-delivery-and-click}

プッシュ通知がタップされると、SDKは処理イベントとクリックイベントをログに記録します。

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

続いてクリックイベントが記録されます。

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

プッシュにディープリンクが含まれている場合は、以下も表示されます。

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

続いて、プッシュペイロードと表示ログが記録されます。ディープリンクについては、Deep Link Delegateまたは `UriAction` エントリを確認してください。

{% endtab %}
{% endtabs %}

### 確認事項

- プッシュペイロードに期待される `title`、`body`、およびディープリンク（`ab_uri`）が含まれていることを確認します。
- タップ後に `pushClick` イベントがログに記録されていることを確認します。
- クリックイベントが記録されていない場合は、アプリのデリゲートまたは通知ハンドラーがプッシュイベントをBraze SDKに正しく転送しているか確認してください。

## アプリ内メッセージ {#in-app-messages}

アプリ内メッセージのログには、サーバーからの配信、イベントに基づくトリガー、表示、インプレッションの記録、クリックトラッキングなど、完全なライフサイクルが表示されます。

### メッセージ配信 {#message-delivery}

ユーザーがセッションを開始し、アプリ内メッセージの対象となると、SDKはサーバーからメッセージペイロードを受信します。

{% tabs %}
{% tab Swift %}

アプリ内メッセージデータを含む、設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）からのレスポンスをフィルターします。

レスポンスボディには、以下のようなメッセージペイロードが含まれます。

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

トリガーイベントに一致するログを探します。

```
Triggering action: <CAMPAIGN_BSON_ID>
```

これにより、アプリ内メッセージがトリガーイベントに一致したことが確認できます。

{% endtab %}
{% endtabs %}

### メッセージの表示とインプレッション {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

その後にインプレッションのログが続きます。

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

一致するトリガーメッセージが他にない場合は、以下も表示されます。

```
No matching trigger for event.
```

これは、そのイベントに対して追加のアプリ内メッセージが設定されていない場合の正常な動作です。

{% endtab %}
{% tab Android %}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエストボディで名前が `sbc`（ボタンクリック）または `si`（インプレッション）のイベントを探します。

{% endtab %}
{% endtabs %}

### 確認すべきポイント

- アプリ内メッセージが表示されない場合は、最初にセッション開始が記録されていることを確認してください。
- 設定済みのBrazeエンドポイントからのレスポンスをフィルターして、メッセージペイロードが配信されたことを確認してください。
- インプレッションが記録されない場合は、ログ記録を抑制するカスタム `inAppMessageDisplay` デリゲートを実装していないか確認してください。
- 「No matching trigger for event」が表示される場合、これは正常であり、そのイベントに対して追加のアプリ内メッセージが設定されていないことを示しています。

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

ディープリンクのログは、プッシュ通知、アプリ内メッセージ、Content Cardsにわたって表示されます。ログの構造は、ソースチャネルに関係なく一貫しています。

{% tabs %}
{% tab Swift %}

SDKがディープリンクを処理する際のログ：

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

`<SOURCE_CHANNEL>` は `notification`、`inAppMessage`、または `contentCard` のいずれかです。

{% endtab %}
{% tab Android %}

ディープリンクについては、Logcatで **Deep Link Delegate** または **UriAction** のエントリを探してください。ディープリンクの解決を独立してテストするには、次のコマンドを実行します：

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

これにより、Braze SDKの外部でディープリンクが正しく解決されるかどうかを確認できます。

{% endtab %}
{% endtabs %}

### 確認すべきポイント

- ディープリンクURLがキャンペーンで設定したものと一致していることを確認してください。
- ディープリンクが1つのチャネル（例：プッシュ）では動作するが、別のチャネル（例：Content Cards）では動作しない場合、ディープリンクの処理実装がすべてのチャネルをサポートしているかどうかを確認してください。
- iOSでは、ユニバーサルリンクには追加の処理が必要です。Brazeチャネルからユニバーサルリンクが動作しない場合、アプリがURL処理用の `BrazeDelegate` プロトコルを実装しているか確認してください。
- Androidでは、カスタムハンドラーを使用している場合、自動ディープリンク処理が無効になっているか確認してください。そうでないと、デフォルトのハンドラーが実装と競合する可能性があります。

## ユーザー識別 {#user-identification}

ユーザーが `external_id` で識別されると、SDKはユーザー変更イベントを記録します。

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

知っておくべき重要なポイント:
- ユーザーがログインしたらすぐに `changeUser` を呼び出してください。早ければ早いほど良いです。
- ユーザーがログアウトした場合、`changeUser` を呼び出して匿名ユーザーに戻す方法はありません。
- 匿名ユーザーを許可しない場合は、セッション開始時またはアプリ起動時に `changeUser` を呼び出してください。

{% endtab %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例: sdk.iad-01.braze.com）へのリクエストをフィルターし、リクエストボディでユーザー識別情報を確認します:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## ネットワークリクエスト {#network-requests}

詳細ログには、SDKとBrazeサーバー間の通信に関するHTTPリクエストおよびレスポンスの完全な詳細が含まれます。これらは接続の問題を診断する際に役立ちます。

### リクエスト構造 {#request-structure}

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルタリングします。リクエスト構造には以下が含まれます：

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

### 確認すべき項目

- **APIキー**: `XBraze-ApiKey` がワークスペースのAPIキーと一致していることを確認します。
- **エンドポイント**: リクエストURLが設定済みのSDKエンドポイントと一致していることを確認します。
- **リトライ回数**: `XBraze-Req-Attempt` が1より大きい場合、SDKが失敗したリクエストをリトライしていることを示しており、接続の問題がある可能性があります。
- **レート制限**: `XBraze-Req-Tokens-Remaining` は残りのリクエストトークン数を示します。カウントが少ない場合、SDKがレート制限に近づいている可能性があります。
- **リクエストの欠落**: Androidでは、セッション開始後にBrazeエンドポイントへのリクエストが表示されない場合、APIキーとエンドポイントの設定を確認してください。

## 一般的なイベントの略称 {#common-event-abbreviations}

冗長ログペイロードでは、Brazeは省略されたイベント名を使用します。以下はリファレンスです。

| 略称 | イベント |
|---|---|
| `ss` | セッション開始 |
| `se` | セッション終了 |
| `si` | アプリ内メッセージのインプレッション |
| `sbc` | アプリ内メッセージのボタンクリック |
| `cci` | Content Cardsのインプレッション |
| `ccc` | Content Cardsのクリック |
| `ccd` | Content Cardsの却下 |
| `lr` | 位置情報の記録 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="一般的なイベントの略称" }

## トラブルシューティング {#troubleshooting}

### Android SDK 13.1.0〜15.x でジオフェンスがトリガーされない {#geofences-not-triggering-on-android-sdk-131015x}

Braze Android SDK 13.1.0 から 15.x には、ジオフェンス更新イベントの記録が停止する可能性のあるリグレッションがありました。Android 10 以前を実行しているデバイスでは、セッション開始時の位置情報の更新も失敗する可能性がありました。Android SDK 16.0.0 以降にアップグレードしてください。SDKの設定については、[ジオフェンス]({{site.baseurl}}/developer_guide/geofences)を参照してください。

### ユーザープロファイルのセッション数が0と記録されるのはどのような場合ですか？ {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

REST API（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)）またはCSVインポートで**First session** や **Last session** フィールドなしにユーザーをインポートした場合、ユーザープロファイルにセッション数が0と表示されることがあります。セッションは、ユーザーがSDKを通じてアプリを操作したときに記録されます。詳細については、[ユーザープロファイルのセッション数が0]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions)を参照してください。

### SDKとREST APIを併用した場合のユーザーデータの不一致 {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

SDKとREST APIを同時に使用すると、競合によりデータの不一致が発生する可能性があります。`changeUser()` を呼び出した後、重要なREST API呼び出しを行う前にSDKが保留中のデータをフラッシュできるようにし、時間に敏感な更新のバッチ処理を避け、SDKとAPIリクエストの間に短い遅延を追加することを検討してください。`changeUser()` の動作については、[changeUser() の仕組み]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works)を参照してください。

### データがBrazeに届かない {#data-not-reaching-braze}

データがBrazeに届かない場合は、ファイアウォールがBraze APIエンドポイントおよびCDNプロバイダーへの送信トラフィックを許可していることを確認してください。問題が発生している間にMTRテストを実行し、[Fastly Debug](https://www.fastly-debug.com/)を使用してください。許可リストへの登録と接続のトラブルシューティングについては、[APIネットワーク接続の問題]({{site.baseurl}}/api/network_connectivity_issues)を参照してください。