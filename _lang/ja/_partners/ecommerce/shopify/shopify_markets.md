---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "このリファレンス記事では、BrazeとのShopify Marketsインテグレーションの設定方法と使用方法について説明します。"
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> この記事では、Shopify Marketsインテグレーション（現在ベータ版）について、対象範囲、仕組み、メッセージングでのマーケットデータの活用方法を説明します。Brazeはベータ期間を通じて追加のMarkets機能を段階的にリリースしており、より複雑なマーケット構造のサポートを拡大していく予定です。

{% alert important %}
Shopify Marketsは現在ベータ版です。詳細については、Brazeのカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 統合の仕組み {#how-the-integration-works}

Shopify Marketsは、既存のShopify統合を拡張します。[スタンダード]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[カスタム（SDK）]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)統合パスを通じてデフォルトのストアフロントを接続し、ストアの設定済みマーケットからBrazeに同期するマーケットを選択します。既存の統合では、カタログ、購読グループ、イベントに影響を与えることなくマーケットを追加できます。ステップバイステップの手順については、[Shopify Marketsの設定](#shopify-markets-setup)を参照してください。

Shopify Marketsは以下の機能を提供します：

- **マーケット対応プロファイル：** 統合により、Brazeの標準的な国と言語の属性とともに各ユーザーのShopifyロケールがキャプチャされるため、カスタム設定なしでマーケットごとにセグメントやトリガーを行うことができます。
- **ローカライズされたカタログ：** マーケット固有の商品データが、価格や通貨、翻訳されたタイトル、説明、商品URLを含めて毎日同期されます。
- **マーケット対応パーソナライゼーション：** {% raw %}`{% shopify_market %}`{% endraw %} Liquidタグを使用して、Shopifyの翻訳コンテンツを含む各ユーザーのマーケットのカタログ商品でパーソナライズできます。また、`ecommerce.order_placed`などのサポートされているShopifyイベントから、表示通貨などのマーケットの詳細を参照することもできます。
- **デフォルトストアフォールバック：** ユーザーが接続済みマーケットのいずれにも属していない場合、Brazeはデフォルトのストア設定と商品を使用するため、すべてのユーザーが完全で正確なメッセージを受け取ります。

例については、[Marketsのユーザーデータを使用する](#use-markets-user-data)および[チュートリアル：マーケットごとに商品と価格を表示する](#tutorial-show-products-and-prices-per-market)を参照してください。

## サポートされるShopifyマーケットタイプ {#supported-shopify-market-types}

最大25個のアクティブな[単一国市場または複数国市場](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets)を選択できます。各国は、選択されたマーケットの1つにのみ属することができます。

サブリージョンマーケット、小売マーケット、B2Bマーケット、およびチャネルマーケットはサポートされていません。

### 各マーケットに必要なもの {#what-each-market-needs}

選択した各マーケットには、アクティブな商品を含むマーケットカタログが必要です。Brazeはそのカタログから以下を読み取ります。

| データ | 説明 |
| --- | --- |
| 価格 | マーケットカタログで設定され、そのマーケットの指定通貨で表示されます。Shopifyの「現地通貨を使用」設定はサポートされていません。 |
| 翻訳 | Shopify Translate & Adaptアプリを通じて作成された適応翻訳（商品タイトルやバリアントタイトルなど）。Brazeは現在、特定のマーケット言語設定をサポートしていません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="各マーケットに必要なもの" }

![オーストラリアマーケットのShopifyマーケットプロファイル。]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### 考慮事項 {#considerations}

#### 一般 {#general}

- **1つの接続ストア:** 1つのBrazeワークスペースには、Markets対応のShopifyストアを1つだけ接続できます。
- **ロケールの範囲:** ロケールは、Shopify Translate & Adaptアプリを使用して設定した内容に基づいて、翻訳された商品タイトルと説明を取得し、ロケール固有のURLを提供します。価格、通貨、およびその他の共有カタログフィールドは、マーケット内のロケール間で同じままです。デフォルトでは、Brazeは各マーケットの[デフォルト言語](https://help.shopify.com/en/manual/markets/languages)（Shopifyがそのマーケットに割り当てるプライマリロケール）を使用します。拡張ロケールサポートを有効にすると、Brazeはそのマーケットに設定された追加のロケールを同期します。

#### マーケットカタログ {#market-catalog}

- **元のShopifyカタログの新しいマーケットビュー:** Marketsは個別のカタログを作成しません。代わりに、Brazeは元のShopifyカタログの一部としてそれらを表示します。マーケットデータは、Shopifyカタログの新しいカタログ行に追加されます。
- **カタログセレクション:** 最大30のカタログセレクションです。
- **更新タイミング:** マーケットカタログの商品データは1日1回更新されます。
- **マーケット価格とローカライズされたコンテンツ:** マーケット行には、マーケットの価格と `compare_at_price` が含まれ、Shopify Translate & Adaptアプリを通じて翻訳が設定されている場合は、ローカライズされた商品タイトル、バリアントタイトル、および商品URLも含まれます。
- **在庫数量:** マーケット行には集計された在庫値が含まれます。Brazeは現在、ロケーション間の在庫の区別をサポートしていません。
- **値下げ:** マーケットカタログでサポートされています。マーケットカタログでの価格変更は、デフォルトのストア価格ではなく、そのマーケットの価格に基づいてトリガーされます。マーケットカタログの商品データは1日1回更新されるため、値下げはShopifyで価格が変更されたときではなく、毎日検出されます。
- **再入荷:** [再入荷]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)は、デフォルトストアカタログの商品でサポートされています。マーケット行は再入荷通知をトリガーしません。再入荷は、すべてのShopifyロケーションにわたる商品バリアントの合計利用可能在庫を確認するため、小売ロケーションで追加された在庫が通知をトリガーする可能性があります。

## Shopify Marketsの設定 {#shopify-markets-setup}

### すでにアクティブなShopifyインテグレーションがある場合 {#if-you-already-have-an-active-shopify-integration}

Marketsは現在のインテグレーションに追加されます。切断したり、設定を再構築したりする必要はありません。

- 購読グループがストア全体のグループとなり、追加で割り当てたグループを含むすべてのオプトインを引き続き受信します。
- 既存の購読者は、すでに登録されているグループにそのまま残ります。後から国別グループを追加しても、Brazeは既存の購読者をそれらに追加しません。
- カタログは引き続き同期されます。マーケット行は新しいカタログではなく既存のカタログに追加され、既存のセレクションはデフォルト行に対して引き続き機能します。
- デフォルトストアが選択したマーケットと並んで表示され、同じ方法で購読グループの割り当てやカタログセレクションの構築ができます。

ストアがすでに接続されている場合は、[ステップ2](#step-2-select-your-market-user-data)から始めて、各設定の詳細と仕組みを確認してください。

### ステップ1: Shopify Markets対応ストアを接続する {#step-1-connect-your-shopify-markets-enabled-store}

1. [Shopify標準インテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[Shopifyカスタムインテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)のいずれかのパスを使用してストアを接続します。ストアが接続されたら、セットアップコンポーザーでShopify Marketsを設定します。
2. OAuthフローを完了し、BrazeがOAuthでマーケットスコープをリクエストしていることを確認します：
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. 認証が成功してセットアップコンポーザーが開いたら、**Begin Setup**を選択します。
4. Braze SDKをオンにします。

### ステップ2: マーケットユーザーデータを選択する {#step-2-select-your-market-user-data}

1. **Track Shopify Data**で、**Sync Shopify Markets data**を選択します。
2. **Select Markets**を選択してマーケットを選び、行動イベントとユーザー属性のトラッキングを選択していることを確認します。
   - （オプション）履歴バックフィルをオンにします

#### マーケットユーザーデータ {#markets-user-data}

Shopify Marketsをサポートするために、Brazeはインテグレーションの[標準イベントと属性]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events)に加えて追加データを同期します。

##### ユーザープロファイル属性 {#user-profile-attributes}

| 属性 | データ型 | 説明 | データソース |
| --- | --- | --- | --- |
| `shopify_locale` | カスタム属性 | 顧客がストアを閲覧している言語（`en`や`fr-CA`など）。ストアフロントの言語を切り替えると変更されます。 | Shopify顧客ロケール |
| `browser_language` | 標準属性項目 | 顧客のブラウザで設定されている言語。 | Braze SDK |
| `country` | 標準属性項目 | 顧客の国。 | Braze SDK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザープロファイル属性"}

##### 注文イベントプロパティ {#order-event-properties}

| プロパティ | 説明 | データソース |
| --- | --- | --- |
| `country` | 顧客の2文字の国コード。 | Shopifyの顧客の`default_address`、またはデフォルトの住所が設定されていない場合は注文の`shipping_address` |
| `presentment_currency` | 顧客が支払いに使用した通貨。ストアの通貨と異なる場合があります。 | Shopify注文のプレゼンテーション通貨 |
| `market_handle` | 顧客の国に一致するマーケットのハンドル。設定されたマーケットに一致しない場合は空です。 | Braze（マーケット設定から） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="注文イベントプロパティ"}

これらのプロパティは以下に追加されます：

- eコマース推奨イベント：`ecommerce.order_placed`、`ecommerce.order_cancelled`、`ecommerce.order_refunded`
- カスタムイベント：`shopify_paid_order`、`shopify_fulfilled_order`、`shopify_partially_fulfilled_order`

##### マーケットイベントプロパティの仕組み {#how-these-market-event-properties-work}

| プロパティ | 仕組み |
| --- | --- |
| `market_handle` | `market_handle`は、Shopifyでマーケットに付けたハンドル（`france`など）です。同じハンドルがカタログ内のマーケット行IDのプレフィックスになります（`france_46714756268231`など）。マーケットを設定していない場合や、注文の国が設定したマーケットに一致しない場合は空になるため、Liquidやセグメントフィルターで使用する前に空の値を確認してください。 |
| `country` | `country`は顧客のデフォルトの住所から取得され、デフォルトが存在しない場合は`shipping_address`が使用されます。例えば、フランスにいる顧客が日本に注文を送った場合でも、フランスのマーケットが適用されます。 |
| イベントプロパティ | イベントプロパティはイベント発生時のスナップショットであり、その後変更されません。顧客が後でデフォルトの住所を更新した場合、新しいイベントには新しい国が使用されますが、過去のイベントは記録時の国を保持します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マーケットイベントプロパティの仕組み"}

##### 通貨 {#currency}

サポートされているShopifyカート、チェックアウト、注文イベントには2セットの値が含まれます：
- 既存の価格および合計フィールドのストア通貨（変更なし）
- 顧客が確認し支払った金額を保持する`presentment_currency`オブジェクト

注文確認や放棄カートメッセージなど、顧客に支払った金額を表示する場合は`presentment_currency`を使用します。マーケット間で収益を比較する場合は、すでに単一通貨になっているストア通貨値を使用します。

##### ローカライズされた商品情報 {#localized-product-information}

サポートされているShopifyイベントには、デフォルトストア言語の商品名とバリアントタイトルが含まれます。Brazeはイベントペイロードを翻訳しません。

翻訳されたタイトル、説明、商品URLはマーケットカタログ行にあります。メッセージにローカライズされた商品情報を表示するには、イベントの商品IDまたはバリアントIDを使用してカタログ内の商品を検索してください。

### ステップ3: ユーザーを管理する {#step-3-manage-users}

1. ドロップダウンから`external_id`のタイプを選択します。
2. Shopifyからのメールおよび SMSオプトインをオンにします。これにより、BrazeがShopifyからメールおよびSMSの購読ステータスを同期できます。2つのオプションがあります：
   - **インテグレーションを使用する：** Brazeがメールおよび SMSのステータスを同期します。同期先の購読グループを選択します。
   - **独自に構築する：** ステータス管理をより細かく制御するために、Brazeの購読グループエンドポイントを使用してカスタムインテグレーションを構築します。
3. Shopifyの同意が同期する購読グループを選択します：
   - **ストア全体のグループ（必須）：** メールグループとSMSグループをそれぞれ1つ以上選択します。BrazeがShopifyから受信するすべてのオプトインがここに記録されます。
   - **国別グループ（オプション）：** 同期したマーケット内の任意の国に1つ以上のグループを割り当てます。Brazeが顧客の国を判定できる場合、オプトインはここにも記録されます。

#### オプトインとオプトアウトの仕組み {#how-opt-ins-and-opt-outs-work}

Shopifyでは、各顧客に1つのメール同意ステータスと1つのSMS同意ステータスがあります。顧客がオプトインすると、国やリストではなく、ブランドに購読します。

Brazeは各オプトインをストア全体のグループに記録します。国別グループを設定し、Brazeが顧客の所在国を判定できる場合、オプトインはその国のグループにも記録されます。

国別グループを設定しない場合、オプトインはストア全体のグループのみに記録されます。これは現在のShopifyの同意処理方法と同じです。

#### Brazeが国を判定する方法 {#how-braze-determines-country}

| チャネル | 国の判定方法 |
| ------- | ---------------------------- |
| メール   | まず顧客のShopifyロケールを使用し、利用できない場合はBrazeプロファイルの国属性を使用します。 |
| SMS     | E.164の国番号ルーティングパターンに基づいて、電話番号の国を使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="チャネルごとのBrazeの国判定方法"}

