---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "このリファレンス記事では、BrazeとJamppのパートナーシップについて説明します。Jamppは、モバイルの顧客の獲得とリターゲティングに利用されるパフォーマンスマーケティングプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/)はモバイルの顧客の獲得とリターゲティングに利用されるパフォーマンスマーケティングプラットフォームです。Jamppは、行動データと予測技術やプログラム技術を組み合わせて、消費者に対して初めての購入やより頻繁な購入を促すパーソナルで関連性の高い広告を表示することで、広告主の収益を創出します。

_この統合はJamppによって管理されます。_

## 統合について {#about-the-integration}

BrazeとJamppの統合により、会社ユーザーはBraze Webhookイベントを使用してイベントをJamppに同期できます。その結果、顧客はモバイル広告エコシステム内で、より豊富なデータセットを各自のリターゲティングイニシアチブに追加できます。

広告で顧客をリターゲティングする状況の例を以下に示します。
- 顧客のメールまたはプッシュサブスクリプションのステートが変化したとき。
- 顧客がBrazeメッセージングCampaignとどのようにインタラクションしたか。
- 顧客が特定のジオフェンスをトリガーした場合。

## 前提条件 {#prerequisites}

この統合はiOSとAndroidアプリをサポートしています。

| 要件 | 説明 |
|---|---|
| Jamppアカウント | このパートナーシップを活用するには、[Jamppアカウント](https://www.jampp.com/)が必要です。 |
| AndroidアプリID | Android用のBrazeアプリケーション固有の識別子（「com.example」など）。 |
| iOSアプリID | iOS用のBrazeアプリケーション固有の識別子（「012345678」など）。 |
| Braze SDKでIDFA収集を有効にする | IDFA収集はBraze SDK内ではオプションであり、デフォルトでは無効になっています。 |
| カスタム属性によるGoogle広告IDの収集 | Google広告IDの収集は顧客向けのオプションであり、[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)として収集できます。
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1: BrazeでWebhookテンプレートを作成する {#step-1-create-a-webhook-template-in-braze}

将来のCampaignsまたはCanvasesで使用するJampp Webhookテンプレートを作成するには、Brazeダッシュボードで**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

一度だけのJampp Webhook Campaignを作成したい場合や、既存のテンプレートを使用したい場合は、新規Campaign作成時にBrazeで**Webhook**を選択してください。

新しいWebhookテンプレートで、次のフィールドに入力します。
- **Request Body**：Raw Text
- **Webhook URL**：
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Webhook URLで次の操作を行う必要があります。
- イベント名を設定します。この名前はJamppダッシュボードに表示されます。
- AndroidとiOSのアプリの一意のアプリケーション識別子（Android：「com.example」、iOS：「012345678」など）を渡します。
- Google広告IDとしてトラッキングしている適切なカスタム属性の[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid)を挿入します。この例では、Google広告IDが `aaid` としてリストされていますが、これを開発者が設定したカスタム属性名に置き換える必要があります。

![Braze Webhookビルダーに表示されるWebhook URLとメッセージプレビュー。]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないため、これらの値を自分で保存する必要があります。このデータを収集するには、ユーザーの同意が必要になる場合があることに注意してください。
{% endalert %}

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Jampp WebhookにはHTTPメソッドとリクエストヘッダーが必要です。

- **HTTP Method**：GET
- **Request Headers**：
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダー、HTTPメソッド、メッセージプレビュー。]({% image_buster /assets/img/jampp_method.png %})

#### リクエスト本文 {#request-body}

このWebhookのリクエスト本文を定義する必要はありません。

### ステップ 2: リクエストをプレビューする {#step-2-preview-your-request}

メッセージをプレビューして、リクエストがさまざまなユーザーに対して正しくレンダリングされていることを確認します。AndroidとiOSの両方のユーザーに対して、プレビューとテストリクエストの送信を推奨します。リクエストが成功すると、APIは `HTTP 204` で応答します。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhook Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}