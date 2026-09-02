---
nav_title: Regal
article_title: Regal
description: "このリファレンス記事では、BrazeとRegalのパートナーシップについて説明しています。Regalは音声AIエージェントプラットフォームであり、BrazeのデータとRegalの会話を活用して、パーソナライズされたオムニチャネルのカスタマージャーニーをオーケストレーションできます。"
alias: /partners/regal/
page_type: partner
search_tag: Partner
---

# Regal

> [Regal.io](https://regal.io)は音声AIエージェントプラットフォームであり、チャネル横断でインテリジェントなリアルタイム会話を通じて、企業がより優れた顧客体験を推進できるよう支援します。

_この統合はRegalによって管理されています。_

RegalとBrazeを統合することで、行動データと会話型AIを統合し、パーソナライズされたオムニチャネルのカスタマージャーニーをオーケストレーションできます。Brazeはカスタマーライフサイクル全体のシグナルをキャプチャし、RegalはそれをAIエージェントの会話、ルーティング、リアルタイムの意思決定に活用します。

Brazeのデータを使用して、AIエージェントが何を話すか、どのように応答するか、いつエンゲージするかを形成できます。会話の結果やインサイトをBrazeに送り返すことで、ターゲティングやライフサイクルマーケティングを改善できます。カスタマージャーニーの重要なタイミングでAI搭載の通話やSMSをトリガーし、各会話の結果に基づいてBrazeでフォローアップを行います。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Regal アカウント | このパートナーシップを利用するには、Regal アカウントが必要です。 |
| Regal API キー | Regal API キーを使用すると、Brazeから Regal にイベントを送信できます。<br><br>このキーを取得するには、[support@regal.io](mailto:support@regal.io) にメールでお問い合わせください。 |
| Braze データ変換 | Regal からデータを受信するには、[データ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携：BrazeからRegalへのデータ送信 {#integration-sending-data-from-braze-to-regal}

Brazeキャンバスまたはキャンペーンwebhookを使用して、顧客プロファイルとイベントデータをBrazeからRegalに送信します。

### ステップ1：Regalで新しいコンタクトを作成する {#step-1-create-new-contacts-in-regal}

Regalで通話やテキストに利用できる新しいBrazeプロファイルが作成されるたびに、Regalにwebhookを送信するキャンバスまたはキャンペーンを作成します。

1. 「Create New Contact for Regal」というタイトルのキャンバスまたはキャンペーンを作成し、エントリタイプとして**アクションベース**を選択します。

2. トリガーロジックを**カスタムイベント**に設定し、電話番号付きのプロファイルが作成されたときに発火するイベントを選択します。Regalでは、電話フィールドが設定されていることを確認するフィルターも追加することを推奨しています。

3. 新しいwebhookテンプレートで、以下のフィールドを入力します。
   - **Webhook URL**：<https://events.regalvoice.com/events>
   - **リクエストボディ**：Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Regalでは認証用のHTTPヘッダーとHTTPメソッドも必要です。以下は**設定**タブのキーと値のペアとしてテンプレートに含まれています。
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
    - **Authorization**：`{{<REGAL_API_KEY>}}`
    - **Content-Type**：application/json
{% endraw %}

#### リクエストボディ {#request-body}

必須の識別子は`traits.phones`内の電話番号のみです。`traits.phones`オブジェクトを使用して、1つ以上の電話番号をコンタクトに関連付けます。各電話番号には、独自のラベル、プライマリ指定、音声およびSMSのオプトインステータスを保存できます。この構造は、コンタクトが複数の電話番号を持つ場合に特に便利です。

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

このペイロード例では、記載されている電話番号に現在の音声およびSMSの同意ステータスが含まれていることを前提としています。これが該当しない場合は、コンタクトを作成する際に`voiceOptIn`と`smsOptIn`を省略し、オプトインが収集された時点で該当する電話番号の同意を更新する別のキャンバスまたはキャンペーンを設定できます。

### ステップ2：オプトイン情報を更新する {#step-2-update-opt-in-information}

アプリ内でオプトインとオプトアウトが異なるタイミングで発生する可能性がある場合は、ユーザーが購読ステータスを変更したときにRegalを更新します。

Regalでは、コンタクトレベルではなく電話番号ごとにオプトインとオプトアウトを管理できるよう、`traits.phones`スキーマの使用を推奨しています。

以下のキャンバス設定を使用して、最新のオプトイン情報をRegalに送信します。

1. 「Send Opt In or Out to Regal」というタイトルの新しいキャンバスまたはキャンペーンを作成します。

2. 以下のトリガーオプションのいずれかを選択し、ユーザーのオプトインステータスを表すフィールドを選択します。
    - **ユーザープロファイルフィールドの更新**
    - **購読グループステータスの更新**
    - **購読ステータス**

3. 新しいwebhookテンプレートで、以下のフィールドを入力します。
   - **Webhook URL**：<https://events.regalvoice.com/events>
   - **リクエストボディ**：Raw Text

#### リクエストヘッダーとメソッド

Regalでは認証用のHTTPヘッダーとHTTPメソッドも必要です。以下は**設定**タブのキーと値のペアとしてテンプレートに含まれています。
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**：
    - **Authorization**：`{{<REGAL_API_KEY>}}`
    - **Content-Type**：application/json
{% endraw %}

#### リクエストボディ

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

このペイロードに追加のユーザープロファイル属性を含めて、他の属性も同時に最新の状態に保つことも可能です。

### ステップ3：カスタムイベントを送信する {#step-3-send-custom-events}

Regalに送信する各主要イベントに対して、キャンバスまたはキャンペーンを設定します。

これらのイベントは、アウトリーチのトリガー（例えば、リードがサインアップを完了した際の確認テキスト）以上の役割を果たします。Regal AIエージェントが会話する方法、意思決定を行う方法、カスタマージャーニー全体を通じて会話をルーティングする方法を支えるリアルタイムのコンテキストを提供します。Brazeからイベントデータと属性を送信することで、AIエージェントが各ユーザーの行動、好み、ライフサイクルステージに基づいて会話を適応できるようになります。

例えば、BrazeのイベントとAttributeは、Regalで以下のように使用できます。

- **AIエージェントの発話をパーソナライズする**：最近の行動や商品への関心を会話内で直接参照します。
  - 例：ユーザーが生命保険のオプションを検討した場合、エージェントは会話の中で`contact.firstName`と`contact.brazeProductInterest`を参照できます。
- **ダイナミックな会話ロジックを駆動する**：エージェントがリアルタイムで優先すべき内容を調整します。
  - 例：`contact.brazeAge`が65を超える場合、Medicareの補償を優先します。それ以外の場合は、ACAプランと現在の保険ステータスに焦点を当てます。
- **インテリジェントなルーティングとエスカレーションを可能にする**：価値やインテントに基づいて会話をルーティングします。
  - 例：`contact.brazeLeadTier`が「High Value」の場合、資格審査後にシニアエージェントに転送します。それ以外の場合は、AIエージェントで続行します。
- **メッセージングとオファーを一致させる**：キャンペーンのコンテキストに基づいて、エージェントが提示する内容を調整します。
  - 例：`contact.brazeCampaignName`が「Spring Mortgage Promo」の場合、会話中にプロモーションオファーをハイライトします。

「Send Product Interest Event to Regal」というタイトルの新しいキャンバスまたはキャンペーンを作成します。

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### 最新のコンタクト属性 {#up-to-date-contact-attributes}

Regalでは、主要なイベントが発生した際にRegalが最新のコンタクト属性を保持できるよう、イベントペイロードに主要なユーザープロファイル属性を含めて送信することも推奨しています。

{% alert note %}
Regalに送信するイベントや、これらのキャンバスやキャンペーンの設定方法についてご質問がある場合は、[support@regal.io](mailto:support@regal.io)までメールでお問い合わせください。
{% endalert %}

## インテグレーション: Regal から Braze へのデータ送信 {#integration-sending-data-from-regal-to-braze}

Regal のレポート用 Webhook と Braze のデータ変換を使用して、Regal のレポートイベント（`SMS.sent` や `call.completed` など）を Braze に送信します。これらのイベントをマッピングすると、ユーザープロファイルに表示され、セグメンテーション、キャンバス、キャンペーンに利用できるようになります。

### ステップ1: Braze でデータ変換を作成する {#step-1-create-a-data-transformation-in-braze}

Braze に送信する予定の Regal Webhook ごとに、1つのデータ変換を作成します。

データ変換を作成するには:
1. Braze ダッシュボードで **Transformations** ページに移動します。
2. 変換に名前を付け、**Create transformation** をクリックします。
3. 変換のリストから <i class="fa-solid fa-ellipsis-vertical" title="アクションを表示"></i> **View actions** を選択し、**Copy webhook URL** を選択します。

### ステップ2: Regal でレポート用 Webhook を有効にする {#step-2-enable-reporting-webhooks-in-regal}

レポート用 Webhook を設定するには:
1. Regal アプリに移動し、**Settings** ページを開きます。

2. **Reporting Webhooks** セクションで **Create Webhooks** をクリックします。

3. Webhook エンドポイントの入力欄に、対応するデータ変換の Braze データ変換 Webhook URL を追加します。

#### エンドポイントの更新 {#updating-an-endpoint}

エンドポイントを編集した場合、キャッシュが更新されて新しいエンドポイントにイベントが送信されるまで最大5分かかることがあります。

#### リトライ {#retries}

現在、Regal はこれらのイベントのリトライを行いません。Braze が5秒以内に応答しない場合、Regal はそのイベントを破棄します。Regal は将来のリリースでリトライ機能を追加する予定です。

#### イベント {#events}
レポートイベントの完全なリスト、プロパティの定義、サンプルペイロードについては、Regal の [Reporting Webhooks ガイド](https://developer.regal.io/docs/reporting-webhooks#events)を参照してください。

### ステップ3: Regal のイベントを Braze のイベントに変換する {#step-3-transform-regal-events-into-braze-events}

Braze の[データ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)機能を使用すると、受信した Regal のイベントを、Braze で属性、イベント、または購入として追加するために必要な形式にマッピングできます。

1. データ変換に名前を付けます。イベント Webhook ごとにデータ変換を設定することをお勧めします。

2. 接続をテストするには、Regal エージェントデスクトップからご自身の電話にアウトバウンドコールを作成し、会話サマリーフォームを送信して `call.completed` イベントを作成します。

3. Regal のコンタクトを Braze のプロファイルにマッピングするために使用する識別子を決定します。Regal のイベントで使用可能な識別子は次のとおりです:
   - `userId` - 以前にこの識別子をコンタクトに送信した場合にのみ、イベントに設定されます
   - `traits.phone`
   - `traits.email` - 以前にこの識別子をコンタクトに送信した場合にのみ、イベントに設定されます

Braze から Regal へのイベントペイロードでは、複数の電話番号と電話レベルの同意をサポートするために `traits.phones` を使用することを Regal は推奨しています。Braze に送り返される Regal のレポートイベントでは、イベントペイロードの識別子として `traits.phone` が引き続き表示される場合があります。

#### Braze がサポートする識別子 {#braze-supported-identifiers}
- Braze は電話番号を識別子としてサポートしていません。電話番号を識別子として使用するには、Braze で[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)として設定できます。
- Braze のデータ変換を使用する場合、メールアドレスを識別子として使用できます。メールアドレスが Braze 内のプロファイルとして存在する場合、既存のプロファイルが更新されます。メールアドレスが Braze 内にまだ存在しない場合、メールのみのプロファイルが作成されます。

## ユースケース {#use-cases}

{% tabs %}
{% tab メールをトリガーする %}

**Regal の通話結果に基づいて Braze からメールをトリガーする**

以下のサンプルペイロードは、Regal の `call.completed` イベントを示しています。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Alex",
    "agent_fullname": "Alex Lee",
    "agent_id": "xxxx@example.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+15555550200",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+15555550123",
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
```

以下のサンプルデータ変換は、これを Braze のカスタムイベントにマッピングします。

```
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
```

{% endtab %}
{% tab プロファイル属性を更新する %}

**Regal の `contact.attribute.edited` イベントに基づいて Braze のプロファイル属性を更新する**

以下のサンプルペイロードは、Regal の `contact.attribute.edited` イベントを示しています。Regal は、エージェントが会話中にコンタクトのプロファイルの属性を更新した際にこのイベントを送信します。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@example.com",
    "contact_phone": "+15555550123",
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
```

以下のサンプルデータ変換は、新しいカスタムプロパティ値を Braze プロファイルの関連する属性にマッピングします。

```
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
```

{% endtab %}
{% tab 実験を同期する %}

**`contact.experiment.assigned` イベントを使用して Braze と Regal の実験を同期する**

以下のサンプルペイロードは、Regal の `contact.experiment.assigned` イベントを示しています。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
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
```

以下のサンプルデータ変換は、これを Braze のカスタムイベントにマッピングします。

```
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

```
{% endtab %}
{% tab コンタクトを購読解除する %}

**Regal の `contact.unsubscribed` イベントに基づいて Braze でコンタクトを購読解除する**

以下のサンプルペイロードは、Regal の `contact.unsubscribed` イベントを示しています。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com",
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
```

以下のサンプルデータ変換は、Braze でコンタクトを購読解除します。

```
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
```

{% endtab %}
{% tab 通話分析からフォローアップをトリガーする %}

**Regal の `call.analysis.available` イベントに基づいて Braze でカスタマイズされたフォローアップジャーニーをトリガーする**

Regal の `call.analysis.available` イベントを使用して、顧客がコンバージョンしなかった主な理由を特定し、Braze でカスタマイズされたフォローアップジャーニーをトリガーします。

例:

- 主な反対理由が価格の場合、価値訴求型のフォローアップメールを送信します。
- 主な反対理由がタイミングの場合、後日再検討するためのナーチャーシーケンスにユーザーを配置します。
- 主な反対理由が信頼性の場合、お客様の声、評価、またはコンプライアンスに関する安心情報を送信します。
- `needs_human_agent` が true の場合、セールスまたはサポートチームに通知し、自動メッセージングを抑制します。

以下のサンプルペイロードは、Regal の `call.analysis.available` イベントを示しています。

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@example.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@example.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@example.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@example.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

データ変換を使用して、`call_analysis` フィールド（`primary_objection` や `needs_human_agent` など）を Braze のカスタムイベントまたはプロファイル属性にマッピングします。次に、それらの値に基づいて分岐するキャンバスまたはキャンペーンのロジックを Braze で構築します。

{% endtab %}
{% tab 通話トランスクリプトリンクを保存する %}

**`call.transcript.available` イベントのトランスクリプトリンクでプロファイル属性を更新する**

`call.transcript.available` イベントを使用して、完全な通話トランスクリプトへのリンクを Braze に送信します。データ変換でトランスクリプト URL を Braze ユーザープロファイル属性にマッピングすることで、チームがユーザープロファイルから会話にアクセスしてレビューできるようになります。

以下のサンプルペイロードは、Regal の `call.transcript.available` イベントを示しています。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@example.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Alex Smith",
    "contact_phone": "+15555550123",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}