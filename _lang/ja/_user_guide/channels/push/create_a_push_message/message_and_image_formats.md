---
nav_title: "メッセージと画像のフォーマット"
article_title: "メッセージと画像のフォーマット"
page_order: 1
page_type: reference
description: "この記事では、プッシュ通知のメッセージと画像のフォーマットについて説明します。"
channel: push

---

# プッシュメッセージと画像のフォーマット {#push-message-and-image-formats}

> このリファレンス記事では、プッシュ通知のメッセージと画像のフォーマットについて説明します。

最良の結果を得るために、プッシュメッセージを作成する際は以下の画像サイズとメッセージの長さに関するガイドラインを参照してください。画像の有無、通知の状態（iOS）、ユーザーのデバイスの表示設定、デバイスのサイズによって多少の差異が生じる場合があります。迷った場合は、コピーを短く簡潔にしてください。

## iOSとAndroidのプッシュ通知 {#ios-and-android-push}

{% tabs local %}
{% tab 画像 %}

**画像タイプ** | **推奨画像サイズ** | **最大画像サイズ** | **ファイル形式**
--- | --- | --- | ---
(iOS) 2:1 *推奨* | 500&nbsp;KB | 5&nbsp;MB | PNG、JPEG、GIF
(Android) プッシュアイコン | 500&nbsp;KB | 5&nbsp;MB | PNG、JPEG
(Android) 拡張通知 | 500&nbsp;KB | 5&nbsp;MB | PNG、JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="iOSとAndroidのプッシュ通知" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab テキスト %}

| メッセージタイプ | 推奨メッセージ長（テキストのみ） | 推奨メッセージ長（リッチ）
--- | ---
(iOS) ロック画面 | 160文字 | 130文字
(iOS) 通知センター | 160文字 | 130文字
(iOS) バナーアラート | 80文字 | 65文字
(Android) ロック画面 | 49文字 | N/A
(Android) 通知ドロワー | 597文字 | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOSとAndroidのプッシュ通知" }

iOSプッシュ通知で切り捨てられずに使用できる文字数を知りたいですか？[iOS文字数ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)をご確認ください。

{% endtab %}
{% tab ペイロードサイズ %}

**プラットフォーム** | **サイズ**
--- | ---
iOS 8以前 | 0.256 KB
iOS 8以降 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOSとAndroidのプッシュ通知" }

{% endtab %}
{% tab 画像の例 %}
{% subtabs %}
{% subtab iOS %}

![「Hi! This is an iOS Push with an image」というテキストと絵文字が表示されたiOSプッシュ通知。テキストの横に小さな画像があります。]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![前のメッセージと同じテキストが表示されたiOSプッシュ通知のハードプッシュ。テキストの前に拡大された画像が表示されています。]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![メッセージテキストの下に大きな画像が表示されたAndroidプッシュ通知。]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
大きな画像の通知は、600x300ピクセル以上の画像を使用すると最適に表示されます。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab テキストの例 %}
{% subtabs %}
{% subtab iOS %}

![「Hi! This is an iOS Push」というテキストが表示されたiOSプッシュ通知。]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![ホーム画面に表示されたAndroidプッシュ通知。]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Webプッシュ {#web-push}

{% tabs local %}
{% tab 画像 %}

| **ブラウザー** | **推奨アイコンサイズ**
| --- | ---
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webプッシュ" }
Chrome | 192 x 192以上
Firefox | 192 x 192以上
Safari | 192 x 192以上（アイコンはmacOS 13以降のSafari 16以降でキャンペーンごとに設定可能）
Opera | 192x192以上
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webプッシュ" }

| **ブラウザー** | **プラットフォーム** | **大きな画像サイズ**
| --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Webプッシュ" }
Chrome | Android | 2:1のアスペクト比
Firefox | Android | N/A
Chrome | Windows | 2:1のアスペクト比
Edge | Windows | 2:1のアスペクト比
Firefox | Windows | N/A
Firefox | Windows | 2:1のアスペクト比
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Webプッシュ" }

{% endtab %}
{% tab テキスト %}

| **ブラウザー** | **プラットフォーム** | **最大タイトル長** | **最大メッセージ本文長**
| --- | --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Webプッシュ" }
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Webプッシュ" }

{% endtab %}
{% endtabs %}