---
nav_title: Contentful
article_title: Contentful
description: "このリファレンス記事では、BrazeとContentfulの連携について説明します。Contentfulは、コネクテッドコンテンツを動的に使用してContentfulからBraze キャンペーンにコンテンツをプルできるコンテンツ管理システムです。"
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) は、コンテンツの作成、管理、およびあらゆるプラットフォームへの配信を可能にするヘッドレスのコンテンツ管理システムです。コンテンツ管理システム (CMS) とは異なり、Contentfulではコンテンツモデルを作成できるため、どのコンテンツを管理するかを決めることができます。<br><br>このページでは、ContentfulのContent Delivery APIからデータを取得するようにBrazeコネクテッドコンテンツを設定する手順について説明します。

統合後は、ContentfulのRESTful APIを使用して、Webサイト、モバイルアプリ（iOS、Android、およびWindows）、その他の多くのプラットフォームなど、複数のチャネルにわたってコンテンツを配信できます。また、Contentfulからコンテンツをダイナミックにプルして、Braze キャンペーンで使用することもできます。

## 前提条件 {#prerequisites}

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
|-----------------------|------------------------------------|
| Contentfulアカウント | Content Delivery APIにアクセスできるContentfulアカウントが必要です。 |
| Brazeアカウント | コネクテッドコンテンツ機能にアクセスできるBrazeアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1:Contentful API認証情報を取得する {#step-1-get-your-contentful-api-credentials}

1. 認証情報を使って[Contentfulにログイン](https://app.contentful.com/login)します。
2. Contentfulダッシュボードの**Settings** > **API keys**でAPIアクセストークンを作成または取得します。APIキーをまだ持っていない場合は、新規に作成します。<br>2.1 **Add API key**を選択します。<br>2.2 必要な詳細を入力し、適切な環境を選択します。<br>2.3 **Save**を選択し、**Space ID**と**Content Delivery API - access token**をメモします。
3. Contentful APIを使用してアクセスするコンテンツモデルを特定します。

### ステップ2:Brazeコネクテッドコンテンツを設定する {#step-2-configure-braze-connected-content}

1. 認証情報を使って[Brazeにログイン](https://dashboard.braze.com/sign_in)します。
2. Brazeダッシュボードで、**Content** > **Content Block** > **Create Content Block** > **HTML code editor**の順に移動します。
3. Contentfulの[Contentful Content Delivery API URL](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links)に対してコネクテッドコンテンツリクエストを作成します。Contentful Content Delivery API URLの例は`https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries`です。<br><br> 異なるアセットを取得するには、特定の変数を含める必要があります。コネクテッドコンテンツURLリクエストの例は、Contentfulの[エントリ](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console)エンドポイントをターゲットにしています。このエンドポイントには`{space_id}`および`{environment_id}`、あるいは`{entry_id}`および`{access_token}`のような変数が必要です。これらはContentfulインスタンスから取得できます。このContent Blockの例では、変数をContentfulのスペースIDと環境IDに置き換える必要があります。<br><br>Content Delivery API URLの例では、Contentfulの利用可能なエンドポイントの1つだけを使用しています。異なるユースケースは、異なるURLを活用することで実現できます。例えば、[Images API](https://www.contentful.com/developers/docs/references/images-api/)を使えば、Contentfulに保存されている画像を取り込むことができます。詳しくは、[Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/)を参照してください。

{% alert note %}
エンドポイントによっては、新しい変数が必要になる場合があります。たとえば、Images APIには`{asset_id}`、`{unique_id},`、`{name}`が必要です。さらなるガイダンスについては、Contentfulにお問い合わせください。
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4. 「Test Endpoint」を使用して、BrazeがContentful APIに正常に接続し、目的のデータを取得できることをテストします。
5. **Done**を選択してContent Blockを保存します。
6. Content Blockに「Contentful API」などのわかりやすい名前をつけ、**Launch Content Block**を選択します。

### ステップ3:キャンペーンやキャンバスでコネクテッドコンテンツを使用する {#step-3-use-connected-content-in-campaigns-and-canvasses}

1. Brazeで、新しいキャンペーンを作成するか、既存のキャンペーンを編集します。
2. コネクテッドコンテンツブロックを使って、Contentfulから取得したデータを挿入します。設定時に定義したデータパスを使用して、キャンペーンのコンテンツをダイナミックに入力します。<br><br>
- **応答パス:** Content BlockをBraze キャンペーンまたはキャンバスに含めた後、変数`{response}`をメッセージに挿入すると、レスポンスが利用可能になります。<br><br>JSONドット表記法では、Contentfulからの応答本文のどの部分をメッセージに含めるかを指定できます。これはユースケースによって異なります。例えば、Contentfulのエントリエンドポイントからタイトル値（{% raw %}`liquid{{response.items[0].fields.title}}`{% endraw %}）を使用し、次のような応答を受け取ることができます。

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3. キャンペーンをプレビューしてテストし、コネクテッドコンテンツデータが正しく表示されることを確認します。
4. 設定に問題がなければ、キャンペーンを起動します。

## トラブルシューティング {#troubleshooting}

### APIレスポンス {#api-response}

Contentful APIの認証情報とエンドポイントURLが正しいことを確認してください。APIコールに問題があることを示すエラーメッセージがBrazeに表示されていないか確認してください。

### データマッピング {#data-mapping}

レスポンスパスのマッピングが正しく設定されていること、およびAPIレスポンスの構造が期待どおりであることを確認してください。

## その他のリソース {#additional-resources}

- [Contentful Content Delivery API documentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Brazeコネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
- [Braze Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)