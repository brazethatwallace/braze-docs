---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "このリファレンス記事では、BrazeとFacebook Messengerのパートナーシップについて説明します。Facebook Messengerは、世界で最も人気があるインスタントメッセージプラットフォームの1つです。"
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/)は、世界で最も人気があるインスタントメッセージングプラットフォームの1つで、1か月あたりのアクティブユーザー数は10億にのぼります。ブランドはこのプラットフォームで、顧客とインテリジェントかつ自動的にやり取りするための魅力的なチャットボットを作成できます。

BrazeとFacebookの統合では、Messenger Platform APIを介してFacebook Messengerのユーザーにメッセージを送信するために、Brazeのwebhook、セグメンテーション、パーソナライゼーション、トリガー機能が利用されます。カスタムFacebook Messengerのwebhookテンプレートは、Brazeプラットフォームの**コンテンツ** > **Webhook**にあります。

Facebook Messengerプラットフォームは、「既存の取引を促進し、他の顧客サポートアクションを提供し、個人が要求したコンテンツを配信する非プロモーションメッセージ」を対象としています。詳細については、[Facebookのプラットフォームガイドライン](https://developers.facebook.com/docs/messenger-platform)と[許容可能なユースケースの例](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)を参照してください。

## 前提条件 {#prerequisites}

統合を進める前に、以下を確認してください。

- Facebookでは、マーケティングメッセージの送信にMessengerプラットフォームを使用することを許可していません。
- お客様のページからのメッセージに対するユーザーの明示的な許可が必要になります。
- Facebookアプリのテストユーザーではないユーザーにメッセージを送信するには、アプリがFacebookの[アプリレビュー](https://developers.facebook.com/docs/messenger-platform/app-review)に合格する必要があります。<br><br>

| 必要条件| 提供元| アクセス| 説明|
| --- | --- | --- | --- |
| Facebook Messengerページ| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Facebookページがボットの IDとして使用されます。アプリとチャットすると、ページ名とプロフィール画像が表示されます。|
| Facebook Messengerアプリ| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Facebookアプリには、アクセストークンなどのMessengerボットの設定が含まれています。
| アプリボットの審査と承認 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | ボットを公開する準備ができたら、審査と承認を受けるためにFacebookに提出する必要があります。この審査プロセスにより、MessengerボットがFacebookのポリシーを遵守し、期待どおりに機能することが確認され、Messengerのすべてのユーザーに公開されます。 |
| ページスコープID (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Facebook Messengerでメッセージを送信するには、ユーザーのPSIDが必要です。ユーザーがMessengerを介してアプリとやり取りするときに、FacebookによってPSIDが作成されます。このPSIDは、文字列カスタム属性としてBrazeに送信できます。
| ページアクセストークン | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | これらのアクセストークンは、Facebook Pageに属するデータの読み取り、書き込み、変更を行うAPIに権限を付与する点を除き、ユーザーアクセストークンと似ています。ページアクセストークンを取得するには、ユーザーアクセストークンを取得し、`manage_pagespermission`を要求する必要があります。ユーザーアクセストークンを取得したら、Graph APIを使用してページアクセストークンを取得できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="前提条件" }

## 統合 {#integration}

以下に、Braze Facebook Messengerのwebhookの設定方法を示します。
ボットのセットアップに追加のヘルプが必要な場合は、[Braze GitHubリポジトリ](https://github.com/Appboy/appboy-fb-messenger-bot)に完全なMessengerボットチュートリアルとサンプルコードがあります。

### ステップ1:PSIDを収集する {#step-1-collect-your-psids}

Facebook Messengerでメッセージを送信するには、ユーザーを識別し、一貫したやり取りを行うためにユーザーのページ固有のID（PSID）を収集する必要があります。PSIDはユーザーのFacebook IDとは異なります。顧客にメッセージを送信する場合または顧客からメッセージが送信される場合は常に、Facebookによりこの識別子が作成されます。

PSIDは、Facebookが提供するさまざまな[エントリポイント](https://developers.facebook.com/docs/messenger-platform/discovery)の1つを使用して確認できます。ユーザーがアプリにメッセージを送ったり、ボタンをタップしたり、メッセージを送信したりといった対話のアクションを行った後は、そのPSIDがwebhookイベントの`sender.id`プロパティに含まれるため、ボットはアクションを行った人を識別できます。

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

メッセージを送信するたびに、そのPSIDがリクエストの`recipient.id`プロパティに含まれ、メッセージを受信するユーザーを識別します。

### ステップ2:カスタム属性としてBrazeに送信する {#step-2-send-to-braze-as-a-custom-attribute}

PSIDを受信していると確信したら、これを開発者と調整して共有し、[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#custom-attributes)としてPSIDをBrazeに送信します。PSIDは、[APIコール](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages)でアクセスできる文字列です。

### ステップ3:webhookテンプレートをセットアップする {#step-3-set-up-your-webhook-template}

Facebook Messengerのwebhookテンプレートを作成するには:

1. **コンテンツ** > **Webhook**に移動し、**webhookテンプレートを作成**を選択します。
2. **テンプレート** > **Brazeテンプレート**を選択します。
3. 「Facebook Messenger」テンプレートを見つけて選択します。
4. **テンプレートを選択**を選択します。

1. テンプレートの名前を入力し、必要に応じてチームとタグを追加します。
2. メッセージを入力するか、[Facebookで利用可能なメッセージテンプレート](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)からメッセージテンプレートを選択します。また、メッセージの[タイプ](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types)や[タグ](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)を選択することもできます。
3. カスタム属性としてPSIDを含めます。これを行うには、**Request Body**ボックスの隅にある、青と白の**+**ボタンを使用します。
3. `FACEBOOK_PAGE_ACCESS_TOKEN`をトークンに置き換えて、webhook URLにページアクセストークンを追加します。

#### webhookのプレビューとテスト {#previewing-and-testing-your-webhook}

メッセージを送信する前に、webhookをテストしてください。Messenger IDがBrazeに保存されていることを確認し（または、それを見つけてカスタマイズしたユーザーとしてテストし）、プレビューを使用してテストメッセージを送信します。

![Facebook Messengerのwebhookテンプレートの「Test」タブ。既存のユーザーにメッセージを送信することでそのメッセージをプレビューできます。]({% image_buster /assets/img_archive/fbm-test.png %})

メッセージが正常に受信された場合は、配信設定を構成できます。

## この統合を使用する {#using-this-integration}

セットアップが完了したら、この統合を使用してFacebook Messengerユーザーをターゲットにします。ユーザーの電話番号を使用してメッセージを送信しておらず、Messengerメッセージを繰り返し送信する予定がある場合は、Messenger IDがカスタム属性として存在するすべてのユーザーに対して[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)し、[分析トラッキング]({{site.baseurl}}/user_guide/audience/segments/segment_data)をオンにして、Messengerの購読率を経時的にトラッキングする必要があります。

![セグメントフィルター「messenger_id」が「is not blank」に設定されています。]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Messengerサブスクライバー向けの特定のセグメントを作成しない場合は、エラーを避けるために、既存のMessenger IDのフィルターを必ず含めてください。

他のセグメンテーションを使用してMessengerキャンペーンをターゲットにし、他のキャンペーンと同様にそれ以降のキャンペーン作成プロセスを実行することもできます。