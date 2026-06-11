---
nav_title: Shopify for Currents
article_title: Shopify for Currents
description: "このリファレンス記事では、Braze CurrentsとShopifyのパートナーシップについて説明します。Shopifyはグローバルなコマース企業であり、BrazeとShopifyストアをシームレスに接続して、内部レポートを強化し、購入のラストタッチアトリビューションをより適切に追跡できます。"
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify for Currents

> [Shopify](https://www.shopify.com/)は、あらゆる規模のビジネスの立ち上げ、成長、マーケティング、管理を支援する信頼性の高いツールを提供する、世界をリードするグローバルコマース企業です。Shopifyのプラットフォームとサービスは、信頼性を重視して設計されており、あらゆる場所の消費者により良いショッピング体験を提供します。

{% alert important %}
この統合は現在ベータ版です。詳細については、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

BrazeとShopifyの統合は、カスタマーエンゲージメントを強化し、パーソナライズされたマーケティング施策を推進したいeコマースビジネスに強力なソリューションを提供します。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用すると、データをShopifyに接続して内部レポートを強化し、購入のラストタッチアトリビューションをより適切に追跡できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Currents | データをShopifyにエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)が設定されている必要があります。 |
| Shopifyストア | Brazeで[少なくとも1つのShopifyストアがすでに設定されている]({{site.baseurl}}/shopify_standard_integration/)ことを確認してください。 |
| Shopifyストアオーナーまたはスタッフメンバーの権限 | {::nomarkdown}<ul><li>すべての<b>General</b>および<b>Online Store</b>設定へのアクセス。</li><li>追加の管理者権限:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ1:Shopifyストアを設定する {#step-1-set-up-your-shopify-store}

まだ設定していない場合は、[Shopify標準統合セットアップ]({{site.baseurl}}/shopify_standard_integration/)の手順に従って、Brazeで少なくとも1つのShopifyストアを設定してください。

### ステップ2:Braze Currentを作成する {#step-2-create-braze-current}

1. Brazeで、**パートナー連携** > **Currents** > **+ 新規Currentを作成** > **Shopify Export** に移動します。
2. 統合名と連絡先メールアドレスを入力します。
3. **認証情報**セクションで、[ステップ1](#step-1-set-up-your-shopify-store)で設定したShopifyストアを選択します。
4. 追跡するイベントを選択します。利用可能なイベントのリストが表示されます。
5. **Launch Current** を選択します。

![Braze Shopify Currentsページ。このページには、統合名、連絡先メール、Shopifyストアのフィールドが含まれています。]({% image_buster /assets/img/shopify/shopify_currents.png %})