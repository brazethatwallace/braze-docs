---
nav_title: "Playable"
article_title: "Playable"
description: "このリファレンス記事では、BrazeとPlayableのパートナーシップについて説明します。Playableは動画プラットフォームであり、動画コンテンツをBrazeのメールキャンペーンに追加できます。"
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable](https://playable.video)では、自動再生動画コンテンツをBrazeのメールキャンペーンに追加できます。

_この統合はPlayableによって管理されています。_

## インテグレーションについて {#about-the-integration}

BrazeとPlayableのインテグレーションにより、最高のコンテンツ（高品質な動画）を最適なオーディエンス（メール）に届けることができ、受信トレイ内で自動再生されるエキサイティングな高品質コンテンツでクリックスルーおよびクリック後の指標を向上させます。

{% alert important %}
埋め込み動画は多くのメールクライアントでネイティブにサポートされておらず、メールのサイズが大幅に増加する可能性があるため、メッセージがスパムとしてマークされることがあります。Playableは、メールクライアント全体で機能する最適化された動画コンテンツを配信することでこの問題に対処します。メールでの動画の詳細については、[メールに動画を埋め込むことはできますか？]({{site.baseurl}}/user_guide/channels/email/faq#can-i-embed-videos-in-emails)を参照してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Playable アカウント | このパートナーシップを利用するには、Playable アカウントが必要です。Playable アカウントをまだお持ちでない場合は、[Playable アカウントに登録](https://signup.playable.video)してください。
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }
動画コンテンツ | Playable に動画ファイルをアップロードするか、Facebook、Instagram、YouTube、X（旧 Twitter）、TikTok などの Web サイトから動画 URL を提供してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 実装 {#implementation}

### ステップ1：Playableに動画を追加する {#step-1-add-your-video-to-playable}

Playableプラットフォームで、動画ファイルをアップロードするか、Facebook、Instagram、YouTube、X（旧Twitter）、TikTokなどの動画URLを指定して動画を追加します。

### ステップ2：Playableから埋め込みコードをコピーする {#step-2-copy-the-embed-code-from-playable}

アップロードが完了すると、Playableがコードを生成します。このコードをBrazeのキャンペーンに挿入すると、メールに動画が埋め込まれ、開封時に自動再生されます。メールが開封されると、Playableのサーバーがメールクライアント、デバイス、画面サイズ、ネットワーク状況に応じて最適なバージョンの動画を配信します。

{% alert tip %}
動画は、iPhone Mail、Gmail、Apple Mail、Outlook for iOS、Outlook for Android、Outlook for Mac、および新しいバージョンのOutlook 365 for Windowsを含む、98%以上の受信トレイで自動再生されます。レガシーのOutlook for Windowsのユーザーには、代わりに静止画像が表示されます。
{% endalert %}

### ステップ3：Brazeに埋め込みコードを貼り付ける {#step-3-paste-the-embed-code-into-braze}

最後に、Brazeのメールキャンペーンにコードを貼り付け、メールキャンペーンのデザイン、テスト、公開を続けます。