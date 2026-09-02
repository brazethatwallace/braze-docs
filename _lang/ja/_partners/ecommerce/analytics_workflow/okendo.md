---
nav_title: Okendo
article_title: Okendo
description: "OkendoとBrazeの統合方法について説明します。"
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/)は、アドボカシーの育成、口コミの拡大、LTVの最大化のためのツールを提供する統合カスタマーマーケティングプラットフォームであり、より迅速で効率的な成長のために顧客を動員します。

*この統合はOkendoによって維持されています。*

## 統合について {#about-the-integration}

BrazeとOkendoの統合は、レビュー、ロイヤルティ、紹介、アンケート、クイズなど、Okendoプラットフォームの複数の製品にまたがって機能します。Okendoはカスタムイベントとユーザー属性をBrazeに送信し、メッセージのパーソナライズやトリガーに使用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|------------------------|-----------------------------------------------------------------------------|
| Okendoアカウント | このパートナーシップを利用するには、Okendoアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ 1: OkendoでBraze Connectorを設定する {#step-1-set-up-braze-connector-in-okendo}

1. Okendoで、**Settings** > **Integrations** > **Email & SMS** > **Braze**に移動します。
2. **Integration**設定にAPIエンドポイントとAPIキーを追加します。

### ステップ 2: 識別子を設定する {#step-2-configure-your-identifier}

`external_id`フィールドは、各イベントに関連するユーザーを識別するために使用されます。フィールドをShopifyカスタマーIDに関連付けるには、**Use Shopify Customer ID for Braze user identification**をオンに切り替えます。それ以外の場合は、各ユーザーのメールアドレスに関連付けるためにオフに切り替えます。

## Okendoのイベントと属性をBrazeに同期する {#syncing-okendo-events-and-attributes-to-braze}

### カスタムイベント {#custom-events}

{% alert note %}
イベントデータのサンプルについては、[Okendoのドキュメント](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)を参照してください。
{% endalert %}

#### レビューイベント {#review-events}

- Okendo Review Created
- Okendo Review Request

#### 紹介イベント {#referral-events}

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### ロイヤルティイベント {#loyalty-events}

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### アンケートイベント {#survey-event}

- Submitted Okendo Survey

#### クイズイベント {#quiz-event}

- Submitted Okendo Quiz

### カスタム属性 {#custom-attributes}

OkendoはユーザープロファイルデータをBrazeのカスタム属性として送信し、オーディエンスセグメントの作成に利用できます。例としては次のようなものがあります:

- 年齢、誕生日、肌のタイプ、髪の色など、アンケートやレビュー投稿時に尋ねられるプロファイルの質問
- *平均レビュー評価*や*平均レビュー感情*などのレビュー指標
- *ポイント残高*や*VIPティア*などのロイヤルティ指標
- *紹介成功数*や*紹介総収益*などの紹介指標
- アンケートから収集したNPSスコア

## Okendo製品でBrazeを使用する {#using-braze-with-okendo-products}

Okendoの製品によっては、BrazeとOkendoを併用するために追加のステップを完了する必要があります。詳細については以下の記事を参照してください:

- [レビューとBrazeの統合](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [ロイヤルティとBrazeの統合](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [紹介とBrazeの統合](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [アンケートとBrazeの統合](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [クイズとBrazeの統合](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
統合の設定についてサポートが必要な場合は、Okendoサポートチームにお問い合わせください。
{% endalert %}