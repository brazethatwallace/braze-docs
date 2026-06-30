---
nav_title: Shopifyのアップグレード
article_title: "Shopify連携のアップグレード"
description: "BrazeのShopify連携をアップグレードする方法を説明します。"
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Shopify連携のアップグレード（標準） {#upgrading-your-shopify-integration-standard}

> Brazeの標準パスを使用してShopify連携をアップグレードする方法を説明します。最高のエクスペリエンスを提供するため、すべてのShopify連携は2025年8月28日までに最新バージョンへの[アップグレード]({{site.baseurl}}/shopify)が必要です。このアップグレードは、Shopifyの技術における重要な変更が連携の機能に影響を与えるため、不可欠です。

## 対象者 {#whos-eligible}

このアップグレードパスは、Shopifyオンラインストアを持つブランドを対象としています。

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## アップグレード要件 {#upgrade-requirements}

開始する前に、以下を確認してください。

- **重要な変更点：** レガシーコネクターから新しいコネクターへの重要な変更点を[Shopifyアップグレードの概要]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)で確認してください。
- **アップグレードの前提条件：** エンジニアリングチームとマーケティングチームで必要な[アップグレードの前提条件]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites)をすべて完了してください。
- **破壊的変更：** Brazeでフラグが立てられたすべての破壊的変更を確認し、修正してください。詳細な手順については、[破壊的変更の修正](#fixing-breaking-changes-fixing-breaking-changes)を参照してください。

## 破壊的変更の修正 {#fixing-breaking-changes}

Brazeで、**パートナー連携** > **Shopify**に移動し、**アップグレードを開始**を選択します。

![アップグレードを開始するオプションがあるパネル。]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Shopifyデータを使用している影響を受けるキャンバス、キャンペーン、セグメントにフラグが立てられます。

![破壊的変更の影響を確認するためのモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

ほとんどのイベントについては、アクティブなメッセージのスムーズなアップグレードを促進するために、「OR」演算子を使用して新しい必須Shopifyイベントと属性を含めることをお勧めします。より具体的なケースについては、以下を参照してください。

{% tabs local %}
{% tab 放棄カート %}
放棄カートメッセージングの場合、新しい放棄カートキャンバステンプレートを使用する必要があります。これには以下が含まれます。

- 「カート更新を実行」アクションに基づく新しいトリガー
- 購入プロセスを進めた顧客を除外するための事前定義された終了条件
- 製品パーソナライゼーションをサポートする新しいショッピングカートLiquidタグ
{% endtab %}

{% tab 放棄チェックアウト %}
放棄チェックアウトメッセージングの場合、新しい放棄チェックアウトキャンバステンプレートを使用する必要があります。これには以下が含まれます。

- エントリ条件に事前定義されたecommerce.checkout_startedイベント
- 購入プロセスを進めた顧客を除外するための事前定義された終了条件
- 製品パーソナライゼーションをサポートする新しいショッピングカートLiquidタグ

連携を通じて利用可能な新しいeコマースキャンバステンプレートと製品パーソナライゼーション用の事前定義されたHTMLブロックの完全なリストについては、[キャンバスユーザージャーニーの作成]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys)を参照してください。

{% alert important %}
Shopify連携で廃止されたイベントを使用するアクティブなメッセージに対応しない場合、影響を受けるメッセージは顧客に送信されなくなります。
{% endalert %}

詳細については、[サポートされるShopifyイベント]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events)を確認してください。
{% endtab %}

{% tab サブスクライバーリスト %}
連携を通じてShopifyからメールまたはSMSサブスクライバーを収集している場合、アクティブなメッセージにShopifyストアの対応するサブスクライバーリストが含まれていることを確認してください。

アップグレードが完了すると、連携用の新しいデフォルトサブスクリプショングループが作成されます。これらをアクティブなメッセージングの一部として活用する必要があります。変更の詳細については、[サブスクライバーの収集]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)を参照してください。
{% endtab %}
{% endtabs %}

