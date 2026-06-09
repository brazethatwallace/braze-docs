---
article_title: プッシュCampaignおよびマルチチャネルCanvasesのレート制限
permalink: /rate_limiting_v3/
page_type: reference
description: "この記事では、プッシュCampaignおよびマルチチャネルCanvasesの配信速度レート制限について説明します。"
---

# プッシュCampaignおよびマルチチャネルCanvasesのレート制限 {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> このページでは、プッシュCampaignおよびマルチチャネルCanvasesのレート制限について、メッセージを調整する際に留意すべき点を含めて説明します。

プッシュCampaignおよびマルチチャネルCanvasesの配信速度レート制限を設定する際に、以下のいずれかを選択できるようになりました。

- チャネルごとのレート制限
- すべてのメッセージチャネルで共有される全体的なレート制限

{% alert important %}
プッシュCampaignおよびマルチチャネルCanvasesのレート制限は早期アクセス段階です。この早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

以下の機能はこの早期アクセスに**含まれていません**。

- あらゆるタイプのマルチチャネルCampaignおよびAPIトリガーのCanvasesにおけるチャネルごとのレート制限の設定
- グローバルレート制限の設定
- Canvasにおけるメッセージステップごとのレート制限の設定

## 考慮事項 {#considerations}

- このレート制限の更新は、非常に低いレート制限の設定を防止するものではありません。つまり、この防止策がない状態では、レート制限を設定した場合、オーディエンスのサイズによっては、メッセージが極めて遅い速度で送信される可能性があります。
- CampaignおよびCanvasesの**送信設定**の概要には、設定されたレート制限に関する不正確な説明が含まれる場合があります。<br><br>![ユーザーがメッセージを受信するレートに制限がないCampaignの送信設定。]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- マルチチャネルCampaign（CanvasesやプッシュCampaignではない）のレート制限は、[更新前のマルチチャネルCampaignのレート制限動作](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)を反映します。この早期アクセス段階では、レート制限付きのマルチチャネルCampaignの作成を避けることをお勧めします。