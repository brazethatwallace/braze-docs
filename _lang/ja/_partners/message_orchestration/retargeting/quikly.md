---
nav_title: Quikly
article_title: Quikly
description: "このリファレンス記事では、BrazeとQuiklyのパートナーシップについて説明しています。Quiklyは緊急マーケティングプラットフォームであり、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速することができます。"
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> 緊急マーケティングプラットフォームである[Quikly](https://www.quikly.com)は、心理学を利用して消費者のモチベーションを高めるため、ブランドは主要なマーケティング施策のレスポンスを即座に高めることができます。

_この統合はQuiklyによって管理されています。_

## 統合について {#about-the-integration}

BrazeとQuiklyのパートナーシップにより、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速させることができます。Quiklyは、緊急性の心理学を利用して、消費者を楽しく、そして即座に動機付けることでこれを実現します。たとえば、ブランドがQuiklyを使用して、新しいメールやSMSサブスクライバーをBrazeに直接取り込んだり、モバイルアプリのダウンロードなどの他の重要なマーケティング目標の達成を促進したりできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Quiklyアカウント | このパートナーシップを利用するには、[Quikly](https://www.quikly.com)ブランドパートナーアカウントが必要です。 |
| Braze REST APIキー | `users.track`、`subscription.status.set`、`users.export.ids`、`subscription.status.get`の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
| Quikly APIキー（オプション） | クライアントサクセスマネージャーから提供されるQuikly APIキー（Webhookのみ）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

Quiklyを使用すると、ブランドはメールまたはSMSサブスクライバーの獲得を加速し、サブスクライバーがBraze内で直接ファーストパーティデータを提供するように促すことができます。またBrazeを使用して、Quiklyアクティベーションで離脱した顧客をターゲットにし、そのオーディエンスを再アクティブ化して維持することもできます。さらに、マーケターはこの統合を使用して、特定のカスタマージャーニーイベントに独自の報酬構造でインセンティブを与えることができます。

以下に例を示します。
 - 消費者が[Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype)でエキサイティングな報酬を獲得できるチャンスのためにオプトインすると、期待とエンゲージメントが日に日に高まります。ファーストパーティデータは自動的にBrazeにプッシュされます。
 - [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap)を使用して、消費者の反応の速さ、他者との比較ランキング、ランダム、または時間や数量がなくなる前に基づく独自のリアルタイムオファーで、新しいメールまたはSMSサブスクライバーの獲得を加速します。
 - Webhookを使用した独自の報酬構造で、カスタマージャーニーの特定のステップを促します。
 - Quiklyアクティベーションに参加すると、ユーザーのプロファイルにカスタム属性やイベントが適用されます。

## 統合 {#integration}

このセクションでは、メール取得、SMS取得、カスタム属性、およびWebhookの4つの異なる統合について説明します。選択する統合は、Quiklyのアクティベーションとユースケースに応じて異なります。

{% tabs %}
{% tab メール取得 %}

### メール取得 {#email-acquisition}

Quiklyのアクティベーションが顧客のメールアドレスやプロファイルデータを収集する場合、唯一必要なステップはQuiklyにREST APIキーとエンドポイントを提供することです。Quiklyがブランドアカウントを設定してこのデータをBrazeに渡します。追加のユーザー属性を含めたい場合は、API認証情報をQuiklyに提供する際にその旨をお伝えください。

以下は、Quiklyがこのワークフローを実行する方法の概要です。
1. Quiklyのアクティベーションに参加すると、Quiklyは指定された`email_address`を持つユーザーが存在するかどうかを確認するために[エクスポートAPI]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を使用してユーザー検索をスケジュールします。
2. ユーザーをログまたは更新します。
  - ユーザーが存在する場合:
    - 新しいプロファイルを作成しません。
    - 必要に応じて、Quiklyはユーザーがアクティベーションに参加したことを示すために、ユーザーのプロファイルにカスタム属性を記録できます。
  - ユーザーが存在しない場合:
    - Quiklyは、Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照します（ユーザーにはexternal IDがないため）。
    - 必要に応じて、Quiklyはカスタムイベントをログに記録して、このプロファイルがQuiklyアクティベーションに参加したことを示すことができます。

{% details /users/track request %}

#### リクエストヘッダー {#request-headers}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### リクエストボディ {#request-body}
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMSサブスクリプション %}

### SMSサブスクリプション {#sms-subscriptions}

Quiklyアクティベーションは、顧客から直接携帯電話番号を収集して新しいSMS購読を開始できます。この統合を有効にするには、Quiklyクライアントサクセスマネージャーに`subscription_group_id`を提供してください。購読グループの`subscription_group_id`にアクセスするには、**購読グループ**ページに移動します。

Quiklyは顧客の電話番号を使用して購読検索を実行し、SMS購読が既に存在する場合はアクティベーションで自動的にクレジットを付与します。それ以外の場合は、新しい購読が開始され、購読ステータスが確認された後、顧客にクレジットが付与されます。

顧客がQuiklyで携帯電話番号と同意を提供する際の全体的なワークフローは次のとおりです。
1. Quiklyは、[購読グループステータス]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を使用して購読検索を実行し、指定された`phone`が`subscription_group_id`に購読されているかどうかを確認します。購読が存在する場合、Quiklyアクティベーションでユーザーにクレジットを付与します。さらなるアクションは必要ありません。
2. Quiklyは、[識別子によるユーザープロファイルのエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を使用してユーザー検索を実行し、指定された`email_address`でユーザープロファイルが存在するかどうかを確認します。ユーザーが存在しない場合、Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照できるようにします（ユーザーにはexternal IDがないため）。
3. [ユーザーの購読グループステータスの更新エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を使用して購読ステータスを更新します。

既存のダブルオプトインSMS購読ワークフローをサポートするために、Quiklyはこのセクションの標準ワークフローの代わりにカスタムイベントをBrazeに送信できます。この場合、購読ステータスを直接更新するのではなく、[カスタムイベントによってダブルオプトインプロセスがトリガーされ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)、購読ステータスが定期的に監視され、ユーザーが完全にオプトインしたことを確認してからQuiklyアクティベーションでクレジットが付与されます。

{% alert important %}
Brazeでは、`/users/track`エンドポイントを使用して新しいユーザーを作成する場合、Brazeがユーザープロファイルを完全に作成するための時間を確保するために、関連する購読グループにユーザーを追加するまでに約2分の遅延を設けることを推奨しています。
{% endalert %}

{% details Detailed /subscription/status/set request %}
#### リクエストヘッダー
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### リクエストボディ
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab カスタム属性 %}
### カスタム属性 {#custom-attributes}

Brazeの実装によっては、Quiklyアクティベーション内のイベントをBrazeを通じてカスケードさせ、さらに処理することを検討する場合があります。たとえば、Quiklyアクティベーションで達成したレベルやインセンティブに基づいてカスタムユーザー属性を適用し、アプリを開いたときやWebサイトにログインしたときに関連するContent Cardsを表示することができます。これらの統合を実装するためにQuiklyがお客様と直接協力します。

{% endtab %}
{% tab Webhook %}
### Webhook {#webhooks}
Webhookを使用して、カスタマージャーニーの特定のイベントに対するインセンティブをトリガーします。たとえば、ユーザーがアプリにログインしたとき、プッシュ通知をオンにしたとき、またはストアロケーターを使用したときのBrazeイベントがある場合、Webhookを使用して、特定のQuiklyアクティベーションの設定に基づき、そのユーザーへのカスタムオファーをトリガーできます。たとえば、カスタムオファーでアクション（アプリへのログインなど）を実行した最初のX人のユーザーに報酬を与える、または即座の応答を促すために時間の経過に伴い価値が減少するオファーを提供するなどの戦術があります。

### BrazeでQuiklyのWebhookを作成する {#create-a-quikly-webhook-in-braze}

将来のキャンペーンやキャンバスのためにQuiklyのWebhookテンプレートを作成するには、Brazeプラットフォームの**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

QuiklyのWebhookキャンペーンを一度だけ作成するか、既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択してください。

**空白テンプレート**を選択し、Webhook URLとリクエストボディに次の内容を入力します。
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **リクエストボディ**: JSONキー/値のペア

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Quiklyでは認証に`HTTP Header`が必要です。

- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### リクエストボディ

***JSONキー/値のペア***を選択し、次のペアを追加します。
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### リクエストをプレビューする {#preview-your-request}

**プレビュー**パネルでリクエストをプレビューするか、`Test`タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、Webhookをテストするために独自のユーザーをカスタマイズできます。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を作成するときに、**保存済みWebhookテンプレート**リストで見つけることができます。
{% endalert %}

{% endtab %}
{% endtabs %}

## サポート {#support}
ご質問はQuiklyのクライアントサクセスマネージャーまでお問い合わせください。