ロケールが国を特定できるのは、`fr-FR`のようにリージョンが含まれている場合のみです。`fr`だけでは特定できません。

SMSの場合、国は電話番号から判定されます。購入者は、その番号にメッセージを送信できる購読グループに追加されている必要があります。

#### オプトイン時の動作 {#what-happens-when-someone-opts-in}

| 国のステータス                           | ストア全体のグループ | 国別グループ                        |
|------------------------------------------|-------------------|---------------------------------------|
| 判定済み、かつマーケットに設定済み | 購読済み        | その国のグループに購読済み   |
| 判定不可                      | 購読済み        | 未購読                        |
| 判定済み、ただしマーケットに未設定 | 購読済み    | 未購読                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="国のステータスごとのオプトイン結果"}

購読グループのメンバーシップは、Shopifyからの同意イベントに基づいています。購入者の国やロケールが変更されても、グループメンバーシップは変更されません。Brazeが更新するのは、Shopifyが新しい同意イベントを送信した場合のみです（例：国やロケールが変更された後に、Shopify上で購入者から再度同意が収集された場合）。

{% alert note %}
国別グループは言語ではなく同意を制御します。1つの国に複数の言語がある場合があります。カナダの英語とフランス語の顧客（`en-CA`と`fr-CA`）は同じ国別グループに属します。メッセージ内で`shopify_locale`を使用して言語を指定してください。
{% endalert %}

