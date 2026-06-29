---
nav_title: Algolia
article_title: Algolia
description: "AlgoliaとBrazeのコネクテッドコンテンツを使用して、パーソナライズされた検索結果や商品レコメンデーションをBrazeメッセージに動的に配信する方法を説明します。"
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> [Algolia](https://www.algolia.com/)は、開発者が高速で関連性の高いスケーラブルな検索体験を構築するための検索・ディスカバリープラットフォームです。強力なAPIファーストのアプローチにより、Algoliaは高度なランキングアルゴリズムとAI駆動のインサイトを組み合わせ、シームレスなサイト検索、ナビゲーション、パーソナライズされたコンテンツディスカバリーを実現します。

AlgoliaとBrazeの統合では、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を使用して、Algoliaを活用した検索結果や商品レコメンデーションをBrazeメッセージに反映します。送信時にAlgoliaのAPIにクエリを実行することで、ユーザーを高コンバージョンの商品詳細ページやランディングページに誘導するパーソナライズされたコンテンツを配信できます。

## ユースケース {#use-cases}

- **トレンド商品のプロモーション:** Algoliaからトレンドまたはパフォーマンスの高い商品を自動的にBrazeメッセージに取り込み、注目度の高いアイテムをプロモーションしてエンゲージメントを向上させます。
- **検索インテリジェンスによるキャンペーンのパーソナライズ:** Algoliaの検索・閲覧インテリジェンスを活用してBraze キャンペーンをパーソナライズし、各ユーザーの興味に合った商品やカテゴリを配信します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|-------------|-------------|
| Algoliaアカウント | このパートナーシップを利用するにはAlgoliaアカウントが必要です。 |
| Algolia API認証情報 | AlgoliaのAPIキーとアプリケーションID。 |
| Algolia商品インデックス | 商品データが登録されたAlgoliaインデックス。Search APIまたはRecommend APIを使用するために必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ 1: Algolia APIリクエストを設定する {#step-1-set-up-your-algolia-api-request}

リクエスト形式、レスポンス構造、使用方法の詳細については、[Algolia Search API](https://www.algolia.com/doc/rest-api/search)および[Algolia Recommend API](https://www.algolia.com/doc/rest-api/recommend)のドキュメントを参照してください。設定についてサポートが必要な場合は、Algoliaチームにお問い合わせください。

{% tabs local %}
{% tab Search API %}

#### Search APIリクエストの例 {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### クエリペイロードの例 {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

この例では、`category_page_id`という属性に基づくカテゴリフィルターを使用するページから上位4件の結果を取得するクエリを実行します。`attributesToRetrieve`パラメーターはレスポンスを制限し、ペイロードを管理しやすいサイズに保ちます。

**ユースケースの例:** 週間オファーのBraze キャンペーンで`https://www.yoursite.com/weekly-offers`の検索結果を表示するには、対応するAlgoliaインデックスにクエリを実行し、フィルターを適用してそのページの上位結果を取得します。

{% alert tip %}
`attributesToRetrieve`を使用して、評価、レビュー、割引などの追加フィールドを取得し、パーソナライゼーションを強化できます。
{% endalert %}

{% endtab %}
{% tab Recommend API %}

#### Recommend APIリクエストの例 {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### クエリペイロードの例

```json
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
```

Recommend APIは、**Frequently Bought Together**、**Related Products**、**Trending Items**、**Trending Facet Values**、**Looking Similar**など、複数のモデルをサポートしています。この例では**Trending Items**モデルを使用しています。

{% alert important %}
レコメンデーションがユーザー固有の属性やobjectIDに依存する場合は、Algolia契約で定義されたレート制限に注意してください。ベストプラクティスについては[考慮事項](#considerations)セクションを参照してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 2: Brazeコネクテッドコンテンツを実装する {#step-2-implement-braze-connected-content}

Brazeのコネクテッドコンテンツ機能を使用して、AlgoliaエンドポイントへのAPI呼び出しを行い、レスポンスをメッセージに動的に挿入します。設定、リクエスト形式、ベストプラクティスの詳細については、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を参照してください。

{% tabs local %}
{% tab Search API %}

#### コネクテッドコンテンツSearchリクエストの例 {#example-connected-content-search-request}

{% raw %}
`````````liquid
{% capture request_body %}
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
  :method post
  :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_search
%}
```
{% endraw %}

{% endtab %}
{% tab Recommend API %}

#### コネクテッドコンテンツRecommendリクエストの例 {#example-connected-content-recommend-request}

{% raw %}
`````````liquid
{% capture request_body %}
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
  :method post
  :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_recommendations
%}
```
{% endraw %}

{% endtab %}
{% endtabs %}

### ステップ 3: Brazeメッセージで検索結果をフォーマットする {#step-3-format-search-results-in-braze-messages}

Algoliaから結果を取得した後、Liquidを使用してAPIレスポンスを解析し、メッセージ内に結果を動的にレンダリングします。

{% tabs local %}
{% tab Search API %}

#### Search API用のLiquidメールテンプレートの例 {#example-liquid-email-template-for-search-api}

{% raw %}
`````````liquid
{% for item in algolia_search.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

これにより、メッセージ本文内にSearch APIの結果から商品リストが生成されます。各商品リンクは、ユーザーを商品詳細ページ（PDP）またはキャンペーン固有のランディングページに誘導します。

{% endtab %}
{% tab Recommend API %}

#### Recommend API用のLiquidメールテンプレートの例 {#example-liquid-email-template-for-recommend-api}

{% raw %}
`````````liquid
{% for item in algolia_recommendations.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

これにより、メッセージ本文内にRecommend APIの結果からおすすめ商品リストが生成されます。各商品リンクは、ユーザーを商品詳細ページ（PDP）またはキャンペーン固有のランディングページに誘導します。

{% endtab %}
{% endtabs %}

## 考慮事項 {#considerations}

### ユニーククエリの回避 {#avoiding-unique-queries}

Algolia契約で定義されたレート制限に注意してください。ユーザー固有のクエリは、割り当てられたリクエスト数をすぐに超過する可能性があるため、避けてください。結果をパーソナライズするには、個々のユーザーIDではなくセグメントをターゲットにするか、特定のobjectIDではなくカテゴリやブランドでフィルタリングしてください。Brazeの属性を使用してレコメンデーションをさらにパーソナライズできます。

### コネクテッドコンテンツ結果のキャッシュ {#caching-connected-content-results}

`cache_max_age`を使用してコネクテッドコンテンツの結果をキャッシュし、AlgoliaへのAPIリクエストを最小限に抑えてパフォーマンスを向上させます。詳細については、[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/)を参照してください。