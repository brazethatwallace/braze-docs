---
nav_title: Notify
article_title: Notify
description: "このリファレンス記事では、カスタマーライフサイクル全体にわたるパーソナライゼーションを提供するリアルタイムのオムニチャネルパーソナライゼーションソリューションであるBrazeとNotifyのパートナーシップについて説明します。"
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/)は、カスタマーリレーションシップマネジメントツールとシームレスに統合し、マーケティング戦略を強化し、複数のチャネルにわたるエンゲージメントを促進するAI主導のソフトウェアソリューションです。

BrazeとNotifyの統合により、マーケターはさまざまなプラットフォームで効果的にエンゲージメントを促進できます。従来のマーケティング手法に頼る代わりに、BrazeのAPIトリガーCampaignでNotifyの機能を活用して、メール、SMS、プッシュ通知など複数のチャネルを通じてパーソナライズされたメッセージを配信できます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Braze REST APIキー | `users.export.segment`および`campaigns.trigger.send`の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| CNAME設定 | Notifyがメッセージングに対するユーザーエンゲージメントを追跡してモデルにさらなる情報を提供するために、メールで使用されるトラッキングピクセル用のサブドメインを作成する必要があります。サブドメインの作成後、そのURLをNotifyと共有してください。 |
| データベースのオプトインエクスポート | 過去1年間（12か月）のCampaignおよび購入データをNotifyに送信します。このエクスポートは、Notifyの予測モデルのトレーニングに使用されます。<br><br>**フィールド:**<br><br>**メール:** メールのSHA256ハッシュ。小文字に変換し、先頭および末尾のスペースを除去したもの。<br><br>**Segment:** アクティビティレベル（アクティブまたは非アクティブ）を定義するSegment情報。<br><br>**サブSegment:** 購買アクティビティレベルなど、その他の関連するアクティビティ情報。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: Campaignを作成する {#step-1-create-your-campaign}

Brazeで[APIトリガーCampaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)を作成します。次に、Campaignの`api_identifier`をNotifyと共有します。

### ステップ2: BrazeでSegmentを作成する {#step-2-create-your-segment-in-braze}

次に、[ステップ1](#step-1-create-your-campaign)で作成したCampaignでターゲットにしたいユーザーのSegmentを作成します。そして、Segment IDをNotifyと共有します。

### ステップ3: Segmentを取得する {#step-3-fetch-your-segment}

Notifyが、Campaignに関連付けられたSegment内のユーザーをエクスポートします。

### ステップ4: NotifyがCampaignをトリガーする {#step-4-notify-triggers-the-campaign}

NotifyのAIは`/campaigns/trigger/send`エンドポイントを使用して、[ステップ1](#step-1-create-your-campaign)で作成したBraze Campaignをトリガーし、ユーザーが最もエンゲージメントしやすいと判断されたタイミングで送信します。