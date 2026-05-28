---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspireは、ロイヤルティ戦略を実装・評価できるようにし、プログラムの有効性を高めるための革新的な機能とカスタマイズされたメンバーコミュニケーションを提供するロイヤルティテクノロジーシステムです。"
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com)はロイヤルティテクノロジーシステムであり、カスタマーエンゲージメントを強化し、顧客の支出を増やし、ロイヤルティの高い行動を称賛する、結果に基づくロイヤルティプログラムによって、比類のないカスタマーエクスペリエンスを実現できるように支援します。

_この統合はKognitiv Inspireによって管理されます。_

## 統合について {#about-the-integration}

BrazeとKognitivの統合により、ロイヤルティ戦略を実装・評価できるようになり、プログラムの有効性を高めるための革新的な機能とカスタマイズされたメンバーコミュニケーションが提供されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Kognitivアカウント | このパートナーシップを活用するには、[Kognitiv](http://kognitiv.com)アカウントが必要です。 |
| Kognitiv APIキー | Kognitiv REST APIキー。これは**API Security Tokens**ページで作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- **パーソナライズされたロイヤルティプログラムの登録**: シームレスなプログラム登録と、会員が希望するチャネルを通じて配信されるカスタマイズされたウェルカム通知で、会員のロイヤルティジャーニーを促進します。
- **報酬の発行とエンゲージメント通知**: 会員のマイルストーンを祝う報酬の発行や通知により、ロイヤルティを維持します。
- **戦略的な会員の階層化とセグメンテーション**: ブランド固有のニーズに合わせて、支出、エンゲージメント、単純または複雑なビジネスルールに基づいて会員を階層化およびセグメント化することで、よりパーソナライズされたエンゲージメントを可能にします。
- **リアルタイムでのプロモーション参加資格の通知**: 限定プロモーションの参加資格を即時に通知することで、各会員に特別感を与えます。

## 統合 {#integration}

Kognitivのwebhookを使用して、ロイヤルティイベント発生時にBrazeにリクエストを送信します。以下の例では、KognitivとBrazeを使用して報酬を発行し、KognitivユーザーをBrazeに登録し、ウェルカムメールを送信する方法を説明します。

{% raw %}
### Brazeによる報酬の発行 {#braze-issue-reward}

次のKognitivの例では、会員報酬を発行します。Kognitiv Inspireはその報酬発行イベントを、webhookを使用してBrazeにカスタムイベントとして伝えます。報酬を伝えるフォローアップメールを送信するには、そのカスタムイベントをトリガーとするキャンペーンまたはキャンバスを作成します。

**Webhook URL**: `<braze-api-rest-endpoint>`
**リクエスト本文**: `Raw Text`

- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### リクエスト本文 {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### ユーザーを作成し、ウェルカムメールを送信する {#create-a-user-and-send-a-welcome-email}

次のKognitivの例では、新規ユーザーがKLSに登録すると、Brazeに新規ユーザーが作成されます。このユーザーのウェルカムメールをスケジュールするには、特定のカスタム属性に基づいてトリガーするキャンペーンまたはキャンバスをBrazeで作成します。

**Webhook URL**: `<braze-api-rest-endpoint>` <br>
**リクエスト本文**: `Raw Text`

- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### リクエスト本文

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Kognitiv Inspireのドキュメントと統合機能 {#kognitiv-inspire-documentation-and-integration-features}

BrazeをKognitiv Inspireと統合すると、Kognitivの広範なAPIポートフォリオ、最先端のwebhook機能、およびシームレスな一括転送のための堅牢なデータインポートおよびエクスポート機能を利用できるようになります。Kognitiv Inspireの機能と統合機能の詳細については、Kognitivの[リソースガイド](https://info.kognitivloyalty.com)を参照するか、Kognitivに連絡してガイド付きデモを依頼してください。

### エンドポイント {#endpoints}

**REST API認証**
- US地域: `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA地域: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC地域: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API（ベースURL）**
- US地域: `https://app.kognitivloyalty.com/api`
- CA/EMEA地域: `https://ca.kognitivloyalty.com/api`
- APAC地域: `https://aus.kognitivloyalty.com/api`

**Webサービスエンドポイント（ベースURL）**
- US地域: `https://app.kognitivloyalty.com/WS`
- CA/EMEA地域: `https://ca.kognitivloyalty.com/WS`
- APAC地域: `https://aus.kognitivloyalty.com/WS`

アクセストークンとSFTPエンドポイントの設定に関する詳細については、Kognitivにデモを依頼してください。