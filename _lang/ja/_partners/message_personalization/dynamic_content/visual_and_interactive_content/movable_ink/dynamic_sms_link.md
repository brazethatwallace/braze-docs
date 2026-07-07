---
nav_title: ダイナミックSMSリンクプレビュー
article_title: ダイナミックSMSリンクプレビュー
description: "このリファレンス記事では、Movable InkのSMSリンクプレビュー機能をオンにして使用する方法について説明します。"
page_type: partner
search_tag: Partner
---

# ダイナミックSMSリンクプレビュー {#dynamic-sms-link-preview}

> Movable InkのダイナミックSMSリンクプレビューを使用すると、SMSと同じコストでMMSの没入感を活用できます。これにより、BrazeとMovable Inkを使用して、コスト効率の高いパーソナライズされたリッチなメッセージングエクスペリエンスを実現できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Movable Inkアカウント | このパートナーシップを活用するには、Movable Inkアカウントが必要です。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Webサイトインポート、またはAPIを使用して実行できます。 |
| MMS送信機能 | Brazeを通じてMMSが設定されていることを確認してください。
| [リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/) | リンク短縮がオンになっていることを確認してください。 |
| 連絡先カード | リンクプレビューがiOSで機能するためには、あなたのブランド（送信者）がユーザーの電話に連絡先として保存されている必要があります。これは、連絡先カードまたは別の方法で行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

iOSおよびAndroidオペレーティングシステム用のダイナミックSMSリンクを送信するには、以下のそれぞれのステップに従ってください。

### iOS

{% alert important %}
iOSでリンクプレビュー画像を表示するには、ユーザーがブランド（送信者）を連絡先として追加する必要があります。
{% endalert %}

#### ステップ 1: 連絡先カードキャンペーンを作成する {#step-1-create-a-contact-card-campaign}

ユーザーが[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card/)または別の方法でブランドを連絡先として保存すると、**Tap to Load Preview**プロンプトとMovable Inkリンクが表示されるようになります。

![1]{: style="max-width:30%;"}

#### ステップ 2: Movable Inkリンクを送信する {#step-2-send-movable-ink-links}

1. Movable InkでSMS キャンペーンを作成し、クリックスルーURLを生成します。
2. Brazeダッシュボードで**キャンペーン**に移動し、**キャンペーンを作成**ドロップダウンから新しいSMS/MMS キャンペーンを設定します。
3. SMS キャンペーン作成画面で以下を行います。
    - サブスクリプショングループを設定します。
    - メッセージを入力します。
    - Movable Inkリンクをメッセージ本文の他のすべてのテキストの後に**最後に**追加します。<br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Liquidパーソナライゼーションについて再確認するには、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/)を参照してください。
{% endalert %}

{: start="4"}
4. ダイナミックSMSリンクプレビューキャンペーンをテストして起動する準備が整いました。

![3]{: style="max-width:70%;"}

ユーザーがリンクプレビューを読み込むと、パーソナライズされた画像がレンダリングされ、Webサイト、アプリ、またはランディングページにリンクアウトできるようになります。

![4]{: style="max-width:30%;"}

### Android（GoogleおよびSamsungデバイス） {#android-google-and-samsung-devices}

Androidユーザーは、ダイナミックSMSリンクプレビューを受信するためにブランドを連絡先として保存する必要はありません。ただし、デバイスが自動的にリンクプレビューを読み込めるように、保存することを推奨します。

![5]{: style="max-width:30%;"}

ブランドを連絡先として保存しておらず、自動プレビューをオンにしているユーザーは、プレビュー画像を読み込むために**Tap to load preview**を選択する必要があります。

![6]{: style="max-width:30%;"}

## 考慮事項 {#considerations}

- メッセージにはプレビューリンクを1つだけ含めてください。SMS本文に複数のリンクがある場合、コンテンツは生成されません。
- プレビューリンクの後に文字を含めないでください。エクスペリエンスが正しく機能しなくなる可能性があります。


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}