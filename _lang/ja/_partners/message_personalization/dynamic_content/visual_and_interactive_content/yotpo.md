---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "このリファレンス記事では、BrazeとYotpoのパートナーシップについて概説しています。Yotpoはeコマースマーケティングプラットフォームのリーディングカンパニーで、何千もの先進的なブランドが消費者直販の成長を加速させるのを支援しています。"
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/) は大手eコマースマーケティングプラットフォームであり、何千もの先進的なブランドが消費者直販の成長を加速できるよう支援しています。Yotpoのシングルプラットフォームアプローチは、レビュー、ロイヤルティ、SMSマーケティングなどのデータドリブン型のソリューションを統合し、ブランドがよりスマートでコンバージョンの高いカスタマーエクスペリエンスを創造できるようにします。

_この統合はYotpoによって管理されます。_

## 統合について {#about-the-integration}

BrazeとYotpoの統合により、Braze内のメールやその他のコミュニケーションチャネルで、商品に関する星評価、トップレビュー、視覚的なユーザー生成コンテンツ（UGC）を動的に取得し、表示できます。また、顧客レベルのロイヤルティデータをメールやその他のコミュニケーション手段に組み込むことで、よりパーソナライズされたインタラクションを実現し、売上とロイヤルティを高めることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Yotpoアカウント | このパートナーシップを利用するには、Yotpoアカウントが必要です。 |
| YotpoレビューAPIキー | このAPIは、コネクテッドコンテンツのコードスニペット内に実装されます。<br><br>詳細については、[Yotpoアプリのキーとシークレットキーの確認方法](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key)を参照してください。 |
| YotpoロイヤルティAPIキー | このAPIキーとグローバル一意識別子（GUID）は、コネクテッドコンテンツのコードスニペット内に実装されます。<br><br>詳細については、[ロイヤルティ&リファーラルAPIキーとGUIDの確認方法](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

続行する前に、YotpoのプロダクトIDが、Brazeから動的に取得される `product_id` と同じであることを確認してください。これは統合が機能するために必須です。

YotpoプロダクトIDを確認するには、以下のステップを実行します。

1. ストアのWebサイトに移動します。
2. 製品ページを開きます。
3. 右クリックして**Inspect**を選択します。
4. <kbd>Control</kbd> + <kbd>F</kbd>キーを押し、コード内で `yotpo-main` を検索します。`data-product ID` 変数とその値がYotpo divに表示されます。

![Inspectでyotpo-mainを検索し、data-product ID変数を確認する]({% image_buster /assets/img/yotpo/image1.png %})

## 統合 {#integration}

YotpoとBrazeを統合するには、以下のステップを実行します。

1. Brazeのダッシュボードに移動します。
2. **キャンペーン**ページで**Create キャンペーン**をクリックし、**Email**を選択します。
3. 好みのテンプレートを選択します。
4. **Edit email body**をクリックし、ユースケースに応じた[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)のスニペットを追加します。
    - [製品の星評価とレビュー件数を表示する](#star-review-count)
    - [製品の最近の5つ星レビューを表示する](#five-star-review)
    - [製品別にビジュアルUGCを表示する](#visual-ugc)
    - [顧客のロイヤルティポイント残高をメールに表示する](#loyalty-balance)

### 商品の星評価とレビュー数を表示する {#star-review-count}

このスニペットを使って、メールに含まれる商品の公開平均スコアとレビュー総数を提供します。

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をお使いのYotpoレビューAPIキーに置き換えてください。`product_id` はBrazeから動的に取得されます。統合を機能させるには、Brazeの `product_id` がYotpoの製品ID（通常はeコマース親製品ID）と一致している必要があります。

![YOTPO-API-KEYをお使いのYotpoレビューAPIキーに置き換える]({% image_buster /assets/img/yotpo/image2.png %})

### 製品の最近の5つ星レビューを表示する {#five-star-review}

このスニペットを使って、メールに含まれる特定の商品のトップ（公開済み）レビューを提供します。

{% raw %}
`````````liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をお使いのYotpoレビューAPIキーに置き換えてください。`product_id` はBrazeから動的に取得されます。統合が機能するためには、Brazeの `product_id` がYotpoの製品ID（通常はeコマース親製品ID）と一致している必要があります。

メールエディターでのスニペットは次のようになります。

![最近の5つ星レビューのスニペットを表示するメールエディターの例]({% image_buster /assets/img/yotpo/image3.png %})

### 製品別にビジュアルUGCを表示する {#visual-ugc}

次のスニペットを使用して、タグ付けされ公開されたYotpo画像を取得し、ストック画像の代わりに、または追加のギャラリーとしてメールに追加します。

{% raw %}
`````````liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product:

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>` をお使いのYotpoレビューAPIキーに置き換えてください。`product_id` はBrazeから動的に取得されます。統合が機能するためには、Brazeの `product_id` がYotpoの製品ID（通常はeコマース親製品ID）と一致している必要があります。

スニペットは次のようになります。

![Yotpoで公開された画像のスニペットを表示するメールエディターの例]({% image_buster /assets/img/yotpo/image4.png %})

### 顧客のロイヤルティポイント残高をメールに表示する {#loyalty-balance}

次のスニペットを使用して、顧客のロイヤルティポイント残高を取得してメールメッセージに使用します。

{% raw %}
`````````liquid
{% connected_content

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

`<YOTPO-LOYALTY-GUID>` と `<YOTPO-LOYALTY-API-KEY>` をお使いのYotpoロイヤルティ認証情報に置き換えてください。`email_address` はBrazeから動的に取得されます。この統合が機能するためには、メールアドレスがこのメールを受信する顧客のメールアドレスと一致している必要があります。

スニペットは次のようになります。

![顧客ロイヤルティ残高のスニペットを表示するメールエディターの例]({% image_buster /assets/img/yotpo/image5.png %})

## よくある質問 {#faq}

### 5つ星レビューがない場合はどうなりますか？ {#what-if-i-dont-have-a-5-star-review}

5つ星のレビューがない場合（エンドポイントのレスポンスが5つ星のレビューに対してNULLを返した場合など）、コンテンツは表示されません。

### 商品の画像が公開されていない場合はどうなりますか？ {#what-if-i-dont-have-an-image-published-for-a-product}

商品の画像がない場合（エンドポイントのレスポンスが商品画像に対してNULLを返した場合など）、コンテンツは表示されません。

### ルック＆フィールをカスタマイズしたり、Yotpoから他のデータフィールドを取得したりできますか？ {#can-i-customize-the-look-and-feel-or-pull-other-data-fields-from-yotpo}

はい、できます。その他のデータポイントやカスタマイズオプションについては、[API呼び出しの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)を参照してください。そのためには、フロントエンド開発者の支援が必要になる場合があります。

{% alert note %}
Yotpoはこのガイドに記載されている以上のカスタム要件には対応していません。
{% endalert %}