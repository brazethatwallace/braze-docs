---
nav_title: Toovio
article_title: Toovio
description: "このリファレンス記事では、BrazeとToovioのパートナーシップについて説明します。Toovioは、実用的なデータを発見し、最も重要な要素を使用して事前に定義された目標に基づき段階的に成果を上げることを支援するdata-as-a-service企業です。"
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) は、人工知能を活用したdata-as-a-service企業であり、実用的なデータを発見し、最も重要な要素を使用して事前に定義された目標に基づき段階的に成果を上げることを支援します。

_この統合はToovioによって管理されています。_

## 統合について {#about-the-integration}

BrazeとToovioのパートナーシップにより、ほぼリアルタイムでのメッセージトリガー、増分パフォーマンスを促進するツール、およびToovioの高度なキャンペーン測定ツールへのアクセスが提供されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Toovioアカウント | このパートナーシップを活用するには、Toovioアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze Currents | Braze Currentsにより、BrazeクライアントはBrazeプラットフォーム外部での処理のためにイベントまたは動作データをBrazeデータパートナー（AWS S3、Google Cloud Storage、またはMicrosoft Azure Blob Storage）にストリーミングできます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

以下の統合により、Toovioは特定の顧客をターゲットとしたトリガーを生成し、ほぼリアルタイムで通信できます。Toovioによって決定されたトリガーは、Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を経由してBrazeに送信されます。

### ステップ 1:データパートナーを定義する {#step-1-define-data-partner}

Currentsフィードのドロップ先をToovioと共有する必要があります。これにより、Toovioはユーザーのイベントおよび動作データにアクセスし、処理することができます。

### ステップ 2:トリガーキャンペーンを設定する {#step-2-set-up-a-triggered-campaign}

Toovioがターゲットとする顧客イベントに基づいて、Brazeの[APIトリガーキャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を作成します。さらに、キャンペーンのトリガーとなるターゲットユーザーの属性と値を定義する必要があります。

### ステップ 3:Toovioアカウントを設定する {#step-3-set-up-your-toovio-account}

アカウントを設定するには、「New Customer Request」という件名のメールでToovio（[info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request)）にご連絡ください。Toovioはクライアントと協力して、トリガーおよび基盤となるモデルを設定します。