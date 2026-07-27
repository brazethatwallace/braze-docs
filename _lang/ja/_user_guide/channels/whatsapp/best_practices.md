---
nav_title: ベストプラクティス
article_title: ベストプラクティス
page_order: 22
description: "この記事では、WhatsAppメッセージングチャネルを使用する際に推奨されるベストプラクティスについて説明します。高い電話品質評価の維持、ブロックや報告の高率化の回避、ユーザーのオプトインおよびオプトアウトの方法を含みます。"
page_type: reference
channel:
  - WhatsApp


---
# WhatsAppのベストプラクティス {#whatsapp-best-practices}

> WhatsAppメッセージを送信する前に、高い電話品質評価を維持し、ブロックや報告を回避し、ユーザーのオプトインおよびオプトアウトを適切に管理するための推奨ベストプラクティスを参照してください。

## 高い電話品質評価を維持する {#maintain-a-high-phone-quality-rating}

WhatsAppは、メッセージを受信したユーザーがビジネスをブロックしたり報告したりするなどのアクションに基づいて、[電話品質評価](https://www.facebook.com/business/help/896873687365001)を決定します。品質評価が低く、一定期間内に改善されない場合、メッセージング制限が引き下げられる可能性があるため、高い品質評価を維持することが重要です。

WhatsAppでユーザーに初めてメッセージを送信すると、メッセージスレッド内に以下のオプションが表示されます。

![ビジネスをブロックまたは報告するオプションが表示されたWhatsAppメッセージスレッド]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
ブロックや報告に関する指標を確認するには、WhatsApp Managerで[インサイトタブ](https://www.facebook.com/business/help/683499390267496)がオンになっていることを確認してください。
{% endalert %}

ブロックや報告の発生を抑えるために、Brazeでは高い電話品質評価と安定したメッセージング制限を維持するための以下のベストプラクティスを推奨しています。

### WhatsAppのオプトイン要件とガイドラインに従う {#follow-whatsapp-opt-in-requirements-and-guidelines}

WhatsAppでユーザーとのコミュニケーションを開始する前に、すべてのユーザーがWhatsAppメッセージの受信に積極的に同意していることを確認してください。ユーザーにオプトインを求める際には、WhatsApp経由でビジネスからのメッセージを受信することに具体的に同意していることを伝える必要があります。

{% alert note %}
オプトイン要件と役立つヒントについては、[WhatsAppのオプトインを取得する](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を参照してください。
{% endalert %}

### メッセージングのベストプラクティスに従う {#follow-messaging-best-practices}

- チャネル名にブランドを反映させ、ユーザーがメッセージをスパムではなくあなたからのものだと認識できるようにしてください。
- ユーザーのオプトイン同意を取得した後、確認メッセージを送信してください。
- 適切な時間帯にメッセージを送信してください。

### 顧客にオプトアウトのオプションを提供する {#give-customers-the-option-to-opt-out}

オプトアウトは電話品質評価に影響しないため、ユーザーがブロックや報告をするよりも、WhatsApp通信のオプトアウトを選択してもらう方が望ましいです。

推奨されるベストプラクティスとして、ユーザーに送信する最初のメッセージのフッターにオプトアウト方法の説明を記載してください。たとえば、オプトアウトトリガーワードを返信することでWhatsAppチャネルの購読解除ができることをユーザーに伝えることができます。また、今後のキャンペーンにも定期的にオプトアウトフッターを含めることもできます。設定方法については、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を参照してください。

![チャネルの購読解除にはSTOPと返信するよう記載されたフッター付きのWhatsAppメッセージ]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

### 双方向フローのレスポンスレイテンシーを最小化する {#minimize-response-latency-for-two-way-flows}

[レスポンスメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#response-messages)で返信するインタラクティブなキャンバスフローの場合：

- レスポンスメッセージステップは、インバウンドトリガーまたはアクションパスの評価の直後に配置してください。
- 返信前に購読変更が不要な場合は、ユーザー更新ステップの代わりに[webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を使用してください。
- インバウンドメッセージとレスポンス送信の間に長い遅延や数日間の待機を設けないでください。WhatsAppのカスタマーサービスウィンドウは、インバウンドメッセージごとに24時間です。