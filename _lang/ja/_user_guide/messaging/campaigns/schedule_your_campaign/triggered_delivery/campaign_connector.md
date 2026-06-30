---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "このハウツー記事では、Campaign Connectorの概要と、適切なタイミングでターゲットを絞った関連性の高いコンテンツを配信するための使い方について説明します。"

---
# Campaign Connector

> Campaign Connectorを使用すると、ユーザーがアクティブなCampaignとインタラクションした際にトリガーされるCampaignを作成できます。適切なタイミングでターゲットを絞った関連性の高いコンテンツを配信できます。

## 仕組み {#how-it-works}

この機能を使用すると、アクティブなCampaignで以下のインタラクションを完了したユーザーをターゲットにできます。

- アプリ内メッセージを表示
- アプリ内メッセージをクリック
- アプリ内メッセージボタンをクリック
- メールをクリック
- メール内のエイリアスをクリック
- メールを開封
- プッシュ通知を直接開封
- プッシュ通知ボタンをクリック
- Push Storiesページをクリック
- コンバージョンイベントを実行
- メールを受信
- SMSを受信
- 短縮SMSリンクをクリック
- プッシュ通知を受信
- Webhookを受信
- コントロールグループに登録
- コンテンツカードを表示
- コンテンツカードをクリック
- コンテンツカードを閉じる

{% alert important %}
Campaign Connectorのトリガーは、アプリ内メッセージCampaignのトリガーには使用できません。アプリ内メッセージは、カスタムイベントやセッション開始などのSDKイベントによってのみトリガーできます。詳細については、[アプリ内メッセージの作成]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)を参照してください。
{% endalert %}

### 配信ルール {#delivery-rules}

Campaign Connectorを使用して、ユーザーがCampaignとのインタラクションを完了した後にメッセージを送信することはできません。たとえば、9週間のマーケティングキャンペーンを実施しており、4週目の初めにCampaign Connectorを使用するフォローアップCampaignを設定した場合、フォローアップCampaignは、フォローアップCampaignが公開された後にマーケティングキャンペーンとインタラクションしたユーザーにのみメッセージを配信します（4〜9週目）。そのため、フォローアップCampaignがターゲットとするすべてのユーザーに届くようにするには、以下の手順に従ってください。

- 元のCampaignを下書きとして設定する
- フォローアップCampaignを設定して公開する
- 元のCampaignを公開する

これらの配信ルールは、コントロールグループに登録されているユーザー、メールを受信するユーザー、またはプッシュ通知を受信するユーザーをターゲットにする場合に特に重要です。元のCampaignを公開するとすぐにユーザーがコントロールグループに登録されるため、元のCampaignを公開する前にフォローアップCampaignを公開する必要があります。同様に、フォローアップCampaignの前に元のCampaignを公開すると、フォローアップCampaignが公開される前に多くのユーザーがメールやプッシュ通知を受信してしまう可能性があります。

## CampaignでのCampaign Connectorの使用 {#using-campaign-connector-with-your-campaigns}

### ステップ1:新しいCampaignを作成する {#step-1-create-a-new-campaign}

ユーザーに送信したいメッセージを作成します。ユースケースに応じて、単一チャネルまたはマルチチャネルのCampaignを選択できます。

### ステップ2:インタラクションとターゲットCampaignを選択する {#step-2-select-interaction-and-target-campaign}

1. [アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を選択し、「Campaignとインタラクション」トリガーを追加して、アクティブなCampaignとインタラクションするユーザーをターゲットにします。
2. トリガーインタラクションを選択します。
3. 次に、ターゲットにしたいアクティブなCampaignを選択します。

![ターゲットにしたいアクティブなCampaignを選択する画面]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### ステップ3:スケジュールの遅延を設定し、例外を追加する（オプション） {#step-3-set-schedule-delay-and-add-exceptions-optional}

スケジュールの遅延を設定する場合、トリガーアクションに例外を追加できます。たとえば、元のメールを開封しなかったユーザーにメールキャンペーンを再送信したい場合があります。このシナリオでは、「メールを受信」をトリガーとして選択し、スケジュールの遅延を1週間に設定します。次に、「メールを開封」を例外として追加します。これにより、受信から1週間以内に元のメールを開封しなかったユーザーにメールが再送信されます。

![スケジュールの遅延を設定し、トリガーアクションに例外を追加する設定画面]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

例外イベントは、ユーザーが関連するメッセージの受信を待っている間にのみトリガーされます。ユーザーがメッセージを待つ前にアクションを実行した場合、例外イベントはトリガーされません。

### ステップ4:Campaignの作成を続行する {#step-4-proceed-with-campaign-creation}

通常どおりCampaignの作成を続行します。特定のCampaignとインタラクションするすべてのユーザーにメッセージを送信したい場合は、アプリのすべてのユーザーを含むSegmentをターゲットにすることをお勧めします。

## ユースケース {#use-cases}

Campaign Connectorを使用して、アクティブなCampaignにエンゲージしたユーザーまたはエンゲージしなかったユーザーをターゲットにできます。

たとえば、送料無料を宣伝するプロモーションプッシュメッセージをクリックしたユーザーをターゲットにして、購入15%オフのプロモーションプッシュメッセージを送信することができます。

Campaign Connectorは、放棄カートのリマインダーとしてプッシュ通知を受信したユーザーをターゲットにすることもできます。たとえば、通知を直接開封しなかったユーザーに通知を再送信したい場合があります。ただし、元の通知を直接開封していなくても、元の通知の送信以降に購入を行ったユーザーは除外したいでしょう。このユースケースは、Campaign「放棄カート」に対して「プッシュ通知を受信」トリガーを追加し、スケジュールの遅延を設定し、「購入を実行」と「プッシュ通知を直接開封」を例外として追加することで実現できます。