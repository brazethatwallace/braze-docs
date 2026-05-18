---
nav_title: Regal
article_title: Regal
description: "このリファレンス記事では、BrazeとRegalのパートナーシップについて説明しています。Regalは電話およびSMSの販売ソリューションであり、両方のソースからのデータを使用して顧客にパーソナライズされた体験を提供することができます。"
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) は、より多くの会話を促進するために構築された電話およびSMSセールスソリューションです。これにより、成長目標をより短期間で達成できるようになります。

RegalとBrazeを統合することで、すべての顧客タッチポイントでより一貫性がありパーソナライズされたエクスペリエンスを作成できます。
- Regalでの電話による会話の内容に基づいて、Brazeから適切なネクストベストのメールまたはプッシュ通知を送信します。
- 価値の高い顧客がBrazeからのマーケティングメールをクリックスルーしたがコンバージョンに至らなかった場合に、Regalでコールをトリガーします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Regalアカウント | このパートナーシップを活用するには、Regalアカウントが必要です。 |
| Regal APIキー | Regal APIキーを使用すると、BrazeからRegalにイベントを送信できます。<br><br>このキーを取得するには、[support@regal.io](mailto:support@regal.io) までメールでご連絡ください。 |
| Brazeデータ変換 | データ変換は現在早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Brazeカスタマーサクセスマネージャーにお問い合わせください。これは、Regalからデータを受信するために必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合：BrazeからRegalにデータを送信する {#integration-sending-data-from-braze-to-regal}

次のセクションでは、BrazeのキャンバスまたはキャンペーンのWebhookを使用して、顧客プロファイルとイベントデータをRegalに送信するためのソースとしてBrazeを使用する方法について説明します。

### ステップ1：Regalで新しい連絡先を作成する {#step-1-create-new-contacts-in-regal}

Brazeで作成される新しい連絡先をRegalでのコールやテキストに利用できるようにするには、新しい連絡先が作成されるたびにWebhookでRegalに通知するキャンバスまたはキャンペーンを作成します。

1. 「Create New Contact for Regal」というタイトルのキャンバスまたはキャンペーンを作成し、エントリタイプとして**アクションベース**を選択します。

2. トリガーロジックを**カスタムイベント**に設定し、電話番号を持つ連絡先が作成されたときに発生するイベントを選択します。Regalでは、電話番号フィールドが確実に設定されるようにフィルターを追加することも推奨しています。

3. 新しいWebhookテンプレートに、次のフィールドを記入してください：
   - **Webhook URL**：<https://events.regalvoice.com/events>
   - **リクエスト本文**：Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Regal.ioには、認証用のHTTPヘッダーとHTTPメソッドが必要です。次の内容は、**設定**タブのキーと値のペアとして既にテンプレートに含まれています：
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
    - **Authorization**：`{{<REGAL_API_KEY>}}`
    - **Content-Type**：application/json
{% endraw %}

#### リクエスト本文 {#request-body}

以下の唯一の必須フィールドは `traits.phone` プロパティです。残りはオプションです。ただし `optIn` を含める場合は、`optIn.channel` と `optIn.subscribed` を含める必要があります。

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
`````````

上記のペイロードの例は、すべての連絡先が音声とSMSのオプトインに同意していることを前提としています。これに該当しない場合は、上記の `optIn` プロパティを削除し、`optIn` が収集されたときにRegalで連絡先を更新する別のキャンバスまたはキャンペーンを設定できます。

### ステップ2：オプトイン情報を更新する {#step-2-update-opt-in-information}

お客様のアプリのユーザーエクスペリエンスのさまざまな部分でオプトインおよびオプトアウトが発生する可能性がある場合、ユーザーがオプトインまたはオプトアウトするたびにRegalを更新することが重要です。以下は、Regalに最新のオプトイン情報を送信するための推奨キャンバスです。これをBrazeプロファイルのフィールドとして保存することを前提としていますが、保存されていない場合は、Brazeアカウントでユーザーがオプトインまたは配信停止したことを表すイベントをトリガーとして同様に使用できます。（以下の例は電話のオプトイン用ですが、SMSオプトインを別々に収集する場合は、同様のキャンバスまたはキャンペーンを設定できます）。

1. 「Send Opt In or Out to Regal」というタイトルの新しいキャンバスまたはキャンペーンを作成します。

2. 次のトリガーオプションのいずれかを選択し、ユーザーのオプトインステータスを表すフィールドを選択します。オプトインまたはオプトアウトを表すイベントをBrazeに送信する場合は、そのイベントをトリガーとして使用してください。
    - ユーザープロファイルフィールド更新済み
    - サブスクリプショングループステータスの更新
    - サブスクリプションステータス

3. 新しいWebhookテンプレートに、次のフィールドを記入してください：
   - **Webhook URL**：<https://events.regalvoice.com/events>
   - **リクエスト本文**：Raw Text

#### リクエストヘッダーとメソッド

Regal.ioには、認証用のHTTPヘッダーとHTTPメソッドが必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります：
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
    - **Authorization**：`{{<REGAL_API_KEY>}}`
    - **Content-Type**：application/json
{% endraw %}

#### リクエスト本文

必要に応じて、追加のユーザープロファイル属性をこのペイロードに追加して、複数の属性が同時に最新の状態であることを確認することもできます。

`````````json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
`````````

### ステップ3：カスタムイベントを送信する {#step-3-send-custom-events}

最後に、Regalに送信するキーイベントごとにキャンバスまたはキャンペーンを設定します。Regalでは、RegalでSMSおよび通話をトリガーするうえで重要なすべてのイベント（登録フローまたは購入フローの各ステップでのイベントなど）を送信することを推奨しています。また、連絡先がRegal キャンペーンの対象外となる終了基準として使用されるイベントも送信してください。

例えば、以下はユーザーがアプリケーションの最初のステップを完了したときにRegalにイベントを送信するためのワークフローです。

1. 「Send Application Step 1 Completed Event to Regal」というタイトルの新しいキャンバスまたはキャンペーンを作成します。

2. トリガーノードのロジックを**カスタムイベント**に設定し、Regalに送信したいイベント名を選択します。例えば、「Application Step 1 Completed」などです。

3. 新しいWebhookテンプレートに、次のフィールドを記入してください：
   - **Webhook URL**：<https://events.regalvoice.com/events>
   - **リクエスト本文**：Raw Text

#### リクエストヘッダーとメソッド

Regal.ioには、認証用のHTTPヘッダーとHTTPメソッドが必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります：
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
    - **Authorization**：`{{<REGAL_API_KEY>}}`
    - **Content-Type**：application/json
{% endraw %}

#### リクエスト本文

必要に応じて、このペイロードに追加のユーザープロファイル属性を追加して、複数の属性が同時に最新であることを確認できます。

`````````json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
`````````

#### 最新の連絡先属性 {#up-to-date-contact-attributes}

これは必須ではありませんが、Regalでは、キーイベントが利用可能になった時点でRegalが最新の連絡先属性にアクセスできるようにするために、イベントワークフローのイベントペイロードに主要なユーザープロファイルデータフィールドも送信することを推奨しています。

{% alert note %}
Regalに送信する重要なイベント、またはこれらのキャンバスやキャンペーンの設定方法についてご質問がある場合は、support@regal.io にお問い合わせください。
{% endalert %}

## 統合：RegalからBrazeにデータを送信する {#integration-sending-data-from-regal-to-braze}

このセクションでは、`SMS.sent` や `call.completed` などのRegalレポートイベントをBrazeに取り込み、Brazeプロファイルに表示され、Brazeのセグメンテーションツール、キャンバス、およびキャンペーンで利用できるようにする方法について説明します。この統合では、Regal Reporting WebhookとBrazeデータ変換を使用してデータフローを自動化します。

### ステップ1：Brazeでデータ変換を作成する {#step-1-create-a-data-transformation-in-braze}

{% alert important %}
データ変換は現在早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

Brazeでは、Brazeに送信する予定のRegal Webhookごとに変換を作成することをお勧めします。

データ変換を作成するには：
1. Brazeダッシュボードの**Transformations**ページに移動します。
2. 変換に名前を付けて、**Create transformation**をクリックします。
3. 変換のリストから、<i class="fa-solid fa-ellipsis-vertical" title="アクションを表示"></i>をクリックし、**Copy webhook URL**を選択します。

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### ステップ2：Regalでレポート Webhookを有効にする {#step-2-enable-reporting-webhooks-in-regal}

レポートWebhookを設定するには：
1. Regalアプリに移動して、**Setting**ページを開きます。

2. **Reporting Webhooks**セクションで、**Create Webhooks**をクリックします。

3. Webhookエンドポイント入力で、関連付けられたデータ変換のBrazeデータ変換Webhook URLを追加します。

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### エンドポイントの更新 {#updating-an-endpoint}
エンドポイントを編集すると、キャッシュが更新されて新しいエンドポイントにイベントが送信されるまでに最大で5分かかることがあります。
#### 再試行 {#retries}
現在、これらのイベントに再試行はありません。応答が5秒以内に受信されない場合、イベントは破棄され、再試行されません。Regalは今後のリリースで再試行を追加する予定です。
#### イベント {#events}
Regalの[Reporting Webhooksガイド](https://developer.regal.io/docs/reporting-webhooks#events)には、公開するレポートイベントの完全なリストが含まれています。そこでは、プロパティの定義やサンプルペイロードも確認できます。

### ステップ3：RegalイベントをBrazeイベントに変換する {#step-3-transform-regal-events-into-braze-events}

Brazeの[データ変換]({{site.baseurl}}/data_transformation/)機能を使用すると、受信したRegalイベントを、Brazeで属性、イベント、または購入として追加するのに必要な形式にマッピングできます。

1. データ変換に名前を付けてください。イベントWebhookごとにデータ変換を設定することをお勧めします。

2. 接続をテストするには、Regal Agent Desktopから携帯電話への発信コールを作成し、Conversation Summaryフォームを送信してcall.completedイベントを作成します。

3. Regalの連絡先をBrazeプロファイルにマッピングするために使用する識別子を決定します。Regalイベントで利用可能な識別子には以下が含まれます：
   - `userId` - この識別子を以前に連絡先に送信した場合にのみ、イベントに設定されます
   - `traits.phone`
   - `traits.email` - この識別子を以前に連絡先に送信した場合にのみ、イベントに設定されます

#### Braze対応の識別子 {#braze-supported-identifiers}
- Brazeは識別子として電話番号をサポートしていません。これを識別子として使用するには、Brazeで電話番号を[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)として設定できます。
- Brazeデータ変換を使用する場合、メールアドレスを識別子として使用できます。メールアドレスがBraze内のプロファイルとして存在する場合、既存のプロファイルが更新されます。メールアドレスがBraze内にまだ存在しない場合、メール専用のプロファイルが作成されます。

## ユースケース {#use-cases}

{% tabs %}
{% tab メールをトリガーする %}

**Regalでのコール処理に基づいて、Brazeからメールをトリガーする**

以下は、Regalの `call.completed` イベントのサンプルペイロードです。

`````````json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
`````````

以下は、これをBrazeのカスタムイベントにマッピングするためのサンプルデータ変換です。

`````````
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
`````````

{% endtab %}
{% tab プロファイル属性を更新する %}

**Regalからの `contact.attribute.edited` イベントに基づいて、Brazeのプロファイル属性を更新する**

以下は、Regalの `contact.attribute.edited` イベントのサンプルペイロードです。このイベントは、いずれかのエージェントが会話で新しい情報を得て、連絡先のプロファイルの属性を更新するたびにトリガーされます。

`````````json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
`````````

以下は、Brazeプロファイルの関連属性に新しいカスタムプロパティ値をマッピングするためのサンプルデータ変換です：

`````````
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
`````````

{% endtab %}
{% tab 実験の同期を維持する %}

**`contact.experiment.assigned` イベントを使用してBrazeとRegalで実験の同期を維持する**

以下は、Regalの `contact.experiment.assigned` イベントのサンプルペイロードです。

`````````json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
`````````

以下は、これをBrazeのカスタムイベントにマッピングするためのサンプルデータ変換です。

`````````
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

`````````
{% endtab %}
{% tab 連絡先の配信停止 %}

**Regalの `contact.unsubscribed` に基づいて、Brazeで連絡先の配信停止を行う**

以下は、Regalの `contact.unsubscribed` イベントのサンプルペイロードです。

`````````json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
`````````

以下は、Brazeで連絡先の配信停止を行うサンプルデータ変換です。

`````````
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
`````````

{% endtab %}
{% endtabs %}