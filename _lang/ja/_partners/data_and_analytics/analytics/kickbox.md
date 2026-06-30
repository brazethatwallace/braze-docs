---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "このリファレンス記事では、メールリストの検証やアプリケーションへの検証統合に使用されるメール検証プラットフォームであるKickboxとBrazeのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/)は、メールデータをクリーンで配信可能な状態に保つために必要な機能、統合、セキュリティを備えたオールインワンのメール検証プラットフォームです。Kickboxとの統合により、送信前にKickboxのメール検証を使用して配信不能なメールアドレスや低品質なメールアドレスを特定し、BrazeのCampaignsの配信性を向上させます。

Kickboxを使用すると、Brazeでユーザープロファイルが更新された瞬間に、ユーザーのメールアドレスの品質を検証できます。これは、プロファイルの`email`フィールドが入力されることでトリガーされる専用のCanvasまたはCampaignワークフローによって実現されます。

CanvasまたはCampaignはKickboxにWebhookを送信し、ユーザーのメールアドレスを共有します。Kickboxはメールアドレスを検証し、Braze REST APIエンドポイントを使用して、品質を詳述するカスタム属性でユーザープロファイルを更新します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --------------------------------------|-------------------------------------------------------------------------------|
| Kickboxアカウント | この統合を使用するには、アクティブなKickboxアカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー** > **APIキー**で作成できます。 |
| 統合へのアクセスをリクエストする | KickboxサポートチームにBraze統合へのアクセスを許可してもらいます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Kickboxと統合するには、[Brazeとの統合](https://docs.kickbox.com/docs/integrating-with-braze#/)のステップに従ってください。

## ユースケース {#use-cases}

### 一括検証 {#bulk-verification}

数か月ごとまたは四半期ごとにリスト全体を検証し、解約されるメールや時間の経過とともに劣化して配信率を徐々に低下させるリストから身を守ることもできます。

これを行うには、Kickboxが説明しているように、ワークフローの**エントリ設定**を変更する必要があります。**アクションベースの配信**を選択する代わりに、**スケジュールされた配信**を選択します。次に、リストを一度に検証するスケジュール時間を選択します。

### 検証済みSegmentsの作成 {#create-verified-segments}

Kickboxのカスタム属性は一貫したスキーマを持っており、以下の例と一致しています。

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@example.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "example.com"
    },
    {
      "email": "example2@exampl.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@example.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "exampl.com"
    }
  ]
}
```
{% endraw %}

これにより、メールアドレスが検証済みのユーザーのオーディエンスSegmentsを作成でき、CampaignsやCanvasesの配信成功率を高め、メールサービスプロバイダー (ESP) での評判を守ることができます。

以下の手順に従ってください。

1. Brazeで、**オーディエンス** > **Segments** > **セグメントを作成**に移動します。
2. **フィルターグループ**セクションで、**カスタム属性**フィルターを追加し、ドロップダウンで「result」を選択します。

ユースケースに応じて、Kickboxカスタム属性「result」がユーザープロファイルに存在する、またはその値が「deliverable」に等しいSegmentを作成することが適切な場合があります。このフィルターを単独で使用してSegmentを作成することも、将来のすべてのSegmentsの一部にしてSegment内のすべてのユーザーを検証することもできます。