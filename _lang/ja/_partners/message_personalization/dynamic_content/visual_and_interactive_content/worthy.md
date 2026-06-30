---
nav_title: Worthy
article_title: Worthy
description: "このリファレンス記事では、BrazeとWorthyのパートナーシップについて説明します。Worthyは、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Brazeを通じて配信できるメッセージパーソナライゼーションプラットフォームです。"
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> [Worthy](https://worthy.ai/)とBrazeの連携では、Worthyのドラッグアンドドロップエディターを使ってパーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Brazeを通じて配信できます。さらに、Worthyは自動的に以下を実行します。

_この連携はWorthyによって管理されています。_

## 連携について {#about-the-integration}

- メッセージングのためのコネクテッドコンテンツサーバーとセキュアなAPIを作成します。
- 分析とクリックトラッキングを備えたアプリ内メッセージを構築し、Brazeに直接表示します。
- Worthyのドラッグアンドドロップエディターを使用してHTMLを自動的にエクスポートし、Brazeの**Custom Code**アプリ内メッセージキャンペーンで使用します。必要なAPI接続と設定したダイナミックなコンテンツが含まれます。

## ユースケース {#use-cases}

- ユーザーのオンボーディング選択に基づくカスタムウェルカムエクスペリエンス
- スペシャルイベントやプロモーションのアプリ内エクスペリエンス
- アプリの動作に基づく顧客フィードバックと評価の収集
- アプリ製品アイデアの迅速なテスト
- リッチな通知、ニュース、コミュニティの更新

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| [Worthy](https://worthy.ai/)アカウント | このパートナーシップを活用するには、Worthyアカウントが必要です。 |
| Braze SDK | リッチなアプリ内メッセージを送信するには、モバイルアプリケーションでBraze SDKを設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Worthyでパーソナライズされたメッセージングを作成する {#step-1-create-personalized-messaging-in-worthy}

Worthyダッシュボードでアプリに移動し、**Message Creator**を選択して、ユーザーのエンゲージメントに使用するパーソナライズされたメッセージを作成します。

### ステップ2：Brazeでキャンペーンを作成する {#step-2-create-a-braze-campaign}

Brazeで[アプリ内メッセージキャンペーン]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)を作成し、**メッセージタイプ**を**Custom Code**に設定します。

### ステップ3：パーソナライズされたメッセージをBrazeにコピーする {#step-3-copy-your-personalized-message-into-braze}

Worthyメッセージクリエーターで**エクスポート**をクリックし、**Braze**を選択して、パーソナライズされたメッセージをBraze キャンペーンで使用するためにエクスポートします。エクスポートされたコンテンツを、Braze キャンペーンエディターの**HTML + Asset Zip**の下にあるHTMLテキストボックスにコピーします。

以上です！Braze キャンペーンエディターの**Test**タブを使用して、パーソナライズされたメッセージをすぐにテストできます。