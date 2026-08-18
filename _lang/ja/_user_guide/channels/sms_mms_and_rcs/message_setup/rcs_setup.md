---
nav_title: "RCSのセットアップ"
article_title: "RCSのセットアップ"
page_order: 1
alias: /rcs_setup/
description: "このリファレンス記事では、RCSを稼働させるために必要な要件について説明します。"
page_type: reference
channel:
  - RCS
---

# RCSのセットアップ {#set-up-rcs}

> この記事では、RCSチャネルを稼働させるために必要な要件について説明します。

RCSのセットアップは、SMSのセットアップと同じくらい簡単です。リッチでインタラクティブなメッセージの送信を開始する方法については、以下をお読みください。

## ステップ1: 適格基準を満たす {#step-1-meet-the-eligibility-criteria}

BrazeでRCSを送信するには、事前に3つの基準を満たす必要があります。

1. 現在のBraze契約にメッセージクレジットまたはアクションクレジットが含まれている必要があります。
2. RCSメッセージの送信先が、Brazeがサポートする以下のいずれかの国である必要があります。
- アメリカ合衆国
- イギリス
- ドイツ
- メキシコ
- スウェーデン
- スペイン
- シンガポール
- ブラジル
- フランス
- イタリア
- コロンビア
3. 契約にRCS SKUを含める必要があります。

## ステップ2: RCS認証済み送信者を登録する {#step-2-register-an-rcs-verified-sender}

RCSメッセージを送信する前に、RCS認証済み送信者を登録する必要があります。これは、ユーザーのモバイルデバイスに表示されるブランドの表現であり、ブランド名、ロゴ、認証バッジ、およびオプションのタグラインが含まれます。RCS認証済み送信者は顧客の信頼を強化し、メッセージが認証されたソースから送信されていることを確認します。

![「Cat Failz Cafe」というRCSメッセージにおけるRCS認証済み送信者の例。]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

RCS SKUを注文書に追加すると、Brazeに通知が届き、RCS送信者登録情報についてご連絡いたします。フォームの形式は、RCSメッセージを送信したい国によって異なります。

記入済みのフォームをBrazeに提出すると、Brazeがお客様に代わって登録プロセスを完了します。

### ステップ2.1: RCS購読グループのSMSフォールバックを設定する {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

現在のキャリアカバレッジは国によって異なり、ユーザーのハードウェアおよびソフトウェアのサポートも個人によって異なるため、SMSフォールバックは現在のRCSプログラムを成功させるための重要な要素です。SMSフォールバックの設定をお勧めします。キャリアがRCSをサポートしていない場合やユーザーのデバイスがRCSメッセージを受信できない場合、SMSフォールバックによってメッセージが送信されるため、ユーザーとの重要な瞬間を逃すことはありません。

最初のRCSキャンペーンを展開する前に、現在のSMSオプトイン体験、購読グループ、およびオーディエンスセグメンテーションを確認することを強くお勧めします。必要に応じて、カスタマーサクセスマネージャーがいつでもガイダンスを提供し、設定プロセスをサポートいたします。

#### SMSフォールバックがイベントとセグメンテーションでどのように機能するか {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab イベントの動作 %}

RCSでSMSフォールバックを使用する場合、イベントの動作はメッセージがRCSで正常に送信されたか、SMSにフォールバックしたかによって異なります。

- **RCS送信が成功した場合：** RCS送信イベントとRCS配信イベントを受信します。
- **RCS送信がSMSにフォールバックした場合：** RCS送信イベント、RCS拒否イベント、およびSMS配信イベントを受信します。SMS配信イベントには`IS_SMS_FALLBACK=TRUE`が含まれます。

{% endtab %}
{% tab セグメンテーションの動作 %}

SMSとRCSでは、受信メッセージの[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)（[キャンペーンからメッセージを受信]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign)や[キャンバスステップからメッセージを受信]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)など）は、メッセージがユーザーのデバイスに届いた時点ではなく、送信された時点で評価されます。SMSフォールバックが有効な場合、RCSメッセージが拒否されてSMSにフォールバックした場合や、フォールバックSMSがユーザーのデバイスに配信されなかった場合でも、ユーザーはこれらのフィルターに一致する可能性があります。

{% endtab %}
{% endtabs %}

### キャリア承認のタイムライン {#timeline-for-carrier-approval}

キャリア承認のタイムラインは国によって異なり、同じ国内でも異なる場合があります。RCS市場はまだ初期段階にあるため、キャリアやアグリゲーターのプロセスは急速に進化していることにご留意ください。米国では、RCS認証済み送信者のキャリア承認のターンアラウンドタイムは通常4〜6週間の範囲内であり、テスト送信者は通常1週間以内に承認されるとBrazeは見積もっています。

RCS認証済み送信者が承認されると、オペレーションチームが必要に応じて購読グループを更新し、RCS送信者が含まれていることを確認します。

## ステップ3:購読グループを設定する {#step-3-set-up-subscription-groups}

統合方法に応じて、BrazeはRCS認証済みの送信者を既存のSMS購読グループに追加するか、新しい購読グループを設定できます。詳細な設定手順については、[SMSおよびRCS購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)を参照してください。

## SMSトラフィックのRCSへの移行 {#migrating-sms-traffic-to-rcs}

SMSとRCSで別々の購読グループがある場合、1ステップのキャンバスを使用してユーザーをSMSからRCSに移行できます。ステップごとの手順については、[SMSトラフィックをRCSに移行する]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs)を参照してください。