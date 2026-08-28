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
- カスタマージャーニー全体にわたって継続的な一連のメッセージを送信するには、ジャーニーオーケストレーションツールであるキャンバスを選択します。キャンペーンはシンプルでターゲットを絞ったメッセージの送信に適していますが、キャンバスは顧客との関係を次のレベルに引き上げるためのツールです。

## キャンペーン {#campaigns}

キャンペーンはチャネルに応じてさまざまな方法で構築できますが、Braze には知っておくべき4つの主要なキャンペーンタイプがあります。

| キャンペーンタイプ | 説明 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通常 | 最も一般的なキャンペーンタイプです。メッセージングの目標に応じて1つまたは複数のチャネルをターゲットにし、Braze のビジュアルエディターでコンテンツを直接デザイン、カスタマイズ、テストできます。[キャンペーンの作成]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)方法を確認してください。 |
| AB テスト | 単一チャネルをターゲットにするキャンペーンでは、同じキャンペーンの複数のバージョンを送信し、どれが最も効果的かを確認できます。[多変量キャンペーン]({{site.baseurl}}/user_guide/messaging/ab_testing)を使用して、コピー、パーソナライゼーションなどを最大8つの異なるバージョンでテストできます。 |
| API | [API キャンペーン]({{site.baseurl}}/api/api_campaigns)を使用すると、タイムリーなメッセージをできるだけ早く送信できます。他のキャンペーンタイプとは異なり、Braze ダッシュボードでメッセージ、受信者、スケジュールを指定しません。代わりに、これらの識別子を API コールに渡します。通常、リアルタイムのトランザクションメッセージングや速報に使用されます。 |
| トランザクションメール | Braze の[トランザクションメール]({{site.baseurl}}/user_guide/channels/email)は、お客様と顧客の間で合意された取引を促進するために、自動化された非プロモーションのメールメッセージを送信する目的で構築されています。ビジネス上重要な通知を、スピードが最も重視される場面で単一ユーザーに送信します。*一部のパッケージでご利用いただけます。* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャンペーン" }

{% alert note %}
通常キャンペーンと AB テストキャンペーンは、スケジュール設定（今後のイベントについてユーザーリストに通知するなど）やユーザーのアクションに応じた自動送信（ニュースレターに登録した際にメールを送信するなど）が可能です。[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)の詳細をご覧ください。
{% endalert %}

作成するキャンペーンのタイプに関係なく、キャンペーンはユーザーのニーズに耳を傾け、思慮深くパーソナライズされたレスポンスを提供できます。キャンペーンを送信した後は、[組み込みの分析ツール]({{site.baseurl}}/user_guide/analytics/reports)を使用して、そのパフォーマンスと[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)に基づいてコンバージョンしたユーザー数を確認できます。

Braze のキャンペーンについて詳しく学ぶには、以下の追加リソースをご覧ください。

- Braze Learning: [キャンペーンの設定](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [キャンペーンの作成]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- [アイデアと戦略]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)

## キャンバス {#canvas}

複数のキャンペーンで散発的にメッセージを送信するのではなく、キャンバスを使用するとユーザーとの継続的で流動的な会話を構築できます。これは、キャンバス内でのユーザーのジャーニーが、ブランドに対するアクション（または非アクション）に応じて異なるパスに分岐できるためです。これにより、ユーザーをリアルタイムで特定のフローに自動的に進めることができます。

![説明されたプロセスのフロー図。]({% image_buster /assets/img/getting_started/canvas_flow.png %})

このように、キャンバスはコンバージョンへのパスから離脱したユーザーを捕捉し、最も効果的なアウトリーチ施策に配置するのに最適です。

キャンバスを作成する際は、キャンペーンの設定と同様の多くのステップを踏みます。全体のオーディエンス、エントリ条件、送信設定を指定します。誰かがトリガー条件に一致すると、キャンバスが開始されます。その後、終了条件を満たすまでキャンバス内のパスを進みます。

キャンバスには、[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)、[ディレイ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)、[実験]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)など、あらゆるコンポーネントを組み合わせることができます。サポートされているすべてのメッセージングチャネルで送信でき、Facebook、Google、TikTokなどの[ソーシャルプラットフォームや広告プラットフォームと統合]({{site.baseurl}}/partners/canvas_audience_sync/overview)することもできます。

キャンバスについてさらに詳しく学ぶには、以下のリソースをご覧ください。

- Braze Learning: [キャンバスフローによるジャーニーオーケストレーション](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [キャンバスのアウトライン]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines)

## メッセージングチャネル {#messaging-channels}

メッセージングチャネルとは、顧客とエンゲージし、ターゲットを絞ったメッセージを配信するためのさまざまなコミュニケーションチャネルです。

![SDKを通じて利用可能なBrazeメッセージングチャネルの図。]({% image_buster /assets/img/getting_started/channels.png %})

以下の表に、サポートされているチャネルの一覧を示します。

| チャネル                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [メール]({{site.baseurl}}/user_guide/channels/email)                        | パーソナライズされたメールをユーザーの受信トレイに送信します。                                                                                                       |
| [モバイルプッシュ]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)                   | 通知としてユーザーのモバイルデバイスに直接メッセージを配信します。                                                                                   |
| [Webプッシュ]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)                         | ユーザーがWebサイトをアクティブに閲覧していない場合でも、Webブラウザに通知を配信します。                                                         |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)    | ユーザーがモバイルアプリをアクティブに使用している間にアプリ内でメッセージを表示します。                                                                             |
| [SMS、MMS、RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)*                   | ユーザーの携帯電話にテキストメッセージを送信します。                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)*              | 人気のメッセージングプラットフォームWhatsAppを通じてメッセージを送信し、ユーザーにリーチしてエンゲージします。                                                   |
| [バナー]({{site.baseurl}}/user_guide/channels/banners)*       | アプリまたはWebサイトにメッセージを直接埋め込みます。 |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)*       | アプリまたはWebサイト内にユーザーがメッセージを受信して操作できる受信トレイを提供したり、カルーセル、バナーなどの形式でメッセージを表示したりします。 |
| [コネクテッドTV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott)                           | コネクテッドテレビプラットフォーム上でユーザーとエンゲージします。                                                                                                   |
| [Webhook]({{site.baseurl}}/user_guide/channels/webhooks) | カスタムHTTPコールバックを通じて外部システムとのリアルタイム通信と統合を可能にします。                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line) | 日本で最も人気のあるメッセージングアプリ、LINE上でユーザーとエンゲージします。                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メッセージングチャネル" }

<sup>*アドオン機能として利用可能です。*</sup>

{% alert tip %}
ほとんどのチャネル（メール、SMS、プッシュ）を通じて送信できる短く緊急性の高いメッセージについては、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel)フィルターを活用して、各ユーザーに最適なチャネルを通じて自動的にメッセージを送信しましょう。
{% endalert %}