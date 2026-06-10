---
nav_title: Shopifyアップグレードの概要
article_title: Shopifyアップグレードの概要
description: "このリファレンス記事では、Shopify統合を最新バージョンにアップグレードする方法について説明します。"
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Shopifyアップグレードの概要 {#shopify-upgrade-overview}

> 最高のエクスペリエンスを提供するための取り組みの一環として、すべてのShopify統合を2025年8月28日までに最新バージョンに[アップグレード]({{site.baseurl}}/shopify/)していただく必要があります。このアップグレードは、Shopifyの技術における重要な変更が統合の機能に影響を与えるため、不可欠です。

## 主要な日程 {#key-dates}

- **2月末から4月:** お客様の特定のグループ（コホート）がアップグレード可能になるタイミングについて通知が届きます。この重要な情報にご注意ください。
- **アップグレード期限:** すべてのお客様は**2025年8月28日**までにアップグレードを完了する必要があります。

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## Shopify統合の変更点 {#whats-changing-in-the-shopify-integration}

Shopifyがチェックアウトの拡張性を強化する計画の一環として、Brazeとの統合に重要な変更が加わります。知っておくべきポイントは以下のとおりです。

- **Script Tagsと`checkout.liquid`の廃止:** ShopifyはScript Tagsと`checkout.liquid`を段階的に廃止します。2025年8月以降、最新バージョンの統合に移行しない限り、BrazeのWeb SDKはScript Tagsを通じてチェックアウトページに読み込まれなくなります。
- **統合の全般的な改善:**
    - **推奨イベントの導入:** 統合に推奨eコマースイベントを追加します。これにより、Brazeの事前構築済みテンプレートを通じて一般的なeコマースのユースケースが簡素化されます。
    - **ID管理の合理化:** ユーザーIDの管理アプローチを強化し、匿名ユーザーデータのトラッキングとアトリビューションを改善します。ID管理の処理方法の詳細については、[ユーザーとデータの同期](https://braze.com/docs/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing)を参照してください。
    - **メールおよびSMSサブスクライバーリスト:** 現在メールおよびSMSサブスクライバーを収集している場合、アップグレードの一環として各チャネルのデフォルトサブスクリプショングループが自動的に作成されます。BrazeがメールおよびSMSのオプトインを同期する際、Brazeはユーザープロファイルのグローバルサブスクリプション状態を上書きせず、サブスクリプショングループのオプトインのみを更新します。
    - 現在のバージョンから新しいバージョンへのすべての変更の詳細については、[変更ログ](#full-changelog)を参照してください。

{% alert important %}
このアップグレードは、ShopifyとBraze間の統合の機能を維持するために不可欠です。開発チームと緊密に連携して、これらの変更の範囲と影響を評価し、シームレスな移行を促進することをお勧めします。
{% endalert %}

## アップグレード要件 {#upgrade-requirements}

Shopify統合ページでアップグレードプロセスを開始する前に、エンジニアリングチームと以下の要件を完了してください。

- **SDKカスタマイズの確認:** BrazeとShopifyの統合をカスタマイズしている場合（例：カスタムイベントや属性のログ記録）、アップグレード後もこれらのカスタマイズが正しく動作することを確認してください。「商品閲覧」や「カート更新」などのアクション用に独自のブラウザイベントを作成している場合は、新しいコネクタが提供する機能と重複するため、アップグレード前に開発者と連携してそれらを削除してください。

{% alert important %}
Shopifyオンラインストアをご利用で、開発者がBraze SDKをShopifyサイトに直接、またはGoogle Tag Managerや顧客データプラットフォームを通じて実装している場合、新しいShopifyコネクタにアップグレードする際にそれらの使用を停止する計画を立てる必要があります。
{% endalert %}

- **ID管理の確認:** Brazeのexternal IDを使用している場合、開発チームと協力して新しい統合との互換性を確認してください。Shopifyストアのエクスペリエンス内でexternal IDを設定している場合は、[新しいID管理プロセス](https://braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing)との競合を避けるために開発者に調整を依頼してください。
- **影響を受けるCampaigns、Canvases、Segmentsの準備:** ガイド付きアップグレードプロセス中に、Shopifyデータに依存するCampaigns、Canvases、Segmentsを表示およびエクスポートできます。アクティブなメッセージのスムーズなアップグレードを促進するために、「OR」演算子を使用して新しい必須Shopifyイベントと属性を追加することをお勧めします。
- **放棄カートおよびチェックアウトのユーザージャーニーの作成:** 放棄カートのユーザージャーニーでは、Canvasのエントリ条件の一部として「Performed Cart Updated」トリガーを使用する必要があります。さらに、放棄カートと放棄チェックアウトの両方のユーザージャーニーで新しいショッピングカートLiquidタグを使用する必要があります。新しい[キャンバステンプレート]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys)を使用して開始できます。

これらのステップを完了することで、Shopify統合の最新バージョンへのアップグレードを円滑に進めることができます。

## 統合オプション {#integration-options}

Brazeは、eコマースビジネスの多様なニーズに対応するために設計された2つのShopifyマーチャント向け統合オプションを提供しています：**標準統合**と**カスタム統合**です。

{% tabs local %}
{% tab 標準 %}
標準統合はShopifyオンラインストア向けに設計されており、シームレスで簡単なセットアッププロセスを提供します。このオプションにより、ShopifyストアをBrazeに素早く接続し、高度な技術的専門知識がなくても強力なカスタマーエンゲージメントツールを活用できます。この統合オプションでは、顧客データの同期、パーソナライズされたメッセージングの自動化、包括的なBraze機能によるマーケティング活動の強化が可能です。

標準アップグレードパスを通じて既存のShopify統合をアップグレードするには、[Shopify統合のアップグレード（標準）]({{site.baseurl}}/shopify_standard_upgrade/)を参照してください。
{% endtab %}

{% tab カスタム %}
カスタム統合は、Shopify Hydrogenを使用している場合やヘッドレスストアをサポートしている場合に、より柔軟でコンポーザブルなソリューションを提供します。このオプションにより、Braze SDKをShopify環境に直接実装し、より深い統合とカスタマイズされた機能を実現できます。ユニークなカスタマーエクスペリエンスの作成や特定のワークフローの最適化を目指す場合、カスタム統合はヘッドレスセットアップでBrazeの機能を最大限に活用するために必要なツールを提供します。

カスタムアップグレードパスを通じて既存のShopify統合をアップグレードするには、[Shopify統合のアップグレード（カスタム）]({{site.baseurl}}/shopify_custom_upgrade/)を参照してください。
{% endtab %}
{% endtabs %}

## 変更ログ {#full-changelog}

{% alert important %}
この統合では、サポートされている属性とイベントの信頼できるソースとしてShopifyを使用します。そのため、データ同期時にShopifyがユーザープロファイル上の既存の値（標準属性やカスタム属性など）を置き換える場合があります。
{% endalert %}

### 標準統合 {#standard-integration}

| 以前のバージョン | 最新バージョン |
| --- | --- |
| {::nomarkdown}<ul><li>Script Tagサポート</li><li>Braze Web SDKのみ</li><li>イベントおよび製品用のShopify webhook</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel APIサポート</li><li>新しいBrazeアプリ埋め込み</li><li>Braze Web SDK & JavaScript SDK</li><li>イベントおよび製品用のShopify webhook</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard integration" }

### 統合でサポートされるユーザー識別子 {#user-identifiers-supported-by-the-integration}

| ユーザー識別子 | 以前のバージョン | 最新バージョン |
| --- | --- | --- |
| BrazeデバイスID | {::nomarkdown}<ul><li>ブラウザに保存されるランダム生成ID</li></ul>{:/} | {::nomarkdown} <ul><li>ブラウザに保存されるランダム生成ID</li></ul>{:/}|
| Brazeエイリアス | {::nomarkdown}<ul><li>Shopify顧客ID</li><li>Shopifyメール</li></ul>{:/} | {::nomarkdown}<ul><li>Shopifyカートトークン</li><li>Shopifyチェックアウトトークン</li></ul>{:/}|
| Braze external ID | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify顧客ID</li><li>メール</li><li>ハッシュ化メール（SHA-256、SHA-1、MD5）</li><li>カスタムexternal ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User identifiers supported by the integration" }

ユーザー同期とID管理の詳細については、[ユーザーデータと同期](https://braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing)を参照してください。

{% alert note %}
デフォルトでは、BrazeはShopifyからのメールをexternal IDとして使用する前に自動的に小文字に変換します。メールまたはハッシュ化メールをexternal IDとして使用している場合、external IDとして割り当てる前、または他のデータソースからハッシュ化する前に、メールアドレスも小文字に変換されていることを確認してください。これにより、external IDの不一致を防ぎ、Brazeでの重複ユーザープロファイルの作成を回避できます。
{% endalert %}

### サポートされるShopifyイベント {#supported-shopify-events}

| イベントまたは属性 | 以前のバージョン | 最新バージョン |
| --- | --- | --- |
| イベント | {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a> に置き換え</li><li><a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">放棄ブラウズCanvasテンプレート</a> を追加</li></ul>{:/} |
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>廃止されたイベント</li></ul>{:/} |
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">放棄カートタイマー設定</a></li></ul>{:/} | {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a> に置き換え</li><li>放棄カートタイマー設定を廃止</li><li><a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">放棄カートCanvasテンプレート</a> を追加</li></ul>{:/} |
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">放棄カートタイマー設定</a></li></ul>{:/}| {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a> に置き換え</li><li>放棄チェックアウトタイマー設定を廃止</li><li><a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">放棄チェックアウトCanvasテンプレート</a> を追加</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a> に置き換え</li><li><a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">注文確認と購入後アンケートのCanvasテンプレート</a> を追加</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze購入イベント</a></li></ul>{:/}| {::nomarkdown}<ul><li>廃止されたイベント。<a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a> を使用してください。</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a> に置き換え</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a> に置き換え</li></ul>{:/}|
| イベント | {::nomarkdown}<ul><li>Shopifyアカウントログインイベントなし</li></ul>{:/}| {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a> を追加</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
| 属性 | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>変更なし</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported Shopify events" }

### サブスクライバー収集 {#subscriber-collection}

| 収集タイプ | 以前のバージョン | 最新バージョン |
| --- | --- | --- |
| メールサブスクライバー収集 | {::nomarkdown}<ul><li>グローバルメールサブスクリプション状態の上書き</li><li>1つ以上のサブスクリプショングループを割り当てる機能</li><li>接続されたShopifyストアの統合用デフォルトサブスクリプショングループなし</li></ul>{:/} | {::nomarkdown}<ul><li>上書き機能を廃止</li><li>アップグレードの一環としてデフォルトサブスクリプショングループが作成されます</li><li>追加のサブスクリプショングループを割り当てる機能</li></ul>{:/} |
| SMSサブスクライバー収集 | {::nomarkdown}<ul><li>1つ以上のサブスクリプショングループの割り当てが必須</li><li>接続されたShopifyストアの統合用デフォルトサブスクリプショングループなし</li></ul>{:/} | {::nomarkdown}<ul><li>アップグレードの一環としてデフォルトサブスクリプショングループが作成されます</li><li>追加のサブスクリプショングループを割り当てる機能</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscriber collection" }

{% alert note %}
現在メールまたはSMSサブスクライバーを収集している場合、アップグレード完了後に新しいデフォルトサブスクリプショングループが作成されます。デフォルトサブスクリプショングループの名前はShopifyストアフロントの名前になります。このプロセスには最大5時間かかる場合があります。<br><br>サブスクリプショングループが利用可能になったら、購読中のショッパーに効果的にリーチするために、アクティブなCampaigns、Segments、またはCanvasesにそれらを含めてください。
{% endalert %}

### 製品同期 {#product-sync}

| 同期タイプ | 以前のバージョン | 最新バージョン |
| --- | --- | --- |
| 初期製品同期 | {::nomarkdown}<ul><li>製品同期が有効な場合、ストアフロント内のすべての製品の初期インポート</li><li>アクティブな製品のみをインポートする機能</li></ul>{:/} | {::nomarkdown}<ul><li>変更なし</li></ul>{:/} |
| リアルタイム製品同期 | {::nomarkdown}<ul><li>ストアで製品が作成、更新、または削除された際のリアルタイム同期</li></ul>{:/} | {::nomarkdown}<ul><li>変更なし</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Product sync" }

### チャネル {#channels}

| チャネル | 以前のバージョン | 最新バージョン |
| --- | --- | --- |
| アプリ内メッセージ | {::nomarkdown}<ul><li>Shopifyオンラインストアの標準統合に含まれます</li></ul>{:/} | {::nomarkdown}<ul><li>変更なし</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Channels" }