#### オプトアウト時の動作 {#what-happens-when-someone-opts-out}

Shopifyでのオプトアウトは、Shopifyインテグレーションに割り当てられたすべての購読グループからユーザーを削除します。マーケットサイトからオプトアウトした場合も、Shopifyアカウントページからオプトアウトした場合も同じです。

インテグレーションに割り当てられていないワークスペース内の購読グループは影響を受けません。

#### 設定していない国からのオプトイン {#opt-ins-from-countries-you-havent-configured}

設定したマーケットに含まれていない国から顧客がオプトインした場合（その国を追加していない場合やそのマーケットを削除した場合）、顧客はストア全体のグループに購読されます。国別グループには追加されません。

マーケットの設定は、メッセージを送信できる対象を制限するものではありません。法的または規制上の理由で特定の国にメッセージを送信できない場合は、セグメントフィルターでそれらのユーザーを除外するか、別の購読グループにルーティングしてください。

{% alert tip %}
そのセグメントは、対象としない国のブロックリストではなく、対象とする国のアローリストとして構築してください。国を判定できなかったユーザーには国の値がないため、ブロックリストでは捕捉できません。
{% endalert %}

SMSの場合、各購読グループの国別権限が引き続き配信を制御します。そのグループで許可されていない国のユーザーは、そのグループからメッセージを受信しません。

