---
nav_title: 10月
page_order: 2
noindex: true
page_type: update
description: "この記事には2021年10月のリリースノートが含まれています。"
---

# 2021年10月 {#october-2021}

## データポイント使用量ダッシュボード {#data-points-usage-dashboard}

**データポイント使用量の合計**ダッシュボードを使用して、契約割り当てに対するデータポイントの使用ペースを追跡できます。このダッシュボードには、契約内容、現在の請求サイクル、会社の請求データ、ワークスペースの請求データに関する情報が表示されます。詳細については、[請求]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage#total-data-points-dashboard)を参照してください。

## セグメントエクステンションの再生成の変更 {#change-to-segment-extension-regeneration}

2022年2月1日以降、未使用の[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)については、エクステンションを毎日再生成する設定が自動的にオフになります。Brazeでは、未使用のエクステンションを次の基準を満たすものと定義しています。

- アクティブなキャンペーン、キャンバス、またはセグメントで使用されていない
- 非アクティブな（下書き、停止、アーカイブされた）キャンペーン、キャンバス、またはセグメントで使用されていない
- 7日以上変更されていない

この設定がオフになると、Brazeは会社の連絡先とエクステンションの作成者に通知します。エクステンションを毎日再生成するオプションはいつでも再度有効にできます。

## Android高度な実装ガイド {#android-advanced-implementation-guides}

### Content Cards

このオプションの高度な[実装ガイド]({{site.baseurl}}/developer_guide/content_cards)では、Content Cardsのコードに関する考慮事項、当社チームが構築した3つのカスタムユースケース、付随するコードスニペット、インプレッション・クリック・却下のログに関するガイダンスについて説明しています。

### アプリ内メッセージ {#in-app-messaging}

このオプションの高度な[実装ガイド]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)では、アプリ内メッセージのコードに関する考慮事項、当社チームが構築した3つのカスタムユースケース、付随するコードスニペットについて説明しています。

### プッシュ通知 {#push-notifications}

このオプションの高度な[実装ガイド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)では、カスタム`FirebaseMessagingService`サブクラスを活用してプッシュメッセージを最大限に活用する方法について説明しています。当社チームが構築したカスタムユースケース、付随するコードスニペット、分析のログに関するガイダンスが含まれています。

## Brazeの新しいパートナーシップ {#new-braze-partnerships}

### Adobe - 顧客データプラットフォーム {#adobe-customer-data-platform}

Adobe Experience Platform上に構築されたAdobeのリアルタイム顧客データプラットフォーム（リアルタイムCDP）は、企業が複数のエンタープライズソースからの既知のデータと匿名データを統合し、すべてのチャネルとデバイスでパーソナライズされた顧客体験をリアルタイムで提供するために使用できる顧客プロファイルを作成するのに役立ちます。

Brazeと[Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe) CDPの統合により、ブランドはAdobeデータ（カスタム属性とセグメント）をリアルタイムでBrazeに接続し、マッピングできます。ブランドはこのデータに基づいて行動し、パーソナライズされたターゲット体験をユーザーに提供できます。

### Shopify - eコマース {#shopify-ecommerce}

[Shopify]({{site.baseurl}}/partners/shopify)は、あらゆる規模の小売ビジネスの開始、拡大、マーケティング、および管理のための信頼できるツールを提供する、世界をリードするコマース企業です。BrazeとShopifyの統合により、ブランドはShopifyストアをBrazeとシームレスに接続し、選択したShopifyのwebhookをBrazeに渡すことができます。Brazeのクロスチャネル戦略とキャンバスを活用して、購入手続き放棄のメッセージングでユーザーをリターゲティングし、顧客に購入を完了するよう促したり、以前の購入に基づいてユーザーをリターゲティングしたりできます。