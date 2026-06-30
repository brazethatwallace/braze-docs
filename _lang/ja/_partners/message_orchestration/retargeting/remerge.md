---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "このリファレンス記事では、BrazeとRemergeのパートナーシップについて説明します。Remergeは、大規模なリターゲティングのための専用アプリであり、アプリのオーディエンスを効率的にセグメント化し、ユーザーをリターゲティングするツールを備えています。"
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) は、大規模なアプリリターゲティングのための専用ツールであり、アプリのオーディエンスを効率的にセグメント化し、ユーザーをリターゲティングするツールを備えています。

_この統合はRemergeによって管理されています。_

## 統合について {#about-the-integration}

BrazeとRemergeの統合により、ユーザーデータをWebhookイベント経由でRemergeに送信し、モバイルデマンドサイドプラットフォームでユーザーのリターゲティングを支援することで、堅牢なクロスチャネルのライフサイクルマーケティングキャンペーンを開発できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Remergeアカウント | このパートナーシップを活用するには、Remergeアカウントが必要です。 |
| Remerge Webhookキー | このキーはRemergeから提供されます。 |
| AndroidアプリID | Android用のBrazeアプリケーション固有の識別子（「com.example」など）。 |
| iOSアプリID | iOS用のBrazeアプリケーション固有の識別子（「012345678」など）。 |
| Braze SDKでIDFA収集を有効にする | IDFA収集はBraze SDK内ではオプションであり、デフォルトでは無効になっています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1: Braze Webhookテンプレートを作成する {#step-1-create-your-braze-webhook-template}

今後のキャンペーンまたはキャンバス用のRemerge Webhookテンプレートを作成するには、Brazeプラットフォームの**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。


単発のRemerge Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択します。

新しいWebhookテンプレートで、以下のフィールドに記入してください:
- **リクエスト本文**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Webhook URLでは、以下の操作を行う必要があります:
- `https://remerge.events/event` APIを使用してWebhookイベントを送信します。
- イベント名を設定します。この名前は[remerge.io](https://www.remerge.io/)ダッシュボードに表示されます。
- AndroidとiOSのアプリの一意のアプリケーション識別子（Android:「com.example」、iOS:「012345678」など）をRemergeに渡します。
- キーを定義します。これはRemergeから提供されます。

![Braze Webhookビルダーに表示されるWebhook URLとメッセージプレビュー。]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないため、これらの値を自分で保存する必要があります。このデータを収集するには、ユーザーの同意が必要になる場合があることに注意してください。
{% endalert %}

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Remerge WebhookにはHTTPメソッドとリクエストヘッダーが必要です。

- **HTTPメソッド**: GET
- **リクエストヘッダー**:
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダー、HTTPメソッド、メッセージプレビュー。]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### リクエスト本文 {#request-body}

このWebhookのリクエスト本文を定義する必要はありません。

## ステップ2: リクエストをプレビューする {#step-2-preview-your-request}

メッセージをプレビューして、リクエストがさまざまなユーザーに対して正しくレンダリングされていることを確認します。AndroidとiOSの両方のユーザーに対して、プレビューとテストリクエストの送信を推奨します。リクエストが成功すると、APIは `HTTP 204` で応答します。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}