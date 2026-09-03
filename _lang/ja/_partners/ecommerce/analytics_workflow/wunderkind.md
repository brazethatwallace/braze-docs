---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "このリファレンス記事では、Wunderkind SignalsとBrazeの統合について説明します。キャンバスジャーニーをトリガーする行動シグナル、Canvas Entry APIを使用したセットアップ、APIトリガー配信でのキャンバスコンテキストペイロード、レポートについて取り上げています。"
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) は、独自の識別技術を使用して匿名のWebサイト訪問者を認識し、実用的なメールアドレスに解決するeコマースパフォーマンスプラットフォームです。平均して、WunderkindはWebサイトトラフィックの3～5%の識別率を40～60%に拡大し、ブランドが既存のメールサービスプロバイダー (ESP) を通じてパーソナライズされた1対1のメッセージを大規模にトリガーできるようにします。

*この統合はWunderkindによって管理されています。サポートについては、[support.wunderkind.co](https://support.wunderkind.co) をご覧ください。*

## 統合について {#about-the-integration}

Wunderkind Signals統合により、カート放棄、商品放棄、価格下落などの高インテントな行動シグナルを使用して、Brazeでリアルタイムのキャンバスジャーニーをトリガーできます。WunderkindはWebサイト上の匿名ユーザーを特定し、配信可能なメールアドレスにIDを解決した上で、キャンバス Entry APIを介してBrazeに構造化されたシグナルペイロードを配信し、事前設定されたメールフローを自動的に開始します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Wunderkind アカウント | Signals が有効になっている Wunderkind アカウントが必要です。利用資格については、Wunderkind の担当者にお問い合わせください。 |
| Braze アカウント | キャンバスにアクセスできる Braze アカウントが必要です。Wunderkind チームにアカウントのシートを付与する必要があります。詳細については、[Wunderkind に Braze アカウントへのアクセスを許可する](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account)を参照してください。 |
| Braze REST APIキー | セットアップ時に特定の権限を持つ専用のAPIキーを作成します（[ステップ1](#step-1-create-a-braze-api-key-for-wunderkind)を参照）。 |
| ユーザー識別 | Wunderkind は通常、`user_alias`（`alias_label: "wknd_email_id"`、多くの場合メールアドレスを `alias_name` として使用）を使って消費者を Braze で解決します。[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)の各受信者には、`external_user_id`、`user_alias`、`braze_id`、または `email` のいずれか1つを含める必要があります（[recipients オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)）。`email` を使用する場合は、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)を含めてください。`user_alias` を使用する場合、トリガーの前にプロファイルが Braze に存在している必要があります。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用して、事前にユーザーとエイリアスを作成または更新してください。詳細については、[制限事項](#limitations)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 仕組み {#how-it-works}

Wunderkind が高インテントの匿名ユーザーを識別し、そのアイデンティティを解決すると、`/canvas/trigger/send` エンドポイントを使用して Braze にシグナルペイロードを送信し、そのユーザーに関連するキャンバスジャーニーをリアルタイムでトリガーします。

技術的な概要の詳細については、[Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview) を参照してください。

## 連携 {#integration}

### ステップ1：Wunderkind 用の Braze API キーを作成する {#step-1-create-a-braze-api-key-for-wunderkind}

Braze ダッシュボードで以下を行います。

1. **設定** > **API キー**に移動し、**新しい API キーを作成**をクリックします。
2. キーにわかりやすい名前を付けます（例：`Wunderkind Signals`）。
3. [Grant Wunderkind access to your Braze account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) に記載されている権限を付与します。
4. API キーをコピーして、次のセクションで Wunderkind プラットフォームに入力します。

{% alert note %}
Wunderkind Signals では、Braze [REST API]({{site.baseurl}}/api/basics) リクエストは OAuth トークンではなく REST APIキーで認証されます。ダッシュボードで専用の API キーを作成し、そのキーを Wunderkind に提供してください。
{% endalert %}

### ステップ2：Wunderkind プラットフォームに Braze を接続する {#step-2-connect-braze-to-the-wunderkind-platform}

1. Wunderkind プラットフォームにログインし、**Integrations Hub** に移動します。
2. **Braze** タイルを選択し、**Connect** を選択します。
3. Braze REST APIキーを入力し、クラスターを選択します。
4. **Save** を選択します。

### ステップ3：新しい Braze アセットを確認する {#step-3-review-new-braze-assets}

有効化すると、Wunderkind は Wunderkind 担当者と合意した戦略に基づいて、Braze ワークスペースに新しい実装アセットをプロビジョニングします。

| アセットタイプ | Wunderkind の作成方法 |
| ---------- | -------------------------- |
| Content Blocks | 自動 |
| API トリガーのキャンバス | マネージドサービス |
| タグ、カスタム属性、リンクテンプレート | マネージドサービス |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ3：新しい Braze アセットを確認する" }

### ステップ4：キャンバスの設定を完了する {#step-4-complete-canvas-setup}

各 Signals キャンバスについて、Braze のドラッグ＆ドロップエディターまたは HTML を使用してメールテンプレートを作成します。

- Wunderkind は送信時に `/canvas/trigger/send` で各受信者の `context` オブジェクトに商品データとセッションデータを入力します。
- テンプレートでそのペイロードを Liquid と組み合わせて使用する方法の詳細については、Wunderkind ヘルプセンターの [Complete キャンバス setup](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) を参照してください。

### ステップ5：キャンバスの適格性を確認する {#step-5-review-canvas-eligibility}

各 Signals キャンバスについて、**ターゲットオーディエンス**設定に移動し、Wunderkind のデフォルトのエントリオーディエンスと終了条件を確認します。

- ユーザーにメッセージを送りすぎないようにするには、[ユーザー中心のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#user-centric-rate-limiting)を参照してください。
- ユーザーが購入後もキャンバスメッセージを受け取り続けないように設定を調整します。例えば、例外として **Make Purchase** を追加します。
- 一部の Signals キャンバスは、ユーザーが最も意図の高いメッセージを受け取れるように、カスタム属性フィルターで事前設定されています。
- キャンバスの適格性と優先順位の詳細については、Wunderkind ヘルプセンターの [Review キャンバス eligibility](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) を参照してください。

### ステップ6：テストとローンチ {#step-6-test-and-launch}

Wunderkind は本番稼働前にエンドツーエンドの QA を実施します。

- シグナルが API エラーなく正しいキャンバス ID に配信されていることを確認します。
- `context` フィールド（商品名、画像、URL）がレンダリングされたメールテンプレートに正しく入力されていることを検証します。
- モック Wunderkind 商品を使用してテンプレートをプレビューする手順については、Wunderkind ヘルプセンターの [Test and launch Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) を参照してください。

QA が合格すると、Wunderkind の実装マネージャーがチームと連携して本番ローンチを調整します。

## キャンバスコンテキストペイロード {#canvas-context-payload}

Wunderkind は6種類のシグナルタイプをサポートしています。それぞれが `/canvas/trigger/send` で受信者ごとの [`context`]({{site.baseurl}}/api/objects_filters/context_object) オブジェクト内に固有のキーと値のセットを配信します（[API トリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照）。`WkPurpose` フィールドは、そのペイロード内のシグナルタイプを識別します。

### 共通フィールド（すべてのキャンバスタイプ） {#canvas-types-table}

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `Origin` | String | 常に `"wunderkind"` |
| `DataOnly` | String | 常に `"Y"` — Wunderkind がデータレイヤーとしてのみ機能し、Braze が送信を実行することを示します |
| `UserType` | String | `"prospect"` または `"customer"` |
| `WkChannel` | String | このインテグレーションでは常に `"email"` |
| `WkPurpose` | String | シグナルタイプの識別子（このセクションのキャンバスごとの値を参照） |
| `WKCouponCode` | String | クーポンコード（該当する場合）（使用しない場合は空文字列） |
| `WKCouponPurpose` | String | クーポンオファーの説明（使用しない場合は空文字列） |
| `Items` | Array | 商品オブジェクトの配列（このセクションの商品フィールドを参照） |
| `WkOpen` | String | レポート用に利用可能なトラッキングピクセル |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="共通フィールド（すべてのキャンバスタイプ）" }

### 商品アイテムフィールド {#product-item-fields}

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `WkCopy` | String | 商品名 |
| `WkId` | String | 商品 ID |
| `WkImageUrl` | String | 商品画像の URL |
| `WkUrl` | String | 商品詳細ページの URL |
| `WkPrice` | String | 元の価格（価格下落キャンバスのみ） |
| `WKSalePrice` | String | セール価格（価格下落キャンバスのみ） |
| `WkQuantity` | String | 残りの数量（在庫わずかキャンバスのみ） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="商品アイテムフィールド" }

### キャンバス固有のフィールドと `WkPurpose` の値 {#canvas-specific-fields-and-wkpurpose-values}

| キャンバスタイプ | `WkPurpose` の値 | 追加フィールド |
| ----------- | ----------------- | ------------------- |
| カート放棄 | `"cart abandonment"` | `WkCartReplenUrl` — カートを復元するための URL |
| 商品放棄 | `"product abandonment"` | — |
| カテゴリリキャップ | `"category recap"` | `WkCategoryUrl` — 閲覧したカテゴリの URL |
| 再入荷 | `"back in stock"` | — |
| 価格下落 | `"price drop"` | 各アイテムの `WkPrice`、`WKSalePrice` |
| 在庫わずか | `"low stock"` | 各アイテムの `WkQuantity` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="キャンバス固有のフィールドと WkPurpose の値" }

### ペイロードの例 {#example-payloads}

`recipients` 内の各オブジェクトには、`external_user_id`、`user_alias`、`braze_id`、または `email` のいずれか1つを正確に含める必要があります。詳細については、[受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)を参照してください。

{% alert note %}
各例では **1つの** Braze 受信者識別子を使用しています。最初の6つは `user_alias` のみを使用し、最後の例は `email` と [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) のみを使用しています。例の JSON では `context` 内の `WkChannel` キーを省略しています。これは、レビューツールがその値（`"email"`）を Braze の受信者 `email` フィールドと混同しないようにするためです。本番環境では、[共通フィールド（すべてのキャンバスタイプ）テーブル](#canvas-types-table)に記載されているとおり、`context` 内に `"WkChannel": "email"` を含めてください。
{% endalert %}

以下の例では、Wunderkind が ID を解決する方法に合わせて `user_alias` と `wknd_email_id` を使用しています。

{% details カート放棄のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 商品放棄のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details カテゴリリキャップのペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 再入荷のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 価格下落のペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details 在庫わずかのペイロード例 %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details メール識別子の例（代替方法） %}
`user_alias` の代わりに Braze の `email` フィールドを使用してキャンバスをトリガーする場合、受信者には `email` と `prioritization` のみを含める必要があります（[API トリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照）。`context` オブジェクトは他の例と同じです。

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Liquid の使用例 {#example-liquid-usage}

Wunderkind が `/canvas/trigger/send` を呼び出すと、各受信者の `context` オブジェクトに渡したキーと値がキャンバスエントリデータになります。メッセージステップでは、`context` Liquid 名前空間を使用して参照します。例えば {% raw %}`{{context.${WkPurpose}}}`{% endraw %} のように使用します。詳細については [キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)および[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。正しい Liquid 構文を使用する以外に追加の設定は不要です。

`for` タグの条件内に Braze の出力タグをネストしないでください。まず `context` の `Items` 配列を変数に割り当ててからループします。詳細については [Liquid の使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#use-a-filter-result-in-a-for-loop)を参照してください。`assign` 行では Braze のキャンバスエントリ形式 {% raw %}`{{context.${Items}}}`{% endraw %} を使用します（[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#summary-of-supported-tags)を参照）。

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## レポート {#reporting}

Wunderkind は **Braze Currents** を使用して Braze からパフォーマンスデータを取り込みます。Currents は生のイベントを Google Cloud Storage にストリーミングします。その後、Wunderkind はこれらのイベントを正規化し、元のシグナルに対して集計して、1:1 のアトリビューションレポートを作成します。

以下の指標は、Wunderkind のレポートダッシュボードでまもなく利用可能になります。

| 指標 | ソース |
| ------ | ------ |
| 配信済み送信 | Braze Currents |
| メール開封 | Braze Currents |
| クリック | Braze Currents |
| コンバージョン | Braze Currents（設定時に定義されたイベント） |
| 購読解除 | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 aria-label="レポート" }

## 制限事項 {#limitations}

- **配信停止／オプトアウトの同期はありません。**配信停止は Braze でネイティブに管理する必要があります。注意：Braze Signals に移行する既存の Wunderkind のお客様については、Wunderkind がチームと連携して現在の設定を維持します。
- **メールチャネルのみ。**SMS は現在このインテグレーションではサポートされていません。
- **キャンバスのトリガーの前にユーザープロファイルが存在している必要があります。**`user_alias` の受信者を指定した [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) は、そのエイリアスが既に設定されている**既存の** Braze プロファイルのみを解決します。エイリアスで `send_to_existing_only` を使用することはできず、キャンバスのトリガーだけではエイリアスから新規プロファイルを作成しません。まずユーザーを作成または更新し、`wknd_email_id` エイリアスを設定する必要があります（例えば、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) または [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) を使用します）。Wunderkind は、Braze が処理を完了できるよう、そのアップサート後にトリガーを発行するまで少し待つ場合があります。
- **識別子としてのメール。**キャンバスのトリガーが `user_alias` ではなく `email` で受信者を識別する場合、Braze の要件に従い、その受信者オブジェクトに [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) を含めてください。

## その他のリソース {#additional-resources}

- [Wunderkind Help Center — Signals for Braze Overview](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integration Overview](https://developer.wunderkind.co/docs/integration-overview)
- [API トリガー配信を使用してキャンバスメッセージを送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [キャンバスコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)