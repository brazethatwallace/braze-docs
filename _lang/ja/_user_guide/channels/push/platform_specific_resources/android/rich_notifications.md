---
nav_title: リッチ通知の作成
article_title: "Android向けリッチプッシュ通知の作成"
page_order: 3
page_layout: tutorial
description: "このチュートリアルでは、BrazeのキャンペーンにおけるAndroidリッチ通知の設定方法について説明します。"
platform: Android
channel:
  - Push
tool:
  - キャンペーン

---

# Android向けリッチプッシュ通知の作成 {#create-rich-push-notifications-for-android}

> リッチ通知を使用すると、テキスト以外のコンテンツを追加してプッシュ通知をさらにカスタマイズできます。Androidの通知では、以前からプッシュ通知に画像を含める機能がサポートされており、「拡張通知画像」と呼ばれています。

## 前提条件 {#prerequisites}

Android向けリッチプッシュ通知を作成する前に、以下の詳細を確認してください。

- Androidの拡張通知画像は2:1の比率である必要がありますが、サイズの制限はありません。
- Androidでは、標準の通知ビュー用に別の画像を設定することもできます。推奨される画像サイズは以下のとおりです。
  - **小:** 512x256
  - **中:** 1024x512
  - **大:** 2048x1024
- 現在、Androidのリッチ通知はJPEGおよびPNG画像形式を含む静止画像のみをサポートしています。GIFやその他の画像形式はまだサポートされていません。
- プッシュ通知にアクションボタンを追加すると、表示可能な画像の領域に影響する場合があります。ダッシュボードのプレビューと実機でテストして、結果が期待どおりであることを確認してください。
- 画像をレンダリングするには、Braze Android SDKが有効になっている必要があります。

{% alert note %}
Brazeではリッチプッシュの設定手順を提供していますが、リッチプッシュ通知の実際のレンダリングは、デバイスのアスペクト比、Androidのバージョン、OEM固有の制約などの外部要因によって異なる場合があります。リッチプッシュ通知が意図したとおりに表示されることを確認するために、複数のAndroidデバイスにテスト送信を行うことをお勧めします。
{% endalert %}

## Androidリッチ通知の設定 {#setting-up-your-android-rich-notification}

### ステップ 1: プッシュキャンペーンを作成する {#step-1-create-a-push-campaign}

[キャンペーンの作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message)の手順に従って、Android向けのプッシュ通知を作成します。リッチコンテンツを含まないプッシュ通知の設定と同じコンポーザーを使用します。

### ステップ 2: キャプションを追加する {#step-2-add-captioning}

通知内の画像の前に表示する**サマリーテキスト**を追加します。

![Dogというペットフードアプリからのリッチプッシュ通知。Spotのフードを追加注文する時期であることをサマリーテキストとともに表示しています。]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### ステップ 3: メディアを追加する {#step-3-add-media}

メッセージのコンポーザーにある**Android通知画像**フィールドに画像を追加します。画像はダッシュボードから直接アップロードするか、外部でホストされているコンテンツURLを指定してアップロードできます。

サポートされている画像の詳細については、[画像の仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#push)を確認してください。

![画像を追加するか画像URLを入力できるAndroid通知画像セクション。]({% image_buster /assets/img_archive/android_rich_image.png %})

### ステップ 4: キャンペーンの作成を続ける {#step-4-continue-creating-your-campaign}

リッチ通知のコンテンツがダッシュボードにアップロードされたら、引き続き[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を行うことができます。