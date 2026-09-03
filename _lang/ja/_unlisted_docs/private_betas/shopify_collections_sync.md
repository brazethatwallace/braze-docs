---
nav_title: Shopify コレクション同期
article_title: Shopify コレクション同期
permalink: "/shopify_collections_sync/"
description: "このリファレンス記事では、Shopify コレクション同期の設定方法について説明します。この機能を使用すると、商品をコレクションにグループ化し、顧客がカテゴリ別に商品を見つけられるようになります。"
hidden: true
---

# Shopify コレクション同期ベータ版 {#shopify-collections-sync-beta}

> Shopify コレクション同期を使用すると、商品をコレクションにグループ化し、顧客がカテゴリ別に商品を見つけられるようになります。よりシームレスなショッピング体験を実現するために、ショップのコレクション内のアイテムをBrazeのメッセージングに組み込むことができます。

{% alert important %}
Shopify コレクション同期は現在ベータ版です。ベータ版への参加をご希望の場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## Shopifyコレクション同期の設定 {#setting-up-shopify-collections-sync}

Shopifyストアから Braze に商品を同期するには、[Shopifyの統合]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze)の**商品を同期**ステップで**Shopifyコレクションを同期**のチェックボックスを選択します。<br><br>![Shopify商品同期のステップ4で「Shopifyコレクションを同期」チェックボックスが選択されている画面。][1]

商品が同期されたら、Shopifyカタログを表示してコレクションに関連付けられている商品を確認できます。<br><br>![「best-sellers」と「front page」のコレクションに含まれる商品を示すカタログテーブルの行。][2]

Shopifyカタログから、**Selections** タブでShopifyコレクションを表示できます。<br><br>![「best-sellers」と「front page」の2つのコレクションのリストを表示するSelectionsタブ。][3]

### ベータ機能 {#beta-functionality}

- Braze は最大30個のコレクションをサポートします。
- コレクションの並び順は現時点では維持またはサポートされていません。現在、並び順は以下に基づいています：
    - コレクションに最近追加されたアイテム。
    - 継続的な同期中にアイテムが更新される順序。
    - Shopifyコレクションの Selection タブで選択した順序。

## Shopifyコレクションの使用 {#using-shopify-collections}

Shopifyコレクションを使用して、[Brazeセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)と同様に、キャンペーン内の各ユーザーに合わせたメッセージをパーソナライズできます。

{% alert warning %}
ベータ版での以下の動作にご注意ください。<br><br>Shopifyコレクションの説明またはフィルター設定を更新すると、Shopifyコレクションの同期が破損します。その結果、Shopifyコレクションが期待どおりに動作しなくなります。
{% endalert %}

### ステップ1:Shopifyコレクションのソート順を設定する {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Shopifyコレクションのセレクションタブで**Sort Order**を選択して、Shopifyコレクションの結果が返される順序を指定します。ソート順をランダムにするオプションも含まれています。
2. **Limit number**に結果の最大数（最大50件）を入力します。
3. **Update Selection**を選択します。

![フィルター設定、ソートタイプ、結果の上限数を選択できるセレクション編集ページ。][4]

### ステップ2:キャンペーンでコレクションを使用する {#step-2-use-the-collection-in-a-campaign}

1. キャンペーンを作成し、メッセージ作成画面で**+ Personalization**を選択します。
2. 以下を選択します。<br>- **Personalization type**として**Catalog Items**<br>- カタログ名<br>- アイテム選択方法<br>- セレクション名（Shopifyコレクション名）<br>- メッセージに表示する情報

{: start="3"}
3. メッセージ内で情報を表示したい場所にLiquidスニペットをコピーして貼り付けます。

![カタログ、アイテム選択方法、表示する情報を選択するフィールドがある「Add Personalization」セクション。][5]{: style="max-width:30%;"}

#### セレクション結果でのLiquid {#liquid-in-selection-results}

カスタム属性やカスタムイベントなど、カタログの結果を使用すると、セレクション内のユーザーごとに異なる結果が返される場合があります。

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}