---
nav_title: Shopifyのアップグレード（カスタム）
article_title: "カスタムShopify連携のアップグレード"
description: "BrazeのカスタムShopify連携をアップグレードする方法を説明します。"
page_type: partner
search_tag: Partner
permalink: "/shopify_custom_upgrade/"
hidden: true
---

# Shopify連携のアップグレード（カスタム） {#upgrading-your-shopify-integration-custom}

> BrazeのカスタムパスでShopify連携をアップグレードする方法を説明します。最高のエクスペリエンスを提供するため、すべてのShopify連携は2025年8月28日までに最新バージョンへの[アップグレード]({{site.baseurl}}/shopify)が必要です。このアップグレードは、Shopifyの技術における重要な変更が連携の機能に影響を与えるため、不可欠です。

## 対象となるのは？ {#whos-eligible}

このアップグレードパスは、Shopifyヘッドレスまたは Shopify Hydrogen ストアを持つブランドを対象としています。

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## アップグレード要件 {#upgrade-requirements}

開始する前に、以下を確認してください。

| 要件           | 説明 |
|-----------------------|-------------|
| **重要な変更点**  | レガシーコネクターから新しいコネクターへの重要な変更点をすべて確認してください。詳細は[Shopifyアップグレードの概要]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)を参照してください。 |
| **アップグレードの前提条件** | 開発チームとマーケティングチームと連携して、必要な[アップグレードの前提条件]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites)をすべて完了してください。Shopifyヘッドレスストアを Braze でアップグレードするには、次の2つの重要なステップを完了する必要があります。<br><br>- Braze Web SDKを初期化して読み込み、オンサイトトラッキングを有効にする<br>- 製品内のアップグレードエクスペリエンスを通じて既存のストアをアップグレードする |
| **破壊的変更**  | Braze でフラグが立てられたすべての破壊的変更を確認し、修正してください。完全なウォークスルーについては、[破壊的変更の修正](#fixing-breaking-changes-fixing-breaking-changes)に進んでください。 |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## 破壊的変更の修正 {#fixing-breaking-changes}

Brazeで、**パートナー連携** > **Shopify**に移動し、**アップグレードを開始**を選択します。

![アップグレードを開始するオプションがあるパネル。]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Shopifyデータを使用している影響を受けるキャンバス、キャンペーン、セグメントにフラグが立てられます。

![破壊的変更の影響を確認するためのモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

ほとんどのイベントでは、「OR」オペレーターを使用して新しい必須Shopifyイベントと属性を含め、アクティブなメッセージのスムーズなアップグレードを促進することをお勧めします。より具体的なケースについては、以下を参照してください。

{% tabs local %}
{% tab 放棄カート %}
放棄カートメッセージングでは、以下を含む新しい放棄カートキャンバステンプレートを使用する必要があります。

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab 放棄チェックアウト %}
放棄チェックアウトメッセージングでは、以下を含む新しい放棄チェックアウトキャンバステンプレートを使用する必要があります。

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

連携を通じて利用可能な新しいeコマースキャンバステンプレートと製品パーソナライゼーション用の事前定義されたHTMLブロックの完全なリストについては、[キャンバスユーザージャーニーの作成]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys)を参照してください。

{% alert important %}
Shopify連携で廃止されたイベントを使用するアクティブなメッセージを考慮しない場合、影響を受けるメッセージは顧客に送信されなくなります。
{% endalert %}

詳細については、[サポートされているShopifyイベント]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events)を確認してください。
{% endtab %}

{% tab サブスクライバーリスト %}
連携を通じてShopifyからメールまたはSMSサブスクライバーを収集している場合、アクティブなメッセージにShopifyストアの対応するサブスクライバーリストが含まれていることを確認してください。

アップグレードが完了すると、連携用の新しいデフォルト購読グループが作成されます。これらをアクティブなメッセージングの一部として活用する必要があります。変更の詳細については、[サブスクライバーの収集]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)を参照してください。
{% endtab %}
{% endtabs %}

## Shopifyのアップグレード {#upgrading-shopify}

