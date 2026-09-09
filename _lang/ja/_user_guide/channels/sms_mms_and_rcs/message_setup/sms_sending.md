---
nav_title: SMS送信
article_title: SMS送信
page_order: 4
alias: /sms_message_sending/
description: "SMSメッセージを送信する際の購読グループ、メッセージの課金、キーワードの基本について確認します。"
page_type: reference
channel:
  - SMS

---

# SMSメッセージ送信 {#sms-message-sending}

> Brazeを使用してSMSメッセージを送信する際の購読、課金、キーワードの基本について確認します。

## SMS送信の基本 {#sms-sending-basics}

### 購読グループの選択 {#select-your-subscription-group}

SMSメッセージは[購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)から送信します。購読グループには、特定のメッセージング目的に使用するショートコード、ロングコード、英数字の送信者IDなどの送信用電話番号が含まれています。トランザクションメッセージやプロモーションメッセージなどのユースケースには、別々の購読グループを使用してください。

### メッセージの作成 {#compose-the-message}

メッセージフィールド、文字数制限、パーソナライゼーション、メディア、リンク短縮については、[SMS、MMS、またはRCSメッセージの作成]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings)を参照してください。

### メッセージセグメントと文字数制限について {#understand-message-segments-and-character-limits}

SMSメッセージはGSM-7またはUCS-2エンコーディングを使用し、メッセージセグメントごとに課金されます。エンコーディングルール、セグメントサイズ、セグメント計算ツールについては、[SMSおよびRCS課金計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。

### キーワードのカスタマイズ（任意） {#keyword-customization-optional}

規制により、オプトイン、オプトアウト、ヘルプまたは情報キーワードへの応答が求められます。キーワード、応答、言語固有のキーワードセットは、[キーワード処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)で定義してください。

送信のベストプラクティス（多国間送信や大量送信のガイダンスを含む）については、[SMS、MMS、およびRCSのベストプラクティス]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices)を参照してください。