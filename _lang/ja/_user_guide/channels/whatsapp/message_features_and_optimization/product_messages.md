---
nav_title: 製品メッセージ
article_title: 製品メッセージ
page_order: 4
description: "このページでは、WhatsApp製品メッセージを使用して、Metaカタログの製品を紹介するインタラクティブなWhatsAppメッセージを送信する方法について説明します。"
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - キャンペーン
channel:
 - WhatsApp
---

# 製品メッセージ {#product-messages}

> 製品メッセージを使用すると、Metaカタログから直接製品を紹介するインタラクティブなWhatsAppメッセージを送信できます。

WhatsApp製品メッセージをユーザーに送信すると、ユーザーは以下のカスタマージャーニーをたどります。

1. ユーザーがWhatsAppで製品またはカタログメッセージを受信します。
2. ユーザーがWhatsAppから直接カートに製品を追加します。
3. ユーザーがWhatsAppで**Place order**をタップします。
4. Webサイトまたはアプリが Brazeからカートデータを受信し、チェックアウトリンクを生成します。
5. ユーザーがWebサイトまたはアプリに誘導され、チェックアウトを完了します。

ユーザーがカタログメッセージを通じてカートにアイテムを追加すると、Brazeはフォローアップアクション用のWebhookデータを受信します。

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| WhatsApp Businessアカウント | WhatsApp製品メッセージを使用するには、Brazeに接続されたWhatsApp Businessアカウントが必要です。 |
| Metaカタログ | Commerce ManagerでMetaカタログを設定する必要があります。 |
| 規約の遵守 | [Meta Commerce利用規約とポリシー](https://www.facebook.com/policies_center/commerce)に準拠する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## 製品メッセージタイプ {#product-message-types}

{% alert note %}
[製品メッセージの設定](#setting-up-product-messages)のステップ4でアクセスできる統合製品セレクターを使用して、製品メッセージ体験を強化できます。
{% endalert %}

{% tabs local %}
{% tab カタログメッセージ %}

カタログメッセージは、製品カタログ全体をインタラクティブな形式で表示します。[テンプレートメッセージおよび応答メッセージ](#building-a-product-message)として利用できます。

[設定](#setting-up-product-messages)時にBrazeへのカタログ権限を有効にしている場合、ユーザーに表示するサムネイルを選択できます。

{% alert note %}
カタログ接続はMetaによって管理され、製品カタログに継承されるため、Brazeで追加の製品選択を行う必要はありません。
{% endalert %}


{% endtab %}
{% tab マルチ製品メッセージ %}

マルチ製品メッセージは、カタログから特定の製品をハイライトし、1メッセージあたり最大30アイテムをハイライトできます。[テンプレートメッセージおよび応答メッセージ](#building-a-product-message)として利用できます。

製品をIDで手動選択するか、[設定](#setting-up-product-messages)時にカタログ権限を有効にしている場合はドロップダウン製品セレクターを使用できます。

{% alert important %}
Metaのマルチ製品メッセージテンプレートには、既知のヘッダー表示の問題があります。Metaはこの問題を認識しており、修正に取り組んでいます。
{% endalert %}

{% endtab %}
{% tab 単一製品 %}

単一製品メッセージは、製品カタログから1つの特定の製品をハイライトします。[応答メッセージ](#building-a-product-message)として利用できます。

製品をIDで手動選択するか、[設定](#setting-up-product-messages)時にカタログ権限を有効にしている場合はドロップダウン製品セレクターを使用できます。

{% endtab %}
{% endtabs %}

## 製品メッセージの設定 {#setting-up-product-messages}

1. [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#)で、[Metaの手順](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1)に従ってMetaカタログを作成します。Brazeに接続されたWhatsApp Businessアカウントが存在するMeta Business Portfolioと同じポートフォリオにいることを確認してください。
2. Metaの手順に従って、Meta Business Managerで「Manage Catalog」権限を割り当てることにより、[Metaカタログを接続](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715)してBrazeに接続されたWhatsApp Businessアカウントに紐付けます。

![「sweeney_catalog」というカタログの「Assign partner」ボタンを指す矢印が表示されたMetaの「Catalogs」ページ。]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

パートナービジネスIDとして、Braze Business Manager ID `332231937299182` を使用してください。

![パートナービジネスIDを入力するフィールドと「Manage catalog」権限を割り当てるフィールドを含む、パートナーとカタログを共有するウィンドウ。]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Metaカタログの設定を選択します。カタログメッセージを送信するには、**Show catalog icon in chat header**を選択する必要があります。

![「Catalog_products」カタログのWhatsApp Manager設定ページ。]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. Brazeで、[埋め込みサインアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)プロセスを実行して権限を付与します。権限を付与するカタログを**すべて**選択してください。これにより、Braze統合製品セレクターが有効になります。

![権限を付与するために5つのカタログが選択されたウィンドウ。]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Metaカタログ作成時のベストプラクティスについては、[Commerce Managerで高品質なカタログを構築するためのヒント](https://www.facebook.com/business/help/2086567618225367?id=725943027795860)を参照してください。
{% endalert %}

## 製品メッセージの作成 {#building-a-product-message}

製品メッセージは、WhatsAppテンプレートメッセージまたは応答メッセージを使用して作成できます。

{% tabs local %}
{% tab WhatsAppメッセージテンプレート %}

1. Meta Business Managerで、**Message Templates**に移動します。
2. フォーマットとして**Catalog**を選択し、**Catalog message**（カタログ全体を表示）または**Multi-product catalog message**（特定のアイテムをハイライト）を選択します。
3. Brazeで、WhatsApp キャンペーンまたはキャンバスメッセージステップを作成します。
4. テンプレートを送信したサブスクリプショングループと一致するものを選択します。
5. **WhatsApp Template Message**を選択します。
6. 使用するテンプレートを選択します。
    - マルチ製品テンプレートを選択した場合、ハイライトする製品のセクションタイトルとコンテンツIDを入力します。Meta Commerce ManagerからコンテンツIDを直接コピーするか、統合製品セレクターの権限を有効にしている場合はアイテムを選択できます。

![セクションタイトルとコンテンツIDを入力するフィールドを含むアイテムリスト。]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![選択可能なアイテムのドロップダウンを含むアイテムリスト。]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. メッセージの作成を続けます。

{% endtab %}
{% tab 応答メッセージ %}

1. Brazeで、WhatsApp キャンペーンまたはキャンバスメッセージステップを作成します。
2. サブスクリプショングループを選択します。
3. **Response Message**を選択します。
4. **Meta Product Messages**を選択します。

![「Response Message」と「Meta Product Messages」がハイライトされた、メッセージタイプと応答メッセージレイアウトを選択するオプション。]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. 使用する[メッセージタイプ](#product-message-types)を選択します。

![「Multi-product」のメッセージレイアウト選択。]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. メッセージの作成を続けます。

![製品情報が入力されたMeta製品メッセージの例。]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## 製品の管理 {#managing-products}

### Commerce Managerへのアクセス {#accessing-commerce-manager}

Meta Business Managerで、**Commerce Manager**に移動し、組織を選択します。ここでは、以下のようなカタログアセットを管理できます。
- 新しいカタログの作成
- 既存のカタログへの製品の追加
- 製品情報の更新
- 廃止アイテムの削除

{% alert important %}
カタログから参照されている製品を削除すると、関連するメッセージの送信に失敗します。
{% endalert %}

## インバウンド製品質問の受信 {#receiving-inbound-product-questions}

ユーザーは、製品またはカタログメッセージに対して製品に関する質問で応答できます。これらはインバウンドメッセージとして届き、[アクションパス]({{site.baseurl}}/action_paths)で分類できます。

さらに、Brazeはこれらの質問から製品IDとカタログIDを抽出するため、応答を自動化したり、質問を別のチーム（カスタマーサポートなど）に送信したりする場合に、それらの詳細を含めることができます。たとえば、WhatsAppプロパティの`inbound_product_id`や`inbound_catalog_id`を使用して応答をパーソナライズできます。

![パーソナライゼーションタイプが「WhatsApp Properties」で、属性「inbound_product_id」がハイライトされた「Add Personalization」ウィンドウ。]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## チェックアウト：カート処理とWebhook {#checkout-cart-processing-and-webhooks}

ユーザーがWhatsApp製品メッセージを操作すると、製品を閲覧してカートにアイテムを追加できます。ただし、現在、配送情報や決済処理のための組み込みチェックアウト機能はありません。代わりに、独自のアプリまたはWebサイト内にカートを作成し、カスタムリンクを使用してユーザーをそのカートに誘導することをお勧めします。

### 考慮事項 {#considerations}

- **アプリ内チェックアウトなし：** ユーザーはWhatsApp内で直接購入を完了できません。すべての取引はWebサイトまたはアプリにリダイレクトする必要があります。
- **カスタムリンクが必要：** プラットフォーム上のカートにユーザーを誘導するカスタムリンクを作成する必要があります。
- **手動設定：** 設定プロセスでは、カートとメッセージングワークフローの手動設定が必要です。

{% alert note %}
現在、WhatsApp内で直接決済を行うことはサポートされていません。将来のサポートは国ごとに異なります（現在、Metaはインド、ブラジル、シンガポールに拠点を置き、それらの国のユーザーと直接取引する企業にのみ提供しています）。
{% endalert %}

### カートイベントトリガーの設定 {#setting-up-cart-event-triggers}

顧客がWhatsAppで注文すると、Brazeは自動的に以下を行います。
1. WhatsAppからカートの内容（製品ID、数量、その他の注文データ）を受信します。
2. `source = whats_app`を含むすべての関連データを持つ`ecommerce.cart_update` eコマースイベントを作成します。
3. 応答をトリガーし、注文に応答する自動キャンペーンを設定できるようにします。

`ecommerce.cart_update` eコマースイベントは、イベントが送信された後にのみBrazeにリストされます。これは、Brazeからテスト製品メッセージを生成し、カートイベントを送信することで実行できます。
カートイベントには以下が含まれます。

- **カートID：** カートの一意の識別子
- **製品：** 製品ID、数量、価格を含むアイテムのリスト
- **合計金額：** すべてのアイテムの合計
- **通貨：** カートの通貨
- **ソース：** 「whats_app」としてマーク
- **メタデータ：** カタログIDやメッセージテキストなどの追加データ

Brazeカートイベントの追加情報については、[eコマース推奨イベントのタイプ]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events)を参照してください。

### トリガー応答の設定 {#setting-up-a-triggered-response}

1. `ecommerce.cart_updated`のカスタムイベントトリガーを作成します。
2. `source = "whats_app"`のプロパティフィルターを追加します。

![基本プロパティ「source」が`whats_app`に等しい`ecommerce.cart_updated`カスタムイベントトリガーのキャンバスステップ。]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. カートデータに基づいてフォローアップアクションを設定します。

### 推奨チェックアウト実装 {#recommended-checkout-implementations}

{% tabs local %}
{% tab シンプルなLiquidベースのカートリンク %}

Liquidを使用して、応答メッセージ内で直接カートURLを構築します。WhatsAppとeコマースプラットフォーム間で一貫した製品IDがある場合に最適です。

#### Liquidの例 {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### 設定 {#setup}

1. `ecommerce.cart_update` eコマースイベントをトリガーとするWhatsApp応答メッセージキャンペーンを作成します。
2. カートURLを含む後続メッセージを作成します。
3. LiquidでカートURLを構築します。Shopifyを使用している場合は、上記のLiquidの例を使用して[カートパーマリンクを作成](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks)できます。

![Liquid生成カートのチェックアウト体験ワークフローを示す図：Metaが注文受信メッセージをBrazeに送信し、アクションベースのトリガーが発動してカートリンク付きメッセージを作成し、WhatsAppメッセージを送信します。]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab コネクテッドコンテンツ %}

eコマースシステムにAPI呼び出しを行い、パーソナライズされたチェックアウトURLを生成します。動的なカートURL生成や複雑な製品マッピングが必要な場合に最適です。

#### 設定

1. [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated) eコマースイベントによってトリガーされるWebhook キャンペーンまたはキャンバスステップを作成し、カートデータをeコマースシステムに送信します。
2. 同じeコマースイベントによってトリガーされるWhatsApp キャンペーンまたはキャンバスメッセージステップを作成し、カートURL付きのWhatsApp応答メッセージをユーザーに送信します。後続の応答メッセージの指示に従い、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用してください。

![コネクテッドコンテンツ呼び出しのチェックアウト体験ワークフローを示す図：Metaが注文受信メッセージをBrazeに送信し、Brazeがeコマースプラットフォームと双方向の呼び出しを行い、WhatsAppメッセージを送信します。]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhookとカスタムイベント %}

Webhookを使用してカートデータをシステムに送信し、カスタムイベントを通じてフォローアップメッセージをトリガーします。広範なカート処理やマルチステップワークフローを必要とする複雑な統合に最適です。

#### 設定

`ecommerce.cart_update` eコマースイベントによってトリガーされるWebhook キャンペーンまたはキャンバスステップを作成し、カートデータをeコマースシステムに送信します。APIは以下を行います。
1. カートデータを受信する
2. システム内にカートを作成する
3. チェックアウトURLを生成する
4. Brazeに`checkout_started`イベントを送信し、チェックアウトリンク付きのWhatsAppメッセージの送信をトリガーする

![Webhookとカスタムイベントのチェックアウト体験ワークフローを示す図：Metaが注文受信メッセージをBrazeに送信し、Brazeがeコマースプラットフォームと双方向の呼び出しを行い、カートURL付きのWhatsAppメッセージを送信します。]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## テストと検証 {#testing-and-validation}

### テストメッセージの要件 {#test-message-requirements}

カート機能はテストメッセージ間で引き継がれますが、インバウンド結果の処理は引き継がれません。

### メッセージプレビュー {#message-preview}

- 製品画像と詳細はMetaカタログから取得されます。
- インタラクティブプレビューは、統合が完了するまでプレースホルダーを表示します。

### エラーコード {#error-codes}

- 製品IDがカタログに存在しない場合、エラー`product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`が返されます。
- カタログがWABAから切断されている場合、エラー`Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`が返されます。