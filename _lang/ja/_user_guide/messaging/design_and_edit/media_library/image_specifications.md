---
nav_title: 画像の仕様
article_title: 画像の仕様
page_order: 1
page_type: reference
description: "このリファレンス記事では、各チャネルタイプの推奨画像サイズと仕様について説明します。"
tool:
  - Templates
  - Media

---

# 画像の仕様 {#image-specifications}

> 一般的に、小さくて高品質な画像ほど読み込みが速くなるため、目的の出力を実現するために可能な限り小さなアセットを使用することをお勧めします。特定のチャネルで画像の使用を最大限に活用するには、この記事の詳細を参照してください。

画像やメッセージの最も重要な部分が期待どおりに表示されることを確認するために、さまざまなデバイスで常に[メッセージをプレビューおよびテスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)してください。

## 画像の動作 {#image-behavior}

{% multi_lang_include channels/image_specs.md variable_name='image behavior' %}

## 動画 {#video}

メディアライブラリにアップロードされた動画は、WhatsAppメッセージでのみ使用できます。詳細については、[WhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#outbound-messages)を参照してください。

## GIF {#gifs}

GIFはiOSプッシュ、アプリ内メッセージ、メール、Content Cards、MMSまたはRCSメッセージでサポートされています。非常に縦長または横長の形状（例：3000 x 2ピクセル）や300フレーム以上のGIFは、合計ファイルサイズが小さくてもアップロードに失敗する場合があります。iOSでのRCS固有のGIF動作については、[RCS](#rcs)を参照してください。

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## チャネルガイダンス {#channel-guidance}

### Content Cards

{% multi_lang_include channels/image_specs.md variable_name='content cards' %}

### メール {#email}

{% multi_lang_include channels/image_specs.md variable_name='email' %}

### アプリ内メッセージ {#in-app-messages}

{% multi_lang_include channels/image_specs.md variable_name='in-app messages' %}

{% alert tip %} 自信を持ってアセットを作成しましょう！アプリ内メッセージの画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスに対応するよう設計されています。[デザインテンプレート ZIP をダウンロード]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %})。{% endalert %}

詳細については、[アプリ内メッセージのクリエイティブの詳細]({{site.baseurl}}/user_guide/channels/in_app_messages/customize)を参照してください。

#### Font Awesome

Brazeは、モーダルアプリ内メッセージアイコンに [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) の使用をサポートしています。

### プッシュ通知 {#push-notifications}

{% multi_lang_include channels/image_specs.md variable_name='payload size' %}

{% multi_lang_include channels/image_specs.md variable_name='push notifications' %}

#### 推奨メッセージ文字数 {#recommended-message-lengths}

最良の結果を得るには、プッシュメッセージの作成時に以下のメッセージ文字数ガイドラインを参考にしてください。画像の有無、通知の状態（iOS）、ユーザーのデバイスの表示設定、デバイスのサイズなどによって多少の差異が生じる場合があります。

| メッセージタイプ | 推奨文字数（テキストのみ） | 推奨文字数（リッチ） |
| --- | --- | --- |
| iOS ロック画面 | 160文字 | 130文字 |
| iOS 通知センター | 160文字 | 130文字 |
| iOS バナーアラート | 80文字 | 65文字 |
| Android ロック画面 | 49文字 | N/A |
| Android 通知ドロワー | 597文字 | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="推奨メッセージ文字数" }

iOSの文字数の詳細については、[iOS文字数ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)を参照してください。

#### Webプッシュ {#web-push}

{% tabs %}
{% tab 画像 %}

| ブラウザ | 推奨アイコンサイズ |
| --- | --- |
| Chrome | 192 x 192 px 以上 |
| Firefox | 192 x 192 px 以上 |
| Safari | 192 x 192 px 以上（macOS 13以降のSafari 16ではキャンペーンごとに設定可能） |
| Opera | 192 x 192 px 以上 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webプッシュ" }

| ブラウザ | プラットフォーム | 大きい画像サイズ |
| --- | --- | --- |
| Chrome | Android | 2:1 アスペクト比 |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 アスペクト比 |
| Edge | Windows | 2:1 アスペクト比 |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 アスペクト比 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Webプッシュ" }

{% endtab %}
{% tab テキスト %}

| ブラウザ | プラットフォーム | 最大タイトル文字数 | 最大本文文字数 |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Webプッシュ" }

{% endtab %}
{% endtabs %}

#### プッシュ通知の例 {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![「Hi! This is an iOS Push with an image」というテキストと絵文字を含むiOSプッシュ通知。テキストの横に小さい画像があります。]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![強調プッシュでのiOSプッシュ通知。前のメッセージと同じテキストで、テキストの前に拡大画像が表示されています。]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![メッセージテキストの下に大きな画像が表示されたAndroidプッシュ通知。]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
大きな画像通知は、600 x 300ピクセル以上の画像を使用すると最適に表示されます。
{% endalert %}

{% endtab %}
{% endtabs %}

その他のリソースについては、[プッシュ画像とテキストの仕様]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)を参照してください。

### SMSとMMS {#sms-and-mms}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

MMSメッセージの作成については、[SMS、MMS、またはRCSメッセージの作成]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)を参照してください。

### RCS {#rcs}

RCSメディアメッセージはJPG、JPEG、GIF画像をサポートしています。ファイルサイズとフォーマットの詳細については、[SMS、MMS、またはRCSメッセージの作成]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)を参照してください。

iOSでは、RCSリッチカード内のGIFは静止画像として表示されます。Androidでは、期待どおりにアニメーションが再生されます。詳細については、[RCSリッチカード内のGIFがiOSで静止画像として表示されるのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios)を参照してください。