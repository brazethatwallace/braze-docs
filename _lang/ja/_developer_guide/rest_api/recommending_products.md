---
nav_title: ユーザーに製品をおすすめする
article_title: ユーザーに製品をおすすめする
page_order: 4
page_type: reference
description: "この参照記事では、Braze REST API、カタログ、コネクテッドコンテンツを使用して、メッセージングチャネル全体でユーザーに製品をおすすめする方法を説明します。"
---

# ユーザーに製品をおすすめする {#recommending-products-to-users}

> Braze REST APIを[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/create)や[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)と組み合わせて使用し、パーソナライズされた製品おすすめをメッセージに表示できます。このアプローチにより、独自のレコメンデーションエンジンをBrazeのメッセージングエコシステムに接続でき、技術者でないユーザーでも各おすすめに関するコンテンツやメッセージングを管理できます。

このアプローチでは、以下のことが可能です。

- REST APIを使用して、バックエンドからユーザープロファイルに製品おすすめを保存する。
- 送信時にカタログまたはコネクテッドコンテンツを使用して製品メタデータを取得する。
- メール、プッシュ、アプリ内メッセージなど、あらゆるメッセージングチャネルでパーソナライズされたおすすめを表示する。

## 前提条件 {#prerequisites}

このガイドを完了するには、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Braze REST APIキー | `users.track` 権限を持つキー。APIを介してカタログを管理する場合は、関連するカタログ権限も必要です。作成するには、**設定** > **APIキー**に移動してください。 |
| Brazeカタログ | 商品メタデータ（名前、カテゴリ、価格、画像URLなど）を含むカタログ。作成するには、[カタログを作成する]({{site.baseurl}}/user_guide/data/activation/catalogs/create)を参照してください。 |
| Liquidの知識 | パーソナライズされた変数のテンプレート化やConnected Contentの使用に関する[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)の中級レベルの知識。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1: ユーザープロファイルにレコメンデーションを保存する {#step-1-store-recommendations-on-user-profiles}

まず、レコメンデーションエンジンが生成した商品レコメンデーションを、Brazeユーザープロファイルにカスタム属性として保存します。これにより、メッセージ送信時に各ユーザーのおすすめ商品を参照できます。

1. 商品IDや好みのカテゴリなど、保存するレコメンデーションデータを決定します。
2. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを使用して、レコメンデーションをユーザープロファイルのカスタム属性として書き込みます。

### リクエスト例 {#example-request}

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT` を、ワークスペースの [REST エンドポイントURL]({{site.baseurl}}/api/basics#endpoints) に置き換えてください。

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

後でLiquidテンプレートで参照しやすいように、わかりやすい属性名（`recommended_product_id` など）を使用してください。レコメンデーションエンジンが新しい結果を生成するたびに定期的に更新し、レコメンデーションを最新の状態に保ちましょう。

## ステップ2: 商品メタデータを取得する {#step-2-retrieve-product-metadata}

各ユーザープロファイルにレコメンデーション識別子を保存した後、メッセージに含めるために完全な商品メタデータ（名前、価格、画像など）を取得する必要があります。2つのオプションがあります。

- **オプションA:** [Brazeカタログ](#option-a-braze-catalogs) — 商品情報をBrazeに直接保存し、高速な組み込みルックアップを行います。
- **オプションB:** [Connected Content](#option-b-connected-content) — 送信時に外部APIから商品情報を取得します。

### オプションA: Brazeカタログ {#option-a-braze-catalogs}

商品インベントリで[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/create)を作成している場合、Liquidを使用してメッセージ内で直接アイテムを検索できます。完全なウォークスルーについては、[カタログの使用]({{site.baseurl}}/user_guide/data/activation/catalogs/use)を参照してください。

#### 特定のカタログアイテムをレコメンドする {#recommend-a-specific-catalog-item}

{% raw %}
特定の商品をIDで参照するには、`catalog_items` Liquidタグを使用します。たとえば、`retail_products`という名前のカタログから商品`1001`をレコメンドするには：

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### 複数のカタログアイテムをレコメンドする {#recommend-multiple-catalog-items}

{% raw %}
1つのタグで複数のアイテムを参照することもできます。たとえば、3つの商品を紹介するには：

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### ユーザーのレコメンデーションを使用してアイテムをテンプレート化する {#template-items-using-a-users-recommendation}

{% raw %}
[ステップ1](#step-1-store-recommendations-on-user-profiles)のカスタム属性とカタログルックアップを組み合わせて、各ユーザーに合わせたレコメンデーションをパーソナライズします：

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### オプションB: Connected Content {#option-b-connected-content}

商品メタデータがBrazeカタログではなく外部サービスにある場合は、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を使用して送信時に取得します。

{% raw %}
たとえば、内部APIがIDで商品詳細を返す場合：

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

メッセージからのAPI呼び出しの詳細については、[API呼び出しを行う]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照してください。

{% alert warning %}
Connected Contentを使用して大量の商品リストを取得し、送信時にLiquidでそのリストを反復処理することは避けてください。大きなレスポンスペイロードは送信レイテンシを増加させ、大規模な配信ではメッセージのタイムアウトや配信失敗を引き起こす可能性があります。代わりに、ユーザーが必要とする特定の商品IDのみをプロファイルに保存し（[ステップ1](#step-1-store-recommendations-on-user-profiles)を参照）、それらの個別アイテムのメタデータを取得するか、高速なルックアップに最適化された[カタログ](#option-a-braze-catalogs)を使用してください。
{% endalert %}

## ステップ3: インテグレーションを確認する {#step-3-verify-your-integration}

設定が完了したら、インテグレーションを確認します。

1. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを使用して、自分のユーザープロファイルにテストレコメンデーションを書き込みます。
2. カタログまたはConnected Contentを使用して、レコメンドされた商品を参照するテストメッセージを送信します。
3. 配信されたメッセージで商品の詳細が正しく表示されることを確認します。
4. Brazeダッシュボードで、キャンペーンまたはキャンバスの結果ページに移動し、送信が記録されていることを確認します。

## 考慮事項 {#considerations}

- レコメンデーションエンジンが新しい結果を生成するたびに、カスタム属性を定期的に更新してレコメンデーションデータの正確性を維持してください。
- Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)を活用して、商品の詳細にユーザー固有のデータを組み合わせるなど、メッセージをさらにカスタマイズすることを検討してください。
- [APIトリガー配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)を使用して、Brazeダッシュボードで定義したテンプレートを使ってバックエンドからメッセージをトリガーすることを検討してください。