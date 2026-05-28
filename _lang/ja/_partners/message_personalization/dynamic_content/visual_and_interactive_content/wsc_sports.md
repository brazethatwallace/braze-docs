---
nav_title: WSC Sports
article_title: WSC Sports
description: "このリファレンス記事では、BrazeとWSC Sportsのパートナーシップについて説明します。WSC Sportsは、リッチで堅牢なスポーツメディアをBrazeのプッシュ通知に組み込むことができるスポーツ動画プラットフォームです。"
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> [WSC Sports](https://wsc-sports.com/)プラットフォームは、すべてのデジタルプラットフォームおよびすべてのスポーツファンのために、パーソナライズされたスポーツ動画を自動的かつリアルタイムで生成します。

_この統合はWSC Sportsによって管理されています。_

## 統合について {#about-the-integration}

BrazeとWSC Sportsの統合により、Brazeのプッシュ通知にリッチで堅牢なスポーツメディアを含めることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| WSCアカウント | このパートナーシップを利用するには、WSCアカウントが必要です。 |
| Braze REST APIキー | **Messages**、**セグメント**、**キャンペーン**、**キャンバス**の権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

WSC Sportsアプリケーションは、動画の選択からエンドユーザーのデバイスへのプッシュ通知の到着まで、エンドツーエンドのプロセスを処理します。

### ステップ1:送信設定を選択する {#step-1-select-send-settings}

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

統合を開始する前に、Brazeで希望するキャンペーンとユーザーセグメントが構築されていることを確認してください。完了したら、WSC Sportsプラットフォームで希望する動画を選択し、送信設定で使用したいBrazeユーザーセグメントとキャンペーン IDを選択します。最後に、プッシュメッセージを送信したい時間を選択してください。

#### APIコール {#api-call}

送信されると、WSC Sportsは選択されたオプションに基づいて、以下のBrazeエンドポイントを使用して、選択されたユーザーセグメントにプッシュ通知を配信します:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#sending-messages-immediately-via-api-only)

メッセージの本文は次のとおりです:
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### ステップ2:テスト送信 {#step-2-test-send}

この時点で、キャンペーンはテストと送信の準備ができているはずです。エラーが発生した場合は、Brazeのエラーメッセージログを確認してください。