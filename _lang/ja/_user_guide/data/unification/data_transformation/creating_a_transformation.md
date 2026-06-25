---
nav_title: 変換の作成
article_title: 変換の作成
page_order: 1
page_type: reference
description: "このリファレンス記事では、Brazeデータ変換を使用して変換を作成するステップについて説明します。"
---

# 変換の作成 {#create-a-transformation}

> Brazeデータ変換を使用すると、Webhook連携の構築および管理を行って、外部プラットフォームからBrazeへのデータフローを自動化できます。これらのWebhook連携により、さらに洗練されたマーケティングユースケースを強化できます。データ変換は、デフォルトのコードから構築することも、専用のテンプレートライブラリーを使用して特定の外部プラットフォームとの連携を開始することもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| 2要素認証またはSSO | アカウントで[2要素認証]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#two-factor-authentication)（2FA）または[シングルサインオン]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#single-sign-on-sso-authentication)（SSO）を有効にする必要があります。 |
| 正しい権限 | アカウント管理者またはワークスペース管理者であるか、「変換の管理」ユーザー権限を持っている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1:ソースプラットフォームの特定 {#step-1-identify-a-source-platform}

Brazeに接続する外部プラットフォームを特定し、そのプラットフォームがWebhookに対応しているか確認します。これらの設定は、「API通知」や「Webサービスリクエスト」と呼ばれることもあります。

以下に[Typeform Webhook](https://www.typeform.com/help/a/webhooks-360029573471/)の例を示します。これは、Typeformのプラットフォームにログインすることで設定できます。

![Typeformプラットフォーム設定でのTypeform Webhookペイロードの例]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## ステップ2:変換の作成 {#step-2-create-a-transformation}

{% multi_lang_include create_transformation.md location="default" %}

## ステップ3:テストWebhookの送信（推奨） {#step-3-send-a-test-webhook-recommended}

このステップは任意ですが、新規に作成した変換にソースプラットフォームからテストWebhookを送信することをお勧めします。

1. 変換からURLをコピーします。
2. ソースプラットフォームで、このURLに送信するサンプルWebhookを生成する「テスト送信」機能を見つけます。
- ソースプラットフォームにリクエストタイプを求められた場合は、**POST** を選択します。
- ソースプラットフォームに認証オプションがある場合は、**No authentication** を選択します。
- ソースプラットフォームにシークレットを求められた場合は、**No secrets** を選択します。
3. Brazeダッシュボードでページを更新し、Webhookが受信されたか確認します。受信した場合は、**Most recent webhook** の下にWebhookペイロードが表示されます。

Typeformの場合は以下のようになります。

![WebhookをBrazeユーザープロファイルにマッピングするデータ変換コードの例]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Brazeデータ変換は、Webhookに特別な検証や認証を必要とする外部プラットフォームをまだサポートしていない可能性があります。Brazeデータ変換でこのタイプのプラットフォームを使用することに関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administer/personal/product_portal/)を残すことを検討してください。
{% endalert %}

## ステップ4:変換コードの記述 {#step-4-write-transformation-code}

JavaScriptコードの経験がほとんどないか、より詳しい手順を希望する場合は、**初心者 - POST:ユーザーの追跡**または**初心者 - PUT:複数のカタログ項目を更新する**タブに従って変換コードを記述してください。

開発者であるか、JavaScriptコードの経験が豊富な場合は、**上級 - POST:ユーザーの追跡**タブで、変換コードを記述するための大まかな手順を確認できます。

{% alert tip %}
AIで変換コードを生成するには、変換コードエディターの上にある**Code with Operator**を選択します。これを使用するには、変換にWebhookを送信する必要があります。ビルド済みテンプレートから開始するには、**Insert Template**を選択します。プロンプトの例については、[データ変換コードの生成]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-data-transformation-code)を参照してください。

**Code with Operator**は、アカウントでOperatorが有効になっている場合にのみ利用できます。表示されない場合は、アカウントマネージャーにお問い合わせください。
{% endalert %}

{% tabs %}
{% tab 初心者 - ユーザーの追跡 %}

ここでは、さまざまなWebhook値をBrazeユーザープロファイルにマッピングする方法を定義する変換コードを記述します。

