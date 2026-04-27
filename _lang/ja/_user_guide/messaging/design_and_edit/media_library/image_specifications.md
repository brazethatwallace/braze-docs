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

# 画像の仕様

> 一般的に、小さくて高品質な画像ほど読み込みが速くなるため、目的の出力を実現するために可能な限り小さなアセットを使用することをお勧めします。特定のチャネルで画像の使用を最大限に活用するには、この記事の詳細を参照してください。

画像やメッセージの最も重要な部分が期待どおりに表示されることを確認するために、さまざまなデバイスで常に[メッセージをプレビューおよびテスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/)してください。

## 画像の動作

{% multi_lang_include image_specs.md variable_name='image behavior' %}

## 動画

メディアライブラリにアップロードされた動画は、WhatsApp メッセージでのみ使用できます。詳細については、[WhatsApp メッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#outbound-messages)を参照してください。

## GIF

GIF は、iOS プッシュ通知、アプリ内メッセージ、メール、コンテンツカード、MMS または RCS メッセージでサポートされています。非常に細長い形状の GIF（例：3000 x 2 ピクセル）や 300 フレーム以上の GIF は、合計ファイルサイズが小さくてもアップロードに失敗する場合があります。

## チャネルガイダンス

### コンテンツカード

{% multi_lang_include image_specs.md variable_name='content cards' %}

### メール

{% multi_lang_include image_specs.md variable_name='email' %}

### アプリ内メッセージ

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

{% alert tip %} 自信を持ってアセットを作成しましょう！アプリ内メッセージの画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスに対応するように設計されています。[デザインテンプレート ZIP をダウンロード]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %})。{% endalert %}

詳細については、[アプリ内メッセージのクリエイティブの詳細]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/)を参照してください。

#### Font Awesome

Braze は、モーダルアプリ内メッセージアイコンに [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) の使用をサポートしています。

### プッシュ通知

{% multi_lang_include image_specs.md variable_name='payload size' %}

{% multi_lang_include image_specs.md variable_name='push notifications' %}

#### 推奨メッセージ長

最良の結果を得るには、プッシュメッセージを作成する際に以下のメッセージ長ガイドラインを参照してください。画像の有無、通知の状態（iOS）、ユーザーのデバイスの表示設定、デバイスのサイズによって多少の差異が生じる場合があります。

| メッセージタイプ | 推奨長（テキストのみ） | 推奨長（リッチ） |
| --- | --- | --- |
| iOS ロック画面 | 160 文字 | 130 文字 |
| iOS 通知センター | 160 文字 | 130 文字 |
| iOS バナーアラート | 80 文字 | 65 文字 |
| Android ロック画面 | 49 文字 | N/A |
| Android 通知ドロワー | 597 文字 | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS の文字数の詳細については、[iOS 文字数ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)を参照してください。

#### Web プッシュ

{% tabs %}
{% tab 画像 %}

| ブラウザ | 推奨アイコンサイズ |
| --- | --- |
| Chrome | 192 x 192 px 以上 |
| Firefox | 192 x 192 px 以上 |
| Safari | 192 x 192 px 以上（MacOS 13+ の Safari 16 ではキャンペーンごとに設定可能） |
| Opera | 192 x 192 px 以上 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| ブラウザ | プラットフォーム | 大きい画像サイズ |
| --- | --- | --- |
| Chrome | Android | 2:1 アスペクト比 |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 アスペクト比 |
| Edge | Windows | 2:1 アスペクト比 |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 アスペクト比 |
| Chrome | MacOS | N/A |
| Safari | MacOS | N/A |
| Firefox | MacOS | N/A |
| Opera | MacOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab テキスト %}

| ブラウザ | プラットフォーム | 最大タイトル長 | 最大本文長 |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | MacOS | 35 | 50 |
| Safari | MacOS | 38 | 84 |
| Firefox | MacOS | 38 | 42 |
| Opera | MacOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### プッシュ通知の例

{% tabs %}
{% tab iOS %}

![「Hi! This is an iOS Push with an image」というテキストと絵文字が表示された iOS プッシュ通知。テキストの横に小さな画像があります。]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![ハードプッシュでの iOS プッシュ通知。前のメッセージと同じテキストが表示され、テキストの前に拡大された画像があります。]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![メッセージテキストの下に大きな画像が表示された Android プッシュ通知。]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
大きな画像の通知は、600 x 300 ピクセル以上の画像を使用すると最適に表示されます。
{% endalert %}

{% endtab %}
{% endtabs %}

その他のリソースについては、[プッシュ通知の画像とテキストの仕様]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)を参照してください。