{% alert important %}
アップグレードを開始する前に、すべての[互換性のない変更を修正](#fixing-breaking-changes)することが不可欠です。
{% endalert %}

### ステップ1: Braze Web SDKを初期化して読み込み、オンサイトトラッキングを有効にする {#step-1}

まだ行っていない場合は、Braze Web SDKを初期化して読み込み、オンサイトトラッキングを有効にします。完全なウォークスルーについては、[Shopifyカスタム連携の設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1)を参照してください。
- Braze Webアプリを作成する
- サブドメインと環境変数を追加する
- オンサイトトラッキングを有効にする
- Shopifyアカウントログインイベントを追加する
- 「商品閲覧」と「カート更新」イベントのトラッキングを追加する

### ステップ2: アップグレードを開始する {#step-2-start-the-upgrade}

Brazeで、**パートナー連携** > **Shopify** に移動し、**Start upgrade** を選択します。

![アップグレードを開始するオプションがあるパネル。]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

チェックボックスをオンにしてアップグレードガイドラインに同意し、**Start the upgrade** を選択します。

![アップグレードにより互換性のない変更が発生する可能性があることを理解していることを確認するモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

開発者と確認して、カスタムパスアップグレードのステップ1が完了したことをチェックボックスをオンにして確認し、**Confirm** を選択します。

![ステップ1～5が完了したことを確認するチェックボックスがあるモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
連携が正しく動作するためには、カスタムアップグレードの[ステップ1](#step-1)を完了してください。このステップを省略すると、連携が正しく機能しない場合があります。
{% endalert %}

### ステップ3: Brazeアプリを再認証する {#step-3-reauthorize-the-braze-app}

Brazeアプリを再認証するには、**Go to Shopify** を選択します。

![Shopifyに移動するオプションがあるパネル。]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

Shopifyサイトで、プロンプトに従ってBrazeアプリを再認証します。これにより、BrazeがShopifyデータにアクセスできるようになります。

{% alert important %}
再認証プロセスには数分かかる場合がありますが、完了するとShopifyページに自動的に更新が反映されます。
{% endalert %}

![「Brazeアプリを再認証」の横にスピニングアイコンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### ステップ4: external IDタイプを選択する {#step-4-choose-an-external-id-type}

選択したexternal IDタイプは、Shopifyアカウントが作成されたとき、または注文が行われたときに、新しいShopify顧客プロファイルに割り当てられます。また、既存のユーザープロファイルがShopify顧客IDエイリアスを持っているがBrazeでexternal IDが割り当てられていない場合、そのプロファイルの更新にも使用されます。

external IDタイプを選択するには、Brazeに戻って **Confirm external ID** を選択します。

![external IDを確認するボタンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

ワークスペースのShopify連携に使用するexternal IDを選択します。完了したら、**Set external ID** を選択します。

![external IDを選択するドロップダウンがあるモーダル。]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
デフォルトでは、BrazeはShopifyからのメールアドレスをexternal IDとして使用する前に自動的に小文字に変換します。メールアドレスまたはハッシュ化されたメールアドレスをexternal IDとして使用している場合、external IDとして割り当てる前、または他のデータソースからハッシュ化する前に、メールアドレスも小文字に変換されていることを確認してください。これにより、external IDの不一致を防ぎ、Brazeで重複するユーザープロファイルが作成されるのを回避できます。
{% endalert %}

カスタムexternal IDタイプを選択した場合は、ステップ4.1～4.3に進みます。それ以外の場合は、ステップ5に進みます。

#### ステップ4.1: `braze.external_id` メタフィールドを作成する {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

メタフィールドを作成したら、顧客のメタフィールドにデータを入力します。以下のアプローチをお勧めします。

- **顧客作成webhookをリッスンする:** [`customer/create` イベント](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)をリッスンするwebhookを設定します。これにより、新しい顧客が作成されたときにメタフィールドを書き込むことができます。
- **既存の顧客をバックフィルする:** [Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、以前に作成された顧客のメタフィールドをバックフィルします。

#### ステップ4.2: external IDを取得するエンドポイントを作成する {#step-42-create-an-endpoint-to-retrieve-your-external-id}

BrazeがextEID を取得するために呼び出せるパブリックエンドポイントを作成する必要があります。これは、Shopifyが `braze.external_id` メタフィールドを提供できないシナリオに必要です。

##### エンドポイントの仕様 {#endpoint-specifications}

**メソッド:** `GET`

| パラメーター | 説明 |
| --- | --- |
| `shopify_customer_id` | Shopify顧客ID。 |
| `email_address` | ログイン中のユーザーのメールアドレス。 |
| `shopify_storefront` | リクエストのストアフロント。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### エンドポイントの例 {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### 期待されるレスポンス {#expected-response}

Brazeは `200` ステータスコードを期待します。その他のコードは失敗と見なされます。

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

{% alert important %}
`shopify_customer_id` と `email_address` がShopifyの顧客値と一致することを検証することが重要です。[Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、これらのパラメーターを検証し、`braze.external_id` メタフィールドを取得できます。
{% endalert %}

#### ステップ4.3: external IDを入力する {#step-43-input-your-external-id}

[ステップ4](#step-4-choose-an-external-id-type)を繰り返し、BrazeのextEIDタイプとしてカスタムexternal IDを選択した後、エンドポイントURLを入力します。

##### 考慮事項 {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### ステップ5: Brazeアプリ埋め込みを有効にする {#step-5-enable-the-braze-app-embed}

ストアのテーマ内でBrazeアプリ埋め込みを有効にするには、Brazeに戻り、**Go to Shopify** を選択します。

![Brazeアプリ埋め込みを有効にするボタンがあるShopifyアップグレードパネル。]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

Shopifyサイトで、Brazeアプリ埋め込みを有効にし、変更を保存します。

![アプリ埋め込みの例。]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### ステップ6: アップグレードを確認する {#step-6-verify-the-upgrade}

Brazeに戻ると、Shopify連携のインストールが完了したときにアラートが表示されます。

![成功バナーが表示されたShopify連携ページ。]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

新しいShopifyコネクターが稼働していることを確認するには、以下をテストしてください。

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

ご質問がある場合は、[サポートにお問い合わせください]({{site.baseurl}}/user_guide/administer/personal/braze_support)。