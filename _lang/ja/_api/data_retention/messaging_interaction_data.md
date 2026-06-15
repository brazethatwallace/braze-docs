---
nav_title: "メッセージングインタラクションデータ"
article_title: "メッセージングインタラクションデータ"
alias: "/messaging_interaction_data/"
page_order: 1
description: "このリファレンス記事では、CampaignおよびCanvasのインタラクションデータとその利用可能性について説明します。"
page_type: reference
---

# メッセージングインタラクションデータの利用可能性について {#about-messaging-interaction-data-availability}

> CampaignおよびCanvasesのメッセージングインタラクションデータについて、Brazeがデータを保持する期間やリターゲティングに使用する機能を含めて説明します。

### メッセージングインタラクションデータとは {#what-is-messaging-interaction-data}

メッセージングインタラクションデータとは、ユーザーが受信したCampaignやCanvasとどのようにやり取りしたかを示すデータです（例：ユーザーがCampaign Aを開封した、ユーザーがバリアントAを受信した、など）。このデータはリターゲティングに使用されます。

### メッセージングインタラクションデータはいつ利用可能ですか {#when-is-messaging-interaction-data-available}

インタラクションデータは常に利用可能です。アクティブなCampaignおよびCanvasesの場合、インタラクションデータは常にリアルタイムで利用できます。

停止されたCampaignおよびCanvasesの場合、そのインタラクションデータは、アクティブなCampaignまたはCanvasesのリターゲティングフィルターで使用されていない限り、3か月後に期限切れになります。期限切れのインタラクションデータは長期ストレージに移動され、以下に説明するプロセスを使用して復元しない限り利用できません。

期限切れのインタラクションデータは削除されることはなく、いつでも復元できます。

#### インタラクションデータを使用する機能 {#features-that-use-interaction-data}

以下の機能はメッセージングインタラクションデータを使用します。

- 特定のCampaignまたはCanvasでリターゲティングするリターゲティングフィルター
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- 特定のタグを持つCampaignまたはCanvasesでリターゲティングするリターゲティングフィルター
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- ユーザープロファイルの**Campaigns Received**および**Canvas Messages Received**リスト
- `/users/export`エンドポイント
- CampaignおよびCanvasサマリーページの**User Data** CSVエクスポート

これらの機能は、期限切れのインタラクションデータを結果に含めません。期限切れのインタラクションデータをこれらの機能の結果に含めるには、期限切れのデータを持つCampaignまたはCanvasを復元してください。

例えば、インタラクションデータが期限切れの場合、Canvasesを起動できません。つまり、Canvasにチームを追加するなどの編集を保存できません。

#### インタラクションデータを使用しない機能 {#features-that-dont-use-interaction-data}

以下の機能はメッセージングインタラクションデータを**使用しません**。つまり、これらの機能はメッセージングインタラクションデータの期限切れの影響を受けません。

- CampaignおよびCanvasの設定
- CampaignおよびCanvasの分析
- 分析レポート（レポートビルダー、クエリビルダー、エンゲージメントレポートなど）
- Currents
- Snowflake Data Share
- セグメントエクステンション
- データポイント
- 以下のリターゲティングフィルター：
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

### メッセージングインタラクションデータを復元するには {#how-do-i-restore-messaging-interaction-data}

インタラクションデータを復元するには、以下の手順に従ってください。

1. 期限切れのCampaignまたはCanvasに移動します。
2. CampaignまたはCanvasのランディングページの上部にあるバナーで**Restore interaction data**を選択します。

また、**Campaigns**ページからCampaignを選択し、**Restore interaction data**を選択することで、複数のCampaignのインタラクションデータを復元することもできます。

インタラクションデータの復元にかかる時間はさまざまですが、ほとんどの場合、5〜15分程度です。復元が完了すると、メールが届きます。

#### タグによる復元 {#restoring-by-tag}

特定のタグを持つ期限切れのCampaignまたはCanvasesのインタラクションデータを復元することもできます。

1. **Campaigns**または**Canvas**ページに移動し、該当するタグで検索します。
2. CampaignまたはCanvasesを選択します。
3. **Restore interaction data**を選択して、それらのCampaignまたはCanvasesのデータを復元します。

さらに3か月間非アクティブな状態が続くと、これらのCampaignまたはCanvasesは再び期限切れになります。

#### タグによるリターゲティング {#retargeting-by-tag}

タグによるリターゲティングを行うリターゲティングフィルターを使用するCampaignは、期限切れの対象から除外されません。タグによるリターゲティングを行うリターゲティングフィルターには以下が含まれます。

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

### 過去のメッセージングインタラクションデータの利用可能性 {#when-was-messaging-interaction-data-available-in-the-past}

以前は、CampaignまたはCanvasが以下の条件を満たした場合、メッセージインタラクションデータは削除されていました。

- 25暦月間メッセージを送信していない、かつ
- アクティブなCampaign、Canvases、またはContent Cardsのリターゲティングに使用されていない。

以前にメッセージングインタラクションデータが削除されたCampaignおよびCanvasesは、Campaign、Canvases、およびSegmentsのリターゲティングフィルターで使用できません。