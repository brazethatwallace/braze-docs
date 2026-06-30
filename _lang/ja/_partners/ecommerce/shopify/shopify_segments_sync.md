---
nav_title: Shopify セグメントの同期
article_title: Shopify セグメントの同期
alias: /shopify_segments_sync/
page_order: 8
description: "このリファレンス記事では、統一されたオーディエンス管理とターゲティングのために、Shopify セグメントをBrazeにコホートとして同期する方法について説明します。"
---

# Shopify セグメントの同期 {#shopify-segments-sync}

> Shopify セグメントの同期は、Shopifyストアの機能をBrazeに拡張し、マーケティングチームがShopifyに存在するより豊富なユーザーデータ（標準のBraze Shopify連携ではキャプチャされないシグナルを含む）に直接アクセスできるようにします。Shopify セグメントをコホートとして同期することで、両プラットフォーム間でオーディエンス定義を統一し、ユーザーがShopifyでターゲティングされる場合でもBraze キャンペーンを通じてエンゲージされる場合でも、一貫性のある連携されたユーザー体験を提供できます。

{% alert important %}
Shopify セグメントの同期は現在ベータ版です。アクセスをリクエストするには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| Braze Shopify連携 | Braze ShopifyアプリがShopifyストアにインストールされ、Brazeワークスペースに接続されている必要があります。セットアップ手順については、[Shopify標準連携セットアップ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/)または[Shopifyカスタム連携セットアップ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/)を参照してください。 |
| Shopifyユーザー権限 | セグメントの同期を開始するShopifyユーザーには、顧客データをエクスポートするための**エクスポート**権限が必要です。Shopifyの権限の詳細については、[Shopifyのストア権限ドキュメント](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 仕組み {#how-it-works}

Shopify セグメントの同期は2つのフェーズで動作します。

1. セグメントを初めて同期する際、Brazeは現在のすべてのメンバーをバックフィルし、Brazeに対応するコホートを作成します。バックフィルは非同期で実行され、完了までに少し時間がかかる場合があります。
2. 初回同期中に、Brazeは現在のメンバーをバックフィルし、Shopify webhookをサブスクライブして、メンバーシップがほぼリアルタイムで同期された状態を維持します。

| Webhookトピック | Brazeでの効果 |
| --- | --- |
| `customer.joined_segment` | ユーザーが対応するBrazeコホートに追加されます。 |
| `customer.left_segment` | ユーザーが対応するBrazeコホートから削除されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhookトピック" }

同期が失敗した場合、アクション拡張モーダルに推奨アクション付きのエラーバナーが表示されます。**Sync with Braze**を選択してリトライしてください。

## データインポート連携 {#data-import-integration}

### ステップ 1: 同期するShopify セグメントを選択する {#step-1-select-a-shopify-segment-to-sync}

Shopifyで、**Customers** > **セグメント**に移動し、Brazeに同期したいセグメントを選択します。注文履歴、製品購入、顧客タグ、生涯支出額、メタフィールドに基づくセグメントなど、Shopifyのネイティブセグメンテーションを使用して構築された任意のセグメントを同期できます。

![Shopify セグメントのリストが表示されたセグメントパネル。]({% image_buster /assets/img/shopify/shopify_segments.png %})

### ステップ 2: 同期を開始する {#step-2-initiate-the-sync}

1. Shopifyのセグメント詳細ページで、**Use segment**ドロップダウンを開き、**Braze セグメント Sync**を選択します。

![「Braze セグメント Sync」オプションを含む「Use segment」ドロップダウンが表示されたセグメント詳細ページ。]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. 表示されるBrazeアクション拡張モーダルに、セグメント名とオーディエンスサイズが表示されます。**Sync with Braze**を選択してインポートを開始します。

![Brazeと同期するボタンが表示されたモーダル。]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. **Done**を選択します。

![同期がアクティブであることを確認するモーダル。]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### ステップ 3: コホートメンバーシップフィルターでBraze セグメントを作成する {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Brazeで、**Audience** > **セグメント**に移動し、新しいセグメントを作成します。**Add Filter**で**Cohort Membership**フィルターを選択し、ドロップダウンから同期済みのShopify セグメントを選択します。保存後、キャンペーンまたはキャンバスでユーザーをターゲティングする際にこのBraze セグメントを参照できます。

![「Shopify Cohorts」フィルターが表示されたセグメントビルダー。]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## ユーザーマッチング {#user-matching}

Shopify セグメントから同期されたユーザーは、Braze Shopify連携の一部として設定される`shopify_customer_id`エイリアスを使用してBrazeユーザープロファイルとマッチングされます。一致するBrazeユーザープロファイルがないユーザーは、同期中にスキップされます。

Shopify連携がユーザーを識別しエイリアスを設定する方法の詳細については、[Shopifyデータ機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。

## 制限事項 {#limitations}

- **一方向同期。** セグメントメンバーシップは、ShopifyからBrazeへの一方向のみです。Brazeで直接行われたコホートメンバーシップの変更は、Shopifyにプッシュバックされません。
- **プロファイル作成なし。** すでにBrazeユーザープロファイルを持つShopify顧客のみがコホートに追加されます。
- **同期の取り消し不可。** Shopify セグメントが同期されると、取り消すことはできません。