1. 新しい変換には、**Transformation Code**セクションに次のデフォルトテンプレートがあります。

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. 変換呼び出しにカスタム属性、カスタムイベント、購入を含めるには、ステップ3に進みます。それ以外の場合は、不要なセクションを削除します。<br><br>
3. 属性、イベント、および購入の各オブジェクトには、`external_id`、`user_alias`、`braze_id`、`email`、または`phone`のいずれかのユーザー識別子が必要です。受信Webhookのペイロード内でユーザー識別子を見つけ、ペイロード行を介して変換コード内のその値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
4. 属性、イベント、または購入として表現するWebhookの値を見つけて、ペイロード行を介して変換コード内のそれらの値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
5. 属性、イベント、および購入の各オブジェクトについて、`_update_existing_only`の値を調べます。存在しない可能性のある新規ユーザーを変換で作成する場合は、この値を`false`に設定します。既存のプロファイルのみを更新する場合は、`true`のままにします。<br><br>
6. **Validate**をクリックして、コードの出力のプレビューを返し、受け入れられる`/users/track`リクエストであるかどうかを確認します。<br><br>
7. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Brazeアカウントマネージャーにお問い合わせください。<br><br>
7. ソースプラットフォームからWebhookの送信を開始します。Webhookが着信するたびに変換コードが実行され、ユーザープロファイルの更新が開始されます。

これでWebhook連携が完了しました。

{% endtab %}
{% tab 初心者 - カタログ項目の更新 %}

ここでは、さまざまなWebhookの値をBrazeカタログ項目の更新にどのようにマッピングするかを定義する変換コードを記述できます。

1. 新規の変換では、**Transformation Code**セクションに次のデフォルトテンプレートがあります。

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",

  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. `/catalogs`送信先の変換には、更新する特定のカタログを定義する`catalog_name`が必要です。このフィールドをハードコードするか、ペイロード行を介してWebhookフィールドでテンプレート化することができます。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
3. カタログのどの項目を更新するかを、items配列の`id`フィールドで定義します。これらのフィールドはハードコードするか、ペイロード行を介してWebhookフィールドでテンプレート化することもできます。<br><br>`catalog_column`はプレースホルダーの値であることに留意してください。項目オブジェクトには、カタログに存在するフィールドのみを含めるようにしてください。<br><br>
4. **Validate**を選択して、コード出力のプレビューを返し、[「複数のカタログ項目の更新」エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/)で受け入れ可能なリクエストであるかどうかを確認します。<br><br>
5. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Brazeアカウントマネージャーにお問い合わせください。<br><br>
6. ソースプラットフォームにWebhookの送信を開始する設定があるかどうかを確認してください。Webhookが着信するたびに変換コードが実行され、カタログ項目の更新が開始されます。

これでWebhook連携が完了しました。

{% endtab %}
{% tab 上級 - ユーザーの追跡 %}

このステップでは、Webhookペイロードをソースプラットフォームからのデータに基づいてJavaScriptオブジェクトの戻り値に変換します。この戻り値は、`/users/track`エンドポイントのリクエスト本文の形式に準拠している必要があります。

- 変換コードはJavaScriptプログラミング言語で記述します。if/elseロジックなど、標準的なJavaScript制御フローがすべてサポートされています。
- 変換コードは、`payload`変数を介してWebhookリクエスト本文にアクセスします。この変数は、リクエスト本文のJSONを解析して読み込まれたオブジェクトです。
- `/users/track`エンドポイントでサポートされるすべての機能がサポートされています。以下が含まれます。
  - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
  - ネストされた属性とネストされたカスタムイベントプロパティ
  - サブスクリプショングループの更新
  - 識別子としてのメールアドレス

**Validate**を選択すると、コードの出力のプレビューが返され、`/users/track`リクエストとして受け入れられるかどうかがチェックされます。

{% alert note %}
外部ネットワークリクエスト、サードパーティライブラリー、およびJSON以外のWebhookは現在サポートされていません。
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ5:変換の監視 {#step-5-monitor-your-transformation}

変換をアクティブにしたら、メインの**Transformations**ページの分析を参照して、パフォーマンスの概要を確認します。

* **Incoming Requests:** この変換のURLで受信したWebhookの数です。受信リクエストが0の場合、ソースプラットフォームがWebhookを送信していないか、接続を確立できません。
* **Deliveries:** 受信リクエストを受け取った後、データ変換は変換コードを適用して、選択されているBrazeの送信先に送信します。

受信リクエストの100%が配信に至ることが良い目標です。配信数が受信リクエスト数を超えることはありません。

### トラブルシューティング {#troubleshooting}

詳細な監視とトラブルシューティングについては、**Logs**ページで特定のログを参照してください。このページには、すべてのワークスペースのすべての変換に対する最新1,000件の受信リクエストが記録されます。各ログを選択すると、受信リクエストの本文、変換出力、および変換の送信先からの応答本文を表示できます。

配信がない場合は、変換コードに構文エラーがないかチェックし、コードがコンパイルされることを確認します。次に、出力が有効な送信先リクエストであるかどうかを確認します。

受信リクエスト数より少ない配信数は、少なくともいくつかのWebhookが正常に配信されていることを示します。エラー例については変換ログを参照し、変換出力が意図どおりかを確認してください。変換コードが、受信したWebhookのすべてのバリエーションに対応していない可能性があります。