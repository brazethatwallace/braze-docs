---
nav_title: SMS送信
article_title: SMS送信
page_order: 4
alias: /sms_message_sending/
description: "このリファレンス記事では、SMS送信の基本とベストプラクティスについて説明します。"
page_type: reference
channel:
  - SMS


---

# SMSメッセージ送信 {#sms-message-sending}

> メッセージングは複雑になりがちですが、必ずしもそうである必要はありません。以下のセクションでは、サブスクリプショングループの重要性、SMSセグメントとメッセージ本文の要件、利用可能な高度なカスタマイズオプションなど、BrazeにおけるSMSメッセージ送信の基本について説明します。

## SMS送信の基本 {#sms-sending-basics}

### 購読グループを選択する {#select-your-subscription-group}

SMSメッセージは[購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)から送信する必要があります。購読グループとは、特定のメッセージング目的に使用される送信用電話番号（ショートコード、ロングコード、英数字の送信者IDなど）の集合です。購読済みのユーザーのみがターゲットとなるように、購読グループを指定する必要があります。クライアントによっては、トランザクションSMSメッセージングやプロモーションSMSメッセージングなど、異なるユースケースに対応する複数の購読グループを持つ場合があります。<br><br>

### メッセージ本文を入力する {#input-message-body}

SMSメッセージ本文には、絵文字、Liquid、Connected Contentを含めて最大1,600文字を入力できます。1回のキャンペーン送信で、複数のメッセージセグメント送信が発生する場合があります。BrazeのSMSメッセージ本文は、[GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)または[UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)のいずれかのエンコーディング規格で構成できます。UCS-2文字（絵文字など）が使用された場合、メッセージ本文は自動的にそのエンコーディング規格にフォーマットされます。<br><br>

### メッセージセグメントと文字数制限を理解する {#understand-message-segments-and-character-limits}

SMSメッセージセグメントは、SMS業界でメッセージをカウントする方法です。メッセージセグメントとは、1回のSMS送信で送られる定義された文字数（GSM-7エンコーディングでは160文字、UCS-2エンコーディングでは67文字）までのグループです。メッセージがGSM-7拡張テーブルの文字（`{`、`}`、`~`など）を使用している場合、各セグメントに含められる文字数が少なくなることがあります。GSM-7エンコーディングで161文字のSMSを送信すると、2つのメッセージセグメントが送信されます。複数のメッセージセグメントを送信すると、追加料金が発生する場合があります。<br><br>

### キーワードのカスタマイズ（オプション） {#keyword-customization-optional}

規制により、すべてのオプトイン、オプトアウト、ヘルプ/情報のSMSキーワード応答に対する返信が必要です。Brazeでは、オプトイン、オプトアウト、ヘルプの応答をトリガーする独自のキーワードを定義し、ユーザーに送信される応答を管理し、異なる言語のキーワードセットを定義できます。詳細については、[キーワード処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)のコレクションを参照してください。

{% alert tip %}
SMSキャンペーンの作成方法を学びたいですか？[SMS、MMS、またはRCSメッセージの作成]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)のステップバイステップガイドをご覧ください。
{% endalert %}

マルチカントリー送信や大量送信のガイダンスを含む送信のベストプラクティスについては、[SMS、MMS、RCSのベストプラクティス]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices)を参照してください。