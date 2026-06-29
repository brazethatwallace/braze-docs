---
nav_title: Roku SDK
article_title: Roku SDKリポジトリガイド
page_order: 8
description: "GitHubからミラーリングされたBraze Roku SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Roku SDKについて {#about-the-braze-roku-sdk}

Braze Roku SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド]({{site.baseurl}}/user_guide/introduction/)
- [Braze開発者ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)

## 初期SDK統合 {#initial-sdk-integration}

Braze Roku SDKは、分析、セグメンテーション、エンゲージメントに使用される情報をレポートするためのAPIを提供します。

## ステップ 1: ファイルの追加 {#step-1-add-files}

1. `source`ディレクトリで、アプリに`BrazeSDK.brs`を追加します。
2. `components`ディレクトリで、アプリに`BrazeTask.brs`と`BrazeTask.xml`を追加します。

## ステップ 2: 参照の追加 {#step-2-add-references}

次の`script`要素を使用して、メインシーンに`BrazeSDK.brs`への参照を追加します。

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## ステップ 3: 設定 {#step-3-configure}

`main.brs`内で、グローバルノードにBrazeの設定を行います。

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## ステップ 4: Brazeの初期化 {#step-4-initialize-braze}

Brazeインスタンスを初期化します。

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## アプリ内メッセージのセットアップ {#in-app-message-setup}

アプリ内メッセージを処理するために、`BrazeTask.BrazeInAppMessage`にオブザーバーを追加できます。

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

次に、ハンドラ内で、Campaignによってトリガーされた最も優先度の高いアプリ内メッセージにアクセスできます。

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

その後、アプリ内メッセージに対して何を行うかを決定できます。利用可能なフィールドの一部を以下に示します。

- `in_app_message.message` - アプリ内メッセージの本文テキスト
- `in_app_message.buttons` - ボタンのリスト（空のリストの場合もあります）。
- `in_app_message.id` - インプレッションまたはクリックをロギングする際に使用するID
- `in_app_message.extras` - キー/値ペア
- `in_app_message.image_url` - 画像URL
- `in_app_message.click_action` - ボタンがない場合、アプリ内メッセージが表示されているときにユーザーが「OK」をクリックした際の動作です。`"URI"`または`"NONE"`を指定できます。
- `in_app_message.dismiss_type` - `"AUTO_DISMISS"`または`"SWIPE"`を指定できます。
- `in_app_message.display_delay` - アプリ内メッセージを表示するまでの待機時間（秒）
- `in_app_message.duration` - `dismiss_type`が`"AUTO_DISMISS"`の場合、メッセージを表示する時間（ミリ秒）
- `in_app_message.header` - アプリ内メッセージのヘッダーテキスト
- `in_app_message.uri` - `click_action`が`"URI"`の場合に表示されるURI

ダッシュボードから使用できるさまざまなスタイリングフィールドもあります。または、Rokuアプリケーション内で標準パレットを使用してアプリ内メッセージを実装し、スタイルを設定することもできます。
- `in_app_message.bg_color` - 背景色
- `in_app_message.close_button_color` - 閉じるボタンの色
- `in_app_message.frame_color` - 背景スクリーンオーバーレイの色
- `in_app_message.header_text_color` - ヘッダーテキストの色
- `in_app_message.message_text_color` - メッセージテキストの色
- `in_app_message.text_align` - `"START"`、`"CENTER"`、または`"END"`を指定できます。

ボタンフィールドには以下が含まれます。
- `buttons[0].click_action` - `uri`フィールドを開くことを示す`"URI"`を指定できます。アプリ内メッセージを閉じることを示す`"NONE"`を指定できます。
- `buttons[0].id` - ボタン自体のID値
- `buttons[0].text` - ボタンに表示するテキスト
- `buttons[0].uri` - `click_action`が`"URI"`の場合に表示されるURI
- `buttons[0].bg_color` - ボタンの背景色
- `buttons[0].border_color` - ボタンの枠線の色
- `buttons[0].text_color` - ボタンのテキスト色

メッセージが表示または確認されたら、インプレッションをロギングします。

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

ユーザーがメッセージをクリックしたら、クリックをロギングします。
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
その後、`in_app_message.click_action`を処理します。

ユーザーがボタンをクリックした場合、ボタンクリックをロギングします。

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
その後、`inappmessage.buttons[selected].click_action`を処理します。

アプリ内メッセージの処理後に、フィールドをクリアする必要があります。

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## 基本SDK統合の完了 {#basic-sdk-integration-complete}

これでBrazeがアプリケーションからデータを収集するようになります。SDKへの属性、イベント、購入のロギング方法については、公開ドキュメントを参照してください。サンプルアプリのシーン`MainScene.brs`にも、APIの使用例が含まれています。

`BrazeInAppMessage.brs`と`CustomSideBySideInAppMessage.brs`は、アプリ内メッセージの処理例を示しています。`MainScene.brs`の`onInAppMessageTriggered()`は、複数のレイアウトをサポートする方法を示しています。

## その他のリファレンス {#additional-reference}

`torchietv`ディレクトリには、Braze SDKが統合されたサンプルアプリが含まれています。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk)を参照してください。