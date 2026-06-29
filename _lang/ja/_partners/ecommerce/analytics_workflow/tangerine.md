---
nav_title: Tangerine
article_title: Tangerine
description: "この記事では、BrazeとTangerine Store360の提携について説明します。Tangerine Store360は、実店舗とオンライン店舗を接続し、消費者と店舗従業員に優れた店内体験を提供するオムニチャネルプラットフォームです。この統合により、Snowflakeセキュアデータシェアリングを介してStore360でBrazeの生のCampaignデータとインプレッションデータが利用可能になります。ブランドは、店内エンゲージメントとストアトラフィックに対するCampaignの影響を測定できます。"
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerineは、Store360というオムニチャネルプラットフォームを設計、構築、運営しています。Store360は、消費者と店舗従業員の店内体験を向上させるために、実店舗とオンラインストアを接続するオムニチャネル対応のプラットフォームです。Store360は、小売業者のモバイルアプリユーザーとその店内エンゲージメントを含む、実店舗訪問トラフィックを追跡および分析します。

BrazeとTangerineの統合により、BrazeからSnowflakeセキュアデータシェアリングを介してStore360に生のCampaignデータとインプレッションデータを統合できます。ブランドは、これらのCampaignが実店舗への訪問や店内エンゲージメントに与える影響を測定できるようになります。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Store360アカウント | このパートナーシップを利用するには、Store360アカウントが必要です。 |
| BrazeアカウントID | BrazeアプリグループIDです。 |
| ユーザーIDの一致 | Store360とBrazeの顧客データは、両方のプラットフォームで一致するユーザーIDを持っている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

### 実店舗への訪問に対するCampaignの影響を分析する {#analyze-campaign-impact-on-physical-store-visit}

ブランドはBrazeを使用して、消費者にCampaignメッセージを送信し、店舗訪問を増やします。Campaign期間中、Store360はユーザーIDで識別されたモバイルアプリユーザーの訪問を記録します。

ブランドはStore360インサイト分析機能を使用して、送信され閲覧されたメッセージ（Brazeのデータ）から、実店舗を訪問した受信者の情報と訪問受信者数（Store360のデータ）まで、Campaignの影響の詳細を視覚化できます。

## 統合 {#integration}

### ステップ1: Snowflakeセキュアデータシェアリングを有効にする {#step-1-enable-snowflake-secure-data-share}

Brazeチームと協力して、Snowflakeセキュアデータシェアリングを有効にして設定します。

### ステップ2: Store360を設定してBrazeデータを取得する {#step-2-configure-store360-to-get-braze-data}

Store360管理マネージャーWebコンソールを使用して、BrazeアプリグループIDをStore360サービスアカウントに設定します。これにより、Tangerine管理チームに対し、Snowflakeデータシェアリングを使用してBrazeデータをStore360に同期するリクエストが送信されます。

### ステップ3: モバイルアプリにStore360 SDKを統合する {#step-3-integrate-store360-sdks-to-mobile-app}

モバイルアプリユーザーのストア訪問と店内アクティビティを、BrazeのCampaignデータおよびインプレッションデータとともに追跡・分析するには、Store360 SDKインストールドキュメントに記載されている手順に従って、Store360 SDKをモバイルアプリに統合する必要があります。このドキュメントは、Tangerine Store 360とのクライアント契約を締結した後に提供されます。

## Store360でBrazeデータを分析する {#analyze-braze-data-in-store360}

Snowflakeのセキュアデータシェアリングを利用して、Brazeの生のCampaignおよびインプレッションデータをStore360のインサイト分析と共有し、オンラインからオフラインまでのユーザーのライフサイクルと活動の全体像を把握できます。

参考までに、Store360分析に組み込むことができるすべての[Brazeフィールド](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)を以下に示します。このステップの詳細は顧客によって大きく異なり、特別な設定が必要です。詳細については、Store360のアカウントマネージャーまたは support@tangerine.io までお問い合わせください。

## 重要な情報と制限 {#important-information-and-limitations}

### サービスの提供状況 {#service-availability}

現在、Store360サービスは日本とインドネシアで商用提供されています。

Tangerineは2023年に以下の国々でStore360製品の発売を計画しています。
- アメリカ合衆国
- タイ
- シンガポール
- ベトナム
- 韓国

### データリテンション {#data-retention}

Snowflakeデータシェアリングに関して、Brazeデータには2年間のリテンションポリシーがあります。

### Brazeイベントデータの反映における時間差 {#time-lag-in-populating-braze-event-data}

Brazeのイベントはストリーミング技術で処理され、ほぼリアルタイムで利用可能です。一般的に、イベントは発生してから30分以内に利用可能になります。