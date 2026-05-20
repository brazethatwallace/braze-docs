---
nav_title: loplat
article_title: loplat
description: "このリファレンス記事では、Brazeとloplatのパートナーシップについて説明します。loplatはオフラインの位置情報ベースのマーケティングプラットフォームで、位置情報のコンテキストを追加することで近接マーケティングキャンペーンを実行できるようにします。"
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/)は、主要なオフラインの位置情報ベースのプラットフォームです。loplat SDKを使用して店舗の来店者数をスマートに増やし、店内購入を促進するマーケティングキャンペーンを実行できます。キャンペーン終了後、フットフォール分析で店舗のパフォーマンスを測定できます。

_この統合はLoplatによって管理されています。_

## 統合について {#about-the-integration}

Brazeとloplatの統合により、loplatの位置情報サービス（店舗POIおよびカスタムジオフェンス）を使用して、ジオコンテキストに応じたマーケティングキャンペーンをトリガーし、オフラインセグメンテーションを使用してカスタムイベントを作成できます。ユーザーがloplat Xで設定したターゲットロケーションを訪れると、キャンペーンおよびロケーション情報が即座にBrazeに送信されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| loplat Xアカウント | この統合を利用するには、loplat Xアカウントが必要です。<br><br>[support@loplat.com](mailto:support@loplat.com) にメールしてloplat Xアカウントをリクエストしてください。 |
| loplat SDK | loplat SDKはユーザーの店舗訪問を認識し、位置イベントを処理し、ユーザーが場所に滞在しているか移動しているかを区別します。loplat SDKを使用して、店舗のフットフォールを分析したり、ユーザーが店舗に入ったときにプッシュメッセージを送信したりできます。<br><br>SDKはAndroidとiOSでのみ利用可能です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー：<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>これはBrazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

loplatが提供するカスタムイベントのロケーション情報は、以下のようなユースケースを実現するためにキャンペーンで使用できます。

- [免税プロモーションアラート](https://www.loplat.com/loplat-x#usecase)
    - 空港の搭乗ゲート付近にいるユーザーに免税店の割引クーポンを送信します。
- 電気自動車（EV）充電ステーションのロケーションプッシュ
    - EV充電ステーションの周囲にジオフェンスを設定し、ユーザーがステーションの近くにいるときに通知して充電を促します。

## 統合 {#integration}

### ステップ1：SDKを統合する {#step-1-integrate-the-sdks}

[loplat-Braze統合](https://developers.loplat.com/braze/)ドキュメントに記載されている手順に従って、loplat SDKとBraze SDKをアプリに統合します。

### ステップ2：Brazeとloplat Xのダッシュボードを同期し、キャンペーンを作成する {#step-2-sync-the-braze-and-loplat-x-dashboards-and-create-a-campaign}

Brazeダッシュボードで新しいAPIキーを作成します。APIキーをコピーして、loplat Xダッシュボードの**Settings** > **API Settings**に貼り付けます。詳細については、[loplat Xユーザーガイド](https://loplatx-user-guide.notion.site/キャンペーン-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25)を参照してください。

#### APIトリガー配信 {#api-triggered-delivery}

1. **API-Triggered Delivery**で送信するBraze キャンペーンまたはキャンバスを作成し、キャンペーン IDをコピーします。
2. すべてのステップを完了した後、Brazeでキャンペーンを起動します。
3. loplat Xに移動し、[loplat Xユーザーガイド](https://loplatx-user-guide.notion.site/キャンペーン-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb)の指示に従ってキャンペーンを作成します。
4. **キャンペーン Message Settings**の下にBraze キャンペーン IDを貼り付け、キャンペーンを起動します。

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### アクションベースの配信 {#action-based-delivery}

この統合により、ジオフェンス情報、地域、ブランド名、または店舗名を送信することでロケーション条件を適用できます。さらに、作成したカスタムイベントを使用してセグメントを追加したり、コンバージョンを割り当てたりできます。
1. [loplat Xユーザーガイド](https://loplatx-user-guide.notion.site/キャンペーン-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598)の指示に従って、loplat Xキャンペーンを作成します。
2. **キャンペーン Message Settings**の下にカスタムイベントを追加し、キャンペーンを起動します。
3. Brazeダッシュボードに移動して、**Action-Based Delivery**で送信するキャンペーンまたはキャンバスを作成します。
4. loplat Xで作成したカスタムイベントを選択して、ロケーショントリガーアクションを設定します。

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})