#### ユーザーは後から国別グループに追加されない {#users-arent-added-to-country-groups-later}

オプトイン時にBrazeが顧客の国を判定できない場合、顧客はストア全体のグループのみに追加されます。後で国が判明しても、その国のグループに自動的に追加されることはありません。

既存のインテグレーション済みストアでMarketsをオンにすると、既存の購読グループがストア全体のグループになります。既存の購読者はこれらのグループに購読されたままとなり、新しい国別グループに自動的に追加されることはありません。

これらのユーザーを手動で追加するには、対象ユーザーのセグメントを構築し、キャンバスの[ユーザー更新]({{site.baseurl}}/user_update)ステップを使用して購読させてください。

#### グループ間の購読者数のカウント {#counting-subscribers-across-groups}

1回のオプトインで1人のユーザーが複数の購読グループに追加される場合があるため、グループの合計を足し合わせると同じ人を複数回カウントすることになります。ユニーク購読者の数が必要な場合はセグメントを使用してください。

#### 仕組み {#how-it-works}

1. 顧客がチェックアウト時またはフォームからSMSを購読します。
2. Shopifyが購読をBrazeに送信します。
3. Brazeがユーザーをペンディングに設定し、確認テキストを送信します。
4. 顧客が確認キーワードで返信すると、購読済みになります。
5. 確認ウィンドウが終了するまでに返信がない場合、ペンディングのままとなります。

