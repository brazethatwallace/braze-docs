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

## 統合について {#about-the-integration}

BrazeとPlayableの統合により、最高のコンテンツ（高品質動画）を最高のオーディエンス（メール）に配信でき、受信トレイで自動的に再生されるエキサイティングな高品質コンテンツにより、クリックスルーとポストクリックの指標が向上します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Playableアカウント | このパートナーシップを活用するには、Playableアカウントが必要です。Playableアカウントをまだお持ちでない場合は、[Playableアカウントに登録](https://signup.playable.video)してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }
| 動画コンテンツ | 動画ファイルをPlayableにアップロードするか、Facebook、Instagram、YouTube、X（旧Twitter）、TikTokなどのWebサイトの動画URLを指定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 実装 {#implementation}

### ステップ1:動画をPlayableに追加する {#step-1-add-your-video-to-playable}

Playableプラットフォームで、動画ファイルをアップロードするか、Facebook、Instagram、YouTube、X（旧Twitter）、TikTokなどの動画URLを指定して動画を追加します。

### ステップ2:埋め込みコードをPlayableからコピーする {#step-2-copy-the-embed-code-from-playable}

アップロードが完了すると、Playableによりコードが生成されます。このコードをBrazeキャンペーンに挿入すると、メールに動画が埋め込まれ、開封時に自動再生されます。メールが開封されると、メールクライアント、デバイス、スクリーンサイズ、およびネットワーク状況に応じて最適な動画がPlayableサーバーから配信されます。

{% alert tip %}
動画は、iPhone Mail、Gmail、Apple Mail、Outlook for iOS、Outlook for Android、Outlook for Mac、およびOutlook 365 for Windowsの新しいバージョンなど、受信トレイの98%以上で自動再生されます。従来のOutlook for Windowsをご利用の場合は、動画の代わりに静止画像が表示されます。
{% endalert %}

### ステップ3:埋め込みコードをBrazeに貼り付ける {#step-3-paste-the-embed-code-into-braze}

最後に、コードをBrazeのメールキャンペーンに貼り付けてから、メールキャンペーンのデザイン、テスト、公開を続行します。