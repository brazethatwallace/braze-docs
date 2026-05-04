---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "このリファレンス記事では、Braze と Radar のパートナーシップについて説明します。Radar は、位置情報コンテキストとトラッキングを iOS アプリと Android アプリに追加するためのジオフェンシングプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.radar.com/) は、業界をリードするジオフェンシングおよび位置情報追跡プラットフォームです。Radar プラットフォームには3つの主力製品があります。[Geofences](https://radar.com/product/geofencing)、[Trip Tracking](https://radar.com/product/trip-tracking)、および [Geo APIs](https://radar.com/product/api) です。Brazeの業界屈指のエンゲージメントプラットフォームと Radar の業界をリードするジオフェンシング機能を組み合わせることで、ロケーションベースの幅広い製品・サービスエクスペリエンスを通じて収益とロイヤルティを向上させることができます。これには、集荷と配送の追跡、ロケーショントリガー通知、文脈に応じたパーソナライゼーション、ロケーション検証、ストアロケーター、住所オートコンプリートなどが含まれます。

_この統合は Radar によって管理されます。_

## 統合について {#about-the-integration}

Braze と Radar の統合により、高度なロケーションベースのCampaignトリガーと、豊富なファーストパーティロケーションデータを使用したユーザープロファイルエンリッチメントにアクセスできます。Radarのジオフェンスまたは移動追跡イベントが生成されると、カスタムイベントとユーザー属性がリアルタイムで Braze に送信されます。これらのイベントおよび属性は、ロケーションベースのCampaignsのトリガー、ラストマイルのピックアップおよび配送オペレーションの推進、フリートおよび配送物流の監視、またはロケーションパターンに基づくユーザーSegmentsの構築に使用できます。

さらに、Radar Geo APIを使用して、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を通じてマーケティングCampaignsを充実させたりパーソナライズしたりすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Radar アカウント | このパートナーシップを活用するには、Radar アカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。<br><br> これは Braze ダッシュボードの**設定** > **APIキー**から作成できます。 |
| アプリ識別子 | [アプリ識別子]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)は、Braze ダッシュボードの**設定** > **APIキー**で確認できます。 |
| iOS APIキー<br>Android APIキー | これらのAPIキーは、Braze ダッシュボードの**設定** > **アプリ設定**で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

Braze SDKと Radar SDK間でデータをマッピングするには、両方のシステムで同じユーザー IDまたはユーザーエイリアスを設定する必要があります。これは、Braze SDKの `changeUser()` メソッドと、Radar SDKの `setUserId()` メソッドを使用して実行できます。

統合を有効にするには:

1. Radarの [[Integrations](https://radar.com/documentation/integrations)] ページで Braze を見つけます。
1. **Enabled** を **Yes** に設定します。
3. アプリ識別子とAPIキーを貼り付けます。

{% alert note %}
テスト環境とライブ環境に別々のAPIキーを設定できます。
{% endalert %}

{:start="4"}
4. Braze エンドポイントを選択します。
5. イベントまたはイベント属性のフィルタリングを入力して、関連データのみがエンゲージメントマーケティングのために Braze に送信されるようにします。Radar イベントが生成されるたびに、Radar からカスタムイベントとユーザー属性が Braze に送信されます。iOS デバイスからのイベントは iOS APIキーを使用して送信され、Android デバイスからのイベントおよびユーザー属性は Android APIキーを使用して送信されます。

{% alert note %}
デフォルトでは、ログインユーザーの Radar `userId` は Brazeの `external_id` にマッピングされます。ただし、ログアウトしたユーザーを追跡したり、Radarの `metadata.brazeAlias` または `metadata.brazeExternalId` を設定してカスタムマッピングを指定したりすることもできます。`metadata.brazeAlias` を設定した場合は、Braze でラベル `radarAlias` を使用して一致するエイリアスを追加する必要もあります。
{% endalert %}

## イベントベースおよび属性ベースのユースケース {#event-and-attribute-based-use-cases}

カスタムイベントとユーザー属性を使用して、ロケーションベースのSegmentsを作成したり、ロケーションベースのCampaignsをトリガーしたりすることができます。

### カーブサイドピックアップの店舗到着通知をトリガーする {#trigger-a-store-arrival-notification-for-curbside-pickup}

ユーザーがカーブサイドピックアップのために店舗に到着したときに、到着の手順を案内するプッシュ通知を送信します。

![アクションベースの配信Campaignで、「arrived_at_trip_destination」カスタムイベントが発生し、「trip_metadata」が「curbside」に等しい場合にCampaignが配信されることを示す画面。]({% image_buster /assets/img_archive/radar-campaign.png %})

### 最近の来店者のオーディエンスSegmentを作成する {#build-an-audience-segment-of-recent-store-visitors}

たとえば、購買の有無にかかわらず、過去7日間に店舗を訪問したすべてのユーザーをターゲットにします。

![「radar_geofence_tags」に値 my_store が含まれ、「radar_updated_at」が7日前以内であるSegment。]({% image_buster /assets/img_archive/radar-segment.png %})

## コネクテッドコンテンツ {#connected-content}

次の例は、デジタルオファーを使用して近くにいるユーザーを店舗に引き付けるプロモーションを実行する方法を示しています。

![Androidに表示されている「New In Store Deals, Walmart and target near you」というコネクテッドコンテンツプッシュメッセージ。]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

開始するには、リクエスト URL内で使用するために、Radarの公開可能なAPIキーを手元に用意しておく必要があります。

次に、`connected_content` タグ内で、[Search Places API](https://radar.com/documentation/api#search-places) への GET リクエストを行います。Search Places APIは、[Radar Places](https://radar.com/documentation/places)（場所、チェーン、カテゴリの位置情報を収録し、全世界の包括的なビューを提供するデータベース）に基づいて付近のロケーションを返します。

以下のコードスニペットは、API呼び出しから JSON オブジェクトとして Radar が返す内容の例です。

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

コネクテッドコンテンツを活用したターゲティング済みのパーソナライズされた Braze メッセージを構築するには、APIリクエストURLの `near` パラメータの入力として Brazeの `most_recent_location` 属性を使用できます。`most_recent_location` 属性は、Radar イベント統合から収集されるか、または Braze SDKを介して直接収集されます。

次の例では、Radar チェーンフィルタリングが Target と Walmart のロケーションに適用され、近くのロケーションの検索範囲は 2 km に設定されています。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

`connect_content` タグからわかるように、JSON オブジェクトはURLの後に `:save nearbyplaces` を追加することで、ローカル変数 `nearbyplaces` に保存されます。
出力内容をテストするには、{% raw %}`{{nearbyplaces.places}}`{% endraw%} を参照します。

ユースケースをまとめると、Campaignの構文は以下のようになります。以下のコードは、`nearbyplaces.places` オブジェクトを反復処理し、一意の値を抽出し、それらを人間が読みやすい区切り文字で連結してメッセージにします。

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }}
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }}
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
コネクテッドコンテンツで使用できるすべての Radar APIについては、[Radar ドキュメント](https://radar.com/documentation/api)を参照してください。
{% endalert %}