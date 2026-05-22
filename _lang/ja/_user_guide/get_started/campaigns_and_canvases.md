---
nav_title: キャンペーンとキャンバス
article_title: "はじめに&#58; キャンペーンとキャンバス"
page_order: 3
page_type: reference
description: "この記事では、Brazeでメッセージを送信するさまざまな方法の概要を説明します。"

---

# はじめに：キャンペーンとキャンバス {#get-started-campaigns-and-canvases}

> この記事では、Brazeでメッセージを送信するさまざまな方法の概要を説明します。Brazeでは、[キャンペーン](#campaigns)または[キャンバス](#canvas)を通じてメッセージを送信できます。

- ターゲットを絞った単一のメッセージをユーザーグループに送信するには、キャンペーンを選択します。キャンペーンは、さまざまなメッセージングチャネルでユーザーとつながるための単一のメッセージステップです。
- カスタマージャーニー全体にわたって継続的なメッセージを送信するには、ジャーニーオーケストレーションツールであるキャンバスを選択します。キャンペーンはシンプルでターゲットを絞ったメッセージの送信に適していますが、キャンバスは顧客との関係を次のレベルに引き上げるためのツールです。

## キャンペーン {#campaigns}

キャンペーンはチャネルに応じて独自に構築できますが、Brazeには主に4種類のキャンペーンがあります。

| キャンペーンの種別 | 説明 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通常 | 最も一般的なキャンペーンタイプです。メッセージの目標に応じて1つまたは複数のチャネルをターゲットに設定し、Brazeのビジュアルエディターを使用してコンテンツを直接デザイン、カスタマイズ、テストできます。[キャンペーンの作成]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)方法をご覧ください。 |
| ABテスト | 単一チャネルをターゲットとするキャンペーンの場合、同じキャンペーンの複数のバージョンを送信して、どれが最も効果的かを確認できます。[多変量キャンペーン]({{site.baseurl}}/user_guide/messaging/ab_testing/)を使用して、最大8つのバージョンでコピー、パーソナライゼーションなどをテストできます。 |
| API | [APIキャンペーン]({{site.baseurl}}/api/api_campaigns/)では、タイムリーなメッセージをできるだけ早く送信できます。他のキャンペーンタイプとは異なり、Brazeダッシュボードではメッセージ、受信者、スケジュールを指定しません。代わりに、これらの識別子をAPI呼び出しに渡します。通常、リアルタイムのトランザクションメッセージングや速報ニュースに使用されます。 |
| トランザクションメール | Brazeの[トランザクションメール]({{site.baseurl}}/user_guide/channels/email/)は、お客様と顧客の間で合意されたトランザクションを円滑に進めるために、自動化された非プロモーションメールメッセージを送信する目的で構築されています。スピードが最も重要な場面で、ビジネスクリティカルな通知を単一のユーザーに送信します。*一部のパッケージでご利用いただけます。* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャンペーン" }

{% alert note %}
通常キャンペーンとABテストキャンペーンは、スケジュール設定（予定されているイベントについてユーザーリストに通知するなど）や、ユーザーのアクションに応じた自動送信（ニュースレターを購読したときにメールを送信するなど）が可能です。[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)の詳細をご覧ください。
{% endalert %}

作成するキャンペーンの種類にかかわらず、キャンペーンはユーザーのニーズに耳を傾け、思慮深くパーソナライズされた応答を提供できます。キャンペーンを送信した後は、[組み込みの分析ツール]({{site.baseurl}}/user_guide/analytics/reports/)を使用して、キャンペーンのパフォーマンスと、[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)に基づいてコンバージョンしたユーザー数を確認できます。

Brazeのキャンペーンについてさらに詳しく学ぶには、以下の追加リソースをご覧ください。

- Braze Learning: [キャンペーンのセットアップ](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [キャンペーンを作成する]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [アイデアと戦略]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## キャンバス {#canvas}

キャンバスを使うと、複数のキャンペーンで散発的にメッセージを送るのではなく、ユーザーとの継続的でスムーズな会話を生み出すことができます。これは、ユーザーのキャンバス内のジャーニーが、ブランドに対するアクション（または非アクション）に応じて異なるパスに分岐するため、特定のフローをリアルタイムで自動的にユーザーを進めることができるからです。

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

このように、キャンバスはコンバージョンへのパスから外れたユーザーをキャッチし、最も効果的なアウトリーチ施策に配置するのに最適です。

キャンバスを作成する際は、キャンペーンの設定と同様のステップに従います。つまり、全体のオーディエンス、エントリ条件、送信設定を指定します。キャンバスは、誰かがトリガー条件に一致したときに開始されます。その後、終了条件を満たすまで、キャンバス内のパスを進みます。

キャンバスには、[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)、[ディレイ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/)、[実験]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/)などを自由に組み合わせることができます。サポートされているすべてのメッセージングチャネルで送信でき、Facebook、Google、TikTokなどの[ソーシャルプラットフォームや広告プラットフォームとの統合]({{site.baseurl}}/partners/canvas_audience_sync/overview/)も可能です。

キャンバスについてさらに詳しく学ぶには、以下の追加リソースをご覧ください。

- Braze Learning: [キャンバス Flowによるジャーニーオーケストレーション](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [キャンバスの概要]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## メッセージングチャネル {#messaging-channels}

メッセージングチャネルは、顧客とエンゲージし、ターゲットを絞ったメッセージを配信するためのさまざまなコミュニケーションチャネルです。

![]({% image_buster /assets/img/getting_started/channels.png %})

以下の表は、サポートされているチャネルの一覧です。

| チャネル | 説明 |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [メール]({{site.baseurl}}/user_guide/channels/email/) | パーソナライズされたメールをユーザーの受信トレイに送信します。 |
| [モバイルプッシュ]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) | メッセージを通知としてユーザーのモバイルデバイスに直接配信します。 |
| [Webプッシュ]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/) | ユーザーがWebサイトをアクティブに閲覧していない場合でも、Webブラウザに通知を配信します。 |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/) | ユーザーがモバイルアプリをアクティブに使用している間に、アプリ内にメッセージを表示します。 |
| [SMS、MMS、およびRCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)* | ユーザーの携帯電話にテキストメッセージを送信します。 |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)* | 人気のメッセージングプラットフォームであるWhatsAppを通じてメッセージを送信し、ユーザーにリーチしてエンゲージします。 |
| [バナー]({{site.baseurl}}/user_guide/channels/banners/)* | メッセージをアプリまたはWebサイトに直接埋め込みます。 |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)* | ユーザーがメッセージを受信して操作できる受信トレイをアプリやWebサイト内に提供したり、カルーセルやバナーなどとしてメッセージを表示したりします。 |
| [コネクテッドTV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/) | コネクテッドTVプラットフォームでユーザーとエンゲージします。 |
| [Webhook]({{site.baseurl}}/user_guide/channels/webhooks/) | カスタムHTTPコールバックを使用して、外部システムとのリアルタイム通信および統合を実現します。 |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | 日本で最も人気のあるメッセージングアプリLINEでユーザーとエンゲージします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging channels" }

<sup>*アドオン機能として利用できます。*</sup>

{% alert tip %}
ほとんどのチャネル（メール、SMS、プッシュ）で送信できる短くて緊急のメッセージについては、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/)フィルターを活用して、各ユーザーに最適なチャネルを通じてメッセージを自動的に送信しましょう。
{% endalert %}