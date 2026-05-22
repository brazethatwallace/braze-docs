---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "このリファレンス記事では、BrazeとRokt Calendarのパートナーシップについて説明します。Rokt Calendarは、ブランドがカレンダーイベントや通知の形式で1:1のイベントやプロモーションコミュニケーションをプッシュできるようにするダイナミックなカレンダーマーケティングテクノロジーです。"
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/)は、ブランドがカレンダーイベントや通知の形式で1:1のイベントやプロモーションコミュニケーションをプッシュできるようにするダイナミックなカレンダーマーケティングテクノロジーです。

*この統合はRokt Calendarによって管理されています。*

## 統合について {#about-the-integration}

BrazeとRokt Calendarの統合により、Rokt Calendarのサブスクライバーとそのデータを Braze Webhook経由でBrazeにプッシュできます。その後、Braze キャンバスでこのデータを使用して、以下のカスタム[Rokt Calendar属性](#audience-segmentation)を使用したジャーニーターゲティングとオーディエンスセグメンテーションを行うことができます。

## 前提条件 {#prerequisites}

| 必要条件  | 説明 |
| ------------ | ----------- |
| Rokt Calendarアカウント | このパートナーシップを利用するには、クライアント専用のRokt Calendarアカウントが必要です。アカウントマネージャーとの相談は[sales-calendar@rokt.com](mailto:sales-calendar@rokt.com)までご連絡ください。  |
| Rokt Calendarの設定 | Rokt Calendarのアカウントマネージャーが、お客様のニーズに最適なカレンダーを設定します。設定には以下が含まれます：<br>- マージフラグ<br>- サブスクライバーIDフォールバックフラグ<br>- 必要に応じたメールキャプチャ |
| Rokt Calendar OAuth認証情報 | Rokt Calendarのアカウントマネージャーから提供されるこのキーにより、BrazeとRokt Calendarのアカウントを接続できます。<br><br>これはBrazeダッシュボードの**設定** > **コネクテッドコンテンツ**で作成できます。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。このキーをRokt Calendarのアカウントマネージャーに提供する必要があります。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| [Braze RESTエンドポイント]({{site.baseurl}}/api/basics/#endpoints) | RESTエンドポイントのURL。エンドポイントはインスタンスのBraze URLに依存します。 |
| 外部サブスクライバーID | これは、Rokt CalendarのサブスクリプションプロセスがカレンダーサブスクライバーとBrazeユーザーを照合するために使用する識別子です。これをRokt Calendarに渡します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## オーディエンスセグメンテーション {#audience-segmentation}

Rokt Calendarが新規ユーザーを作成するか、既存のサブスクライバーとBrazeユーザーを照合すると、Rokt CalendarからBraze内でフィルタリングできる以下のカスタムサブスクリプション属性が送信されます。

| カスタム属性  | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Rokt Calendarアカウントのコード | `brazetest/f5733866ade2` と `brazetest/ff10919f1078` |
| `rokt:account_id` | Rokt CalendarアカウントのID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Rokt Calendarアカウントの名前 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Rokt Calendarカレンダーのコード | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | Rokt CalendarカレンダーのID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Rokt Calendarカレンダーのタイトル | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 作成されたサブスクリプションに関連する国コード | `AU/f5733866ade2` |
| `rokt:device_name` | 作成されたサブスクリプションに関連するデバイスタイプ | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 作成されたサブスクリプションに関連する原産国 | `Australia/f5733866ade2` |
| `rokt:optIn1` | ユーザーが、作成されたサブスクリプションに関連する2つのオプトインのうち最初のオプトインにオプトインしたかどうか | `True/f5733866ade2` |
| `rokt:optIn2` | ユーザーが、作成されたサブスクリプションに関連する2つのオプトインのうち2番目にオプトインしたかどうか | `True/f5733866ade2` |
| `rokt:source` | 作成されたサブスクリプションのソース | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | サブスクリプションプロセス中にユーザーが入力したメールアドレス | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 作成されたサブスクリプションに関連する、一意な識別子としてのサブスクリプションID | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 作成されたサブスクリプションに関連するサブスクリプション方法（webcal/Google） | `WebCal/f5733866ade2` |
| `rokt:tags` | 作成されたサブスクリプションに関連して使用されたカレンダータグ | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

また、Rokt Calendarは、ユーザーがRokt Calendarをサブスクライブするとすぐに `subscribe` カスタムイベントをトリガーします。このイベントはBrazeセグメンテーションで使用することも、キャンペーンまたはキャンバスコンポーネントのトリガーとして使用することもできます。

## 統合 {#integration}

### ステップ1：カレンダーサブスクライバーのオーディエンスを作成する {#step-1-building-an-audience-of-calendar-subscribers}

キャンバスからカレンダーイベントを送信するには、まずすでにサブスクライブしているユーザーがいるRokt Calendarを設定する必要があります。そのためには、カレンダーをサブスクライブする場所と方法をユーザーに通知する必要があります。Rokt Calendarでは以下を推奨しています。

#### サブスクリプションの統合ポイントを提供する {#provide-subscription-integration-points}
カレンダーサブスクライバーのオーディエンスを作成するには、ユーザーが移動してサブスクライブできる送信先を提供する必要があります。サブスクリプション統合ポイントの例には以下があります：
  - Webサイトにカレンダーボタンを追加する
  - メールやSMSにカレンダーリンクを追加する
  - アプリにカレンダーボタンを追加する
  - ソーシャルメディアにカレンダーリンクを追加する

#### カレンダーを宣伝する {#promote-the-calendar}
サブスクライバーのオーディエンスを作成するには、サブスクライブ方法がわかるようにオーディエンスにカレンダーを宣伝する必要があります。カレンダー宣伝の例には以下があります：
  - ソーシャルメディアへの投稿
  - メールニュースレターと最新情報
  - ブログ記事
  - アプリ内通知

### ステップ2：BrazeでRokt CalendarのWebhookを作成する {#step-2-create-a-rokt-calendar-webhook-in-braze}

Brazeでは、以下のいずれかを行うためにWebhook キャンペーンまたはキャンバス内のWebhookを設定できます。

- 新しいパーソナライズ済みイベントを送信する：サブスクライバーのカレンダーのセグメントに新しいイベントを追加できるようにします。
- パーソナライズ済みイベントを更新する：サブスクライバーのカレンダーにある既存のイベントを更新できるようにします。

今後のキャンペーンやキャンバスで使用するRokt Calendar Webhookテンプレートを作成するには、Brazeプラットフォームの**テンプレート** > **Webhookテンプレート**に移動します。

単発のRokt Calendar Webhook キャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択します。

{% tabs %}
{% tab Send a new event %}
Rokt Calendar Webhookテンプレートを選択すると、以下が表示されます：
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **リクエスト本文**：Raw Text
{% endtab %}
{% tab Update an existing event %}
Rokt Calendar Webhookテンプレートを選択すると、以下が表示されます：
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **リクエスト本文**：Raw Text
{% endtab %}
{% endtabs %}

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Rokt Calendarでは、認証のためにRokt Calendarコネクテッドコンテンツの認証情報名を含む `HTTP Header` が必要です。以下はすでにキーと値のペアとしてテンプレート内に含まれていますが、**設定**タブで `<Rokt-Calendar-API>` を `Manage Settings > Connected Content > Credential` にある認証情報名に置き換える必要があります。

{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### リクエスト本文 {#request-body}

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update an existing event %}
{% raw %}
`````````javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
以下のフィールドには、イベントレベルでカスタマイズできる情報が含まれています。

| フィールド             | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***必須** | 追加または更新されるイベントの一意な識別子 | `Event_00001`
| `eventTitle` <br>***必須** | カレンダーに表示されるイベントのタイトル | Summer Sale 2019
| `eventDescr` | カレンダーに表示されるイベントの説明 | セール期間は3日間です。このリンク `www.mybusiness.com/sale` をクリックしてオファーをご覧ください。 |
| `eventLocation` | カレンダーに表示されるイベントの場所。これはeventTitleを補完する2番目の行動喚起として使用されることが多い点に注意してください。 | イベントを開いて50%オフを獲得 |
| `eventStart` <br>***必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T15:00:00` |
| `eventEnd` <br>***必須**  | カレンダーに表示されるイベントの終了日時 | `2019-02-21T16:00:00` |
| `eventTz` <br>***必須**  | カレンダーに表示されるイベントのタイムゾーン。適用可能なタイムゾーンのリストは[こちら](https://roktcalendar-api.readme.io/docs/timezones)で確認できます。 | `Eastern Standard Time` |
| `notifyBefore` <br>***必須**  | カレンダーに表示されるイベントのリマインダー時刻。分単位で表されます。 | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
有効なタイムゾーンのリストは、[https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones)を参照してください。
{% endalert %}

### ステップ3：リクエストをプレビューする {#step-3-preview-your-request}

**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、独自にカスタマイズしてWebhookをテストします。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhook キャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済みWebhookテンプレート**リストで見つけることができます。
{% endalert %}