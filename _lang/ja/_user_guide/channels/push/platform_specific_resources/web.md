---
nav_title: "Webプッシュ"
article_title: Webプッシュ通知
page_order: 8.5
page_type: reference
description: "このリファレンスページでは、Webプッシュ通知の概要と、作成に必要なステップへのリンクを紹介します。"
platform: Web
channel:
  - push

---

# Webプッシュ {#web-push}

> BrazeのWebプッシュ通知について学び、独自のWebプッシュ通知を作成するためのリソースを見つけましょう。

Webプッシュは、Webアプリケーションのユーザーとエンゲージメントを図るもう一つの優れた方法です。[サポートされているブラウザ](#supported-browsers)からWebサイトにアクセスしている顧客は、Webページが読み込まれているかどうかに関係なく、WebアプリケーションからのWebプッシュの受信をオプトインできます。

## 前提条件 {#prerequisites}

Brazeを使用してプッシュメッセージを作成・送信するには、開発者と協力してWebサイトにプッシュを統合する必要があります。詳細なステップについては、[Webプッシュ統合ガイド]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)を参照してください。

### プッシュ許可 {#push-permission}

どのブランドでも、Webサイトにプッシュ通知を統合して使用できます。通知は、Webブラウザを開いている限り、現在および過去のWeb訪問者の両方に届きますが、訪問者は従来のモバイルアプリプッシュと同様に、[通知の受信をオプトインする]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#push-permission)必要があります。

{% alert tip %}
ブラウザ内メッセージを使用して、ユーザーにWebプッシュのオプトインを促すことを検討してください。これは[プッシュプライマー]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)とも呼ばれます。
{% endalert %}

## 概要 {#overview}

Webプッシュ通知は、迅速なコンバージョンを促す緊急性の高い実用的な更新情報を配信します。Webプッシュを使用すると、以下のことが可能です。

- 価格の下落など、重要なデータが変更されたタイミングでメッセージをトリガーする
- 明確なコールトゥアクションボタンでユーザーをWebサイトに呼び戻す
- 製品や顧客の情報でプッシュをパーソナライズし、メッセージの関連性を高める

Webプッシュは、スマートフォンのアプリプッシュ通知と同じように機能します。Webプッシュの作成について詳しくは、[プッシュ通知を作成する]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message)をご覧ください。

![ノートパソコンとスマートフォンに同じプッシュメッセージが表示されたWebプッシュの例。]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 想定されるユースケース {#potential-use-cases}

一般的なWebプッシュメッセージのユースケース例を以下に示します。

| ユースケース | 説明 |
| --- | --- |
| 無料トライアル | Webサイトの新規訪問者に無料トライアルへの登録を促します。自社の魅力を体験する機会を提供することで、有料顧客になる可能性を高めることができます。 |
| アプリダウンロード | Webユーザーをモバイルアプリに誘導し、製品からさらに多くの価値を得られるようにします。パーソナライゼーションを活用して、現在のエンゲージメントパターンに基づいたアプリのメリットを強調することを検討してください。 |
| 割引とセール | 期間限定のイベントやプロモーションに対する顧客の認知度を高めます。Webプッシュを含む複数のチャネルでメッセージを配信し、ブランドのプロモーションの認知度を向上させましょう。 |
| カート放棄 | 取引を完了していないユーザーに自動リマインダーを送信し、チェックアウトフローに呼び戻します。<br><br>Brazeが実施した調査によると、Webプッシュは受信者を呼び戻して購入を完了させる効果において、メールより53%、モバイルプッシュより23%高い効果があることがわかっています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="想定されるユースケース" }

## サポートされているブラウザ {#supported-browsers}

以下のブラウザがWebプッシュ通知をサポートしています。

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome（およびAndroidモバイル版Chrome）
- Safari（バージョン16以降）
- Firefox（およびAndroidモバイル版Firefox）
- Opera
- Edge

プッシュプロトコルの標準とブラウザサポートの詳細については、お使いのブラウザに基づいて以下のリソースを確認できます。

- [Safari（デスクトップ）](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari（モバイル）]({{site.baseurl}}/developer_guide/push_notifications?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## 410（Gone）と無効なWebプッシュエンドポイント {#410-gone-and-invalid-web-push-endpoints}

ブラウザやプッシュサービスは、Webプッシュの購読が受け付けられなくなった場合に**410 Gone**（または類似の「エンドポイントが無効」エラー）を返すことがあります。一般的な原因は以下のとおりです。

- ユーザーがブラウザまたはOSの設定でサイトの通知を無効にした。
- 同じブラウザプロファイルで別のユーザープロファイルが購読を登録したため、エンドポイントが新しい購読者にローテーションされた。
- エンゲージメントがない長期間の後に購読が期限切れになった。ユーザーが再度オプトインすると、次のセッションで新しい購読が作成されます。

ユーザーが通知を再度有効にした後、サイトの通常のWebプッシュ登録フローを再度トリガーして、Brazeが新しい購読エンドポイントを保存できるようにしてください。