詳細については、[ダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)を参照してください。

### ステップ4: 商品を同期する {#step-4-sync-products}

1. マーケット内の商品を同期するには、**Sync Shopify products and variants to Braze**を選択します。
2. BrazeカタログIDを割り当て、追加の設定を行います。

カタログには、ストアのデフォルト商品のマーケットごとのビューが含まれます。マーケットに公開された各商品について、Brazeはすでにサポートされている[標準Shopifyカタログフィールド]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data)に加えて、既存のカタログにマーケット行を追加します。既存のインテグレーションでShopify Marketsをオンにした場合、同期に数分かかることがあります。

マーケット行では、以下のフィールドにマーケット固有の値が含まれます：

| フィールド | 説明 |
| --- | --- |
| `id` | マーケットハンドルをプレフィックスとした複合ID（`france_46714756268231`など）。デフォルト行は元のアイテムIDを保持します。 |
| `market_handle` | Shopifyでマーケットに付けたハンドル（`france`など）。 |
| `locale` | マーケットのロケール。翻訳コンテンツの言語を決定します。 |
| `price` | マーケットのコンテキストプライシングからのマーケット固有の価格（価格リストの調整が適用された後）。 |
| `compare_at_price` | 調整後のマーケット固有の比較価格。そのマーケットで比較価格が解決されない場合（マーケットの価格リストが比較価格を無効にするよう設定されている場合を含む）、Brazeは`0`を返します。 |
| `product_title`と`variant_title` | Shopify Translate & Adaptアプリで翻訳が設定されている場合の翻訳済みタイトル。 |
| `product_url` | そのマーケット向けの商品URL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マーケット行カタログフィールド"}

