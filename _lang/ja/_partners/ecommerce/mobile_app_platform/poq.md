---
nav_title: Poq
article_title: PoqとBrazeの統合
description: "プッシュ通知、アプリ内メッセージ、分析、Content Cards、バナーなど、ネイティブモバイルアプリ体験を実現するPoqとBrazeの統合について説明します。"
page_type: partner
search_tag: Partner
alias: /partners/poq/
---

# Poq

[Poq](https://poqcommerce.com/)は、エンタープライズ企業が完全ネイティブのiOSおよびAndroidアプリを迅速に立ち上げ、管理、スケーリングできるようにし、コマースを促進しブランドの約束を実現する高パフォーマンスのモバイル体験を提供します。

*この統合はPoqによって管理されています。*

## 統合について {#about-the-integration}

PoqとBrazeの統合により、ネイティブモバイルアプリ体験をBrazeのカスタマーエンゲージメントプラットフォームに接続できます。BrazeのiOSおよびAndroid SDKを使用して、BrazeはPoqを搭載したアプリに直接統合され、モバイルでのセグメンテーション、パーソナライゼーション、ターゲットキャンペーン配信が可能になります。

## サポートされている機能 {#whats-supported}

以下のチャネルと機能がサポートされています。

| チャネル/機能 | 説明 |
| :---- | :---- |
| プッシュ通知 | リッチプッシュ通知を含む、ターゲットを絞ったパーソナライズ済みプッシュ通知をBrazeを通じてアプリユーザーに送信します。 |
| アプリ内メッセージ | ネイティブアプリ体験内でBrazeのアプリ内メッセージを表示し、カスタマージャーニーの適切なタイミングでユーザーにエンゲージします。 |
| 分析とイベントトラッキング | Poqはカスタマージャーニー全体をカバーする包括的なアプリイベントセットをBrazeに送信します。このデータにより、Brazeでのセグメンテーション、キャンペーントリガー、パーソナライゼーションが可能になります。 |
| Content Cardsとメッセージ受信トレイ | アプリ内で永続的なBraze Content Cardsを配信します。専用のメッセージ受信トレイ画面、PoqのDynamic Contentページビルダーで構築されたページ、またはアプリ全体の事前定義されたスロット内に表示できます。Content Cardsは、Brazeで設定されたキーと値のペアを使用してフィルタリングされます。 |
| バナー | アプリ内でBrazeバナーを表示します。PoqのDynamic Contentページビルダーで構築されたページ、またはアプリ全体の事前定義されたスロット内に表示できます。バナーコンテンツはプレースメントIDを使用して取得されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What's supported" }

## 前提条件 {#prerequisites}

この統合を使用するには、以下が必要です。

| 要件 | 説明 |
| :---- | :---- |
| Poqアプリ | この統合を利用するには、Poqアプリが必要です。 |
| BrazeアプリAPIキー | 各プラットフォーム（iOSおよびAndroid）にBrazeアプリAPIキーが必要です。Brazeダッシュボードの**Settings** > **APIs and Identifiers** > **App Identifiers**から取得できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

セットアップはPoqアプリの実装の一環として行われます。ご質問がある場合は、Poqのデリバリーチームまたはカスタマーサクセスチームに連絡するか、[Poqにお問い合わせ](https://poqcommerce.com/contact-us/)ください。