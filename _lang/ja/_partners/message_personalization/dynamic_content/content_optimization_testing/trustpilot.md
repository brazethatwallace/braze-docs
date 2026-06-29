---
nav_title: Trustpilot
article_title: Trustpilot
description: このページでは、TrustpilotとBrazeを統合し、レビュー招待を送信し、製品レビューインサイトを使用してメッセージをパーソナライズする方法について説明します。
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/)は、顧客がフィードバックを共有し、レビューの管理と対応を行うためのオンラインレビュープラットフォームです。

このページでは、以下の手順について説明します。

* TrustpilotのCreate Invitation APIを使用したレビュー招待の作成
* TrustpilotのProduct Reviews APIを使用した製品レビューによるメッセージのパーソナライズ

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Trustpilotアカウント | TrustpilotのAPIへのアクセス権を持つTrustpilotアカウントが必要です。 |
| Trustpilot認証キー | APIキーを設定し、アクセストークンをリクエストする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1:Trustpilot APIの認証情報を取得する {#step-1-get-your-trustpilot-api-credentials}

1. 認証情報を使用して[Trustpilotにログイン](https://app.contentful.com/login)します。
2. Trustpilotダッシュボードで**Integrations** > **Developers** > **APIs**に移動し、APIキーとシークレットを作成または取得します。まだAPIキーがない場合は、新規作成します。
   1. **Application Name** > **Create Application**に移動します。
   2. APIキーとシークレットをコピーします。これらはコネクテッドコンテンツリクエストの認証に使用されます。

## Trustpilotレビュー招待の送信 {#sending-trustpilot-review-invitations}

### ステップ1:Braze Webhookキャンペーンを設定する {#step-1-set-up-a-braze-webhook-campaign}

アクションベースのBraze Webhookキャンペーンをセットアップして、Trustpilot APIをトリガーし、メールレビュー招待をユーザーに送信します。たとえば、ユーザーが注文した後に以下のWebhook詳細を使用してレビュー招待を送信できます。
   * [Webhook URL](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`
   * メソッド: POST
   * 関連する顧客情報をキーと値のペアとして追加します

### ステップ2:アクセストークンを取得する {#step-2-retrieve-the-access-token}

1. [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を使用して、[Trustpilotの認証エンドポイント](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..)にリクエストしてアクセストークンを取得します。
2. **client_credentials**グラントタイプを使用し、APIキーとシークレットをコネクテッドコンテンツタグに入力してトークンを取得します。コネクテッドコンテンツリクエストはリクエストヘッダーに入力できます。コネクテッドコンテンツは次のようになります。

{% raw %}

```liquid
{% connected_content
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3. アクセストークンをWebhookキャンペーンのリクエストヘッダーに追加します。

{% alert tip %}
詳細な手順については、[Trustpilotのドキュメント](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites)を参照してください。
{% endalert %}

## 製品レビューインサイトを使用したメッセージのパーソナライズ {#personalizing-messages-with-product-review-insights}

Brazeのキャンペーンで、Trustpilotの[製品レビューサマリー取得エンドポイント](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary)（{% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}）からデータをリクエストするコネクテッドコンテンツコールを実行します。このメソッドは、ビジネスユニットから特定のSKUの製品レビューを取得します。以下の例では、特定の製品SKUを指定し、5つ星レビューでフィルタリングしています。

{% raw %}
`````````liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Liquidを使用してメールに情報を取り込むコネクテッドコンテンツ。]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

コネクテッドコンテンツリクエストは製品レビューを返します。

{% raw %}
`````````liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2. Liquid構文を使用して、関連するコンテンツをメッセージに取り込みます。たとえば、製品レビューのコンテンツを取り込むには、Liquidタグ{% raw %}`{{result.productReviews[0].content}}`{% endraw %}を使用します。

![ユーザーがカートに入れたままにしていたおもちゃのトラックのレビューを含むパーソナライズされたメール。]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}