{% alert important %}
`inventory_quantity`はマーケット行には含まれません。デフォルト行にのみ表示され、すべてのShopifyロケーションにおける商品バリアントの合計利用可能在庫を反映します。<br><br>Liquidで`compare_at_price`を使用する場合、表示したり割引を計算したりする前に「0」を確認してください。比較価格がないマーケットでは、ゼロの価格や不正確な割引が表示されます。
{% endalert %}

### ステップ5: チャネルを有効化する {#step-5-activate-channels}

1. （オプション）ブラウザ内メッセージングを有効にするかどうかを選択します。
2. **Finish Setup**を選択します。

## Marketsユーザーデータの使用 {#use-markets-user-data}

これらの属性とプロパティがユーザープロファイルに反映された後、マーケット別にユーザーをターゲティングしたり、メッセージをパーソナライズしたりできます。

### セグメンテーションでマーケット別にターゲティングする {#target-by-market-in-segmentation}

セグメントやキャンペーンまたはキャンバスのエントリ条件で、国、ブラウザ言語、または`shopify_locale`でフィルターします。例えば、特定のマーケットのユーザーのオーディエンスを構築したり、ロケール別にキャンバスを分岐させたりできます。

### Liquidによるトリガーとパーソナライゼーション {#trigger-and-personalize-with-liquid}

以下のLiquid変数を使用して、メッセージ内でマーケットデータを参照します。

#### ユーザープロファイルから {#from-the-user-profile}

| 属性 | Liquid |
| --- | --- |
| 顧客の言語 | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| 顧客の国 | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Marketsユーザープロファイルの Liquid変数"}

#### 注文イベントから {#from-order-events}

| イベントプロパティ | Liquid |
| --- | --- |
| 注文の国 | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| 注文のマーケット | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| 顧客が支払った通貨 | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| その通貨での注文合計 | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Markets注文イベントのLiquid変数"}

#### 顧客の通貨で価格を表示する {#show-prices-in-the-customers-currency}

金額には必ず通貨コードを組み合わせてください。金額を単独で表示することは、マルチマーケットメッセージングで最もよくある間違いです。「129.95」はマーケットごとに異なる意味を持つためです。

確認メールなどの注文レベルのメッセージには注文合計を、カートやレコメンデーションなどの商品レベルのコンテンツには商品価格を使用してください。

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

これらのプロパティはイベントとともに送信されるため、追加の設定なしで各顧客のマーケットに応じた正確なメッセージが表示されます。

#### 空の値を確認する {#check-for-empty-values}

2つの値が常に存在するとは限らず、どちらも欠落している場合は正しく表示されません。

`market_handle`は、顧客の国が設定済みのマーケットと一致しない場合に空になります。分岐する前に確認してください：

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price`は、そのマーケットで比較価格が解決されない場合に`0`を返します。表示したり割引を計算したりする前に`0`かどうかを確認してください。そうしないと、顧客に取り消し線付きの0円という価格が表示されてしまいます。

#### ローカライズされた商品情報を表示する {#show-localized-product-information}

イベント内の商品名はデフォルトのストア言語で表示されます。翻訳されたタイトル、説明、または商品URLを表示するには、イベントの商品IDまたはバリアントIDを使用してカタログ内の商品を参照してください。例については、[チュートリアル：マーケットごとに商品と価格を表示する](#tutorial-show-products-and-prices-per-market)を参照してください。

### 注文アクティビティからメッセージをトリガーする {#trigger-messages-from-order-activity}

マーケットプロパティはサポートされているShopifyイベントに含まれているため、注文によってトリガーされるキャンペーンやキャンバスは、追加の設定なしでこれらのプロパティを使用できます。これらのイベントには`country`、`presentment_currency`、`market_handle`が含まれます。

| イベントタイプ | イベント |
| --- | --- |
| eコマース推奨イベント | `ecommerce.order_placed`、`ecommerce.order_cancelled`、`ecommerce.order_refunded` |
| カスタムイベント | `shopify_paid_order`、`shopify_fulfilled_order`、`shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マーケットプロパティを含むShopify Markets注文イベント"}

