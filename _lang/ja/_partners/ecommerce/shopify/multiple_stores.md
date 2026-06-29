---
nav_title: 複数のストアを接続する
article_title: Shopify 複数ストアサポート
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "この参考記事では、複数のShopifyストアを1つのワークスペースに接続し、設定する方法について説明します。"
---

# 複数のShopifyストアを接続する {#connect-multiple-shopify-stores}

> 単一のワークスペースに複数のShopifyストアドメインを接続して、すべての市場における顧客の全体像を把握できます。地域のストア間で作業を重複させることなく、単一のワークスペースでオートメーションプログラムとジャーニーを構築し、起動します。

{% alert important %}
この機能はShopify MarketsやMarkets Proには対応していません。これらのサポートを希望する場合は、[製品リクエスト]({{site.baseurl}}/user_guide/administer/personal/product_portal/)を送信してください。
{% endalert %}

## 要件 {#requirements}

| 要件 | 説明 |
| ----------- | ----------- |
| Shopifyストアを設定する | [Brazeで少なくとも1つのShopifyストアを設定]({{site.baseurl}}/shopify_overview/)済みであることを確認してください。 |
| 各地域の固有のShopifyストアフロントドメイン | 複数ストアサポートは、さまざまな地域のストアフロントの固有のShopifyストアドメインで使用することを目的としています。<br><br>複数のサブブランドをBrazeに接続したい場合は、サブブランドごとに別々のワークスペースを作成することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 追加のストアを接続する {#connecting-an-additional-store}
Shopifyストアに Brazeアプリをインストールし、最初のストアをインストールしたら、**+ Connect New Store**を選択します。

![Shopify統合ページの「+ Connect New Store」ボタン。]({% image_buster /assets/img/shopify/begin_setup_button.png %}){: style="max-width:80%;"}

追加のShopify地域ストアについて、**Begin setup**を選択します。

![「Begin setup」ボタンがある「Integration settings」セクション。]({% image_buster /assets/img/shopify/multiple_stores.png %}){: style="max-width:80%;"}

最初のShopifyストア統合と同様に、標準またはカスタム設定のいずれかを選択できます。

![標準またはカスタム設定でBraze Web SDKを実装するオプションがある「Enable the Braze SDKs」セクション。]({% image_buster /assets/img/shopify/standard_or_custom.png %}){: style="max-width:80%;"}

ニーズに最も適したオプションを選択します。

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

各ストアの統合を表示し、詳細設定を行うには、ドロップダウンメニューからストアを選択します。

![Shopifyストアを選択するドロップダウンメニューがある「Integration settings」。]({% image_buster /assets/img/shopify/store_dropdown_menu.png %})

## ストア間でユーザーを同期する {#syncing-users-across-stores}

### Shopifyエイリアス {#shopify-alias}

複数のストアを接続すると、ログインまたは注文をした同期済みShopifyユーザーは、{% raw %}`shopify_customer_id_{{storename}}`{% endraw %}の形式で新しいエイリアスを受け取ります。

### Braze external ID

Braze external IDは以下のオプションから選択できます。

| オプション | 説明 |
|------|-----------|
| Shopify顧客ID | Shopifyの顧客IDをBraze external IDとして使用する場合、各ストアはユーザーごとに固有の顧客IDを生成します。つまり、ユーザーが複数のストアとやり取りする場合、Brazeでは別々のプロファイルを持つことになります。|
| メール、ハッシュ化メール、またはカスタムexternal ID | メール、ハッシュ化されたメール、またはカスタムexternal IDタイプを使用する場合、複数のストアとエンゲージメントを持つユーザーは、ログインまたは注文時にプロファイルが1つの統合プロファイルにマージされます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze external ID" }

### マージされるフィールド {#merged-fields}

ユーザープロファイルが同期されると、以下のフィールドがマージされます。マージの動作の詳細については、[マージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)を参照してください。

- デバイス情報
- 合計セッション数（両プロファイルの合計）
- カスタムイベントと購入データ
- セグメンテーション用のカスタムイベントプロパティ（例：「Y日間にX回」（X ≤ 50、Y ≤ 30））
- イベント数（両プロファイルの合計）
- 最初と最後のイベントの日付（Brazeは最も早い日付と最も新しい日付を選択します）
- Campaignインタラクションデータ（最新の日付フィールド）
- ワークフローのサマリー（最新の日付フィールド）
- メッセージとエンゲージメントの履歴
- サブスクリプショングループ

### サブスクライバーの収集（オプション） {#collecting-subscribers-optional}

Brazeを通じて直接（Shopifyコネクターの設定で）サブスクライバーを収集するか、Shopifyからデータを同期するAPIやSDKの代替手段を通じてサブスクライバーを収集するかを選択できます。

{% tabs local %}
{% tab Shopify connector %}
Shopifyコネクター設定の**ユーザーを管理**ステップで、Brazeを使用してメールやSMSサブスクライバーのオプトインを収集し、専用のサブスクリプショングループに整理できます。

1. 接続する各ストアに固有のサブスクリプショングループを作成します。これにより、サブスクライバーがどこから来ているかについての正確なデータを維持できます。
2. メールおよびSMSサブスクライバーの収集を有効にします。
{% endtab %}

{% tab Braze API or SDKs %}
また、Braze APIやSDKを使って、Shopifyから直接メールやSMSマーケティングのオプトイン情報を同期することもできます。

| オプション | リソース |
|------|---------|
| API | - 統合によってサポートされるものを直接置き換える[サブスクリプショングループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/)<br>- サブスクリプショングループデータまたは[グローバルメールのサブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)を設定する[`Users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups)<br>- よりカスタマイズされたマーケティングオプトイン収集オプションのための[Brazeユーザー設定センター]({{site.baseurl}}/user_guide/channels/email/subscriptions/) |
| SDK | - [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Collecting subscribers (optional)" }
{% endtab %}
{% endtabs %}

## Shopifyデータ {#shopify-data}

### 同期される属性 {#synced-attributes}

複数のストアを接続した場合、以下の属性はShopifyプロファイルの最新の状態と同期されます。
- 名
- 姓
- メール
- 性別
- 生年月日
- 国
- 市区町村
- 最後に使用したアプリ
- 言語
- タイムゾーン
- Shopifyタグ
- Shopifyオーダー数
- Shopify総支出額

### サポートされているイベント {#supported-events}

#### eコマース推奨イベント {#ecommerce-recommended-events}

複数のストアを接続すると、受信するeコマース推奨イベントにはソースイベントプロパティが含まれます。このプロパティは、イベントがどのストアフロントURLから発生したかを識別し、この情報をセグメンテーションや特定のユースケースのトリガーに使用できるようにします。

![`ecommerce.order_placed`カスタムイベントを実行したユーザーをエントリさせるトリガーを持つアクションベースのCanvas。]({% image_buster /assets/img/shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Shopify統合内でサポートされているeコマース推奨イベントは次のとおりです。

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopifyカスタムイベント {#shopify-custom-events}

受信するShopifyカスタムイベントには、`shopify_storefront`というイベントプロパティが含まれます。このプロパティは、イベントがどのストアフロントURLから来たかを示し、セグメンテーションやユースケースのトリガーに活用できます。

![`shopify_paid_order`カスタムイベントを実行したユーザーをエントリさせるトリガーを持つアクションベースのCanvas。]({% image_buster /assets/img/shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

サポートされているShopifyカスタムイベントは以下のとおりです。

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

すべてのイベントペイロードの完全な概要については、[Shopifyデータ機能]({{site.baseurl}}/shopify_data_features/)を参照してください。

### Shopify製品の同期 {#shopify-product-sync}

Brazeで各Shopifyストアを接続および設定する際、必要に応じて、統合の一部としてShopify製品の同期を有効にできます。

ストアごとに製品の同期を有効にすると、BrazeはShopifyストアの名前をカタログ名に含めます。これにより、異なるストアの商品を区別できます。

![Shopifyストア名が含まれたShopifyカタログ。]({% image_buster /assets/img/shopify/catalog_store_name.png %})