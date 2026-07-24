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

BrazeとShopifyの統合は、カスタマーエンゲージメントを強化し、パーソナライズされたマーケティング施策を推進したいeコマースビジネスに強力なソリューションを提供します。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用すると、データをShopifyに接続して内部レポートを強化し、購入のラストタッチアトリビューションをより適切に追跡できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Currents | Shopifyにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)が設定されている必要があります。 |
| Shopifyストア | すでに[Brazeで少なくとも1つのShopifyストアを設定]({{site.baseurl}}/shopify_standard_integration)していることを確認してください。 |
| Shopifyストアオーナーまたはスタッフメンバーの権限 | {::nomarkdown}<ul><li>すべての<b>一般</b>および<b>オンラインストア</b>設定へのアクセス。</li><li>追加の管理者権限:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 連携 {#integration}

### ステップ1:Shopifyストアを設定する {#step-1-set-up-your-shopify-store}

まだ設定していない場合は、[Shopify標準連携の設定]({{site.baseurl}}/shopify_standard_integration)手順に従って、Brazeで少なくとも1つのShopifyストアを設定してください。

### ステップ2:Braze Currentsを作成する {#step-2-create-braze-current}

1. Brazeで、**パートナー連携** > **Currents** > **+ Create New Current** > **Shopify Export** に移動します。
2. 連携名と連絡先メールアドレスを入力します。
3. **認証情報**セクションで、[ステップ1](#step-1-set-up-your-shopify-store)で設定したShopifyストアを選択します。
4. トラッキングしたいイベントを選択します。利用可能なイベントの一覧が表示されます。
5. **Launch Current** を選択します。

![Braze Shopify Currentsページ。このページには、連携名、連絡先メール、Shopifyストアのフィールドが含まれています。]({% image_buster /assets/img/shopify/shopify_currents.png %})

## ユーザープロファイルの同期 {#user-profile-sync}

イベントデータに加えて、Shopify連携ではBrazeからShopifyストアへのユーザープロファイルの更新を同期できます。Brazeでユーザーのプロファイルが更新されると、Currentsがストア内の一致する顧客を作成または更新します。

### ユーザーマッチング {#user-matching}

BrazeはBrazeの`user_id`をShopifyの[カスタム識別子](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet)（`customId`）として使用し、名前空間`braze`とキー`user_id`でShopifyの顧客とマッチングします。そのストアにその識別子を持つ顧客が存在しない場合、新しい顧客が作成されます。匿名ユーザーは同期されません。

### フィールドマッピング {#field-mapping}

以下のBrazeプロファイルフィールドがShopifyに同期されます。

| Brazeフィールド | Shopify顧客フィールド | 備考 |
| ----------- | ---------------------- | ----- |
| `first_name` | `firstName` | そのままマッピングされます。プロファイル更新に含まれている場合のみ送信されます。 |
| `last_name` | `lastName` | そのままマッピングされます。プロファイル更新に含まれている場合のみ送信されます。 |
| `email_address` | `email` | 送信前にトリミングされ、小文字に変換されます。 |
| `phone_number` | `phone` | [E.164](https://en.wikipedia.org/wiki/E.164)形式で送信されます。 |
| `language` | `locale` | Shopifyがサポートするロケールに変換されます。ポルトガル語と中国語は、ユーザーの国に基づいて地域バリアント（`pt-BR`など）が割り当てられます。ユーザーの言語がShopifyでサポートされていない場合、このフィールドは省略されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

プロファイル更新に含まれているフィールドのみが送信されます。更新から省略されたフィールドはShopifyで変更されません。同期によってShopify顧客のフィールドがクリアまたは削除されることはありません。

### 同期されないフィールド {#fields-that-are-not-synced}

この連携は現在Shopifyメタフィールドへの書き込みに対応していないため、メタフィールドが必要なプロファイルフィールドは同期されません。特に、カスタム属性はShopifyに送信されません。その他送信されないフィールドは、`external_user_id`、`gender`、`dob`（生年月日）、`timezone`、`home_city`、`country`、`archived`です。

Brazeはストア上の`braze`名前空間にメタフィールド定義を作成する場合があります（例：`braze.gender`）。これらの定義は将来の使用のために予約されており、Brazeは現在これらに値を書き込みません。例外は`braze.user_id`で、顧客のマッチングに使用される識別子を保存します。