---
nav_title: 統合
article_title: オンボーディング統合の概要
page_order: 8
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# 統合 {#integration}

> Brazeとの統合は価値あるプロセスです。しかし、あなたは賢い方です。あなたは**ここに**います。明らかに、あなたはすでにそれを知っています。しかし、おそらくあなたが知らないことは、あなたと開発者がこれから一緒に旅に出ようとしているということです。この旅には、技術的な専門知識、戦略的な計画、そして両者間の調整に役立つ一貫したコミュニケーションが必要です。

{% alert note %}
なお、この記事の内容はメールには当てはまりません。[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup)のセクションで確認してください。
{% endalert %}

## 統合プロセスの技術的な側面 {#the-technical-side-of-the-integration-process}

「開発者は魔法使い！何でもできるから、全部任せればいい！」と思っているかもしれません。おそらくその通りでしょう！しかし、彼らが裏で何をしているかを知っておくべきでないという理由はありません。むしろ、いつ情報を提供すべきか、「APIキーとAPIエンドポイントを送ってもらえますか？」と言われたときに何を探すべきかを把握しておけば、プロセス全体がスムーズに進みます。

では、開発者がBrazeをアプリやサイトに統合するとき、何をしているのでしょうか？よくぞ聞いてくれました！

### ステップ1: Braze SDKの実装 {#step-1-they-implement-the-braze-sdk}

Braze SDK（ソフトウェア開発キット）は、アプリやサイトとの間で情報を送受信するための仕組みです。エンジニアは、基本的に双方のアプリを連携させています。これを行うには、いくつかの重要な情報が必要です。

* [APIキー]({{site.baseurl}}/api/basics)
* [SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Brazeではカスタムエンドポイントの提供を終了していますので、事前に定義されたSDKエンドポイントを使用してください。既存のカスタムエンドポイントが提供されている場合は、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup)、[iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)、および[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk)統合の設定ステップをご覧ください。

この情報を直接渡すか、アカウントを作成してBrazeへのアクセスを提供することもできます。

{% alert warning %}
あなたと開発者が、意図せずまたは不注意でBrazeの会社認証情報を変更しないようにしてください。変更すると、実装プロセスで問題が発生したり、アカウントからロックアウトされたりする可能性があります。
{% endalert %}

### ステップ2: 希望するメッセージングチャネルの実装 {#step-2-they-implement-your-desired-messaging-channels}

Brazeには、ユーザーに連絡するための多くのオプションがあり、それぞれが期待どおりに動作するための独自の設定や調整が必要です。ここで、エンジニアとのコミュニケーションが非常に重要になります。

使用したいチャネルを開発者に必ず伝えて、実装が効率的かつ適切な順序で行われるようにしましょう。

| チャネル | 詳細 |
|---|---|
| アプリ内メッセージ | SDKの実装に加えて、チャネル固有のステップが必要です。 |
| プッシュ | メッセージング認証情報とプッシュトークンの適切な処理を行うために、SDKの実装が必要です。 |
| メール | これはまったく異なるプロセスです。統合の詳細については、[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup)セクションをご覧ください。 |
| Content Cards | [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)を始めるには、Brazeのカスタマーサクセスマネージャーにお問い合わせください。 |
| SMS & MMS | 統合の詳細については、[SMS設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending)セクションをご覧ください。 |
| Webhook | SDKの実装に加えて、チャネル固有のステップが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: 希望するメッセージングチャネルの実装" }

{% alert tip %}
Brazeを使用して、各チャネルでアクセシブルなメッセージングキャンペーンを作成できます。開発者と協力して、実装がアクセシビリティ基準を満たしていることを確認してください。
{% endalert %}

### ステップ3: データの設定 {#step-3-they-set-up-your-data}

Brazeは一芸だけのプラットフォームではありません。単にメールやプッシュを送るだけのものではありません。すべてのユーザーや顧客にとってユニークなパーソナライズされたカスタマージャーニーを作成するためのものです。カスタマージャーニーは、アプリやサイト内での行動に基づいており、その行動を定義するのはあなた自身です！開発者の次のタスクは、アプリやサイト内で行われたアクションがBrazeで取得されるようにすることです。

では、この情報を開発者に提供するために何をすべきでしょうか？

1. マーケティングチームと協力して、追跡が必要なキャンペーン、目標、属性、イベントを定義します。それらのユースケースを定義し、チームと共有します。
2. カスタムデータの要件を定義します（[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)など）。
3. そこから、そのデータをどのように追跡すべきか（SDK経由でトリガーするなど）を検討します。
4. 必要な[ワークスペース]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)の数を定義します。エンジニアはこれらのワークスペースを[テストおよび設定]({{site.baseurl}}/user_guide/get_started/workspaces)する方法を知っておく必要があります。

これらの情報がすべて揃ったら、エンジニアと共有してください。エンジニアはその情報を元に[カスタムデータ]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)を実装します。[ユーザーのインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)が必要になる場合もあります。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)についても把握しておくべきです。

### ステップ4: 要件に基づいたカスタマイズ {#step-4-they-customize-based-on-what-you-want}

APIトリガーによる起動やConnected Contentなどの機能が必要な場合は、Brazeの担当者と開発者の両方と相談して、アプリやBrazeの外部にあるデータをメッセージに取り込めるようにしてください。

### ステップ5: 実装のQAを共同で実施 {#step-5-you-both-perform-qa-on-your-implementation}

エンジニアと協力して、すべてが正しく動作することを確認してください。[テストメッセージ]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を送信し、[Android用テストアプリ]({{site.baseurl}}/developer_guide/references?tab=android)や[iOS用テストアプリ]({{site.baseurl}}/developer_guide/references?tab=swift)を使用して、送信を開始する前にすべての項目を確認しましょう！

[AndroidまたはFireOSの統合テスト]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)や[iOSのプッシュテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing)に関する具体的な手順もご用意しています。

## 実装後 {#after-implementation}

実装の完了は、一度に100万通のメッセージを送信してよいという合図ではないことに注意してください。すべての顧客が同時に同じリンクをクリックした場合、100万通のプッシュを送信するとアプリが停止する可能性があります。**送信**ボタンをクリックする前に、Brazeからのリクエストを処理するための内部セットアップの容量について話し合うことをお勧めします。その上で、それに基づいて[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting)を設定できます。

![Braze Firebrands コミュニティロゴ]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Brazeの使用に慣れてきたら、Braze Firebrandになることを検討してみてください！Braze Firebrands は、Brazeを使用して顧客体験とマーケティングを革新する変革者たちのコミュニティです。詳しく知りたいですか？[今すぐ参加](https://brazefirebrands.splashthat.com/)してください。