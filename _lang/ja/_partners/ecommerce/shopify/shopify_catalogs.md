---
nav_title: Shopify 製品の同期
article_title: Shopify 製品の同期
alias: /shopify_catalogs/
page_order: 5
description: "このリファレンス記事では、ShopifyからBrazeカタログに製品をインポートする方法について説明します。"
---

# Shopify 製品の同期 {#shopify-product-sync}

> Shopifyストアの全製品をBrazeの[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)に同期し、より深いメッセージングパーソナライゼーションを実現できます。

Shopifyカタログは、Shopifyストア内の製品に編集や変更を加えると、ほぼリアルタイムで更新されます。カート放棄や注文確認などを、最新の製品詳細や情報で強化できます。

{% alert warning %}
Brazeは各Shopify製品につき最大250のバリアントをカタログに同期します。この制限を超えるバリアントは同期されません。1製品あたり250を超えるバリアントが必要な場合は、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## Shopify 製品の同期を設定する {#setting-up}

Shopifyストアがすでにインストールされている場合でも、以下の手順に従って製品を同期できます。

### ステップ1: 同期をオンにする {#step-1-turn-on-the-sync}

ShopifyのインストールフローまたはShopifyパートナーページで、製品をBrazeカタログに同期できます。

![設定プロセスのステップ3。「カタログの製品識別子」に「Shopify バリアント ID」が設定されている。]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Brazeカタログに同期された製品は、[カタログ制限]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers)の対象になります。

### ステップ2: 製品識別子を選択する {#step-2-select-your-product-identifier}

カタログIDとして使用する製品識別子を選択します。
- Shopify バリアント ID
- SKU

選択する製品識別子のIDとヘッダーの値には、文字、数字、ハイフン、アンダースコアのみを使用できます。製品識別子がこの形式に従っていない場合、Brazeはカタログの同期からその識別子を除外します。

これは、Brazeカタログ情報を参照するときに使用する主要な識別子です。

{% alert note %}
カタログIDとしてSKUを選択する場合は、ストア内のすべての製品とバリアントにSKUが設定されており、それらが一意であることを確認してください。
- アイテムにSKUが設定されていない場合、Brazeはその製品をカタログに同期できません。
- 同じSKUを持つ複数の製品がある場合、予期しない動作が発生したり、重複したSKUによって意図せず製品情報が上書きされる可能性があります。
{% endalert %}

### ステップ3: 同期中 {#step-3-sync-in-progress}

ダッシュボード通知が表示され、ステータスに「In Progress」と表示されて、初回同期が開始されたことを示します。同期の完了にかかる時間は、BrazeがShopifyから同期する必要がある製品やバリアントの数によって異なります。この間、このページから離れて、同期完了を通知するダッシュボード通知またはメールが届くまで待つことができます。

初回同期が[カタログ制限]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers)を超えた場合、Brazeはそれ以上の製品の同期を停止します。時間の経過とともに新しい製品が追加されたために同期成功後に制限を超えた場合、同期はアクティブではなくなります。いずれの場合も、Shopifyからの製品更新はBrazeに反映されなくなります。ティアのアップグレードについてはアカウントマネージャーにお問い合わせください。

### ステップ4: 同期完了 {#step-4-sync-completed}

同期が成功するとダッシュボード通知とメールが届きます。Shopifyパートナーページでも、Shopifyカタログの下のステータスが「Syncing」に更新されます。Shopifyパートナーページでカタログ名をクリックすると、製品を表示できます。

カタログデータを活用してメッセージをパーソナライズする方法の詳細については、[カタログの追加ユースケース]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)を参照してください。

#### サポートされているShopifyカタログデータ {#supported-shopify-catalog-data}

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Shopifyカタログを何らかの方法で変更すると、意図せずリアルタイムの製品同期に干渉する可能性があります。Shopifyカタログは、Shopifyによって上書きされる可能性があるため、編集しないでください。代わりに、Shopifyインスタンスで必要な製品更新を行ってください。<br><br>Shopifyカタログを削除するには、Shopifyページに移動し、同期を非アクティブにしてください。カタログページでShopifyカタログを直接削除しないでください。
{% endalert %}

## 再入荷と値下げのユースケース {#back-in-stock-and-price-drop-use-cases}

再入荷通知を設定するには、[こちら]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)の手順に従ってください。

値下げ通知を設定するには、[こちら]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)の手順に従ってください。

Shopifyインテグレーションでは、ユースケースごとにユーザーのサブスクリプションステータスをカタログにキャプチャするカスタムイベントを作成する必要があります。カスタムイベントには、Shopify製品の同期の一部として選択した[SKUまたはShopifyバリアントID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier)のいずれかにマップされるイベントプロパティが必要です。

## カタログIDを変更する {#changing-catalog-id}

Shopifyカタログの製品識別子を変更するには、同期を非アクティブにする必要があります。まず、このShopifyカタログデータを使用したメッセージの送信を停止していることを確認してください。Shopifyカタログの初回同期を再実行し、[製品の同期](#setting-up)の手順に従って目的の製品識別子を選択します。

## 製品の同期の非アクティブ化 {#deactivate}

Shopify製品の同期機能を非アクティブにすると、カタログと製品がすべて削除されます。この操作は、このカタログの製品データをアクティブに使用しているメッセージにも影響する可能性があります。製品詳細のないメッセージが送信される可能性があるため、非アクティブ化する前にCampaignsまたはCanvasesを更新または一時停止していることを確認してください。カタログページでShopifyカタログを直接削除しないでください。

## トラブルシューティング {#troubleshooting}
Shopify製品の同期でエラーが発生した場合は、次のいずれかのエラーが原因である可能性があります。問題を修正し、同期を解決する方法については、以下の手順に従ってください。

| エラー | 理由 | ソリューション |
| --- | --- | --- |
| サーバーエラー | 製品を同期しようとしたときに、Shopify側でサーバーエラーが発生した場合に起こります。 | [同期を非アクティブにし](#deactivate)、製品の在庫全体を再同期します。 |
| 重複するSKU | カタログアイテムIDとしてSKUを使用している場合に、複数の製品に同じSKUが設定されていると発生します。カタログアイテムIDは一意である必要があるため、すべての製品に一意のSKUが必要です。 | Shopifyで製品とバリアントの一覧をすべて監査して、重複するSKUがないことを確認します。SKUが重複している場合は、Shopifyストアアカウントで一意のSKUに更新します。修正後、[同期を非アクティブにし](#deactivate)、製品の在庫全体を再同期します。 |
| カタログ制限の超過 | カタログ制限を超えた場合に発生します。Brazeは、利用可能なストレージがないため、同期を完了することや、同期をアクティブな状態で維持することができなくなります。 | この問題には2つのソリューションがあります。<br><br>1. アカウントマネージャーに連絡してティアをアップグレードし、カタログ制限を増やします。<br><br>2. 次のいずれかを削除して、ストレージ領域を解放します。<br>- 他のカタログからのカタログアイテム<br>- 他のカタログ<br>- 作成されたセレクション<br><br> いずれのソリューションを取った場合でも、同期を非アクティブにしてから再同期を実行する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }