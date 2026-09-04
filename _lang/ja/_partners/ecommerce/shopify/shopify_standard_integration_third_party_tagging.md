---
nav_title: Shopify標準統合とサードパーティタギング
article_title: Shopify標準統合とサードパーティタギング
description: "このリファレンス記事では、サードパーティのタグツールを使用してShopifyの標準統合を設定する方法について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Shopify標準統合とサードパーティタグツール {#shopify-standard-integration-with-third-party-tagging-tool}

> このページでは、Google Tag マネージャーのようなサードパーティツールを[Shopify標準統合]({{site.baseurl}}/shopify_standard_integration)で使用し、Braze Web SDKを初期化して読み込む方法をご案内します。

Shopifyオンラインストアの場合は、Brazeの標準統合方法を使用して、サイトでBraze SDKをサポートすることを推奨します。ただし、Google Tag マネージャーのようなサードパーティツールの使用を希望される場合があることも理解しています。BrazeのShopifyコネクターでサードパーティツールを使用する場合は、Braze統合とアプリ埋め込みがチェックアウトプロセス中にSDKを管理することに留意してください。

## 要件 {#requirements}

- **サードパーティツールとShopifyコネクター間でAPIキーを統一する：** APIキーは、Brazeとサードパーティツールの両方で一貫している必要があります。これにより、重複ユーザーの作成を防ぎ、SDK間の互換性を維持できます。
  - **APIキーの場所：** 標準統合パスでオンボーディングした後、統合により「Shopify」という名前のBraze Webアプリが自動的に作成されます。サードパーティツールの設定で使用するAPIキーを統合内から取得してください。
- **サードパーティツールとShopifyコネクター間でSDKバージョンを統一する：** 新規顧客には、設定時に最新のSDKバージョンがプロビジョニングされます。サードパーティツールでは、Braze統合設定で構成されたものと同じSDKバージョンを使用する必要があります。既存の顧客には、新しいバージョンが利用可能になると通知され、統合設定からセルフサービスでアップグレードできます。
- **SDK初期化のタイミングを統一する：** Shopifyの標準統合設定で、セッション開始時またはアカウントログイン時に初期化するSDKを選択できます。この設定は、サードパーティツールとBrazeの間で一貫している必要があります。不整合があると、ユーザーやデータ同期に下流の問題が発生する可能性があります。

{% alert note %}
Braze SDKとサードパーティツールの間で競合が発生する可能性があるため、サードパーティタグマネージャーと併用するのではなく、標準統合方法のみを使用することを推奨します。サードパーティツールを使用する場合は、すべてが期待どおりに機能することをテストして確認してください。
{% endalert %}

## サードパーティツールとの統合設定 {#setting-up-the-integration-with-a-third-party-tool}

提供されたステップから外れると予期しない問題が発生する可能性があるため、必ず手順に従ってください。

1. [Shopify標準統合セットアップ]({{site.baseurl}}/shopify_standard_integration)で提供されているステップに従います。[Braze Web SDKを有効にする]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-2-enable-braze-web-sdks)際に、サードパーティツールを使用してShopifyサイトにBraze Web SDKを追加することを示すチェックボックスをオンにします。
2. **設定** > **アプリ設定**に移動し、**Shopify** Webアプリを選択して、**API key for Shopify on Web**をコピーします。
3. APIキーをサードパーティツールのWeb SDK設定に貼り付け、SDKバージョンをBraze Shopify統合と一致するように設定します。

{% alert note %}
Google Tag マネージャーを使用している場合は、GTMとBraze Shopify統合設定の両方でSDKバージョンを揃えてください。
{% endalert %}

## Shopifyデータの取得とユーザーの同期 {#capturing-shopify-data-and-syncing-users}

Web SDKがサードパーティツールを通じてShopifyサイトのフロントエンドでアクセス可能である限り、標準統合は期待どおりにShopifyデータを取得し、ユーザーを同期します。

## 考慮事項と免責事項 {#considerations-and-disclaimers}

- **初期化設定：** サードパーティツールで初期化設定を変更した場合、ユーザーとデータの同期に影響が出る可能性があります。たとえば、Cookie同意フォームが承認されたときにSDKを初期化するように選択した場合、ユーザーが同意するまでBrazeは匿名ユーザーやデータのトラッキングを受信しません。
- **`dataLayer`を通じて直接属性を設定することはサポートされていません：** 属性を設定するには、`dataLayer`ではなく`window.braze`を使用してください。
- **重複ユーザーの可能性：** APIキーがBrazeとサードパーティツールで一致しない場合、重複ユーザーが作成される可能性があります。
- **SDKの非互換性：** 正しくないバージョン番号を使用すると、SDKメソッドで問題が発生する可能性があります。