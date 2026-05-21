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

| 必要条件 | 説明 |
|---|---|
| Foursquareアカウント | このパートナーシップを利用するには、Foursquareのアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| BrazeのワークスペースとApp ID | BrazeのワークスペースとApp IDは[開発者コンソール]({{site.baseurl}}/api/api_key/)で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

2つのプラットフォームを統合するには、2つのSDKを統合し、一致するユーザーフィールドをマッピングする必要があります。Pilgrim SDKを統合すると、デバイスまたはWebhookで位置情報イベントを受け取ることができます。

### ステップ1:ユーザーIDフィールドをマップする {#step-1-map-user-id-fields}

2つのSDK間でフィールドを正しくマッピングするには、Braze SDKの[`changeUser`メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids)とPilgrim SDKの[`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data)の`setUserId`メソッドを使用して、両方のシステムで同じユーザーIDを設定します。

### ステップ2:Pilgrimコンソールを設定する {#step-2-configure-pilgrim-console}
![Group ID、Android App ID、iOS App IDの入力を促すPilgrimコンソールの画像。]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Braze開発者コンソールでワークスペースとApp IDを確認します。次に、Foursquare Pilgrim ConsoleにBraze REST APIキーとApp IDを入力します。

Pilgrimコンソールの設定が完了すると、Pilgrim SDKが位置情報イベントを記録してBrazeに転送します。これにより、条件を満たした顧客をリターゲティングおよびセグメント化できます。詳細は[Foursquare開発者サイト](https://developer.foursquare.com/)を参照してください。

{% alert important %}
Pilgrim SDKを使用するには、位置情報サービスを有効にする必要があります。
{% endalert %}

## メッセージのトリガー {#triggering-messages}

統合が設定されたら、Pilgrim SDKにより生成される位置情報イベントからアクションを実行するキャンペーンやキャンバスを設定できます。この統合ルートは、ユーザーが特定の会場に入った直後にリアルタイムメッセージを送信する場合、または退場後にフォローアップコミュニケーション（お礼やリマインダーなど）を行う場合に最適です。

設定した場所に基づいてメッセージを送信するキャンペーンを作成するには：
- **アクションベースの配信**で送信するBrazeのキャンペーンまたはキャンバスを作成します
- トリガーには、以下のスクリーンショットに示すように、`locationType`のイベントプロパティフィルターを含むカスタムイベント`arrival`を使用します。

![配信ステップ内のアクションベースのキャンペーンで、「カスタムイベントを実行」オプションとして「arrival」が選択され、「locationType」が「home」に設定されている画面。]({% image_buster /assets/img_archive/action-based-campaign.png %})

## リターゲティング {#retargeting}

ユーザーをリターゲティングするには、Pilgrim SDKを使用して、Brazeユーザーのユーザープロファイルに`last_location`カスタム属性を設定します。そして、`matches regex`の比較を使って、現実世界で特定の場所に行ったユーザーをリターゲティングできます。例えば、最近ピザ屋に行ったすべてのユーザーをセグメント化できます。

![ターゲットユーザーステップのアクションベースのキャンペーンで、「last_location」が「Pizza Place」に設定されている画面。]({% image_buster /assets/img_archive/last-location-segment.png %})

またBrazeで、特定のタイプの会場を訪問したユーザーを、特定の時間枠内のFoursquareの`primaryCategoryId`に基づいてセグメント化することもできます。このデータポイントをリターゲティングのユースケースに利用するには、オーディエンスのセグメンテーションプロセスでイベントプロパティとして`primaryCategoryId`をログに記録します。Foursquare APIとPilgrim SDKで使用されるユーザーとプロパティを確認するには、[Foursquare開発者サイト](https://developer.foursquare.com/)を参照してください。