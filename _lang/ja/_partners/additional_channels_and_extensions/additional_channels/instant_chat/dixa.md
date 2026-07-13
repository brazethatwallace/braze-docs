---
nav_title: Dixa
article_title: Dixa
description: "この記事では、BrazeとDixaのパートナーシップについて概説します。"
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) は、チャット、メール、電話、ソーシャルメディアなどのコミュニケーションチャネルを単一のインターフェイスに統合することで、サポート体験を向上させるように設計された顧客サービスプラットフォームです。インテリジェントなルーティング、オートメーション、リアルタイムのパフォーマンスインサイトを通じて、企業が顧客満足度と効率性を向上させるのを支援します。

BrazeとDixaの統合により、カスタマーサービス担当者にリアルタイムのBrazeデータを提供することで、すべてのユーザーをより良く把握できます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dixaアカウント | このパートナーシップを活用するには、Dixa管理者アカウントが必要です。 |
| Braze REST APIキー | `users.export.ids` および `email.status` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

メール、Messenger、チャットなどのさまざまな通信チャネルでユーザーとコミュニケーションしている間に、Brazeデータをカスタマーサービスエージェントビューに表示します。さらに、Brazeのデータ変換を使用してDixaからBrazeにデータを送信し、ユーザーの問題を解決している間はマーケティングを一時停止したり、Dixaの満足度アンケートをセグメンテーションに活用したりできます。

## 統合 {#integration}

Dixa内で統合を設定するには、Dixa管理者である必要があります。Brazeとの統合は、Dixaで**Settings** > **Integrations** > **Braze**に移動します。

![Dixaの Brazeウィジェット作成ページ。ウィジェット名、API URL、APIキーを入力します。]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### ステップ1:Dixaで統合を作成する {#step-1-create-the-integration-in-dixa}

**Create Braze widget**ページで、以下の必須フィールドに入力して統合を作成します。

- **Widget name:** これは、後に会話サイドバーでタイトルとして使用される統合の名前です。
- **API URL:** インスタンスのBraze REST APIエンドポイントURLです。
- **API Key:** これは、前提条件で作成したBraze APIキーです。

### ステップ2:統合を設定する {#step-2-configure-the-integration}

次に、BrazeとDixaの統合を設定します。会話サイドバーのBrazeウィジェットの表示を調整するには、以下のオプションから選択します。

#### 会話サイドバーにウィジェットを表示する {#show-the-widget-in-the-conversation-sidebar}

この設定は、Dixaの会話サイドバー内の統合全体を表示または非表示にします。

統合の設定を行っている場合は、必須フィールドに入力する間、これをオフにすることをお勧めします。設定が完了したら、再びオンにすることで、Dixaのエージェントが統合を使用できるようになります。

#### 顧客の詳細を表示する {#display-customer-details}

ユーザーの詳細を表示するか非表示にするかを選択します。詳細には、ロケーション、メール、電話番号、メール購読の状態、プッシュ通知購読の状態、Brazeでの会員期間に関するデータが含まれます。

#### メール購読の状態を変更するボタンを表示する {#display-the-button-to-change-the-email-subscription-state}

ボタンは、`subscribed`、`opted-in`、`unsubscribed` というBrazeの3つの購読状態のいずれかに基づいています。ユーザーが `subscribed` の場合、エージェントは `opt-in` または `unsubscribe` を選択できます。ユーザーが `opted-in` または `unsubscribed` の場合、エージェントはこの2つの間でのみ切り替えることができます。

#### カスタム属性のリストを表示する {#display-a-list-of-custom-attributes}

ユーザーのBrazeカスタム属性の表示・非表示を選択します。

#### カスタムイベントのリストを表示する {#display-a-list-of-custom-events}

ユーザーのBrazeカスタムイベントの表示・非表示を選択します。

#### 購入リストを表示する {#display-a-list-of-purchases}

ユーザーが購入した製品リストの表示・非表示を選択します。ここでは、ユーザーがその製品を何回購入したかを確認できます。最初の購入日と最後の購入日を表示するには、アイテムにカーソルを合わせます。

### 統合の例 {#example-integration}

以下に統合の例を示します。

![ユーザーのメール購読状態、カスタム属性、カスタムイベント、購入を表示するDixaでのBrazeとDixaの統合。]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## データ変換ツール {#data-transformation-tool}

Dixaはwebhookを使用してBrazeにデータを送信します。webhookを設定するには、Dixa管理者である必要があります。

### Dixaでの会話を追跡する {#track-conversations-in-dixa}

最初のステップは、Brazeでデータ変換を作成することです。

1. **データ設定** > **データ変換** > **変換を作成**に移動します。
2. **ゼロから開始**を選択し、送信先として**POST: Track Users**を選択して、**変換を作成**を選択します。
3. 変換エディターで、このセクションの**データ変換ツールの例**からコードをコピーし、**変換コード**フィールドに挿入します。**保存**を選択し、**Webhook URL**をコピーして、Dixaを開きます。
4. Dixaで、**Settings** > **Integrations** > **Webhooks** > **+ Outbound webhook**に移動します。
5. Webhook設定ページで、BrazeからコピーしたURLを貼り付け、追跡したいイベントをトグルで有効にします。**Conversation created**は、顧客の会話を追跡するための良い出発点です。
6. **Save**を選択してDixaのセットアップを完了します。

### データ変換ツールの例 {#example-transformation-tool}

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```

### BrazeでCSATスコアを使用する {#use-csat-score-in-braze}

1. **データ設定** > **データ変換** > **変換を作成**に移動します。
2. **ゼロから開始**を選択し、送信先として**POST: Track Users**を選択して、**変換を作成**を選択します。
3. 変換エディターで、このセクションの**CSATスコアの追跡**からコードをコピーし、**変換コード**フィールドに挿入します。**保存**を選択し、**Webhook URL**をコピーして、Dixaを開きます。
4. Dixaで、**Settings** > **Integrations** > **Webhooks** > **+ Outbound webhook**に移動します。
5. Webhook設定ページで、BrazeからコピーしたURLを貼り付け、追跡したいイベントをトグルで有効にします。**Conversation created**は、顧客の会話を追跡するための良い出発点です。
6. **Save**を選択してDixaのセットアップを完了します。

#### CSATスコアの追跡 {#track-csat-score}

```js
const body = payload?.data;

// values from your webhook
const score = body.score;         // number
const comment = body.comment;     // string
const type = body.type;           // string
const ratedAt = body.event_timestamp;   // ISO 8601 string
const contactemail = body.conversation.requester.email;

// ALWAYS identify by email
const email = contactemail;

if (!email) {
  // Can't identify a user without email
  return { attributes: [] };
}


let brazecall = {
  "attributes": [
    {
      // Using the Dixa user email as the external_id to identify the user in Braze
      "email": contactemail,
      "_update_existing_only": true,

      // Your new custom object attribute
      "last_csat": {
        "score": score,
        "comment": comment,
        "type": type,
        "rated_at": ratedAt
      }
    }
  ]
};

return brazecall;
```
