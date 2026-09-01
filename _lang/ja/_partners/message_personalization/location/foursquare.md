---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "このリファレンス記事では、BrazeとFoursquareのパートナーシップについて説明します。Foursquareは、位置情報に基づいてリアルタイムでイベントをトリガーする機能を提供する位置情報データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) は、Brazeのキャンペーンに位置情報データターゲティング機能を提供する位置情報データプラットフォームです。iOSとAndroidアプリでFoursquareのPilgrim SDKを使用して、位置情報に基づいたリアルタイムのイベントトリガーを提供し、Foursquareの強力なジオターゲティング機能を活用して、Brazeで関連性の高いパーソナライズされたメッセージを送信できます。

_この統合はFoursquareによって管理されています。_

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Foursquare アカウント | このパートナーシップを利用するには、Foursquare アカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeワークスペースとアプリ ID | Brazeワークスペースとアプリ IDは[開発者コンソール]({{site.baseurl}}/api/api_key)で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

2つのプラットフォームを統合するには、2つのSDKを統合し、対応するユーザーフィールドをマッピングする必要があります。Pilgrim SDKを統合すると、デバイス上またはWebhookを介してロケーションイベントを受信できます。

### ステップ1:ユーザーIDフィールドをマッピングする {#step-1-map-user-id-fields}

2つのSDK間でフィールドを正しくマッピングするには、Braze SDKの[`changeUser`メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids)と、Pilgrim SDKの[`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)の`setUserId`メソッドを使用して、両方のシステムで同じユーザーIDを設定します。

### ステップ2:Pilgrimコンソールを設定する {#step-2-configure-pilgrim-console}
![グループID、Android App ID、iOS App IDの入力を求めるPilgrimコンソールの画像。]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Braze開発者コンソールでワークスペースとアプリIDを確認します。次に、Braze REST APIキーとアプリIDをFoursquare Pilgrimコンソールに入力します。

Pilgrimコンソールを設定すると、Pilgrim SDKがロケーションイベントを記録してBrazeに転送します。これにより、条件を満たした顧客をリターゲティングしたり、セグメンテーションしたりできます。詳細については、[Foursquare開発者サイト](https://developer.foursquare.com/)を参照してください。

{% alert important %}
Pilgrim SDKでは、位置情報サービスを有効にする必要があります。
{% endalert %}

## メッセージのトリガー {#triggering-messages}

インテグレーションの設定が完了したら、Pilgrim SDKによって生成されたロケーションイベントに基づいてアクションを実行するキャンペーンまたはキャンバスを設定できます。このインテグレーションルートは、ユーザーが関心のある場所に入った直後のリアルタイムメッセージングや、退出後のお礼メッセージやリマインダーなどの遅延フォローアップコミュニケーションに最適です。

設定した場所に基づいてメッセージを送信するキャンペーンを送信するには:
- **アクションベース配信**で送信するBrazeキャンペーンまたはキャンバスを作成します
- トリガーとして、以下のスクリーンショットに示すように、`locationType`のイベントプロパティフィルターを持つ`arrival`のカスタムイベントを使用します。

![配信ステップのアクションベースキャンペーンで、「カスタムイベントを実行」オプションとして「arrival」が選択され、「locationType」が「home」に等しいことを示しています。]({% image_buster /assets/img_archive/action-based-campaign.png %})

## リターゲティング {#retargeting}

ユーザーをリターゲティングするには、Pilgrim SDKを使用してBrazeユーザーのユーザープロファイルに`last_location`カスタム属性を設定します。その後、`matches regex`比較を使用して、実際に特定の場所を訪れたユーザーをリターゲティングできます。たとえば、最近ピザ店にいたすべてのユーザーをセグメンテーションできます。

![ターゲットユーザーステップのアクションベースキャンペーンで、「last_location」が「Pizza Place」に等しいことを示しています。]({% image_buster /assets/img_archive/last-location-segment.png %})

また、Foursquareの`primaryCategoryId`に基づいて、特定の時間枠内に特定のタイプの場所を訪れたユーザーをBrazeでセグメンテーションすることもできます。このデータポイントをリターゲティングのユースケースに活用するには、オーディエンスのセグメンテーションプロセス中に`primaryCategoryId`をイベントプロパティとして記録します。Foursquare APIとPilgrim SDKで使用されるユーザーとプロパティを特定するには、[Foursquare開発者サイト](https://developer.foursquare.com/)を参照してください。