## Shopifyのアップグレード {#upgrading-shopify}

{% alert important %}
アップグレードを開始する前に、すべての[破壊的変更を修正](#fixing-breaking-changes)することが不可欠です。
{% endalert %}

### ステップ1：アップグレードの開始 {#step-1-start-the-upgrade}

Brazeで、**パートナー連携** > **Shopify**に移動し、**アップグレードを開始**を選択します。

![アップグレードを開始するオプションがあるパネル。]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

チェックボックスをオンにして利用規約に同意し、**アップグレードを開始**を選択します。

![アップグレードにより破壊的変更が発生する可能性があることを理解していることを確認するモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### ステップ2：Braze SDKのセットアップ {#step-2-set-up-the-braze-sdks}

標準連携では、Braze SDKがShopifyサイトに自動的に追加されます。すでにBraze SDKを直接統合しているか、サードパーティツールを使用している場合は、アップグレード時に以前のSDK実装を削除するよう開発者と調整してください。

![新しい連携がBrazeおよびJavaScript SDKをストアに自動的に実装することを確認するモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### ステップ3：Brazeアプリの再認証 {#step-3-reauthorize-the-braze-app}

Brazeアプリを再認証するには、**Shopifyに移動**を選択します。

![Brazeアプリを再認証するためにShopifyに移動するボタンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

Shopifyサイトで、プロンプトに従ってBrazeアプリを再認証します。これにより、BrazeがShopifyデータにアクセスできるようになります。

{% alert note %}
再認証プロセスには数分かかる場合がありますが、完了するとShopifyページで自動的に更新されます。
{% endalert %}

![Shopifyイベントのステータスを表示する「連携設定」ページ。]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### ステップ4：external IDタイプの選択 {#step-4-choose-an-external-id-type}

選択したexternal IDタイプは、Shopifyアカウントが作成されるか注文が行われた際に、新しいShopify顧客プロファイルに割り当てられます。また、既存のユーザープロファイルにShopify顧客IDエイリアスがあるがBrazeでexternal IDが割り当てられていない場合、そのプロファイルの更新にも使用されます。

external IDタイプを選択するには、Brazeに戻り、**external IDを確認**を選択します。

![external IDを確認するボタンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

ワークスペースのShopify連携に使用するexternal IDを選択します。完了したら、**external IDを設定**を選択します。

![external IDを選択するドロップダウンがあるモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスをBrazeのexternal IDとして使用すると、データソース全体のID管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報：** メールアドレスは容易に推測できるため、攻撃に対して脆弱です。
- **悪用のリスク：** 悪意のあるユーザーがWebブラウザーを改変して他人のメールアドレスをexternal IDとして送信した場合、機密性の高いメッセージやアカウント情報にアクセスされる可能性があります。
{% endalert %}

デフォルトでは、BrazeはShopifyからのメールをexternal IDとして使用する前に自動的に小文字に変換します。メールまたはハッシュ化されたメールをexternal IDとして使用している場合、メールアドレスがexternal IDとして割り当てられる前、または他のデータソースからハッシュ化される前に、小文字に変換されていることを確認してください。これにより、external IDの不一致を防ぎ、Brazeでの重複ユーザープロファイルの作成を回避できます。

カスタムexternal IDタイプを選択した場合は、ステップ4.1〜4.3に進んでください。それ以外の場合は、ステップ5に進んでください。

#### ステップ4.1：`braze.external_id`メタフィールドの作成 {#step-41-create-the-brazeexternal_id-metafield}

1. Shopify管理パネルで、**設定** > **メタフィールド**に移動します。
2. **顧客** > **定義を追加**を選択します。
3. **名前空間とキー**に`braze.external_id`と入力します。
4. **タイプ**で**IDタイプ**を選択します。

メタフィールドが作成されたら、顧客に対してデータを入力します。以下のアプローチをお勧めします。

- **顧客作成webhookのリッスン：** [`customer/create`イベント](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)をリッスンするwebhookを設定します。これにより、新しい顧客が作成された際にメタフィールドを書き込むことができます。
- **既存顧客のバックフィル：** [Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、以前に作成された顧客のメタフィールドをバックフィルします。

#### ステップ4.2：external IDを取得するエンドポイントの作成 {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Brazeがexternal IDを取得するために呼び出せるパブリックエンドポイントを作成する必要があります。これは、Shopifyが`braze.external_id`メタフィールドを提供できないシナリオで必要です。

##### エンドポイントの仕様 {#endpoint-specifications}

**方法：** `GET`

| パラメーター | 説明 |
| --- | --- |
| `shopify_customer_id` | Shopify顧客ID。 |
| `email_address` | ログインユーザーのメールアドレス。 |
| `shopify_storefront` | リクエストのストアフロント。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### エンドポイントの例 {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### 期待されるレスポンス {#expected-response}

Brazeは`200`ステータスコードを期待します。その他のコードは失敗とみなされます。

{% raw %}
```json
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
`shopify_customer_id`と`email_address`がShopifyの顧客値と一致していることを検証することが重要です。[Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、これらのパラメーターを検証し、`braze.external_id`メタフィールドを取得できます。
{% endalert %}

#### ステップ4.3：external IDの入力 {#step-43-input-your-external-id}

[ステップ4](#step-4-choose-an-external-id-type)を繰り返し、Brazeのexternal IDタイプとしてカスタムexternal IDを選択した後、エンドポイントURLを入力します。

##### 考慮事項 {#considerations}

- Brazeがエンドポイントにリクエストを送信した際にexternal IDが生成されていない場合、`changeUser`関数が呼び出された際にShopify顧客IDがデフォルトとして使用されます。このステップは、匿名ユーザープロファイルと識別済みユーザープロファイルのマージに不可欠です。その結果、ワークスペース内に異なるタイプのexternal IDが一時的に存在する期間が発生する場合があります。
- `braze.external_id`メタフィールドでexternal IDが利用可能になると、連携はこのexternal IDを優先して割り当てます。
    - Shopify顧客IDが以前にBrazeのexternal IDとして設定されていた場合、`braze.external_id`メタフィールドの値に置き換えられます。

### ステップ5：Brazeアプリ埋め込みの有効化 {#step-5-enable-the-braze-app-embed}

ストアのテーマ内でBrazeアプリ埋め込みを有効にするには、Brazeに戻り、**Shopifyに移動**を選択します。

![Brazeアプリ埋め込みを有効にするボタンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

Shopifyサイトで、Brazeアプリ埋め込みを有効にし、変更を保存します。

![アプリ埋め込みの例。]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### ステップ6：アップグレードの確認 {#step-6-verify-the-upgrade}

Brazeに戻ると、Shopify連携のインストールが完了した際に通知されます。

![成功バナーが表示されたShopify連携ページ。]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

新しいShopifyコネクターが稼働していることを確認するには、以下をテストしてください。

- **アクティブなキャンバス、キャンペーン、セグメント：** 正常に機能していることを確認します。
- **ID管理プロセス：** これらのプロセスが期待どおりに動作していることを確認します。
- **SDKカスタマイズ（オプション）：** BrazeとShopifyの連携にカスタマイズ（カスタムイベントや属性のログ記録など）を行った場合、アップグレード後に正しく動作していることを確認します。
- **メールまたはSMSサブスクライバーの収集（オプション）：** 以前にメールまたはSMSサブスクライバーの収集を有効にしていた場合、アップグレード中にサブスクライバーの最新ステータスを反映する新しいデフォルトサブスクリプショングループが作成されます。デフォルトサブスクリプショングループの名前はShopifyストアフロントの名前になります。これらの新しいデフォルトサブスクリプショングループはアップグレード後約5時間で利用可能になり、アクティブなメッセージに追加する必要があります。

ご質問がある場合は、[サポートにお問い合わせ]({{site.baseurl}}/user_guide/administrative/access_braze/support)ください。