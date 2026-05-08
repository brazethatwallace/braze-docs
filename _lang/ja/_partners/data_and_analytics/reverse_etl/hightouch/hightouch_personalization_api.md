---
nav_title: Hightouch Personalization API
article_title: Hightouch Personalization API
description: "このリファレンス記事では、Braze と Hightouch の Personalization API の統合について説明します。この API は、クラウドデータウェアハウス内の任意のデータセットに基づいて低レイテンシーのデータ API をホストするためのマネージドサービスです。このリファレンス記事では、Hightouch Personalization API が解決するユースケース、使用するデータ、設定方法、Braze との統合方法について説明します。"
page_type: partner
search_tag: Partner
---

# Hightouch Personalization API

> Hightouchの[Personalization API](https://hightouch.com/docs/destinations/personalization-api) は、クラウドデータウェアハウスの任意のデータセットに基づいて低レイテンシーのデータ API をホストできるマネージドサービスです。

![]({% image_buster /assets/img/hightouch/cohort7.png %})

Braze と Hightouchの統合により、[Braze コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)とこの API を使用して、送信時に最新の顧客またはオブジェクトのデータをCampaignやCanvasesに取り込むことができます。

Hightouchの Personalization API は、Brazeの設定で使用する REST エンドポイントを提供します。具体的には、Brazeのコネクテッドコンテンツを使用して Personalization API に対する GET リクエストを実行し、特定の識別子に関連するすべての情報を取得できます。この API によって公開されるデータは、顧客、製品、またはその他のオブジェクトデータを表す場合があります。

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## 前提条件 {#prerequisites}

| 必要条件| 説明|
| ---| ---|
| Personalization API を有効にした [Hightouch アカウント](https://app.hightouch.com/login) | このパートナーシップを活用するには、Hightouchの[Business Tier アカウント](https://hightouch.com/pricing)が必要です。|
| 定義されたユースケース | API を設定する前に、この統合のユースケースを決定しておく必要があります。一般的なユースケースについては、以下のリストを参照してください。 |
| クラウドデータウェアハウスなどのソースに保存されているデータ | Hightouchは、[25以上のデータソース](https://hightouch.com/integrations)と統合しています。 |
| Hightouch API キー | これは、**Hightouch > Settings > API keys > Add API key** 内で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Use Cases %}

### ユースケース {#use-cases}

始める前に、Personalization API をどのように使いたいかを正確に計画しておくと便利です。

一般的なユースケースには以下のようなものがあります。
- メールテンプレート、Campaign、アプリ内エクスペリエンスへのパーソナライズされた製品レコメンデーションの埋め込みを効率化する**製品レコメンデーション**
- ダイナミックな製品レコメンデーションでマーケティングタッチポイントを充実させることで**パーソナライズされたマーケティングキャンペーンを強化する**
- カスタマイズされた検索結果、コホートベースの価格設定、メッセージング、おすすめ記事、最寄りの店舗など、**アプリ内またはWebでパーソナライゼーションを提供する**
- **財務データまたは医療データに基づくレコメンデーション** — 財務データには厳しい要件がありますが、Hightouchはその[厳格なデータセキュリティポリシー](https://hightouch.com/docs/security/overview#compliance)によってこれらの要件を満たしています。Hightouchを使用すると、セグメンテーション基準で使用される基本的な属性を公開せずに、財務データまたは医療データに基づいて顧客Segmentを作成できます。

{% endtab %}
{% tab Datasets %}

### データセット {#datasets}

Personalization API は、ウェアハウス内の選択されたデータのキャッシュとして機能するため、レコメンデーションデータはすでにそこに保存されている必要があります。必要に応じて、Hightouchを使用してテンプレートに従って変換できます。この種のデータには以下が含まれます。
- 地理的地域、年齢、その他の人口統計学的情報などのユーザーメタデータ
- 過去の購入、ページビュー、クリックなどのユーザーアクションやイベント

{% endtab %}
{% endtabs %}

## 統合 {#integration}

### ステップ1: データソースをHightouchに接続する {#step-1-connect-data-source-to-hightouch}

Hightouchの[ソース](https://hightouch.com/docs/getting-started/concepts#sources)は、組織のビジネスデータが存在する場所です。この場合、ユーザーデータが保存されている場所になります。
1. Hightouchで、**Sources Overview > Add Source** に移動します。ソースとしてデータウェアハウスを選択します。<br><br>
2. 関連する認証情報を入力します。これらはソースによって異なります。

詳細については、関連するソースの[ドキュメント](https://hightouch.com/docs)を参照してください。

### ステップ2: モデルデータ {#step-2-model-data}

Hightouchモデルは、ソースからどのようなデータを取得するかを定義します。新しいモデルをセットアップするには、以下の手順に従います。

1. Hightouchで [**Models overview**](https://app.hightouch.com/models) > **Add model** に移動し、接続したソースを選択します。<br><br>
2. 次に[モデリング方法](https://hightouch.com/docs/models/creating-models)を選択します。すべての情報を1つのテーブルに結合する必要があるため、ビジュアルテーブルセレクタを使って定義できます。あるいは、必要なカラムだけを含む SQL を書いたり、既存の dbt モデル、Looker Looks、Sigma ワークブックに頼ることもできます。<br><br>
3. 続行する前に、モデルをプレビューして、目的のデータをクエリしていることを確認します。デフォルトでは、Brazeはプレビューを最初の100レコードに制限しています。データを検証したら、**Continue** をクリックします。<br><br>
4. モデルに名前を付けます（例: 「User recommendations」）。<br><br>
5. 最後に主キーを選択し、**Finish** をクリックします。主キーは、一意の識別子を持つ列である必要があります。これは、特定のユーザーのレコメンデーションを取得するために Personalization API を呼び出すときに使用するフィールドでもあります。

### ステップ3: Personalization API を設定する {#step-3-configure-personalization-api}

API でリクエストを受信するための準備は、次の2つのステップからなります。
- お客様のインフラに最も近い地域で Personalization API を有効にする
- Hightouchが管理するキャッシュでマテリアライズされるべきモデルを定義するために同期を作成する

以下の手順に従って、両方を完了させます。

1. Hightouchで [**Destinations**](https://app.hightouch.com/destinations) に移動し、作成済みの Hightouch Personalization API を選択します。この送信先が有効になっていない場合は、[Hightouch サポート](mailto:friends@hightouch.com)にお問い合わせください。<br><br>
2. 次に、適切な地域を選択します。インフラに最も近い地域を選択することで、応答時間を短縮できます。インフラに近いリージョンが表示されない場合は、[Hightouch サポート](mailto:friends@hightouch.com)にお問い合わせください。<br><br>
3. [**Syncs** 概要ページ](https://app.hightouch.com/syncs)に移動し、**Add sync** ボタンをクリックします。次に、該当するモデルと、以前に設定した送信先を選択します。<br><br>
4. 英数字のコレクション名を入力します。コレクションは概念的にはデータベースのテーブルに似ています。各コレクションは特定のデータタイプ（顧客や請求書など）を表します。コレクション名には英数字のみを使用する必要があり、Personalization API エンドポイントの一部になります。<br><br>
5. 次に、モデルのどの列をレコード検索のプライマリインデックスとして使用するかを指定します。このフィールドは、コレクション内の各レコードを一意に識別する必要があり、多くの場合、モデルの主キーと同じです。Personalization API は、複数のインデックスでの検索をサポートしています。たとえば、`user_id`、`anonymous_id`、または `email_address` を使用して顧客プロファイルを取得できます。複数のインデックスを有効にする場合は、[Hightouch サポート](mailto:friends@hightouch.com)にご連絡ください。<br><br>
6. フィールドマッパーを使用して、API レスポンスペイロードに含めるモデルのカラムを指定します。これらのフィールドの名前を変更したり、Liquid テンプレート言語を使用して変換を適用するために高度なマッパーを使用したりできます。<br><br>
7. ユースケースに適した[削除動作](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)を選択します。<br><br>
8. 最後に **Continue** をクリックし、[同期スケジュール](https://hightouch.com/docs/syncs/schedule-sync-ui)を選択します。

Hightouchは、ウェアハウス内のデータをマネージドデータベースに同期し、Personalization API を介して公開します。

### ステップ4: Brazeコネクテッドコンテンツを通じて Personalization API を呼び出す {#step-4-call-personalization-api-through-braze-connected-content}

Personalization API インスタンスを設定したら、それをBrazeコネクテッドコンテンツのエンドポイントとして使用できます。

API は `https://personalization.{region}.hightouch.com` でアクセスできます（例: `https://personalization.us-west-2.hightouch.com`）。

情報はエンドポイント `/v1/collections/:collection_name/records/:index_key/:index_value` を使用して取得できます。

たとえば、CampaignやCanvasにこのスニペットを含めることができます。

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Liquid テンプレートを使って、JSON ペイロードで返されたプロパティを参照し、メッセージングで使用できます。

以下のペイロードの例の場合:

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ]
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    }
}
```

以下の Liquid リファレンスは、この例のデータを返します。

| Liquid テンプレート | 返されるデータの例 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Universal Language |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラブルシューティング {#troubleshooting}

ご質問がある場合は、[Hightouch サポート](mailto:friends@hightouch.com)までお問い合わせください。