`presentment_currency`は他のプロパティと比較して最も広い対応範囲を持っています。サポートされているカート、チェックアウト、注文イベントに含まれるため、カートイベントが`country`や`market_handle`を含まない場合でも、放棄カートメッセージで顧客が確認した金額を表示できます。詳細については、[通貨](#currency)を参照してください。

## マーケットレポート {#markets-reporting}

マーケットが有効になっている場合、Brazeは収益とメッセージのパフォーマンスを国別に分類します。

### 国別収益 {#revenue-by-country}

収益レポートには、全期間と選択した期間の両方について、アプリの内訳とともに国別の内訳が含まれます。

各注文は1つの国に紐づけられ、その収益全額がその国に計上されます。国は最初に注文から選択され、次に購入者のプロファイルから選択されます。どちらも利用できない注文は**不明**として表示されます。

収益は、収益レポートの他の部分と同様にUSDで表示されます。購入者が実際に支払った金額を確認するには、注文イベントの`presentment_currency`を使用してください。

### 国別パフォーマンス {#performance-by-country}

キャンペーンとキャンバスの分析には、各国でのメッセージのパフォーマンスと各国の合計行を示す**国別パフォーマンス**テーブルが含まれます。通貨と合計収益は、注文の`presentment_currency`から集計されます。

| 列 | 表示内容 |
| --- | --- |
| 国 | メッセージが配信された各国。 |
| 通貨 | presentment_currencyで集計されたその国の収益の通貨。 |
| 合計収益 | その国に帰属する収益。 |
| 購入数 | その国に帰属する購入数。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="国別パフォーマンスの各列の表示内容"}

## マーケットの削除 {#remove-a-market}

マーケットを削除すると、Brazeはその国々の新しいデータの同期を停止します。既に保有しているデータは削除されません。

### 購読グループ {#subscription-groups}

マーケットを削除すると、マーケット設定が更新されます。ワークスペースから購読グループが削除されたり、既に国別グループに購読しているユーザーが削除されたりすることはありません。

#### 設定で変わること {#what-changes-in-your-setup}

- 削除されたマーケットの国々はマーケットUIに表示されなくなります。
- Brazeは、それらの国の購読グループ割り当てをインテグレーション設定から削除します。

#### 変わらないこと {#what-stays-the-same}

- 国別購読グループはワークスペースに残り、ターゲティングに引き続き使用できますが、Shopifyはそれらのグループへのオプトアウトを同期しなくなります。Shopifyでオプトアウトしたユーザーは、別の方法（たとえば[購読グループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups)やBrazeでのオプトアウトワークフローなど）で購読ステータスを更新しない限り、それらの国別グループで購読中のまま表示される場合があります。
- 削除されたマーケットの国別グループに既に購読しているユーザーは、引き続き購読状態を維持します。

#### 今後の同意同期 {#future-consent-sync}

