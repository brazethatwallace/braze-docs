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

## 統合プロセスの技術的側面 {#the-technical-side-of-the-integration-process}

こんなふうに思うかもしれません。「うちの開発者は魔法使いだ！何でもできるから、いつも任せているんだ！」。そして、彼らはおそらく実際にそうであり、おそらくそれができるでしょう！しかし、彼らが舞台裏で何をしているのか、あなたが知らない理由はありません。実際、彼らが「APIキーとAPIエンドポイントを送ってもらえますか？」と言ったときに、いつ情報を持って飛び込むべきか、何を探すべきかを知っていれば、プロセス全体の助けになるでしょう。

では、Brazeをあなたのアプリやサイトに統合するとき、彼らは何をしているのでしょうか？聞いていただけて嬉しいです！

### ステップ1: Braze SDKを実装する {#step-1-they-implement-the-braze-sdk}

Braze SDK（ソフトウェア開発キット）は、アプリまたはサイトとの間で情報を送受信するためのものです。エンジニアは、本質的に私たちのアプリを結びつけています。そのためには、いくつかの重要な情報が必要となります。

* [APIキー]({{site.baseurl}}/api/api_key)
* [SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Brazeはカスタムエンドポイントを提供しなくなったので、定義済みのSDKエンドポイントを使用してください。既存のカスタムエンドポイントが提供されている場合は、こちらで[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup)、[iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk)統合の設定ステップを確認できます。

この情報を直接開発者に渡すか、アカウントを作成してBrazeへのアクセスを提供することもできます。

{% alert warning %}
あなたと開発者がBraze上で会社の認証情報を知らずに、または意図せずに変更しないようにしてください。実装プロセス中に問題が発生したり、1人または複数のユーザーがアカウントからロックアウトされたりする可能性があります。
{% endalert %}

### ステップ2: 希望するメッセージングチャネルを実装する {#step-2-they-implement-your-desired-messaging-channels}

Brazeにはユーザーと連絡を取るための多くのオプションがありますが、どのオプションも希望どおりに動作させるためには独自の設定や調整が必要です。ここでエンジニアとのコミュニケーションが重要になります。

実装が効率的かつ適切な順序で行われるように、どのチャネルを使いたいかを必ず開発者に伝えてください。

| チャネル | 詳細 |
|---|---|
| アプリ内メッセージ | SDKの実装とチャネル固有のステップが必要です。 |
| プッシュ | メッセージング認証情報とプッシュトークンに関する適切な処理を提供するSDK実装が必要です。 |
| メール | これはまったく別のプロセスです。統合の詳細については、[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup)セクションを確認してください。 |
| Content Cards | [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)の利用を開始するには、Brazeのカスタマーサクセスマネージャーに連絡してください。 |
| SMS & MMS | 統合の詳細については、[SMSセットアップ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending)セクションを参照してください。 |
| Webhook | SDKの実装とチャネル固有のステップが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: 希望するメッセージングチャネルを実装する" }

{% alert tip %}
Brazeを使えば、各チャネルでアクセスしやすいメッセージングキャンペーンを作成できます。開発者と協力して、実装においてアクセシビリティ基準を満たすようにしてください。
{% endalert %}

### ステップ3: データを設定する {#step-3-they-set-up-your-data}

Brazeは1つの機能しかないツールではありません。これは、単にメールを送信したり、プッシュを送信したりするだけのものではありません。これは、すべてのユーザーと顧客にとってユニークで、パーソナライズされたカスタマージャーニーを創造するためのものです。カスタマージャーニーは、アプリやサイト内でのアクションに基づいており、その内容を定義することができます！開発者の次の仕事は、アプリやサイト内で行われたアクションがBrazeによって検出されるようにすることです。

では、開発者にこの情報を提供するにはどうすればいいのでしょうか？

1. マーケティングチームと協力して、キャンペーン、目標、属性、追跡が必要なイベントを定義します。それらのユースケースを定義し、チームと共有します。
2. カスタムデータ要件（[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)など）を定義します。
3. そこから、そのデータがどのように追跡されるべきか（SDKを通じてトリガーされるなど）について議論します。
4. 必要な[ワークスペース]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)の数を定義します。エンジニアは、これらのワークスペースを[テストおよび設定する]({{site.baseurl}}/user_guide/get_started/workspaces)方法を知っておく必要があります。

これらの情報をすべて把握したら、エンジニアと共有します。エンジニアはその情報をもとに、あなたの[カスタムデータ]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)を実装します。[ユーザーをインポートする]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)必要がある場合もあります。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)にも注意する必要があります。

### ステップ4: 希望に応じてカスタマイズする {#step-4-they-customize-based-on-what-you-want}

APIトリガーによる起動やConnected Contentなどが必要な場合は、Brazeの担当者と開発者の両方と話し合い、アプリやBrazeの外部にあるデータをメッセージに取り込めるようにします。

### ステップ5: 実装のQAを一緒に行う {#step-5-you-both-perform-qa-on-your-implementation}

エンジニアと協力して、すべてが機能していることを確認します。[テストメッセージ]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を送信し、[Android用のテストアプリ]({{site.baseurl}}/developer_guide/references?tab=android)と[iOS用のテストアプリ]({{site.baseurl}}/developer_guide/references?tab=swift)を使用して、送信を開始する前にすべての項目を確認してください！

[AndroidやFireOSとの統合をテスト]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration#test-your-basic-integration)したり、[iOSのプッシュ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing)をテストするための具体的な手順も用意されています。

## 実装後 {#after-implementation}

実装のゴールラインは、一度に100万件のメッセージを送信するためのゴーサインでもないことに注意してください。100万件のプッシュを送信すると、すべての顧客が同じリンクを同時にクリックした場合、アプリが破損する可能性があります。**送信**ボタンをクリックする前に、Brazeからのリクエストを処理するための内部設定のキャパシティについて話し合うことをお勧めします。そして、それに基づいて[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting)を設定できます。

![Braze Firebrandsコミュニティのロゴ]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Brazeを使い慣れたら、Braze Firebrandになることを検討しましょう！BrazeのカスタマーエンゲージメントコミュニティであるBraze Firebrandsでは、顧客体験とマーケティングを近代化するためにBrazeを使用している有力者のコミュニティを構築しています。もっと詳しく知りたいですか？[今すぐ参加しましょう](https://brazefirebrands.splashthat.com/)。