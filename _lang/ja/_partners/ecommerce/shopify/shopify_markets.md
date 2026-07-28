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

## インテグレーションの仕組み {#how-the-integration-works}

Shopify Marketsは、既存のShopifyインテグレーションを拡張します。[標準]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[カスタム（SDK）]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)インテグレーションパスを通じてデフォルトのストアフロントを接続し、ストアで設定されたマーケットからBrazeに同期するマーケットを選択します。既存のインテグレーションでは、カタログ、購読グループ、イベントを中断することなくマーケットを追加できます。ステップバイステップの手順については、[Shopify Marketsの設定](#shopify-markets-setup)を参照してください。

Shopify Marketsは以下の機能を提供します：

- **マーケット対応プロファイル。** インテグレーションは、各ユーザーのShopifyロケールとBrazeの標準的な国と言語の属性をキャプチャするため、カスタム設定なしでマーケットごとにセグメントやトリガーを設定できます。
- **ローカライズされたカタログ。** マーケット固有の商品データが毎日同期されます：マーケットごとの価格、通貨、在庫状況に加え、翻訳されたタイトル、説明、商品URLが含まれます。
- **マーケット対応パーソナライゼーション。** {% raw %}`{% shopify_market %}`{% endraw %} Liquidタグを使用して、Shopifyの翻訳コンテンツを含む各ユーザーのマーケットのカタログ商品でパーソナライズできます。また、`ecommerce.order_placed`などのサポートされているShopifyイベントから、表示通貨などのマーケット詳細を参照することもできます。
- **デフォルトストアのフォールバック。** ユーザーが接続されたマーケットのいずれにも属していない場合、Brazeはデフォルトのストア設定と商品を使用するため、すべてのユーザーが完全で正確なメッセージを受け取ります。

例については、[Marketsユーザーデータの使用](#use-markets-user-data)および[マーケット対応カタログのユースケース](#tutorial-show-products-and-prices-per-market)を参照してください。

## サポートされているShopifyマーケットタイプ {#supported-shopify-market-types}

ベータのこのフェーズでは、以下のルールに従い、Brazeで最大25の単一国マーケットを選択できます：

- 選択する各マーケットは、アクティブな[単一国マーケット](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets)である必要があります。B2Bマーケットおよび小売マーケットはサポートされていません。
  - Shopifyの「現地通貨を使用」設定はサポートされていません
- 1つの国は、選択されたマーケットの1つにのみ属することができます。
- ベータのこのフェーズでは、複数国マーケットはサポートされていません。

選択した各マーケットには、Brazeがサポートするためにアクティブな商品を含むマーケットカタログが必要です：

- マーケットカタログで設定された通貨を使用した、商品のマーケット固有の価格設定
- マーケットごとの商品の在庫状況
- Shopify Translate & Adaptアプリを通じて行われた商品翻訳（商品タイトルやバリアントタイトルなど）

![オーストラリアマーケットのShopifyマーケットプロファイル。]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### 考慮事項 {#considerations}

#### 全般 {#general}

- **接続できるストアは1つ：** 1つのBrazeワークスペースに同時に接続できるMarkets対応Shopifyストアは1つのみです。
- **ロケールの範囲：** ロケールは、Shopify Translate & Adaptアプリを使用して設定した内容に基づいて、翻訳された商品タイトルと説明を取り込みます。また、ロケール固有のURLも取り込みます。価格、通貨、その他の共有カタログフィールドは、マーケット内のロケール間で同じままです。デフォルトでは、Brazeは各マーケットの[デフォルト言語](https://help.shopify.com/en/manual/markets/languages)（Shopifyがそのマーケットに割り当てるプライマリロケール）を使用します。アカウントで拡張ロケールサポートが有効になっている場合、Brazeはそのマーケットに設定された追加のロケールを同期します。

#### マーケットカタログ {#market-catalog}

- **元のShopifyカタログの新しいマーケットビュー：** Marketsは個別のカタログを作成しません。代わりに、元のShopifyカタログの一部として表示されます。Marketsデータは、Shopifyカタログの新しいカタログ行として追加されます。
- **カタログセレクション：** 最大30のカタログセレクション。
- **更新タイミング：** マーケットカタログの商品データは1日1回更新されます。
- **価格のみのマーケットカタログ：** 価格のみのマーケットカタログは、販売チャネルに商品を公開せずにマーケット固有の価格を設定します。在庫と商品の在庫状況はデフォルトのストアカタログから同期され、価格はマーケットカタログの価格リストまたは状況に即した価格設定を反映します。

### サポートされていない機能 {#unsupported-features}

このベータでは以下はサポートされていません：

- マーケットカタログの値下げおよび再入荷トリガー
- マーケット設定された購読グループのメールおよびSMSダブルオプトイン
- 現在の単一国および複数国選択モデルを超えたネストされたマーケットグループまたは国グループワークフロー
- 25を超えるマーケットの選択
- Markets対応カタログのカタログエクスポート
- Shopifyの現地通貨変換、丸めルール、閲覧時およびチェックアウト時の複数カタログ最低価格動作との完全な同等性

## Shopify Marketsの設定 {#shopify-markets-setup}

### ステップ1：Shopify Markets対応ストアを接続する {#step-1-connect-your-shopify-markets-enabled-store}

1. [Shopify標準インテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[Shopifyカスタムインテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)パスを使用してストアを接続します。ストアが接続されたら、セットアップコンポーザーでShopify Marketsを設定します。
2. OAuthフローを完了し、BrazeがOAuthでマーケットスコープをリクエストしていることを確認します：
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. 認証が成功しセットアップコンポーザーが開いたら、**Begin Setup**を選択します。
4. Braze SDKを有効にします。

### ステップ2：マーケットとデータ設定を選択する {#step-2-select-your-market-and-data-settings}

1. **Track Shopify Data**で、**Sync Shopify Markets data**を選択します。
2. **Select Markets**を選択してマーケットを選び、行動イベントとユーザー属性の追跡を選択していることを確認します。
   - （オプション）履歴バックフィルを有効にします

#### Marketsユーザーデータ {#markets-user-data}

Shopify Marketsをサポートするために、Brazeはインテグレーションの[標準イベントと属性]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events)よりも多くのデータを同期します。

Brazeは各ユーザープロファイルに以下の追加マーケットコンテキストを書き込みます：

| データタイプ | 値 | データソース |
| --- | --- | --- |
| カスタム属性 | `shopify_locale` | Shopify |
| 標準属性 | ブラウザ言語 | Braze SDK |
| 標準属性 | 国 | Braze SDK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザープロファイルのデータタイプ"}

Brazeはまた、マーケットコンテキストをサポートするために以下の追加注文イベントプロパティを収集します：

| データタイプ | 影響を受けるイベント | 追加される新しいプロパティ |
| --- | --- | --- |
| eコマース推奨イベント | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`、`presentment_currency`、`market_handle` |
| カスタムイベント | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`、`presentment_currency`、`market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="注文イベントのデータタイプ"}

各プロパティは以下のソースから取得されます：

| プロパティ | データソース |
| --- | --- |
| `country` | Shopify顧客の`default_address`。利用できない場合、Brazeは`shipping_address`を使用します |
| `presentment_currency` | Shopifyの表示通貨値 |
| `market_handle` | 注文国に対して設定されたShopifyマーケット。マーケットが設定されており、国が一致する場合にのみ設定されます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="注文イベントプロパティのデータソース"}

### ステップ3：ユーザーを管理する {#step-3-manage-users}

1. ドロップダウンから`external_id`タイプを選択します。
2. ShopifyからのメールおよびSMSオプトインを有効にします。これにより、BrazeはShopifyからメールおよびSMSの購読状態を同期できます。2つのオプションがあります：
  - **インテグレーションを使用する：** BrazeがメールおよびSMSの状態を同期します。同期先の購読グループを選択するだけです。
  - **独自に構築する：** 状態管理をより細かく制御するために、Brazeの購読グループエンドポイントを使用してカスタムインテグレーションを構築できます。
3. セットアップ中に、同期されたマーケットに関連付けられた各国のデフォルト購読グループを作成します。
  - **新しいShopifyインテグレーション：** 国ごとにデフォルトのメールおよびSMS購読グループを割り当てます。
  - **既存のShopifyインテグレーション：** ストアの現在のデフォルトグループは同期を停止します。国ごとに新しいデフォルトのメールおよびSMSグループを割り当てます。以前の設定は自動的に引き継がれません。

#### オプトインと購読解除の仕組み {#how-opt-ins-and-unsubscribes-work}

セットアップ中に、同期されたマーケットに関連付けられた各国（最大25か国）のデフォルトのメールおよびSMS購読グループを設定します。これは、国の設定を保存する前に必要です。また、同意を複数のリストにルーティングしたい場合は、国ごとに追加の購読グループを割り当てることもできます。

##### 同意はすべての設定された国に適用されます {#consent-applies-to-all-configured-countries}

ユーザーの同意状態がShopifyで変更されると、Brazeはその変更をユーザーの特定の国だけでなく、接続されたストアに紐づくすべての国のデフォルト購読グループに適用します：
  - ユーザーがShopifyで購読状態になると、設定した各国のデフォルトのメールまたはSMS購読グループに購読されます。
  - ユーザーがShopifyで購読解除状態になると、設定した各国のデフォルトのメールまたはSMS購読グループから購読解除されます。

{% alert important %}
Shopifyの同意はストア単位であり、国単位ではありません。Shopifyでは、同意は顧客レコードごとにメールで1回、SMSで1回追跡され、国別やリストタイプ別に購読または購読解除することはありません。このため、Brazeは同意の変更を単一の国や単一の購読グループに適用することができません。Shopifyでの購読または購読解除イベントは、常にすべての設定された国のデフォルト購読グループに一度に適用されます。<br><br>ただし、Braze内では、ユーザーがメッセージングチャネルとエンゲージする際に、購読グループレベルのオプトインとオプトアウトをより細かく制御できます。
{% endalert %}

### ステップ4：商品を同期する {#step-4-sync-products}

1. マーケット内の商品を同期するには、**Sync Shopify products and variants to Braze**を選択します。
2. Brazeの**カタログID**を割り当て、追加の設定を行います。

カタログには、ストアのデフォルト商品のマーケットごとのビューが含まれます。マーケットに公開された各商品について、Brazeは既にサポートされている[標準Shopifyカタログフィールド]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data)に加えて、既存のカタログにマーケット行を追加します。既存のインテグレーションでShopify Marketsを有効にした場合、同期に数分かかることがあります。

マーケット行では、以下のフィールドにマーケット固有の値が設定されます：

| フィールド | 説明 |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | 行のマーケットを識別します。デフォルトマーケットの行は`default`を使用し、追加のマーケットはそのハンドル（例：`au`）を使用します。 |
| {% raw %}`locale`{% endraw %} | 拡張ロケールサポートが有効な場合、行のロケールを識別します（例：`fr`）。 |
| {% raw %}`price`{% endraw %} | マーケットの状況に即した価格設定からのマーケット固有の価格。 |
| {% raw %}`compare_at_price`{% endraw %} | マーケット固有の比較価格。そのマーケットでShopifyに比較価格がない場合は`0`。 |
| {% raw %}`product_title`{% endraw %} | 行のロケールにShopify翻訳が存在する場合の翻訳された商品タイトル。 |
| {% raw %}`variant_title`{% endraw %} | 行のロケールにShopify翻訳が存在する場合の翻訳されたバリアントタイトル。 |
| {% raw %}`product_url`{% endraw %} | ローカライズされたURLが有効な場合のマーケットおよびロケールのストアフロントURL。それ以外の場合はデフォルトの`myshopify.com`商品URLです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マーケット行のカタログフィールド"}

マーケット行は、`<market>_<variant_id>`のようにマーケットハンドルをプレフィックスとした複合`id`を使用します。拡張ロケールサポートが有効な場合、IDにはロケールも含まれます（例：`<market>_<locale>_<variant_id>`）。デフォルトの商品は元のIDを保持します。

### ステップ5：チャネルを有効にする {#step-5-activate-channels}

1. （オプション）**アプリ内メッセージング**を有効にするかどうかを選択します。
2. **Finish Setup**を選択します。

## Marketsユーザーデータの使用 {#use-markets-user-data}

これらの属性とプロパティがユーザープロファイルに設定されると、マーケットごとにユーザーをターゲティングし、メッセージをパーソナライズするために使用できます。

### セグメンテーションでマーケットごとにターゲティングする {#target-by-market-in-segmentation}

セグメントやキャンペーンまたはキャンバスのエントリ条件で、国、ブラウザ言語、または`shopify_locale`でフィルタリングします。例として、特定のマーケットのユーザーのオーディエンスを構築したり、ロケールごとにキャンバスを分割したりできます。

### Liquidでパーソナライズおよびトリガーする {#personalize-and-trigger-with-liquid}

メッセージ内でデータを直接参照します。

| 参照するユーザーデータ | 使用するLiquid |
| --- | --- |
| ユーザーのロケール | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| ユーザーの国 | {% raw %}`{{${country}}}`{% endraw %} |
| 注文の国（トリガーメッセージ内） | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| 注文のマーケット（トリガーメッセージ内） | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| 注文の通貨（トリガーメッセージ内） | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquidで参照するユーザーデータ"}

### 注文アクティビティからメッセージをトリガーする {#trigger-messages-from-order-activity}

新しい注文プロパティは各注文イベントに付随するため、注文からメッセージをトリガーし、マーケット対応の詳細を使用してメッセージの内容をパーソナライズできます。

メッセージ本文のシンプルなバージョンは次のようになります：

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

プロパティはイベント自体に含まれているため、追加の設定なしで各ユーザーのマーケットに正確なメッセージが送信されます。

## チュートリアル：マーケットごとに商品と価格を表示する {#tutorial-show-products-and-prices-per-market}

マーケット対応カタログを使用して、各ユーザーに自分のマーケットの商品と価格を表示する単一のメッセージを作成します。

1. マーケットデータを使用するセレクションを作成します。
2. Liquidを使用してメッセージ内でセレクションを参照します。

メッセージが特定のマーケットをターゲットにする場合は、固定マーケットを使用できます。

### ステップ1：マーケットデータを使用してセレクションを作成する {#step-1-create-a-selection-using-markets-data}

[セレクション]({{site.baseurl}}/catalog_selections)は、メッセージ内で参照するキュレートされた商品セットです。同期されたマーケットを持つShopifyカタログの場合、**フィルター設定**セクションには、商品データを1つのマーケットにスコープするか、ユーザーごとにパーソナライズする**マーケットスコープ**エリアが含まれます。

1. Shopifyカタログに移動し、**セレクション**タブを開きます。
2. **セレクションを作成**を選択し、セレクションに名前を付け、オプションの説明を追加し、結果の上限を設定します。
3. **フィルター設定**の**マーケットスコープ**で、**マーケット**ドロップダウンを使用して、セレクションがマーケット固有の商品をどのように解決するかを選択します：
   - **パーソナライズ：** 各受信者は、プロファイルの`country`属性に一致するマーケットの商品と価格を表示します。
   - **同期されたマーケット：** 名前でマーケットを選択し、セレクションをそのマーケットの商品と価格に固定します。メッセージが単一のマーケットのみをターゲットにする場合に使用します。
4. 追加のフィルター条件を完了し、セレクションを保存します。
5. **ユーザーでプレビュー**で、ユーザーを選択して、そのプロファイルに対してセレクションが返す内容を確認します。**パーソナライズ**を使用するセレクションは、ユーザーを選択した後にのみプレビューできます。

| ターゲット | フィルター |
| --- | --- |
| 特定のマーケット | `market_handle` = `au` |
| デフォルト商品のみ | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ターゲットと関連フィルター"}

{% alert note %}
マーケットを指定しない場合、Brazeはデフォルトの商品を使用します。
{% endalert %}

### ステップ2：マーケット対応カタログセレクションをメッセージに追加する {#step-2-add-market-aware-catalog-selections-to-messages}

単一のメッセージですべてのユーザーに自分のマーケットの商品を提供するには、以下のフィルターでセレクションを1つ作成します：

| セレクション名 | フィールド | オペレーター | 値 |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="セレクション名と関連フィルター"}

送信時に、Brazeは{% raw %}`{{shopify_market.handle}}`{% endraw %}を各ユーザーのマーケットに置き換えるため、`market_products`はすべてのユーザーに適切な商品を提供します。`default_products`は、一致するマーケットがないユーザーのフォールバックです。

{% raw %}`{% shopify_market %}`{% endraw %}タグを使用して、メッセージ内でセレクションを参照します：

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
- `<your_catalog_name>`をカタログ名に置き換え、異なる場合は独自のセレクション名を使用してください。
- {% raw %}`{{shopify_market.handle}}`{% endraw %}のチェックにより、一致するマーケットがないユーザーは`default_products`にルーティングされるため、空のメッセージではなく商品を受け取ります。

マーケット内のユーザーとしてプレビューし、メッセージにそのマーケットの商品、価格、翻訳されたタイトルが表示されることを確認します。