- 削除された国の買い物客からの新しいオプトインは、ストア全体のグループにのみ同期されます。これは[設定していない国からのオプトイン](#opt-ins-from-countries-you-havent-configured)と同じ動作です。
- Brazeは、削除された国の国別グループへの新しいオプトインやオプトアウトを同期しなくなります。
- ストア全体の購読グループは引き続き同意の更新を受け取ります。

### ユーザーデータ {#user-data}

- `shopify_locale`や`country`を含む、ユーザープロファイルに既に設定されている属性は変更されません。
- 新しい注文イベント内の`market_handle`は利用できなくなります。
- 削除されたマーケットのShopifyマーケットセグメントフィルターは利用できなくなります。
- 削除されたマーケットを参照するLiquidは利用できなくなります。

### カタログ {#catalogs}

- そのマーケットのマーケット行は更新を停止し、カタログから削除されます。
- それらのマーケット行に基づいて構築されたカタログセレクションは、商品を返さなくなります。次の送信の前にそれらを更新または削除してください。
- デフォルトの行、およびそれらに基づいて構築されたセレクションには影響ありません。

## チュートリアル: マーケットごとに商品と価格を表示する {#tutorial-show-products-and-prices-per-market}

マーケット対応のカタログを使用して、各ユーザーの所属するマーケットの商品と価格を表示する単一メッセージを作成します。

1. マーケットデータを使用するセレクションを作成します。
2. メッセージ内でLiquidを使ってセレクションを参照します。

メッセージが特定のマーケットのみを対象とする場合は、固定マーケットを使用できます。

### ステップ1: マーケットデータを使用してセレクションを作成する {#step-1-create-a-selection-using-markets-data}

[セレクション]({{site.baseurl}}/catalog_selections)は、メッセージで参照するキュレートされた商品セットです。マーケットが同期されたShopifyカタログでは、**フィルター設定**セクションに**マーケットスコープ**エリアがあり、商品データを1つのマーケットに限定したり、ユーザーごとにパーソナライズしたりできます。

1. Shopifyカタログに移動し、**セレクション**タブを開きます。
2. **セレクションを作成**を選択し、セレクション名を入力し、任意で説明を追加し、結果の上限を設定します。
3. **フィルター設定**の**マーケットスコープ**で、**マーケット**ドロップダウンからセレクションがマーケット固有の商品をどのように解決するかを選択します。
   - **パーソナライズされた:** 各受信者は、プロファイルの`country`属性に一致するマーケットの商品と価格を表示します。
   - **同期されたマーケット:** マーケット名を選択して、そのマーケットの商品と価格にセレクションを固定します。メッセージが単一のマーケットのみを対象とする場合に使用します。
4. 追加のフィルター条件を設定し、セレクションを保存します。
5. **ユーザーでプレビュー**で、ユーザーを選択してそのプロファイルに対するセレクションの返却内容を確認します。**パーソナライズされた**を使用するセレクションは、ユーザーを選択した後にのみプレビューできます。

| ターゲット | フィルター |
| --- | --- |
| 特定のマーケット | `market_handle` = `au` |
| デフォルト商品のみ | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ターゲットと関連フィルター"}

{% alert note %}
マーケットを指定しない場合、Brazeはデフォルトの商品を使用します。
{% endalert %}

### ステップ2: マーケット対応のカタログセレクションをメッセージに追加する {#step-2-add-market-aware-catalog-selections-to-messages}

単一メッセージで各ユーザーに所属マーケットの商品を配信するには、次のフィルターでセレクションを1つ作成します。

| セレクション名 | フィールド | オペレーター | 値 |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セレクション名と関連フィルター"}

送信時に、Brazeは{% raw %}`{{shopify_market.handle}}`{% endraw %}を各ユーザーのマーケットに置き換えるため、`market_products`はすべてのユーザーに適切な商品を提供します。`default_products`は一致するマーケットがないユーザーのフォールバックです。

{% raw %}`{% shopify_market %}`{% endraw %}タグを使用して、メッセージ内でセレクションを参照します。

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- {% raw %}`{% shopify_market %}`{% endraw %}を{% raw %}`{% catalog_selection_items %}`{% endraw %}の前に配置して、セレクションが実行される前にユーザーのマーケットが設定されるようにします。
- `<your_catalog_name>`をご自身のカタログ名に置き換え、異なるセレクション名を使用している場合はそれに合わせてください。
- {% raw %}`{{shopify_market.handle}}`{% endraw %}のチェックにより、一致するマーケットがないユーザーは`default_products`にルーティングされるため、空のメッセージではなく商品が表示されます。
- Liquidで`compare_at_price`を使用する場合、表示または割引計算の前に「0」をチェックしてください。比較価格のないマーケットでは、価格がゼロとしてレンダリングされたり、不正確な割引が生成されたりします。

ご自身のマーケットのユーザーとしてプレビューし、メッセージにそのマーケットの商品、価格、翻訳されたタイトルが表示されることを確認してください。