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

Wunderkind Signalsの統合により、カート放棄、商品放棄、価格低下などの高インテントな行動シグナルが、Brazeでリアルタイムのキャンバスジャーニーをトリガーできます。WunderkindはWebサイト上の匿名ユーザーを識別し、配信可能なメールアドレスにアイデンティティを解決し、キャンバス Entry APIを介して構造化されたシグナルペイロードをBrazeに配信することで、事前設定されたメールフローを自動的に開始します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Wunderkindアカウント | Signalsが有効になっているWunderkindアカウントが必要です。資格の確認については、Wunderkindの担当者にお問い合わせください。 |
| Brazeアカウント | キャンバスにアクセスできるBrazeアカウントが必要です。WunderkindチームにBrazeアカウントのシートを付与する必要があります。詳細については、[Grant Wunderkind access to your Braze account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) を参照してください。 |
| Braze REST APIキー | セットアップ中に特定の権限を持つ専用のAPIキーを作成します（[ステップ1](#step-1-create-a-braze-api-key-for-wunderkind) を参照）。 |
| ユーザー識別 | Wunderkindは通常、`user_alias`と`alias_label: "wknd_email_id"`（多くの場合メールアドレスを`alias_name`として使用）を使用して消費者をBrazeに解決します。各[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)の受信者には、`external_user_id`、`user_alias`、`braze_id`、または`email`のいずれか1つを含める必要があります（[recipientsオブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)）。`email`を使用する場合は、[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)を含めてください。`user_alias`を使用する場合、トリガーの前にプロファイルがBrazeに既に存在している必要があります。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用して、ユーザーとエイリアスを先に作成または更新してください。詳細については、[制限事項](#limitations)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 仕組み {#how-it-works}

Wunderkindが高インテントの匿名ユーザーを識別し、そのアイデンティティを解決すると、`/canvas/trigger/send`エンドポイントを使用してシグナルペイロードをBrazeに送信し、そのユーザーに対して関連するキャンバスジャーニーをリアルタイムでトリガーします。

技術的な概要の全体については、[Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview) を参照してください。

## 統合 {#integration}

### ステップ1: Wunderkind用のBraze APIキーを作成する {#step-1-create-a-braze-api-key-for-wunderkind}

Brazeダッシュボードで以下を行います。

1. **設定** > **APIキー**に移動し、**新しいAPIキーを作成**をクリックします。
2. キーにわかりやすい名前を付けます（例: `Wunderkind Signals`）。
3. [Grant Wunderkind access to your Braze account](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) に記載されている権限を付与します。
4. APIキーをコピーして、次のセクションでWunderkindプラットフォームに入力します。

{% alert note %}
Wunderkind Signalsの場合、Braze [REST API]({{site.baseurl}}/api/basics)リクエストはOAuthトークンではなくREST APIキーで認証されます。ダッシュボードで専用のAPIキーを作成し、そのキーをWunderkindに提供してください。
{% endalert %}

### ステップ2: BrazeをWunderkindプラットフォームに接続する {#step-2-connect-braze-to-the-wunderkind-platform}

1. Wunderkindプラットフォームにログインし、**Integrations Hub**に移動します。
2. **Braze**タイルを選択し、**Connect**を選択します。
3. Braze REST APIキーを入力し、クラスターを選択します。
4. **Save**を選択します。

### ステップ3: 新しいBrazeアセットを確認する {#step-3-review-new-braze-assets}

アクティベーション時に、WunderkindはWunderkindの担当者と合意した戦略に基づいて、Brazeワークスペースに新しい実装アセットをプロビジョニングします。

| アセットタイプ | Wunderkindの作成方法 |
| ---------- | -------------------------- |
| Content Blocks | 自動 |
| APIトリガーキャンバス | マネージドサービス |
| タグ、カスタム属性、リンクテンプレート | マネージドサービス |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Review new Braze assets" }

### ステップ4: キャンバスのセットアップを完了する {#step-4-complete-canvas-setup}

各Signalsキャンバスについて、Brazeのドラッグ＆ドロップエディターまたはHTMLを使用してメールテンプレートを作成します。

- Wunderkindは、送信時に`/canvas/trigger/send`で各受信者の`context`オブジェクトに商品データとセッションデータを入力します。
- テンプレートでそのペイロードをLiquidで使用する方法の詳細な手順については、Wunderkindヘルプセンターの[Complete キャンバス Setup](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup)を参照してください。

### ステップ5: キャンバスの適格性を確認する {#step-5-review-canvas-eligibility}

各Signalsキャンバスについて、**ターゲットオーディエンス**設定に移動し、Wunderkindのデフォルトのエントリオーディエンスと終了条件を確認します。

- ユーザーへのメッセージ送信頻度が高くなりすぎないようにするには、[ユーザー中心のレート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)を参照してください。
- ユーザーが購入後もキャンバスメッセージを受信し続けることを防ぐために設定を調整します。例えば、例外として**Make Purchase**を追加します。
- 特定のSignalsキャンバスは、ユーザーが最もインテントの高いメッセージを受信できるように、カスタム属性フィルターで事前設定されています。
- キャンバスの適格性と優先度の詳細については、Wunderkindヘルプセンターの[Review キャンバス Eligibility](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility)を参照してください。

### ステップ6: テストとローンチ {#step-6-test-and-launch}

Wunderkindは本番稼働前にエンドツーエンドのQAを実施します。

- シグナルがAPIエラーなしで正しいキャンバスIDに配信されていることを確認します。
- `context`フィールド（商品名、画像、URL）がレンダリングされたメールテンプレートに正しく入力されていることを検証します。
- モックWunderkind商品でテンプレートをプレビューする手順については、Wunderkindヘルプセンターの[Test and Launch Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze)を参照してください。

QAが合格すると、Wunderkindの実装マネージャーがチームと連携して本番環境へのローンチを調整します。

## キャンバスコンテキストペイロード {#canvas-context-payload}

Wunderkindは6種類のシグナルタイプをサポートしています。各タイプは、`/canvas/trigger/send`でその受信者の[`context`]({{site.baseurl}}/api/objects_filters/context_object)オブジェクト内に固有のキーと値のセットを配信します（[APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照）。`WkPurpose`フィールドは、そのペイロード内のシグナルタイプを識別します。

### 共通フィールド（すべてのキャンバスタイプ） {#canvas-types-table}

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `Origin` | 文字列 | 常に`"wunderkind"` |
| `DataOnly` | 文字列 | 常に`"Y"` — Wunderkindがデータレイヤーとしてのみ機能し、Brazeが送信を実行することを示します |
| `UserType` | 文字列 | `"prospect"`または`"customer"` |
| `WkChannel` | 文字列 | この統合では常に`"email"` |
| `WkPurpose` | 文字列 | シグナルタイプ識別子（このセクションの各キャンバスの値を参照） |
| `WKCouponCode` | 文字列 | クーポンコード（該当する場合。使用しない場合は空文字列） |
| `WKCouponPurpose` | 文字列 | クーポンオファーの説明（使用しない場合は空文字列） |
| `Items` | 配列 | 商品オブジェクトの配列（このセクションの商品フィールドを参照） |
| `WkOpen` | 文字列 | レポート目的で利用可能なトラッキングピクセル |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Common fields (all キャンバス types) #canvas-types-table" }

### 商品アイテムフィールド {#product-item-fields}

| プロパティ | タイプ | 説明 |
| -------- | ---- | ----------- |
| `WkCopy` | 文字列 | 商品名 |
| `WkId` | 文字列 | 商品ID |
| `WkImageUrl` | 文字列 | 商品画像URL |
| `WkUrl` | 文字列 | 商品詳細ページURL |
| `WkPrice` | 文字列 | 元の価格（価格低下キャンバスのみ） |
| `WKSalePrice` | 文字列 | セール価格（価格低下キャンバスのみ） |
| `WkQuantity` | 文字列 | 残り数量（在庫僅少キャンバスのみ） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Product item fields" }

### キャンバス固有のフィールドと`WkPurpose`の値 {#canvas-specific-fields-and-wkpurpose-values}

| キャンバスタイプ | `WkPurpose`の値 | 追加フィールド |
| ----------- | ----------------- | ------------------- |
| カート放棄 | `"cart abandonment"` | `WkCartReplenUrl` — カートを補充するURL |
| 商品放棄 | `"product abandonment"` | — |
| カテゴリーまとめ | `"category recap"` | `WkCategoryUrl` — 閲覧されたカテゴリーのURL |
| 再入荷 | `"back in stock"` | — |
| 価格低下 | `"price drop"` | 各アイテムの`WkPrice`、`WKSalePrice` |
| 在庫僅少 | `"low stock"` | 各アイテムの`WkQuantity` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvas-specific fields and WkPurpose values" }

### ペイロードの例 {#example-payloads}

`recipients`内の各オブジェクトには、`external_user_id`、`user_alias`、`braze_id`、または`email`のいずれか1つを含める必要があります。詳細については、[recipientsオブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)を参照してください。

{% alert note %}
各例では**1つの**Braze受信者識別子を使用しています。最初の6つは`user_alias`のみを使用し、最後の1つは`email`と[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)のみを使用しています。例のJSONでは、レビューツールがその値（`"email"`）をBrazeの受信者`email`フィールドと混同しないように、`context`内の`WkChannel`キーを省略しています。本番環境では、[共通フィールド（すべてのキャンバスタイプ）テーブル](#canvas-types-table)に記載されているとおり、`context`に`"WkChannel": "email"`を含めてください。
{% endalert %}

以下の例では、Wunderkindがアイデンティティを解決する方法に合わせて、`wknd_email_id`を使用した`user_alias`を使用しています。

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

{% details カテゴリーまとめのペイロード例 %}
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

{% details 価格低下のペイロード例 %}
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

{% details 在庫僅少のペイロード例 %}
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

{% details メール識別子の例（代替） %}
`user_alias`の代わりにBrazeの`email`フィールドでキャンバスをトリガーする場合、受信者には`email`と`prioritization`のみを含める必要があります（[APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照）。`context`オブジェクトは他の例と同じです。

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

### Liquidの使用例 {#example-liquid-usage}

Wunderkindが`/canvas/trigger/send`を呼び出すと、各受信者の`context`オブジェクトに渡されたキーと値がキャンバスエントリデータになります。メッセージステップでは、`context` Liquid名前空間を使用してそれらを参照します。例えば、[キャンバスcontextオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)および[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)に記載されているように {% raw %}`{{context.${WkPurpose}}}`{% endraw %} を使用します。正しいLiquid構文を使用する以外に、追加の設定は不要です。

Brazeの出力タグを`for`タグの条件内にネストしないでください。[Liquidの使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#use-a-filter-result-in-a-for-loop)に記載されているように、まず`context`から`Items`配列を変数に割り当ててからループしてください。`assign`行ではBrazeのキャンバスエントリ形式 {% raw %}`{{context.${Items}}}`{% endraw %} を使用します（[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#summary-of-supported-tags)を参照）。

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

Wunderkindは**Braze Currents**を使用してBrazeからパフォーマンスデータを取り込みます。Braze Currentsは生のイベントをGoogle Cloud Storageにストリーミングします。Wunderkindはこれらのイベントを正規化し、元のシグナルに対して集計することで、1対1のアトリビューションレポートを作成します。

以下の指標は、Wunderkindレポートダッシュボードで近日中に利用可能になります。

| 指標 | ソース |
| ------ | ------ |
| 配信済み送信数 | Braze Currents |
| メール開封数 | Braze Currents |
| クリック数 | Braze Currents |
| コンバージョン | Braze Currents（セットアップ時に定義されたイベント） |
| 購読解除 | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reporting" }

## 制限事項 {#limitations}

- **抑制/オプトアウトの同期なし。** 抑制はBraze内でネイティブに管理する必要があります。注: Braze Signalsに移行する既存のWunderkind顧客の場合、Wunderkindはチームと連携して現在のセットアップを維持します。
- **メールチャネルのみ。** SMSはこの統合では現在サポートされていません。
- **キャンバストリガーの前にユーザープロファイルが存在している必要があります。** `user_alias`受信者を使用した[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)は、そのエイリアスを既に持つ**既存の**Brazeプロファイルのみを解決します。エイリアスで`send_to_existing_only`を使用することはできず、キャンバストリガーはエイリアスのみから新しいプロファイルを作成しません。ユーザーを先に作成または更新し、`wknd_email_id`エイリアスを設定する必要があります（例えば、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用）。Wunderkindは、Brazeが処理を完了できるように、そのアップサート後にトリガーを発火する前に少し待機する場合があります。
- **識別子としてのメール。** キャンバストリガーが`user_alias`の代わりに`email`で受信者を識別する場合、Brazeの要件に従って、その受信者オブジェクトに[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)を含めてください。


## その他のリソース {#additional-resources}

- [Wunderkindヘルプセンター — Signals for Braze Overview](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integration Overview](https://developer.wunderkind.co/docs/integration-overview)
- [APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [キャンバスcontextオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)