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

## Shopify コレクション同期の設定 {#setting-up-shopify-collections-sync}

ShopifyストアからBrazeに商品を同期するには、[Shopifyの統合]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#setting-up-shopify-in-braze)の**商品を同期**ステップで**Shopify コレクションを同期**のチェックボックスを選択します。<br><br>![Shopify 商品同期のステップ4。「Shopify コレクションを同期」チェックボックスが選択されている状態。][1]

商品が同期されたら、Shopifyカタログを表示して、どの商品がコレクションに関連付けられているかを確認できます。<br><br>![カタログテーブルの行。「best-sellers」と「front page」のコレクションに含まれる商品が表示されている。][2]

Shopifyカタログから、**セレクション**タブでShopifyコレクションを表示できます。<br><br>![セレクションタブ。「best-sellers」と「front page」の2つのコレクションのリストが表示されている。][3]

### ベータ版の機能 {#beta-functionality}

- Brazeは最大30のコレクションをサポートします。
- コレクションの並び順は現時点では維持またはサポートされていません。現在の並び順は以下に基づいています:
    - コレクションに最近追加されたアイテム。
    - 継続的な同期中にアイテムが更新される順序。
    - Shopifyコレクションのセレクションタブで選択した順序。

## Shopify コレクションの使用 {#using-shopify-collections}

Shopifyコレクションを使用して、Campaign内の各ユーザーに対してメッセージをパーソナライズできます。これは[Brazeセレクション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)の使用方法と同様です。

{% alert warning %}
ベータ版では以下の動作にご注意ください。<br><br>Shopifyコレクションの説明やフィルター設定を更新すると、Shopifyコレクション同期が壊れます。その結果、Shopifyコレクションが期待どおりに動作しなくなります。
{% endalert %}

### ステップ1: Shopifyコレクションの並び順を設定する {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Shopifyコレクションのセレクションタブで**並び順**を選択して、Shopifyコレクションの結果が返される順序を指定します。並び順をランダムにするオプションも含まれています。
2. **結果の上限数**に最大結果数（最大50）を入力します。
3. **セレクションを更新**を選択します。

![セレクションの編集ページ。フィルター設定、並び替えの種類、結果の上限を選択できる。][4]

### ステップ2: Campaignでコレクションを使用する {#step-2-use-the-collection-in-a-campaign}

1. Campaignを作成し、メッセージ作成画面で**+ パーソナライゼーション**を選択します。
2. 以下を選択します:<br>- **パーソナライゼーションタイプ**として**カタログアイテム**<br>- カタログ名<br>- アイテムの選択方法<br>- セレクション名（Shopifyコレクション名）<br>- メッセージに表示する情報

{: start="3"}
3. メッセージ内で情報を表示したい場所にLiquidスニペットをコピーして貼り付けます。

![「パーソナライゼーションを追加」セクション。カタログ、アイテムの選択方法、表示する情報を選択するフィールドがある。][5]{: style="max-width:30%;"}

#### セレクション結果でのLiquid {#liquid-in-selection-results}

カスタム属性やカスタムイベントなど、カタログ内の結果を使用すると、セレクション内のユーザーごとに異なる結果が返される場合があります。

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}